import string

def is_palindrome(data):
    
    
    cleaned = ''.join(char.lower() for char in data if char.isalnum())
    return cleaned == cleaned[::-1]


user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
