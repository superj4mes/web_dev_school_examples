def function_name(parameter_list):
    ["documentation string"] 
    # function_body
    return value(s)

def is_palindrome(s):
    """returns True if s is palindrome"""
    s = s.lower()
    return s == s[::-1]

value = function_name(function_args)
Examples
s = input("Give me a word: ")
if is_palindrome(s):
    print(s, "is palindrome")
else:
    print(s, "is not a palindrome")
# functions can be also referenced via variable
new_name = is_palindrome
print(new_name(input("word?")))
