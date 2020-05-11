from PIL import Image, ImageColor, ImageDraw


def reset_image():
    im = Image.new('RGB', (162, 92))  # create the Image of size 1 pixel
    ImageDraw.Draw(im).rectangle([(0, 0), im.size], fill=(255, 255, 255))
    for x in range(10, 160, 10):
        im.putpixel((x, 0), (0, 0, 0))
        im.putpixel((x, 91), (0, 0, 0))
    for y in range(10, 90, 10):
        im.putpixel((0, y), (0, 0, 0))
        im.putpixel((161, y), (0, 0, 0))
    im.save('simplePixel.png')  # or any image format


def write_pixel(input_string):
    im = Image.open('simplePixel.png')
    params = input_string.split()
    try:
        x = int(params[1])
        y = int(params[2])
        if x <= 0 or x > 160 or y <= 0 or y > 90:
            return False
        xy = (x, y)
        color_name = params[3]
        rgb = ImageColor.getrgb(color_name)
        im.putpixel(xy, rgb)
        im.save('simplePixel.png')
        return True
    except:
        return False
