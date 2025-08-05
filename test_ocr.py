import cv2
import pytesseract
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def create_test_image():
    # Create a white image
    img = Image.new('RGB', (400, 100), color='white')
    d = ImageDraw.Draw(img)
    
    # Add some text
    text = "Test Receipt\nAmount: $50.00\nDate: 2025-04-06"
    d.text((10,10), text, fill='black')
    
    # Save the image
    img.save('test_receipt.png')
    return 'test_receipt.png'

def test_ocr():
    # Create test image
    image_path = create_test_image()
    
    print("Testing OCR with a sample image...")
    
    try:
        # Read the image
        image = cv2.imread(image_path)
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Extract text
        text = pytesseract.image_to_string(gray)
        
        print("\nExtracted Text:")
        print("--------------")
        print(text)
        
        if text.strip():
            print("\n✓ OCR is working correctly!")
            return True
    except Exception as e:
        print(f"\n✗ Error during OCR:")
        print(f"  {str(e)}")
        return False

if __name__ == "__main__":
    test_ocr() 