def is_palindrome(string):
  string = string.lower()
  reversed_string = string[::-1]
  return string == reversed_string
string = input("Enter a string: ")
if is_palindrome(string):
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")