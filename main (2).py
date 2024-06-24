import re

def check_password_strength(password):
  """
  Checks the strength of a given password.
  Args:
    password: The password to be checked.
  Returns:
    A string indicating the password strength:
      "Very Weak" - Less than 8 characters.
      "Weak" - 8 to 12 characters, but no special characters.
      "Medium" - 8 to 12 characters, with at least one special character.
      "Strong" - More than 12 characters, with at least one special character.
      "Very Strong" - More than 12 characters, with at least one uppercase, lowercase, number, and special character.
  """

  length = len(password)
  has_upper = re.search(r'[A-Z]', password) is not None
  has_lower = re.search(r'[a-z]', password) is not None
  has_number = re.search(r'[0-9]', password) is not None
  has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

  if length < 8:
    return "Very Weak"
  elif length <= 12 and not has_special:
    return "Weak"
  elif length <= 12 and has_special:
    return "Medium"
  elif length > 12 and has_special:
    return "Strong"
  elif length > 12 and has_upper and has_lower and has_number and has_special:
    return "Very Strong"
  else:
    return "Strong"

# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)