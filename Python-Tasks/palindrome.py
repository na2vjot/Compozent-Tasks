#B - Palindrome Checker

def palindrome():
    str = input("Enter the input string:\t")
    
    rev = str[::-1]
    
    if str == rev:
        print("The input string is a palindrome.")
        
    else:
        print("The input string is not a palindrome.")
        
palindrome()