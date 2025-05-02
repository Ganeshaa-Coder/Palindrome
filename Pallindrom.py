import re

def is_palindrome(text):
  """
  Checks if a string is a palindrome, ignoring case, whitespace, 
  punctuation, and special characters.
  """
  # Remove non-alphanumeric characters and convert to lowercase
  cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
  # Reverse the cleaned text
  r = cleaned_text[::-1]
  # Compare the cleaned text with its reverse
  return r == cleaned_text

s = input("Enter a String:")

if is_palindrome(s):
    print("String Palindrome")
else:
    print("String is Not Palindrome")

# Basic tests run when the script is executed directly
if __name__ == "__main__":
    assert is_palindrome("Racecar") == True
    assert is_palindrome("taco cat") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("") == True 
    assert is_palindrome("No 'x' in Nixon") == True
    print("Basic tests passed!")
