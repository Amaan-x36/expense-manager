import pytesseract
from PIL import Image
import os

def test_tesseract():
    print("Testing Tesseract OCR installation...")
    
    # Print Tesseract version
    try:
        print(f"Tesseract Version: {pytesseract.get_tesseract_version()}")
        print("✓ Tesseract is properly installed")
    except Exception as e:
        print("✗ Error getting Tesseract version:")
        print(f"  {str(e)}")
        return False
    
    # Test if we can access the Tesseract executable
    try:
        tesseract_cmd = pytesseract.pytesseract.tesseract_cmd
        print(f"Tesseract Command Path: {tesseract_cmd}")
        if os.path.exists(tesseract_cmd):
            print("✓ Tesseract executable found")
        else:
            print("✗ Tesseract executable not found at specified path")
            return False
    except Exception as e:
        print("✗ Error accessing Tesseract executable:")
        print(f"  {str(e)}")
        return False
    
    print("\nTesseract OCR is properly configured!")
    return True

if __name__ == "__main__":
    test_tesseract() 