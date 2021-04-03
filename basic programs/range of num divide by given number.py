low=int(input("Enter the lower limit "))
up=int(input("Enter the upper limit "))
n=int(input("Enter the number that can divide the range of numbers "))

for i in range(low,up+1):
    if (i%n==0):
        print(i,end=" ")
        
