import re


def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = not any(char.isdigit() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    special_char_error = not re.search(r"[@#$%^&*!]", password)

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    strength = sum(errors)

    if strength == 0:
        return "Strong"
    elif strength <= 2:
        return "Moderate"
    else:
        return "Weak"


def get_feedback(password):
    feedback = []
    if len(password) < 8:
        feedback.append("- Password should be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        feedback.append("- Include at least one digit.")
    if not any(char.isupper() for char in password):
        feedback.append("- Include at least one uppercase letter.")
    if not any(char.islower() for char in password):
        feedback.append("- Include at least one lowercase letter.")
    if not re.search(r"[@#$%^&*!]", password):
        feedback.append("- Include at least one special character (@, #, $, etc.).")

    return "\n".join(feedback) if feedback else "Your password is strong!"


def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if strength != "Strong":
        print("\nSuggestions to improve your password:")
        print(get_feedback(password))


if __name__ == "__main__":
    main()
