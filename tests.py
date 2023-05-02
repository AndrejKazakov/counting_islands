import unittest
from unittest.mock import patch
from main import main


class TestCase(unittest.TestCase):
    def test_emoty_matrix(self):
        with patch('builtins.input', side_effect=['']):
            self.assertEqual(main(), 0)

    def test_one_island(self):
        with patch('builtins.input', side_effect=['11110',
                                                  '11010',
                                                  '11000',
                                                  '00000',
                                                  '']):
            result = main()
            self.assertEqual(result, 1)

    def test_some_island(self):
        with patch('builtins.input', side_effect=['11000',
                                                  '11000',
                                                  '00100',
                                                  '00011',
                                                  '']):
            result = main()
            self.assertEqual(result, 3)

    def test_no_island(self):
        with patch('builtins.input', side_effect=['0000',
                                                  '0000',
                                                  '0000',
                                                  '0000',
                                                  '']):
            result = main()
            self.assertEqual(result, 0)

    def test_one_str_island(self):
        with patch('builtins.input', side_effect=['0001',
                                                  '']):
            result = main()
            self.assertEqual(result, 1)

    def test_regional_island(self):
        with patch('builtins.input', side_effect=['1001',
                                                  '0000',
                                                  '1001',
                                                  '']):
            result = main()
            self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
