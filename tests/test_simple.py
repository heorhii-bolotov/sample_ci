import unittest


class SimplisticTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_fails(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
