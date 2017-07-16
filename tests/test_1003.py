from tests.utils import PrintRewrite

from PAT1003 import City, main

from mock import patch, Mock


class Test1003(object):

    def test_city(self):
        great = City(0, 1, 2)
        small = City(1, 1, 1)
        assert great > small

    @patch('builtins.input', Mock(side_effect=[
            '5 6 0 2',
            '1 2 1 5 3',
            '0 1 1',
            '0 2 2',
            '0 3 1',
            '1 2 1',
            '2 4 1',
            '3 4 1',
        ]))
    def test_1(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '2 4'

    @patch('builtins.input', Mock(side_effect=[
        '7 21 4 5',
        '2 10 8 7 1 6 9',
        '0 1 5',
        '0 2 8',
        '0 3 5',
        '0 4 6',
        '0 5 3',
        '0 6 1',
        '1 2 8',
        '1 3 10',
        '1 4 7',
        '1 5 7',
        '1 6 6',
        '2 3 1',
        '2 4 6',
        '2 5 8',
        '2 6 8',
        '3 4 6',
        '3 5 5',
        '3 6 4',
        '4 5 1',
        '4 6 6',
        '5 6 8',
    ]))
    def test_2(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '1 7'

