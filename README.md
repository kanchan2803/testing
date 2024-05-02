# Text Detection from Images using OpenCV, Tesseract, and Streamlit

This repository contains code for a simple application to detect text from images using Python libraries OpenCV, Tesseract, and Streamlit. The application allows users to upload images or capture them via camera input and extracts text present in the images.

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

## Folder Structure
- **temp/**: Temporary directory to store intermediate image files during processing.
- **main.py**: Main Python script containing the text extraction logic.
- **requirements.txt**: File containing the required Python libraries.

## Contributions
Contributions to improve the functionality, efficiency, or documentation of this application are welcome. Feel free to submit a pull request with your changes.

## License
This project is licensed under the [MIT License](LICENSE).