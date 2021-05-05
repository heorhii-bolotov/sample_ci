import os
import unittest


class FixturesTest(unittest.TestCase):
    def setUp(self) -> None:
        print("In setUp()")
        self.fixture = range(1, 10)

    def tearDown(self) -> None:
        print("In tearDown()")
        del self.fixture

    @unittest.skipIf(os.getenv('ENV') == 'dev', "Dev Environment")
    def test(self) -> None:
        print("in test()")
        self.assertEqual(self.fixture, range(1, 10))

    def test1(self) -> None:
        print("in test()")
        self.assertEqual(self.fixture, range(1, 10))

    @unittest.skip("good reason for skipping")
    def test_something(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
