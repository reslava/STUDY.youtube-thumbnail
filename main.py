import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageFilter
    
def create_glow(image: Image, glow_amount: int = 12) -> Image:
    """
    Create a glow effect for an image
    glow_amount: intensity of the glow (blur radius)
    """
    # Create larger canvas for glow
    bg_width = image.size[0] + glow_amount * 2
    bg_height = image.size[1] + glow_amount * 2
    bg = Image.new('RGBA', (bg_width, bg_height), (0, 0, 0, 0))
    
    # Paste original image in center
    bg.paste(image, (glow_amount, glow_amount), image)
    
    # Apply blur for glow effect
    glow = bg.filter(ImageFilter.GaussianBlur(glow_amount))
    return glow

def add_image(base_image: Image, image: Image, size: tuple[int, int], loc: tuple[int, int], rotation: int, glow: bool = False, glow_amount: int = 12):
    """
    size: (width, height)
    loc: (x, y)
    rotation: angle in degrees
    glow: whether to add glow effect
    glow_amount: intensity of the glow (blur radius)
    """
    image = image.resize(size)
    image = image.rotate(rotation, expand=True)

    if glow:
        glow_image = create_glow(image, glow_amount)
        # Adjust location to account for glow margin
        glow_loc = (loc[0] - glow_amount, loc[1] - glow_amount)
        base_image.paste(glow_image, glow_loc, glow_image)

    base_image.paste(image, loc, image)

def make_thumbnail(texts: dict[str, tuple[int, tuple[int, int], tuple[int, int, int], tuple[int, int, int], int]], images: dict[str, tuple[int, int]]):
  """
  texts: dictionary of strings mapped to (font_size, (x, y), font_color, stroke_color, stroke_width)
    - font_size: integer
    - (x, y): position tuple
    - font_color: RGB tuple (r,g,b)
    - stroke_color: RGB tuple (r,g,b)
    - stroke_width: integer
  images: dictionary of images and locations
  """
  base_image = Image.open("background.png")
  # Add images  
  for index, i in enumerate(images.keys()):
    image = Image.open(i)
    add_image(base_image, image, size=image.size, loc=images[i], rotation=0, glow=False)
  
  # Add text
  draw = ImageDraw.Draw(base_image)
  for text, (font_size, pos, font_color, stroke_color, stroke_width) in texts.items():
    font = ImageFont.truetype("BebasNeue-Regular.ttf", font_size)      
    draw.text(xy=pos, text=text, fill=font_color, stroke_fill=stroke_color, stroke_width=stroke_width, font=font)
              
  # Save the final image
  base_image.save("thumbnail.png")

def main() -> None:
    texts = {
        "Creating youtube thumbnails with Python": (73, (20, 470), (255, 255, 255), (50, 50, 50), 7),
        "Rafa Eslava": (65, (1010, 310), (255, 223, 89), (0, 0, 0), 4)}  
    images = {
        "python.webp": ((30, 10), True), 
        "rafa.png": ((1280-220, 720-220), True)}  
    
    base_image = Image.open("background.png")
    for img_path, (loc, has_glow) in images.items():
        image = Image.open(img_path)
        add_image(base_image, image, size=image.size, loc=loc, rotation=0, glow=has_glow)
        
    # Add text
    draw = ImageDraw.Draw(base_image)
    for text, (font_size, pos, font_color, stroke_color, stroke_width) in texts.items():
        font = ImageFont.truetype("BebasNeue-Regular.ttf", font_size)      
        draw.text(xy=pos, text=text, fill=font_color, stroke_fill=stroke_color, stroke_width=stroke_width, font=font)
                
    base_image.save("thumbnail.png")

if __name__ == "__main__":
    main()