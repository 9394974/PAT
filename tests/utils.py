
class PrintRewrite(object):

    def __init__(self):
        self.res = ''

    def __enter__(self):
        import sys
        self.origin_write = sys.stdout.write
        sys.stdout.write = self.log_print
        return self

    def log_print(self, text):
        self.res += text
        self.origin_write(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.origin_write
