# -*- coding=utf-8 -*-

from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random

class ImageOpt(object):

    def __init__(self):
        self._font_type, self._font_size = 'Ubuntu-C.ttf', 18
        self._bg_color, self._fg_color = (255, 255, 255), (0, 0, 255)
        self._diagram_size = (120, 30)
        self._mode = 'RGB'

    def make_valid_diagram(self, **kwargs):

        diagram = Image.new(
            mode=kwargs.get('mode') or self._mode,
            size=kwargs.get('size') or self._diagram_size,
            color=kwargs.get('color') or self._bg_color
        )
        diagram



    @staticmethod
    def random_code():
        collection = [x for x in range(48, 58)] + \
                     [x for x in range(65, 91)] + \
                     [x for x in range(97, 113)]

        return [chr(collection[random.randint(0, len(collection))-1])
                for i in range(4)]


if __name__ == '__main__':
    print(ImageOpt.random_code())