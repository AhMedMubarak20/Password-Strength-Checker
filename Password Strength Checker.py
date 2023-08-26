def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    elif not any(char.isalpha() for char in password):
        return "Weak: Password should contain at least one letter."
    else:
        return "Strong: Password is strong."

password = input("Enter a password: ")
strength = check_password_strength(password)
print(strength)
