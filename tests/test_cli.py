import unittest
from wc_cli import cli


class TestCli(unittest.TestCase):
    def test_count(self):
        filename = "tests/test.txt"
        with open(filename, "rb") as file_data:
            result = cli.count(text_data=file_data)
        newlines, word_count, char_count, byte_count, max_line_len = result
        self.assertEqual(newlines, "4")
        self.assertEqual(byte_count, "385")

    def test_result(self):
        filename = "tests/test.txt"
        with open(filename, "rb") as file_data:
            result = cli.count(text_data=file_data)

        test_1 = cli.get_result(filename, result, False, False)
        self.assertEqual(test_1, "4 67 375 385 171 tests/test.txt")

        test_2 = cli.get_result(filename, result, True, False)
        self.assertEqual(test_2, " 385  tests/test.txt")

        test_3 = cli.get_result(filename, result, True, True)
        self.assertEqual(test_3, " 4  385  tests/test.txt")


if __name__ == "__main__":
    unittest.main()
