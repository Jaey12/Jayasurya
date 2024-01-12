
#print(1)
#print("hello")

a=3
b=5
c=a+b
print(c)

a, b, c, d, e, f = 1, 2, 3.0, 000.4, "Five", "six"

#print(e)

#we can print 2 integer at once
print(a,b)
#we can print 2 string at once
print(e,f)
#-----------------------------------------------------------
#we cannot print str and int in
#print statement so we use below method called "format"
#how to concadenate string and integer???
print("{} {}".format("The Number is", e))
print(f"The Number is: {f}")
#-----------------------------------------------------------
#how to find variable type
#syntax1
print(type(d))
#syntax 2 getting type of variable wih concatenation.....
type = type(a)
print(f"Variable 'a' has data type: {type}")

