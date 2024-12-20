'''## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.'''

namelist = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

name = input("Enter the name you are searching for. (Case Sensitive): ")

if name in namelist:
    print(f"{name} was in the list.")
else:
    print(f"{name} was not in the list.")
