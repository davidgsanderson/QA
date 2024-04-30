import unittest
from unittest.mock import patch
from password_checker import PasswordChecker

class TestPasswordChecker(unittest.TestCase):
    def setUp(self):
        self.password_checker = PasswordChecker()

    def test_check_length(self):
        self.password_checker.current_password = "short"
        self.password_checker.check_length()
        self.assertEqual(self.password_checker.strength_score, 1)

        self.password_checker.current_password = "longpassword"
        self.password_checker.check_length()
        self.assertEqual(self.password_checker.strength_score, 2)

    def test_check_caps(self):
        self.password_checker.current_password = "alllowercase"
        self.password_checker.check_caps()
        self.assertEqual(self.password_checker.strength_score, 1)

        self.password_checker.current_password = "MixedCase"
        self.password_checker.check_caps()
        self.assertEqual(self.password_checker.strength_score, 2)

    def test_check_digits(self):
        self.password_checker.current_password = "nodigits"
        self.password_checker.check_digits()
        self.assertEqual(self.password_checker.strength_score, 1)

        self.password_checker.current_password = "pass123word"
        self.password_checker.check_digits()
        self.assertEqual(self.password_checker.strength_score, 2)

    def test_check_special_chars(self):
        self.password_checker.current_password = "alphanumeric"
        self.password_checker.check_special_chars()
        self.assertEqual(self.password_checker.strength_score, 1)

        self.password_checker.current_password = "pass@word"
        self.password_checker.check_special_chars()
        self.assertEqual(self.password_checker.strength_score, 2)

    def test_check_common(self):
        self.password_checker.current_password = "password"
        self.password_checker.check_common()
        self.assertEqual(self.password_checker.strength_score, 1)


    def test_strength_score_3(self):
        self.password_checker.current_password = "Abc123!"
        self.password_checker.check_length()
        self.password_checker.check_caps()
        self.password_checker.check_digits()
        self.password_checker.check_special_chars()
        self.password_checker.check_common()
        self.assertEqual(self.password_checker.strength_score, 4)

    def test_strength_score_5(self):
        self.password_checker.current_password = "Str0ngP@ssw0rd!"
        self.password_checker.check_length()
        self.password_checker.check_caps()
        self.password_checker.check_digits()
        self.password_checker.check_special_chars()
        self.password_checker.check_common()
        self.assertEqual(self.password_checker.strength_score, 5)

if __name__ == '__main__':
    unittest.main()