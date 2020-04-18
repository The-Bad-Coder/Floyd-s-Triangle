
n = int(input("Enter Number of Rows : "))

for i in range(1,n+1):
    for j in range(1,n+2):
        if j <= i :
            print(" " , end = " ")
        else:
            print(i , end = " ")
    print("  ")
          
input()