import os
import cv2
import pytesseract

# Set the Tesseract command path
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"


def preprocess_image(img):
    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Contrast and brightness adjustments
    alpha = 1.5  # Contrast
    beta = 25    # Brightness
    contrast_img = cv2.convertScaleAbs(gray_img, alpha=alpha, beta=beta)

    return contrast_img


def read_text_from_image(img):
    preprocessed_img = preprocess_image(img)

    # OCR processing
    ocr_result = pytesseract.image_to_string(preprocessed_img, config='--psm 6')
    return ocr_result


def process_images_in_directory(directory):
    result_text = ""

    for img_name in os.listdir(directory):
        img_path = os.path.join(directory, img_name)

        if os.path.isfile(img_path) and img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = cv2.imread(img_path)
            image_text = read_text_from_image(image)

            result_text += f"Image: {img_name}\n{image_text}\n{'-' * 50}\n"

    return result_text
