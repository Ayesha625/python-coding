n=int(input("Enter the number of subjects"))
print("Enter the",n,"subject marks separated by space")
l=input().split()
x=0
for i in range(0,n):
    x+=int(l[i])
avg=x//n
print("average of marks = ",avg)
