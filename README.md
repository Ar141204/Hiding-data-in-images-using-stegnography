# Steganography: Hiding Information in an Image

## Overview
This project demonstrates how to hide information inside an image using steganography techniques. The main goal is to provide a practical implementation of steganography using Python and the Pillow library.

## Prerequisites
Before you start, ensure you have the following installed:
- Python 3.x
- virtualenv

## Installation

1. Clone the repository.
2. Create a `virtualenv` and install the requirements:

   ```bash
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Navigate to the project directory:
   ```bash
   cd steganography
## Usage
To hide and retrieve information in an image, use the following commands:

Hiding Information
``bash
python steganography.py -e -m "Your secret message" -o output.png

Retrieving Information
``bash
python steganography.py -d output.png

To use the hide_data and retr_data functions in your Python code, follow the example:
from PIL import Image

# Hiding information
hide_data('path/to/input/image.png', 'Your secret message', 'path/to/output/image.png')

# Retrieving information
message = retr_data('path/to/output/image.png')
print(message)

Note: The output image must be in PNG format to ensure lossless compression and successful retrieval of the hidden information.

Steganography
Let’s understand what is steganography, digital images, pixels, and color models.

What is steganography?
Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video.

What is the advantage of steganography over cryptography?
The advantage of steganography over cryptography alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages, no matter how unbreakable they are, arouse interest and may in themselves be incriminating in countries in which encryption is illegal.

What is a digital image?
A digital image is a finite set of digital values, called pixels. Pixels are the smallest individual element of an image, holding values that represent the brightness of a given color at any specific point. We can think of an image as a matrix (or a two-dimensional array) of pixels, which contains a fixed number of rows and columns.

Pixel concept and color models
Pixels are the smallest individual element of an image. Each pixel is a sample of an original image, meaning more samples provide more accurate representations of the original. The intensity of each pixel is variable. In color imaging systems, a color is typically represented by three or four component intensities such as red, green, and blue, or cyan, magenta, yellow, and black.

Here, we will work with the RGB color model. The RGB color model has 3 channels: red, green, and blue.

Each pixel in the image is composed of 3 values (red, green, blue), which are 8-bit values (the range is 0–255).

When working with binary codes, we have more significant bits and less significant bits. The leftmost bit is the most significant bit, and if changed, it will have a large impact on the final value. The rightmost bit is the least significant bit, and if changed, it will have less impact on the final value.

Summarizing: Each pixel has three values (RGB), each RGB value is 8-bit (it means we can store 8 binary values), and the rightmost bits are least significant. Changing the rightmost bits will have a small visual impact on the final image. This is the steganography key to hide information inside an image: Change the least significant bits from an image and include the most significant bits from the hidden information.

Contact
For any questions or feedback, feel free to reach out at Ar141204.

Feel free to adjust any part of the README to better fit your project's details and specific requirements! If you need any more changes, just let me know.
You can update the README.md file in your repository using the [link provided](https://github.com/Ar141204/stegnography/edit/main/README.md#L1C0-L30C140).
