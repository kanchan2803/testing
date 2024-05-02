# Text Detection from Images using OpenCV, Tesseract, and Streamlit

This repository contains code for a simple application to detect text from images using Python libraries OpenCV for image processing, Tesseract for Optical Character Recognition (OCR), and Streamlit for creating a user-friendly web application. The application allows users to upload images or capture them via camera input and extracts text present in the images.

## Features:

- Text extraction from uploaded images (JPG, PNG, JPEG)
- Camera input for real-time text capture
- Image preprocessing for improved OCR accuracy (grayscale ->conversion, Gaussian blurring, thresholding)
- Text bounding box visualization
- Extracted text displayed in a code block

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- Tesseract (`pytesseract`)
- Streamlit (`streamlit`)

Make sure you have these libraries installed in your Python environment before running the application.

## Setup
1. Clone this repository to your local machine.
2. Install the required Python libraries by running:
   ```
   pip install -r requirements.txt
   ```
3. [Download](https://github.com/tesseract-ocr/tesseract) and install Tesseract OCR. Make sure to add the Tesseract binary path to the script (`main.py`) where indicated.

## Usage
Run the application using the following command:
```
streamlit run main.py
```
Once the Streamlit server starts, you can access the application via your web browser.

### Camera Input
- Click on the "Camera Input" section to capture an image using your device's camera.
- Once captured, the image will be displayed, and text will be extracted from it.
- The extracted text will be shown below the processed image.

### File Input
- Click on the "File Input" section to upload an image from your local machine.
- Once uploaded, the image will be displayed, and text will be extracted from it.
- The extracted text will be shown below the processed image.

### Tesseract Path:

- Edit the line pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' in app.py to point to the correct path of your Tesseract executable on your system.

## Folder Structure
- **temp/**: Temporary directory to store intermediate image files during processing.
- **main.py**: Main Python script containing the text extraction logic.
- **requirements.txt**: File containing the required Python libraries.

## Contributions
Contributions to improve the functionality, efficiency, or documentation of this application are welcome. Feel free to submit a pull request with your changes.

## License
This project is licensed under the [MIT License](LICENSE).