#example-1
n=int(input("Enter Number"))
val=1
if n==0:
    print("Wrong Input")
else:
    for i in range(1,n+1):
        val=val*i
print(val)

#example-2
x=7
for i in range(1,x+1):
    print(7*i)

#example 3
x=int(input("enter 1st side"))
y=int(input("enter 2nd side"))
z=int(input("enter 3rd side"))
if(x*x==y*y+z*z or y*y==x*x+z*z or z*z==y*y+x*x):
    print("Right Angled Triangle")
else:
    print("Not Right Angled Triangle")

#examplee 4
x = int(input("enter number"))

for i in range(1, x + 1):
    for j in range(1, i + 1):
        print('*',end=" ")
    print()

for i in range(x - 1, 0, -1):
    for j in range(1, i + 1):
        print('*',end=" ")
    print()
#example 5
binary_num = input()
binary_list = binary_num.split(',')
divisible_by_5 = [binary for binary in binary_list if int(binary, 2) % 5 == 0]
print(','.join(divisible_by_5))
