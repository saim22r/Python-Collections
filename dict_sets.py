## Dictionaries and sets are data collections in Python

### Dictionaries are another way to manage data but can be a little more dynamic
### Dictionaries work as a KEY AND VALUE
### Key is the reference of the object
### Value is the data storage mechanism you wish to use
### Dynamic as we have lists and another dict inside a dict
## Syntax - name = {} we use {} brackets to declare a Dict
## key = value

# students_1 = {
#     "name":"James",
#     "stream":"DevOps",
#     "completed_lessons":4,
#     "completed_lesson_names":["data types","git and github","operators", "Lists and tuples"]
#
# }
# Check if we have got the syntax right and print the dict
# print(students_1)
# print(type(students_1))
# print(students_1["stream"])
# print(students_1["completed_lesson_names"][2])

# lets see how we can remove an item from out completed lessons names
# students_1["completed_lesson_names"].remove("operators")
# print(students_1["completed_lesson_names"])

# We have some built in methods that we can use with dict
# To print all the keys keys()
# print(students_1.keys())

# To print all the values only values()
# print(students_1.values)

# Set are also Data collection
## Syntax name = {"", "", ""}
## Whats is the difference between sets and dict
## Sets are unordered
shopping_list = ["eggs", "tea", "milk"]
print(shopping_list)

car_part = {"Engine", "Wheels", "Windows"}
print(car_part)
# Add something to the set
car_part.add("seats")
print(car_part)

# Remove something
car_part.discard("Wheels")
print(car_part)