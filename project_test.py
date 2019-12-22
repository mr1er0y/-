import unittest
from PIL import Image
from pr import nrz, nrzi, manch
from dec import decode_img
from random import randint


class ProjectTests(unittest.TestCase):
    def test_nrz_0123(self):
        test_list = list(range(256))
        nrz(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'NRZ'))

    def test_nrzi_0123(self):
        test_list = list(range(256))
        nrzi(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'NRZI'))

    def test_manch_0123(self):
        test_list = list(range(256))
        manch(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'MANCH'))

    def test_nrz_longer(self):
        test_list = list(range(256))*3
        nrz(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'NRZ'))

    def test_nrzi_longer(self):
        test_list = list(range(256))*3
        nrzi(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'NRZI'))

    def test_manch_longer(self):
        test_list = list(range(256))*3
        manch(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'MANCH'))

    def test_nrz_random(self):
        test_list = [randint(0, 255) for x in range(1024)]
        nrz(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'NRZ'))

    def test_nrzi_random(self):
        test_list = [randint(0, 255) for x in range(1024)]
        nrzi(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'NRZI'))

    def test_manch_random(self):
        test_list = [randint(0, 255) for x in range(1024)]
        manch(test_list)
        self.assertEqual(list(test_list), decode_img(Image.open('digital_signal.png'), 'MANCH'))


if __name__ == '__main__':
    unittest.main()
