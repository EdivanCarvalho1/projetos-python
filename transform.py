from PIL import Image

def resize_image(image_path, size):
    img = Image.open(image_path)
    resized_img = img.resize(size)
    return resized_img

def rotate_image(image_path, degrees):
    img = Image.open(image_path)
    rotated_img = img.rotate(degrees)
    return rotated_img
