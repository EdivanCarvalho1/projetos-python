from PIL import Image, ImageFilter

def apply_grayscale(image_path):
    img = Image.open(image_path).convert("L")
    return img

def apply_edge_filter(image_path):
    img = Image.open(image_path)
    return img.filter(ImageFilter.FIND_EDGES)