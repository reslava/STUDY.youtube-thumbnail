# Project Overview

This project is a Python script that generates YouTube thumbnails. It uses the Pillow and NumPy libraries to combine a background image with other images and text. The script allows for customization of text content, font, size, color, and position, as well as the placement and effects of overlayed images.

## Building and Running

### Dependencies

This project requires the following Python libraries:

*   Pillow
*   NumPy

You can install them using pip:

```bash
pip install Pillow numpy
```

### Running the script

To generate a thumbnail, run the `main.py` script:

```bash
python main.py
```

This will create a `thumbnail.png` file in the project directory.

## Development Conventions

### Customization

To customize the thumbnail, you can modify the `texts` and `images` dictionaries within the `main` function in `main.py`.

*   **`texts` dictionary:** This dictionary controls the text elements on the thumbnail. Each entry consists of the text string as the key and a tuple containing the font size, position, font color, stroke color, and stroke width.

*   **`images` dictionary:** This dictionary controls the images to be overlaid on the background. Each entry consists of the image file path as the key and a tuple containing the position and a boolean indicating whether to apply a glow effect.

### File Structure

*   `main.py`: The main Python script for generating thumbnails.
*   `background.png`: The background image for the thumbnail.
*   `BebasNeue-Regular.ttf`: The font file used for the text.
*   Image files (`*.png`, `*.webp`, `*.jpg`): Images to be overlaid on the thumbnail.
*   `thumbnail.png`: The output thumbnail image.
