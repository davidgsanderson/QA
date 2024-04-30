"""
This module provides a class to check the strength of a password.
"""

import string

class PasswordChecker:
    """
    A class to check the strength of a password based on various criteria.

    Attributes:
        common_passwords (list): A list of common passwords to be avoided.
        strength_ratings (dict): A dictionary mapping strength scores to their respective ratings.
    """

    common_passwords = [
        "123456", "123456789", "12345", "qwerty", "password", "12345678", "111111",
        "123123", "1234567890", "1234567", "qwerty123", "000000", "1q2w3e",
        "aa12345678", "abc123", "password1", "1234", "qwertyuiop", "123321",
        "password123"
    ]

    strength_ratings = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    def __init__(self):
        """
        Initialize a PasswordChecker instance.
        """
        self.current_password = ""
        self.running = True
        self.strength_score = 1
        self.password_history = {}

    def check_length(self):
        """
        Check if the password length is greater than or equal to 8 characters.
        If so, increment the strength score.
        """
        if len(self.current_password) >= 8:
            self.strength_score += 1

    def check_caps(self):
        """
        Check if the password contains both uppercase and lowercase letters.
        If so, increment the strength score.
        """
        if any(char.isupper() for char in self.current_password) and \
           any(char.islower() for char in self.current_password):
            self.strength_score += 1

    def check_digits(self):
        """
        Check if the password contains at least one digit.
        If so, increment the strength score.
        """
        if any(char.isdigit() for char in self.current_password):
            self.strength_score += 1

    def check_special_chars(self):
        """
        Check if the password contains at least one special character.
        If so, increment the strength score.
        """
        special_chars = set(string.punctuation)
        if any(char in special_chars for char in self.current_password):
            self.strength_score += 1

    def check_common(self):
        """
        Check if the password is a common password.
        If so, set the strength score to 1.
        """
        if self.current_password in self.common_passwords:
            self.strength_score = 1

    def main(self):
        """
        The main loop to handle user input and password checking.
        """
        while self.running:
            print("\n1 - Check Password")
            print("2 - See History")
            print("3 - Quit")

            option = input("\nPlease enter your option: ")

            if option == "1":
                self.strength_score = 1
                self.current_password = input("Please enter your password: ")
                self.check_length()
                self.check_caps()
                self.check_digits()
                self.check_special_chars()
                self.check_common()
                print(f"Password strength: {self.strength_ratings[self.strength_score]}")
                strength_rating = self.strength_ratings[self.strength_score]
                self.password_history[self.current_password] = strength_rating
            elif option == "2":
                print("Password History:")
                for password, strength in self.password_history.items():
                    print(f"{password}: {strength}")
            elif option == "3":
                print("\nGoodbye!")
                self.running = False
            else:
                print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    password_checker = PasswordChecker()
    password_checker.main()
    