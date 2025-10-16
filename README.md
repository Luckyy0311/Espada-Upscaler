# Espada-Upscaler 🖼️✨

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

Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Download the Real-ESRGAN model weights

python download_models.py


This will download RealESRGAN_x4plus.pth and RealESRGAN_x2plus.pth into the project directory.

Usage

Run the Streamlit app:

streamlit run app.py


Open the provided local URL in your browser (usually http://localhost:8501).

Upload an image or multiple images, choose your enhancement level (2× or 4×), and click Enhance Image.

View the enhanced images, comparisons, and download them.

File Structure
Espada-Upscaler/
├── app.py                 # Main Streamlit app
├── download_models.py     # Script to download Real-ESRGAN weights
├── requirements.txt       # Python dependencies
├── README.md
└── (Real-ESRGAN model weights will be downloaded here)

Dependencies

Python 3.10+

Streamlit

OpenCV

Pillow

NumPy

Real-ESRGAN

BasicSR

gdown

PyTorch

Screenshots

Add some screenshots of your app here for better visibility

Contributing

Contributions are welcome!

Fork the repo

Create a feature branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/YourFeature)

Open a Pull Request
License

This project is licensed under the MIT License - see the LICENSE
 file for details.

Acknowledgements

Real-ESRGAN
 - AI super-resolution models

Streamlit
 - Web app framework

Inspired by AI image enhancement projects in the community
