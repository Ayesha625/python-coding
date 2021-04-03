"""def ispal(str):
    return str==str[::-1]

str="pythoncoder"
res=ispal(str)
if res:
    print("palindrome")
else:
    print("not palindrome")"""



s=input("Enter the string to check palindrome or not: ")
if(s==s[::-1]):
    print("The string is palindrome")
else:
    print("The string is not palindrome")  
