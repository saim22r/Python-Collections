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


