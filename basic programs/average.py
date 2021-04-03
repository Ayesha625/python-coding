num=int(input("enter the number of elements "))
l=[]
for i in range(0,num):
    elem=int(input("enter the element "))
    l.append(elem)
    #appends the element in the list
avg=sum(l)/num
print("average of list elements= ",round(avg,3))
#prints the average value . after 3 digits
