Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add(x, y):
    return x + y
... 
... def subtract(x, y):
...     return x - y
... 
... def multiply(x, y):
...     return x * y
... 
... def divide(x, y):
...     if y == 0:
...         return "Cannot divide by zero"
...     return x / y
... 
... def main():
...     print("Welcome to Simple Calculator!")
...     while True:
...         try:
...             num1 = float(input("Enter first number: "))
...             num2 = float(input("Enter second number: "))
...             operation = input("Enter operation (+, -, *, /): ")
... 
...             if operation == '+':
...                 print("Result:", add(num1, num2))
...             elif operation == '-':
...                 print("Result:", subtract(num1, num2))
...             elif operation == '*':
...                 print("Result:", multiply(num1, num2))
...             elif operation == '/':
...                 print("Result:", divide(num1, num2))
...             else:
...                 print("Invalid operation.")
...         except ValueError:
...             print("Please enter valid numbers.")
...         except Exception as e:
...             print("An error occurred:", str(e))
... 
...         choice = input("Do you want to perform another calculation? (yes/no): ")
...         if choice.lower() != 'yes':
...             print("Exiting program.")
...             break
... 
... if __name__ == "__main__":
