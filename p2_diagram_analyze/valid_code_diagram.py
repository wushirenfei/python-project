# -*- coding=utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


class ImageOpt(object):

    def __init__(self):
        self._font_type, self._font_size = 'Ubuntu-C.ttf', 18
        self._bg_color, self._fg_color = (255, 255, 255), (0, 0, 255)
        self._diagram_size = (120, 30)
        self._mode = 'RGB'
        self._img, self._draw = None, None

    def make_valid_diagram(self, **kwargs):
        self._img = Image.new(
            mode=kwargs.get('mode') or self._mode,
            size=kwargs.get('size') or self._diagram_size,
            color=kwargs.get('color') or self._bg_color)
        self._draw = ImageDraw.Draw(self._img)

    @staticmethod
    def _random_code():
        # random char including [a-z], [A-Z] and [0-9]
        collection = [x for x in range(48, 58)] + \
                     [x for x in range(65, 91)] + \
                     [x for x in range(97, 113)]

        return [chr(collection[random.randint(0, len(collection))-1])
                for i in range(4)]

    def draw_valid_card(self):
        text = ' %s ' % ' '.join(self._random_code())
        font = ImageFont.truetype(self._font_type, self._font_size)
        font_width, font_height = font.getsize(text)
        self._draw.text(xy=((self._diagram_size[0]-font_width) / 3,
                               (self._diagram_size[1]-font_height) / 3),
                        text=text, font=font, fill=self._fg_color)
        print(text)

    def save(self):
        params = [1 - float(random.randint(1, 2)) / 100,
                  0,
                  0,
                  0,
                  1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500,
                  0.001,
                  float(random.randint(1, 2)) / 500
                  ]
        img = self._img.transform(self._diagram_size, Image.PERSPECTIVE, params)
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

        img.save('new.jpg', 'JPEG')


def main():
    img = ImageOpt()
    img.make_valid_diagram()
    img.draw_valid_card()
    img.save()


if __name__ == '__main__':
    main()
    # print(ImageOpt._random_code())