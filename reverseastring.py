s=str(input("Enter a string:"))
string2=('')
for i in s:
    string2=i + string2
    print("\n s=",string2)
print("The original string is",s)
print("Reversed string is",string2)