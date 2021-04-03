"""question list comprehension:Print an array of the elements that  sum not equal to 'n'.


Sample Input 0
x=1
y=1
z=1
n=2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]"""


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if((i+j+k)!=n):
                    l.append([i,j,k])
    print(l)
