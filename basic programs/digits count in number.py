"""num=int(input("Enter the number to count the no. of digits : "))
cnt=0
while(num>0):
    num=num//10
    cnt=cnt+1
print("no.of digits is ",cnt)"""


num=input("Enter the number to count the no. of digits : ")
print(f"no.of digits in {num} is ",len(num))
