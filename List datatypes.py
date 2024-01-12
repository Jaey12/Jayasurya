# List of integers
a = [1, 2, 3, 4, 5, 6]
print("List of integers:", a)

# List of strings
b = ["hello", "john", "reese"]
print("List of strings:", b)

# List of both integers and strings
c = ["hey", "you", 1, 2, 3, "go"]
print("List of mixed data types:", c)

#Accessing any one element from variable
print("Element at index 1 in list c:", c[0])

#Modifying the data
a[2] = 99
print("Modified list a after changing element at index 2:", a)

#Appending
a.append(7)
print("List a after appending 7:", a)

#delete the value
del a[1]
print([a])

#insert the value
a.insert(3, 12)
print([a])

#slicing
print("Sliced list a[1:4]:", c[1:4])

# Concatenating lists
d = a + c
print("Concatenated list d:", d)

# Removing elements from the list
b.remove("john")
print("List b after removing 'john':", b)

# Checking if an element is in the list
check_element = "you" in b
print(f"Is 'hello' in list b? , {check_element}")

# Finding the length of a list
length_of_c = len(c)
print("Length of list c:", length_of_c)

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)
print(nested_list[0])
print(nested_list[1][2])
print(nested_list[2][2])

#insert element without using insert function
a[2]=34
print([a])