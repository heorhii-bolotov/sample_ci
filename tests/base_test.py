import unittest


class BaseTestCase(unittest.TestCase):
    @staticmethod
    def assertEndsInR(seq):
        if seq[-1].lower() != 'r':
            raise AssertionError("{} does not end in 'r'".format(seq))


class ExampleTestCase(BaseTestCase):
    def test_str_ends_in_r(self):
        self.assertEndsInR('Doctor')
