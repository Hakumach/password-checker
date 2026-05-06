import random
import string

# Password Generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


# Password Analyzer
def analyze_password(password):
    score = 0
    feedback = []

    common_passwords = {
        "password", "123456", "12345678", "qwerty",
        "abc123", "111111", "letmein"
    }

    # Common password check
    if password.lower() in common_passwords:
        feedback.append("This is a very common password — avoid using it")
        return 0, feedback

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include numbers")

    # Special characters
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Include special characters (!, @, #, etc.)")

    # Repeated characters
    if len(set(password)) <= 2:
        feedback.append("Avoid repeated characters or patterns (e.g., 'aaaaaa')")
        score = max(score - 1, 0)

    # Simple sequences
    sequences = ["1234", "abcd", "qwerty"]
    if any(seq in password.lower() for seq in sequences):
        feedback.append("Avoid common sequences like '1234', 'abcd', or 'qwerty'")
        score = max(score - 1, 0)

    return score, feedback


# Main Program
def main():
    choice = input("Choose an option:\n1. Check password\n2. Generate password\n> ")

    if choice == "1":
        password = input("Enter a password: ")
        score, feedback = analyze_password(password)

        print(f"\nPassword strength score: {score}/5")

        if score <= 2:
            print("Weak password")
        elif score <= 4:
            print("Moderate password")
        else:
            print("Strong password")

        if feedback:
            print("\nSuggestions to improve:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("\nGreat password! No improvements needed.")

    elif choice == "2":
        length = input("Enter desired password length (default 12): ")

        if length.isdigit():
            length = int(length)
        else:
            length = 12

        new_password = generate_password(length)
        print(f"\nGenerated password: {new_password}")

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()