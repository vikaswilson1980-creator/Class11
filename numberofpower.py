base=int(input("Enter a base number:"))
n=int(input("Enter how many power to calculate:"))

print("\n The first",n,"of",base,"are:")
for i in range(1,n+1):
    power=base**i
    print("base ^ i=power)