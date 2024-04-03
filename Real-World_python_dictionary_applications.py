'''
1. Real-World Python Dictionary Applications
Objective:
The aim of this assignment is to reinforce your understanding and application of Python dictionaries, 
nested collections, and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, 
demonstrating your ability to manipulate and manage complex data structures.

Task 1: Restaurant Menu Update
You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update 
this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

Problem Statement:
Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
Add a new category called "Beverages" with at least two items.
Update the price of "Steak" to 17.99.
Remove "Bruschetta" from "Starters".
'''


# Task one

def add_category(menu,category):
  if category not in menu:
    menu[category] = {}
    print(f"Category '{category}' was added to the menu")
  else:
    print(f"Category '{category}' already exists")

def update_items(menu,category,item):
  if category in menu:
    if item not in menu[category]:
      menu[category].update({item: 0})
      print(f"item '{item}' has been added to Category '{category}'")

def update_items_price(menu,category,item,price):
  if category in menu:
    if item in menu[category]:
        menu[category][item] = price
        print(f"The price of {item} has been updated to ${price}")
    else:
      print("The item you selected is not found.")
  else:
    print("The Category that you selected is not found")

def remove_category(menu,category,item):
  if category in menu:
    if item in menu[category]:
      menu[category].pop(item)
      print(f"'{item}' has been removed in category '{category}'")
    else:
      print (f"'{item}' does not exist")
  else:
    print(f"Category '{category}' doesn't exists")


restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
  }

while True: 

  print("Restaurant Menu Editor\nMain Menu")
  print("1. Add a category\n2. Update a Item\n3. Item Pricing\n4. Remove a category\n5. View\n6. Quit")
  user_action = input("Enter your choice: ")
  if user_action =="1":
    user_action1 = input("What category would you like to add: ")
    add_category(restaurant_menu ,user_action1.title())
  elif user_action =="2":
    user_action1 = input("What category would you like to select: ")
    user_action2 = input("Which item would like to add: ")
    update_items(restaurant_menu,user_action1.title(),user_action2.title())
  elif user_action =="3":
    user_action1 = input("What category would you like to select: ")
    user_action2 = input("Which item would like to select: ")
    user_action3 = float(input("What is the price that you would like to add: "))
    print(user_action1,user_action2,user_action3)
    update_items_price(restaurant_menu,user_action1.title(),str.capitalize(user_action2),user_action3)
  elif user_action =="4":
    user_action = input("What category would you like to select: ")
    user_action2 = input("Which item would like to remove: ")
    remove_category(restaurant_menu,user_action.title(),str.capitalize(user_action2))
  elif user_action =="5":
    for category, items in restaurant_menu.items():
      print(f"\n{category}")
      for item, cost in items.items():
        print(f"{item}: ${cost}")
  elif user_action =="6":
    print("Thank you for using our restaurant programming menu!")
    break
  else:
    print("Invalid choice choose a menu option!")