# Espada-Upscaler ❤️‍🔥🔥

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.25+-orange.svg)](https://streamlit.io/)
[![GitHub stars](https://img.shields.io/github/stars/Luckyy0311/Espada-Upscaler?style=social)](https://github.com/Luckyy0311/Espada-Upscaler/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Luckyy0311/Espada-Upscaler?style=social)](https://github.com/Luckyy0311/Espada-Upscaler/network/members)

**Espada-Upscaler** is a Streamlit-based AI photo enhancer that lets you upscale and enhance your images using state-of-the-art Real-ESRGAN super-resolution models. Quickly transform low-resolution images into high-quality, sharp visuals — all in your browser!  

---

## Features

- **AI-Powered Image Enhancement**  
  Uses Real-ESRGAN for high-quality super-resolution.

- **Multiple Upscaling Options**  
  - 4× (High Quality)  
  - 2× (Faster)  

- **Side-by-Side Comparison**  
  Easily compare original and enhanced images.

- **Batch Processing**  
  Enhance multiple images at once with progress feedback.

- **Download Enhanced Images**  
  Save the enhanced images or the comparison images directly.

---

## Demo

> Run a live demo locally using Streamlit.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Luckyy0311/Espada-Upscaler.git
cd Espada-Upscaler
```

2. **Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies
```bash
pip install -r requirements.txt
```

4. **Download the Real-ESRGAN model weights
```bash
python download_models.py
```

This will download RealESRGAN_x4plus.pth and RealESRGAN_x2plus.pth into the project directory.

5. **Usage

  1. **Run the Streamlit app:
```bash
streamlit run app.py
```

  2. **Open the provided local URL in your browser (usually http://localhost:8501).

  3. **Upload an image or multiple images, choose your enhancement level (2× or 4×), and click Enhance Image.

  4. **View the enhanced images, comparisons, and download them.

6. **File Structure
Espada-Upscaler/
├── app.py                 # Main Streamlit app
├── download_models.py     # Script to download Real-ESRGAN weights
├── requirements.txt       # Python dependencies
├── README.md
└── (Real-ESRGAN model weights will be downloaded here)

7. **Dependencies

Python 3.10+

Streamlit

OpenCV

Pillow

NumPy

Real-ESRGAN

BasicSR

gdown

PyTorch

**Screenshots

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/658fa93b-af3c-4d1f-bed6-a7adb46812d5" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9b2e533b-c4b8-4a20-95de-96659fb18385" />


**Contributing

Contributions are welcome!

Fork the repo

Create a feature branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/YourFeature)

Open a Pull Request

**License

This project is licensed under the MIT License - see the LICENSE
 file for details.

**Acknowledgements

Real-ESRGAN
 - AI super-resolution models

Streamlit
 - Web app framework

Inspired by AI image enhancement projects in the community
