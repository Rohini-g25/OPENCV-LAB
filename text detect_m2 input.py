import cv2
import pytesseract

# Set Tesseract path (IMPORTANT)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image (change path if needed)
img = cv2.imread("D:/11239A023/123.jpg")

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple threshold
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# OCR
text = pytesseract.image_to_string(thresh)

print("\nDetected Text:\n")
print(text)

# Show image
cv2.imshow("Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
