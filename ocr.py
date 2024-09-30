import pytesseract
from PIL import Image

def extract_text(image):
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(image, lang='eng+hin')
    return text

def extract_and_format_text(image):
    extracted_text = extract_text(image)
    return {"extracted_text": extracted_text}
