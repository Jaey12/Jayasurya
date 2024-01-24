
#for loop syntax
#for variable in iterable:
for num in range(1,5):
    print(num)

sumation=0
for num1 in range(6):
    sumation = sumation + num1
print(sumation) #print statement should be outside of the for loop to sum.

#for loop using list datatype
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == fruits[1]: #print one fruit from the list
        print(fruit)

for k in range(1, 12, 3): #third number is given to jumping the value
    print(k)

#for loop is generally used to iterate over a
#sequence, such as a list, tuple, or a range of numbers.
#accessing elements from list, tuple and dict
a=[1, 2, 3, 4, 5]
b=("one", "two", "three")
c={1:"aana", 2:"aavanna", 3:"eena", 4:"eeyanna"}
for numeric in a:
    if numeric == a[2]:
        print("the value of numeric is:", numeric)
for letters in b:
    if letters == b[1]:
        print("the value of letters is:", letters)
for tamil in c:
    if tamil == 2:
        print("the value of tamil is:", c[tamil])
