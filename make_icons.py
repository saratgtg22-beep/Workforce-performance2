import os
from PIL import Image
im = Image.open('logo.png').convert('RGBA')
c = im.getpixel((2, 2))
bg = (c[0], c[1], c[2], 255) if c[3] > 200 else (255, 255, 255, 255)
def fit(img, size):
    img = img.copy(); img.thumbnail((size, size), Image.LANCZOS); return img
def put(canvas, img):
    canvas.alpha_composite(img, ((1024 - img.width) // 2, (1024 - img.height) // 2)); return canvas
os.makedirs('assets', exist_ok=True)
put(Image.new('RGBA', (1024, 1024), bg), fit(im, 1024)).convert('RGB').save('assets/icon-only.png')
put(Image.new('RGBA', (1024, 1024), (0, 0, 0, 0)), fit(im, 680)).save('assets/icon-foreground.png')
Image.new('RGB', (1024, 1024), bg[:3]).save('assets/icon-background.png')
