# Task 1: Create a Dictionary of Student Marks
print("Task 1ss")
dictionary = {
    'Sachin':80,
    'Virat':75,
    'Neeraj':72,
    'Lata':98,
    'Amrita':55}

studentName = input("Enter the student's name:")

if studentName in dictionary:
    print("{} marks: {}".format(studentName, dictionary[studentName]))
else:
    print("Student not found.")



# Task 2: Demonstrate List Slicing
print("Task 2")
list = [1,2,3,4,5,6,7,8,9,10]
print("Original list: {}".format(list))
first_five = list[:5]
print("Extracted first five elements: {}".format(first_five))
reverse = first_five[::-1]
print("Reversed extracted elements: {}".format(reverse))


