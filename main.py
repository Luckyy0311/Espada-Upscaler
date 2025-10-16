"""
AI Photo Enhancer - Streamlit Web Interface
Upload images and enhance them with AI super-resolution
"""

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import tempfile
import os

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="AI Photo Enhancer",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# Custom CSS
# ============================================

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.5rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #145a8c;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# Helper Functions
# ============================================

@st.cache_resource
def load_model(model_type):
    """Load and cache the AI model"""
    try:
        from basicsr.archs.rrdbnet_arch import RRDBNet
        from realesrgan import RealESRGANer
        
        if model_type == "4x (High Quality)":
            model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, 
                           num_block=23, num_grow_ch=32, scale=4)
            model_path = 'RealESRGAN_x4plus.pth'
            scale = 4
        else:
            model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                           num_block=23, num_grow_ch=32, scale=2)
            model_path = 'RealESRGAN_x2plus.pth'
            scale = 2
        
        upsampler = RealESRGANer(
            scale=scale,
            model_path=model_path,
            model=model,
            tile=400,
            tile_pad=10,
            pre_pad=0,
            half=False
        )
        
        return upsampler, scale
        
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.info("Make sure you have installed: pip install realesrgan basicsr")
        st.info("Download model from: https://github.com/xinntao/Real-ESRGAN/releases")
        return None, None

def pil_to_cv2(pil_image):
    """Convert PIL image to OpenCV format"""
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

def cv2_to_pil(cv2_image):
    """Convert OpenCV image to PIL format"""
    return Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))

def enhance_image(image, model, scale):
    """Enhance image using AI model"""
    try:
        # Convert PIL to CV2
        cv2_img = pil_to_cv2(image)
        
        # Enhance
        output, _ = model.enhance(cv2_img)
        
        # Convert back to PIL
        enhanced_pil = cv2_to_pil(output)
        
        return enhanced_pil, scale
        
    except Exception as e:
        st.error(f"Enhancement error: {str(e)}")
        return None, None

def create_comparison(original, enhanced):
    """Create side-by-side comparison image"""
    # Resize original to match enhanced
    orig_resized = original.resize(enhanced.size, Image.Resampling.LANCZOS)
    
    # Create side by side
    width = enhanced.size[0]
    height = enhanced.size[1]
    comparison = Image.new('RGB', (width * 2, height))
    comparison.paste(orig_resized, (0, 0))
    comparison.paste(enhanced, (width, 0))
    
    return comparison

# ============================================
# Main App
# ============================================

def main():
    # Header
    st.markdown('<p class="main-header">AI Photo Enhancer</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Upscale and enhance your images with AI super-resolution</p>', 
                unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.header("Settings")
    
    model_choice = st.sidebar.selectbox(
        "Enhancement Level",
        ["4x (High Quality)", "2x (Faster)"],
        help="4x provides better quality but takes longer"
    )
    
    show_comparison = st.sidebar.checkbox("Show Comparison", value=True)
    show_details = st.sidebar.checkbox("Show Image Details", value=True)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### How to use:
    1. Upload an image
    2. Click 'Enhance Image'
    3. Download the result
    
    ### Features:
    - 2x or 4x upscaling
    - AI-powered enhancement
    - Side-by-side comparison
    - Batch processing
    """)
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=['jpg', 'jpeg', 'png', 'bmp', 'webp'],
            help="Supported formats: JPG, PNG, BMP, WEBP"
        )
        
        if uploaded_file is not None:
            # Display original image
            original_image = Image.open(uploaded_file)
            st.image(original_image, caption="Original Image", use_container_width=True)
            
            if show_details:
                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                st.write(f"**Original Size:** {original_image.size[0]} x {original_image.size[1]} pixels")
                st.write(f"**Format:** {original_image.format}")
                st.write(f"**Mode:** {original_image.mode}")
                st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("Enhanced Result")
        
        if uploaded_file is not None:
            if st.button("🚀 Enhance Image", use_container_width=True):
                with st.spinner("Loading AI model..."):
                    model, scale = load_model(model_choice)
                
                if model is not None:
                    with st.spinner(f"Enhancing image ({scale}x upscaling)..."):
                        enhanced_image, scale_used = enhance_image(original_image, model, scale)
                    
                    if enhanced_image is not None:
                        st.success(f"Image enhanced successfully! ({scale_used}x upscale)")
                        
                        # Display enhanced image
                        st.image(enhanced_image, caption="Enhanced Image", use_container_width=True)
                        
                        if show_details:
                            st.markdown('<div class="info-box">', unsafe_allow_html=True)
                            st.write(f"**Enhanced Size:** {enhanced_image.size[0]} x {enhanced_image.size[1]} pixels")
                            st.write(f"**Upscale Factor:** {scale_used}x")
                            improvement = (enhanced_image.size[0] * enhanced_image.size[1]) / (original_image.size[0] * original_image.size[1])
                            st.write(f"**Resolution Increase:** {improvement:.1f}x")
                            st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Download button
                        buf = io.BytesIO()
                        enhanced_image.save(buf, format='PNG')
                        byte_im = buf.getvalue()
                        
                        st.download_button(
                            label="⬇️ Download Enhanced Image",
                            data=byte_im,
                            file_name="enhanced_image.png",
                            mime="image/png",
                            use_container_width=True
                        )
                        
                        # Show comparison
                        if show_comparison:
                            st.markdown("---")
                            st.subheader("Before / After Comparison")
                            comparison = create_comparison(original_image, enhanced_image)
                            st.image(comparison, caption="Left: Original (upscaled) | Right: AI Enhanced", 
                                   use_container_width=True)
                            
                            # Download comparison
                            comp_buf = io.BytesIO()
                            comparison.save(comp_buf, format='PNG')
                            comp_byte = comp_buf.getvalue()
                            
                            st.download_button(
                                label="⬇️ Download Comparison",
                                data=comp_byte,
                                file_name="comparison.png",
                                mime="image/png",
                                use_container_width=True
                            )
        else:
            st.info("Upload an image to get started")
    
    # Batch processing section
    st.markdown("---")
    st.header("Batch Processing")
    
    uploaded_files = st.file_uploader(
        "Upload multiple images for batch enhancement",
        type=['jpg', 'jpeg', 'png', 'bmp', 'webp'],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.write(f"Uploaded {len(uploaded_files)} images")
        
        if st.button("🔄 Enhance All Images"):
            model, scale = load_model(model_choice)
            
            if model is not None:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                enhanced_images = []
                
                for i, file in enumerate(uploaded_files):
                    status_text.text(f"Processing {i+1}/{len(uploaded_files)}: {file.name}")
                    
                    img = Image.open(file)
                    enhanced, _ = enhance_image(img, model, scale)
                    
                    if enhanced:
                        enhanced_images.append((file.name, enhanced))
                    
                    progress_bar.progress((i + 1) / len(uploaded_files))
                
                status_text.text(f"Completed! Enhanced {len(enhanced_images)} images")
                
                # Display results in grid
                cols = st.columns(3)
                for idx, (name, img) in enumerate(enhanced_images):
                    with cols[idx % 3]:
                        st.image(img, caption=f"Enhanced: {name}", use_container_width=True)
                        
                        buf = io.BytesIO()
                        img.save(buf, format='PNG')
                        
                        st.download_button(
                            label=f"Download",
                            data=buf.getvalue(),
                            file_name=f"enhanced_{name}",
                            mime="image/png",
                            key=f"download_{idx}"
                        )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with Streamlit | Powered by Real-ESRGAN</p>
        <p>Free and open source AI photo enhancement</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
