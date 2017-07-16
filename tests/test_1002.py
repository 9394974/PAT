from tests.utils import PrintRewrite

from PAT1002 import main

from mock import Mock, patch


class Test1002(object):

    @patch('builtins.input', lambda: '2 1 2.4 0 3.2')
    def test_1(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '2 1 4.8 0 6.4'

    @patch('builtins.input', Mock(side_effect=['2 1 2.4 0 3.2', '2 2 1.5 1 0.5']))
    def test_2(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '3 2 1.5 1 2.9 0 3.2'

    @patch('builtins.input', Mock(side_effect=['3 1 2.55 2 4.678 5 99', '2 2 1.456 3 7.89']))
    def test_3(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '4 5 99.0 3 7.9 2 6.1 1 2.6'

    @patch('builtins.input', Mock(side_effect=['3 1 2.55 2 4.678 5 99', '3 1 -2.55 2 1.456 3 7.89']))
    def test_4(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '3 5 99.0 3 7.9 2 6.1'

    @patch('builtins.input', Mock(side_effect=['3 999 5 100 -5 0 -0.5', '4 100 5 10 -1 3 5.7 0 10']))
    def test_5(self):
        with PrintRewrite() as t:
            main()
            assert t.res == '4 999 5.0 10 -1.0 3 5.7 0 9.5'


