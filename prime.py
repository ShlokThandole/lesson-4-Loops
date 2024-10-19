num = int(input("enter number to be checked"))

flag = False

if num>1:
    for i in range (2,num):
        if (num % i)==0:
            flag = True
            break

if flag:
    print("this is not a prime number")
else:
    print("this is a prime number")