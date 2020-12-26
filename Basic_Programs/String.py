"""
   * author - kajol
   * date - 12/24/2020
   * time - 2:37 PM
   * package - com.bridgelabz.basicprograms
   * Title - Replace String Template “Hello <<UserName>>, How are you?”
"""
import re
name = input("Enter username: ")
regex = re.compile("[a-zA-Z]{3,}")
isValid = regex.search(name)
if isValid:
    print("Hello,", name, ". How are you ?")
else:
    print("Enter complete name")