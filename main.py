import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog, QSlider, QComboBox, QLineEdit,
    QMessageBox, QHBoxLayout, QRadioButton, QButtonGroup
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PIL import Image
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ImageProcessor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Image Processor')
        self.setWindowIcon(QIcon(resource_path('./assets/logo.png')))  # Replace with the path to your favicon file
        self.setGeometry(100, 100, 800, 600)

        self.image_path = None
        self.image = None
        self.output_folder = None

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(
            QPixmap(resource_path('./assets/logo.png')).scaled(150, 150,
                                                               Qt.KeepAspectRatio))  # Replace with the path to your logo file
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.logo_label)

        self.title_label = QLabel('Image Processor', self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.title_label)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.load_button = QPushButton('Load Image', self)
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        self.resize_method_label = QLabel('Resize Method:', self)
        self.layout.addWidget(self.resize_method_label)

        self.resize_method_group = QButtonGroup(self)
        self.percentage_radio = QRadioButton("By Percentage", self)
        self.dimensions_radio = QRadioButton("By Dimensions", self)
        self.percentage_radio.setChecked(True)
        self.resize_method_group.addButton(self.percentage_radio)
        self.resize_method_group.addButton(self.dimensions_radio)
        self.layout.addWidget(self.percentage_radio)
        self.layout.addWidget(self.dimensions_radio)

        self.resize_label = QLabel('Resize Percentage:', self)
        self.layout.addWidget(self.resize_label)

        self.resize_slider = QSlider(Qt.Horizontal, self)
        self.resize_slider.setMinimum(1)
        self.resize_slider.setMaximum(100)
        self.resize_slider.setValue(100)
        self.resize_slider.valueChanged.connect(self.update_resize_label)
        self.layout.addWidget(self.resize_slider)

        self.resize_value_label = QLabel('100%', self)
        self.resize_value_label.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.resize_value_label)

        self.dimensions_layout = QHBoxLayout()
        self.width_label = QLabel('Width:', self)
        self.dimensions_layout.addWidget(self.width_label)
        self.width_input = QLineEdit(self)
        self.dimensions_layout.addWidget(self.width_input)
        self.height_label = QLabel('Height:', self)
        self.dimensions_layout.addWidget(self.height_label)
        self.height_input = QLineEdit(self)
        self.dimensions_layout.addWidget(self.height_input)
        self.layout.addLayout(self.dimensions_layout)

        self.compress_label = QLabel('Compression Quality:', self)
        self.layout.addWidget(self.compress_label)

        self.compress_slider = QSlider(Qt.Horizontal, self)
        self.compress_slider.setMinimum(1)
        self.compress_slider.setMaximum(100)
        self.compress_slider.setValue(100)
        self.compress_slider.valueChanged.connect(self.update_compress_label)
        self.layout.addWidget(self.compress_slider)

        self.compress_value_label = QLabel('100%', self)
        self.compress_value_label.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.compress_value_label)

        self.format_label = QLabel('Output Format:', self)
        self.layout.addWidget(self.format_label)

        self.format_combo = QComboBox(self)
        self.format_combo.addItems(['JPEG', 'PNG', 'BMP', 'GIF'])
        self.layout.addWidget(self.format_combo)

        self.output_name_label = QLabel('Output File Name:', self)
        self.layout.addWidget(self.output_name_label)

        self.output_name_edit = QLineEdit(self)
        self.layout.addWidget(self.output_name_edit)

        self.output_folder_button = QPushButton('Select Output Folder', self)
        self.output_folder_button.clicked.connect(self.select_output_folder)
        self.layout.addWidget(self.output_folder_button)

        self.output_folder_label = QLabel('No folder selected', self)
        self.output_folder_label.setStyleSheet("font-style: italic; color: grey;")
        self.layout.addWidget(self.output_folder_label)

        self.process_button = QPushButton('Process Image', self)
        self.process_button.clicked.connect(self.process_image)
        self.layout.addWidget(self.process_button)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # Set custom stylesheet for styling
        self.setStyleSheet("""
            QWidget {
                font-family: Arial;
                font-size: 14px;
            }
            QLabel {
                font-weight: bold;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QSlider::groove:horizontal {
                height: 8px;
                background: #ddd;
                border: 1px solid #bbb;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #4CAF50;
                border: 1px solid #4CAF50;
                width: 18px;
                margin: -4px 0;
                border-radius: 9px;
                transition: background 0.3s ease, width 0.3s ease;
            }
            QSlider::handle:horizontal:hover {
                background: #45a049;
                width: 24px;
            }
            QComboBox {
                padding: 5px;
                border: 1px solid #bbb;
                border-radius: 5px;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #bbb;
                border-radius: 5px;
            }
            QRadioButton {
                margin-right: 20px;
            }
        """)

    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                   "Images (*.png *.xpm *.jpg *.bmp *.gif)", options=options)
        if file_name:
            self.image_path = file_name
            self.image = Image.open(self.image_path)
            pixmap = QPixmap(self.image_path)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))

    def select_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.output_folder = folder
            self.output_folder_label.setText(f'Selected folder: {folder}')

    def process_image(self):
        if self.image is None:
            QMessageBox.warning(self, 'Warning', 'No image loaded!')
            return

        if not self.output_folder:
            QMessageBox.warning(self, 'Warning', 'No output folder selected!')
            return

        if self.percentage_radio.isChecked():
            resize_percentage = self.resize_slider.value()
            new_width = int(self.image.width * (resize_percentage / 100))
            new_height = int(self.image.height * (resize_percentage / 100))
        else:
            try:
                new_width = int(self.width_input.text())
                new_height = int(self.height_input.text())
            except ValueError:
                QMessageBox.warning(self, 'Warning', 'Please enter valid dimensions!')
                return

        compression_quality = self.compress_slider.value()
        output_format = self.format_combo.currentText().lower()
        output_file_name = self.output_name_edit.text()

        if not output_file_name:
            QMessageBox.warning(self, 'Warning', 'Please enter an output file name!')
            return

        output_file_path = f"{self.output_folder}/{output_file_name}.{output_format}"

        try:
            resized_image = self.image.resize((new_width, new_height), Image.LANCZOS)

            # Convert image to RGB if saving as JPEG
            if output_format == 'jpeg' and resized_image.mode in ("RGBA", "P"):
                resized_image = resized_image.convert("RGB")

            resized_image.save(output_file_path, format=output_format.upper(), quality=compression_quality)
            QMessageBox.information(self, 'Success', f'Image processed and saved as {output_file_path}')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')

    def update_resize_label(self, value):
        self.resize_value_label.setText(f'{value}%')

    def update_compress_label(self, value):
        self.compress_value_label.setText(f'{value}%')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageProcessor()
    ex.show()
    sys.exit(app.exec_())
