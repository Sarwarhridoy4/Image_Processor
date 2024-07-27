
# Image Processor Application

## Overview

The Image Processor application is a Python-based GUI tool developed using PyQt5 and PIL (Pillow). It allows users to load, resize, compress, and convert images in a user-friendly manner. The application provides multiple features to ensure high-quality image processing while maintaining aspect ratios.

## Features

- **Load Image**: Load images from your local storage for processing.
- **Resize Image**: Resize images by percentage or specific dimensions while preserving the aspect ratio.
- **Compression**: Adjust the compression quality of images to reduce file size without significant loss of quality.
- **Format Conversion**: Convert images to different formats including JPEG, PNG, BMP, and GIF.
- **Output Customization**: Specify output file names and select output folders for saving processed images.
- **Professional UI**: Stylish and intuitive user interface with responsive design elements.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/image-processor.git
    cd image-processor
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```sh
    python image_processor.py
    ```

## Usage

1. **Load Image**:
    - Click on the `Load Image` button to open a file dialog.
    - Select the desired image file (supported formats: PNG, JPG, BMP, GIF).

2. **Resize Image**:
    - Choose the resize method:
        - **By Percentage**: Use the slider to set the desired resize percentage.
        - **By Dimensions**: Enter the specific width and height for the image.
    
3. **Adjust Compression**:
    - Use the compression slider to set the desired quality level (1-100).

4. **Select Output Format**:
    - Choose the desired output format from the dropdown (JPEG, PNG, BMP, GIF).

5. **Specify Output File Name**:
    - Enter a name for the processed image file.

6. **Select Output Folder**:
    - Click on the `Select Output Folder` button to choose a directory for saving the processed image.

7. **Process Image**:
    - Click on the `Process Image` button to apply the changes and save the processed image in the selected output folder.

## Customization

- **Logo and Favicon**: Replace the `./assets/logo.png` file with your own logo and favicon images.

## Dependencies

- Python 3.x
- PyQt5
- Pillow (PIL)

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyQt5](https://pypi.org/project/PyQt5/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)

## Screenshots

Add screenshots of your application here to provide users with a visual overview.

---

Thank you for using the Image Processor application! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.
