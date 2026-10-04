# Simple Username and Password Program

print("=====")
print("      Create Your Account")
print("====")

# Ask the user for a username
username = input("Enter your username: ")

# Ask the user for a password
password = input("Enter your password: ")

# Password specifications
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*" for char in password)
has_length = len(password) >= 8

# Check all requirements
if has_length and has_uppercase and has_lowercase and has_digit and has_special:
    print("\nAccount created successfully!")
    print("Welcome,", username + "!")
else:
    print("\nYour password does not meet the requirements.")

    print("\nPassword requirements:")
    
    if not has_length:
        print("- At least 8 characters")
    
    if not has_uppercase:
        print("- At least one uppercase letter (A-Z)")
    
    if not has_lowercase:
        print("- At least one lowercase letter (a-z)")
    
    if not has_digit:
        print("- At least one number (0-9)")
    
    if not has_special:
        print("- At least one special character (! @ # $ % ^ & *)")
