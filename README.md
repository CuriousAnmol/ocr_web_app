# OCR and Document Search Web Application

## Overview
This web application performs Optical Character Recognition (OCR) on uploaded images containing text in both Hindi and English. It also allows users to search for keywords within the extracted text.

## Features
- Upload images (JPEG, PNG) for OCR processing.
- Extracted text displayed on the same page.
- Basic keyword search functionality to highlight matching sections.

## Requirements
- Python 3.6 or higher
- Tesseract OCR installed on your system
- Required Python packages:
  - `torch`
  - `transformers`
  - `gradio`
  - `pytesseract`
  - `Pillow`
  - `numpy`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Abhi5143/ocr_web_app.git
   cd ocr-document-search-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR:
   - Follow the instructions for your operating system (Windows, macOS, or Linux).

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:7860` (or the provided public link).
3. Upload an image containing text.
4. Enter keywords to search within the extracted text.

## Deployment
This application can be deployed on platforms like [Hugging Face Spaces](https://huggingface.co/spaces) or Heroku.

## Acknowledgments
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for OCR capabilities.
