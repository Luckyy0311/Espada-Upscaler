#!/usr/bin/env python3
"""
download_models.py - Automatically download Real-ESRGAN model weights
"""

import os
import gdown

# Dictionary of model names and download URLs
MODEL_URLS = {
    "RealESRGAN_x4plus.pth": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.3.0/RealESRGAN_x4plus.pth",
    "RealESRGAN_x2plus.pth": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.3.0/RealESRGAN_x2plus.pth"
}

def download_model(model_name, output_dir="."):
    """
    Download the model if it doesn't exist in the output directory.
    """
    if model_name not in MODEL_URLS:
        raise ValueError(f"No download URL defined for {model_name}")

    output_path = os.path.join(output_dir, model_name)
    if os.path.exists(output_path):
        print(f"[INFO] {model_name} already exists at {output_path}, skipping download.")
    else:
        print(f"[INFO] Downloading {model_name}...")
        gdown.download(MODEL_URLS[model_name], output_path, quiet=False)
        print(f"[INFO] Download completed: {output_path}")

def main():
    """
    Download all Real-ESRGAN models to the current directory.
    """
    output_dir = os.getcwd()
    os.makedirs(output_dir, exist_ok=True)

    for model_name in MODEL_URLS.keys():
        download_model(model_name, output_dir)

if __name__ == "__main__":
    main()
