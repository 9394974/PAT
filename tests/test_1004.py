from tests.utils import PrintRewrite

from PAT1004 import main

from mock import patch, Mock


class Test1004(object):

    @patch('builtins.input', Mock(side_effect=[
            '2 1',
            '01 1 02',
        ]))
    def test_1(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '0 1'

    @patch('builtins.input', Mock(side_effect=[
        '72 34',
        '01 5 26 04 66 11 31',
        '26 5 57 60 14 17 25',
        '04 2 69 20',
        '57 4 35 13 16 45',
        '66 3 41 36 56',
        '69 3 37 02 07',
        '41 3 58 38 65',
        '35 4 46 68 59 61',
        '11 2 15 44',
        '14 1 18',
        '37 1 06',
        '13 2 30 67',
        '30 1 34',
        '46 3 42 27 62',
        '18 2 72 71',
        '42 3 29 51 53',
        '31 1 12',
        '12 2 54 63',
        '15 5 05 52 47 21 64',
        '17 4 08 23 19 49',
        '08 1 24',
        '23 1 09',
        '52 2 39 03',
        '24 1 48',
        '48 1 10',
        '54 1 70',
        '71 1 55',
        '06 1 43',
        '64 1 33',
        '39 1 50',
        '70 1 22',
        '20 1 40',
        '25 1 32',
        '40 1 28',
    ]))
    def test_2(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '0 0 4 14 9 7 4'
