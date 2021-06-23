# Python Data Collections

- Lists
- Tuples
- Dict
- Sets
- Lists (AKA array in other languages)
- Shopping list - Multiple items
- add, edit, delete, update
- What is `CRUD` = Create, Replace, Update, Delete

# Lets create a shopping list
Syntax [] - name_of_list = ["", ""]

``` shopping_list = ["Apples", "Eggs", "Chocolate", "Tea", "Bread"]
  print(shopping_list)
  print(type(shopping_list))
  ```

How to access an item in the list using index
```print(shopping_list[2]) # displays chocolate
print(shopping_list[-2]) # displays tea
```

How can I replace an item in the list
```shopping_list[0] = "Mango"
 print(shopping_list)
 ```

How can we add an item to the list
```shopping_list.append("Tuna")
 print(shopping_list)

 Removes last item in the list
 shopping_list.pop()
 print(shopping_list)

 Remove a specific item from the list
 shopping_list.remove('Bread')
 print(shopping_list)
 ```

We can have multiple data types in the same list
```mix_list =[1, 2, 3, "one", "two", "three"]
 print(mix_list)
```
What are Tuples and whats the difference between it and lists
Syntax () - name_of_tuple = ("", "", "")
```essentials = ("paracetamol", "Milk", "Butter")
print(essentials)

Lists are mutable and Tuples and Immutable
essentials.pop(1)
print(essentials)
```
# Dictionaries and sets are data collections in Python

- Dictionaries are another way to manage data but can be a little more dynamic
- Dictionaries work as a KEY AND VALUE
- Key is the reference of the object
- Value is the data storage mechanism you wish to use
- Dynamic as we have lists and another dict inside a dict
#### Syntax - name = {} we use {} brackets to declare a Dict
##### key = value

``` 
students_1 = {
"name":"James",
"stream":"DevOps",
"completed_lessons":4,
"completed_lesson_names":["data types","git and github","operators", "Lists and tuples"]

 }
# Check if we have got the syntax right and print the dict
 print(students_1)
 print(type(students_1))
 print(students_1["stream"])
 print(students_1["completed_lesson_names"][2])

# lets see how we can remove an item from out completed lessons names
 students_1["completed_lesson_names"].remove("operators")
 print(students_1["completed_lesson_names"])
 
# We have some built in methods that we can use with dict
# To print all the keys keys()
 print(students_1.keys())
 
# To print all the values only values()
 print(students_1.values)
 
# Set are also Data collection
 Syntax name = {"", "", ""} 
 ```
## Whats is the difference between sets and dict?
### Sets are unordered

``` shopping_list = ["eggs", "tea", "milk"]
print(shopping_list)

car_part = {"Engine", "Wheels", "Windows"}
print(car_part)

# Add something to the set
car_part.add("seats")
print(car_part)

# Remove something
car_part.discard("Wheels")
print(car_part)
```

