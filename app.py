import gradio as gr
from ocr import extract_and_format_text
from PIL import Image
import numpy as np

def process_image(image):
    # Convert numpy array to PIL Image if necessary
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    
    text_data = extract_and_format_text(image)
    return text_data["extracted_text"]

def search_text(extracted_text, keyword):
    matches = [line for line in extracted_text.splitlines() if keyword.lower() in line.lower()]
    return "\n".join(matches) if matches else "No matches found."

def interface(image, keyword):
    extracted_text = process_image(image)
    search_results = search_text(extracted_text, keyword)
    return extracted_text, search_results

iface = gr.Interface(
    fn=interface,
    inputs=["image", "text"],
    outputs=["text", "text"],
    live=True,
    title="OCR and Document Search",
    description="Upload an image containing text and search for keywords."
)

iface.launch(share=True)  # Enable public sharing
