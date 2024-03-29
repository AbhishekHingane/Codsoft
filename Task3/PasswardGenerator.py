Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... import string
... 
... def generate_password(length=12, complexity='medium'):
...     if complexity == 'low':
...         characters = string.ascii_letters + string.digits
...     elif complexity == 'medium':
...         characters = string.ascii_letters + string.digits + string.punctuation
...     elif complexity == 'high':
...         characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
...     else:
...         raise ValueError("Complexity level should be 'low', 'medium', or 'high'.")
... 
...     password = ''.join(random.choice(characters) for _ in range(length))
...     return password
... 
... def main():
...     print("Welcome to the Password Generator!")
...     while True:
...         length = int(input("Enter the length of the password: "))
...         complexity = input("Enter complexity level (low/medium/high): ")
... 
...         try:
...             password = generate_password(length, complexity)
...             print("Your generated password is:", password)
...         except ValueError as e:
...             print(e)
... 
...         another = input("Generate another password? (yes/no): ")
...         if another.lower() != 'yes':
...             print("Exiting program.")
...             break
... 
... if __name__ == "__main__":
