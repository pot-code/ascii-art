from argparse import ArgumentParser
from PIL import Image
from pylab import array

ASCII_DICT=[ '.', '.', ',', '-', '-', '+', '*', '*', '?', '%', '#']

def resize_image(img, newWidth):
    width, height = img.size
    ratio = width / height
    return img.resize((newWidth, int(newWidth // ratio)))


def intensity_mapper(i):
    return ASCII_DICT[i // 25]  # 将 0-255 区间映射到 0-10 范围内


def image_to_ascii(path, newWidth):
    image = Image.open(path)
    image = image.convert('L')
    image = resize_image(image, newWidth)
    out_str = ''

    for e in map(lambda x: map(intensity_mapper, x), array(image)):
        out_str += "".join(list(e))
        out_str += '\n'

    print(out_str)

if __name__ == '__main__':
    parser = ArgumentParser(description='image to ascii.')
    parser.add_argument('path', help='path to image')
    parser.add_argument('-w', '--width', help='print width', dest='newWidth', type=int, default=100)
    args = parser.parse_args()

    image_to_ascii(args.path, args.newWidth)
