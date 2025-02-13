
# Steganography: Hiding an image inside another

## Usage

Create a `virtualenv` and install the requirements:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, merge and unmerge your files with:

```
python steganography.py merge --image1=res/image1.jpg --image2=res/image2.jpg --output=res/output.png
python steganography.py unmerge --image=res/output.png --output=res/output2.png
```

To use the **Steganography** class in your **Python** code, you will need to use the **Image** module from the **Pillow** library, for example:

```python
from PIL import Image

merged_image = Steganography().merge(Image.open(image1), Image.open(image2))
merged_image.save(output)
```

**Note**: the **output image** from the **merge operation** and the **input image** for the **unmerge operation** must be in **PNG** format.
