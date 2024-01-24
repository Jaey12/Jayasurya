
#A while loop allows code to be executed repeatedly
a=11
while a>5:
    a=a-1
    print(a)

num = 16
while num >= 1:
    print(num)
    num = num - 1

#when using range Without the if statement and break, the while loop would
#keep executing until num becomes less than 5, which might result in an infinite loop.
for num in range (1, 10):
   while num >= 5:
       print(num)
       num = num - 1
       if num >=5:
           break

#The continue statement is used in programming to skip the rest
#of the code inside a loop for the current iteration and move on to the next iteration.
b=10
while b>1:
    if b==9:
        print("I skip ", b)
        b = b - 1
        continue
    elif b==8:
        print("I skip ", b)
        b = b - 1
        continue
    elif b==1:
        break
    print(b)
    b = b - 1
print("Hi, while executed properly")

