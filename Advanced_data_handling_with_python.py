'''
2. Advanced Data Handling with Python
Objective:
The aim of this assignment is to deepen your knowledge and practical skills in handling complex data 
structures using Python. You will work on real-world inspired tasks that require advanced manipulation of dictionaries, 
nested collections, and implementing custom functions for specific data processing needs.

Task 1: Hotel Room Booking Tracker
Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

Problem Statement:
Develop a program that:

Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
Implement functions to:
Book a room (mark as booked and assign to a customer).
Check-out a customer (mark room as available and remove customer name).
Display the status of all rooms.
Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}
Task 2: E-commerce Product Search Feature
Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

Problem Statement:
Create a system that:

Holds a dictionary of products where each product has attributes like name, category, and price.
Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).
Handle cases where no matches are found.
Example product dictionary:

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}
'''
# Task one 


def adding_rooms(hotel,room_number):
  if room_number not in hotel:
    hotel[room_number] = {"status": "available", "customer": ""}
    print(f"Room Number {room_number} has been added")
  else:
    print(f"Room Number {room_number} already exists")


def booking_room(hotel, room_number,customer):
  if room_number in hotel:
    if hotel_rooms[room_number].get("status") == "available" and hotel_rooms[room_number].get("customer") == "":
      print(f"Room #{room_number} is Available")
      user_choice = input("Would you like to book this room: [YES/NO] ").upper()
      if user_choice == "YES":
        hotel[room_number] = {"status": "booked", "customer": customer}
        print(f"Room #{room_number} is now booked by '{customer}'")
      else:
        pass
    else:
      print(f"Room #{room_number} is already booked.")
  else:
    print(f"Room #{room_number} doesn't exists")


def check_out(hotel,room_number):
  if room_number in hotel:
    if hotel_rooms[room_number].get("status") == "booked":
      print(f"Room #{room_number} is booked")
      user_choice = input("Would you like to check them out: [YES/NO] ").upper()
      if user_choice == "YES":
        hotel[room_number] = {"status": "available", "customer": ""}
        print(f"Room #{room_number} has been checked out and is not available")
      else:
        pass
    else:
      print(f"We don't have any bookings under room #{room_number}")
  else:
    print(f"Room #{room_number} doesn't exists")


def view_rooms(hotel):
  for room, statuses in hotel_rooms.items():
    print(f"\nRoom: {room}")
    for status, customer in statuses.items():
      print(f"{str.capitalize(status)}: {str.capitalize(customer)}")
      



hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

while True:
  print("Welcome to the Hotel Management Systems!")
  print("Main Menu\n1. Add Rooms\n2. Room Booking\n3. Customer Check-out\n4. View Rooms\n5. Exit")
  user_input = input("Select one of out Menu options: ")
  if user_input == "1":
    user_input1 = input("Enter the room number you would like to add: ")
    adding_rooms(hotel_rooms,user_input1)
  elif user_input == "2":
    user_input1 = (input("Enter the room number you would like to book: "))
    user_input2 = input("Enter customers fist and last name: ").title()
    booking_room(hotel_rooms,user_input1,user_input2)
  elif user_input == "3":
    user_input1 = (input("Enter the room number you want to check-out: "))
    check_out(hotel_rooms,user_input1,)
  elif user_input == "4":
    view_rooms(hotel_rooms)
  elif user_input == "5":
    print("Thank you for using out Hotel Management System! Good Bye!")
    break
  else:
    print("Please enter in one of our Menu options")


# Task two
  

def product_search(products,item):
  matched_products = []
#  list numbers|list of categories 
  for item_num, product_names in products.items():
    # check to see if the product we are looking up is in the key 'name' values and lower it to match 
    if item.lower() in product_names["name"].lower():
      matched_products.append(product_names)
      return matched_products
  else:
    print("The item you are looking for is not in our inventory")
  
 
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}


print("Welcome to the Item Look-Up Systems!")
while True:
  print("Main Menu\n1. Search Products\n2. Exit")
  user_input = input("Select one of out Menu options: ")
  if user_input == "1":
    user_input1 = input("What item would you like to look up: ")
    product_readout = product_search(products,user_input1)
    #if product_readout is returned true
    if product_readout:
      print(f"Found {user_input1} in Catalog")
      # runs the appended list in product_search
      for product in product_readout:
        #         print value of key 'name'    print value of key 'category'    print value of key 'price' 
        print(f"Name: {product['name']}, Category: {product['category']}, Price: ${product['price']}")
    
  elif user_input == "2":
    print("Thank you for using our Item Look-Up System")
    break
  else:
    print("Please enter in one of our Menu options")