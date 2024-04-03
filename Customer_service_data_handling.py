'''
3. Python Programming Challenges for Customer Service Data Handling
Objective:
This assignment is designed to test and enhance your Python programming skills, focusing on real-world 
applications in customer service data management. You will practice correcting code, organizing customer data, 
and implementing a feedback system using Python dictionaries.

Task 1: Customer Service Ticket Tracker
Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement:
Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
'''


def add_tacket(tickets,ticket_num,customer,issue):
  fixed_ticket = "Ticket"+ticket_num
  if fixed_ticket in tickets:
    print(f"{fixed_ticket} alright exists in our system {tickets[0]}")
  else:
    tickets[fixed_ticket] = {"Customer": customer, "Issue": str.capitalize(issue), "Status": "open"}
    print(f"'{fixed_ticket}' has been added for '{customer}' with a problem of '{str.capitalize(issue)}'")
  
  
def update_ticket_status(tickets,ticket_num,status):
  fixed_ticket = "Ticket"+ticket_num
  if fixed_ticket in tickets:
    tickets[fixed_ticket]["Status"] = status
    print(f"Ticket {fixed_ticket} status updated to {status}")
  else:
    print(f"{fixed_ticket} doesn't exist")
      

def view_tickets(tickets,choice = None):
  if choice:
    filtered_tickets = {id: ticket for id, ticket in tickets.items() if ticket["Status"] == choice}
    if filtered_tickets:
      print(f"\nTickets with status '{choice}':")
      for id, ticket in filtered_tickets.items():
        print(f"{id}: Customer: {ticket['Customer']}, Issue: {ticket['Issue']}")
    else:
        print(f"No tickets found with status '{choice}'")
  else:
    print("All tickets:")
    for id, ticket in tickets.items():
        print(f"{id}: Customer: {ticket['Customer']}, Issue: {ticket['Issue']}, Status: {ticket['Status']}")


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

print("Welcome to Service Ticket Handling Program")
while True:
  print("\nMain Menu\n1. Add Ticket\n2. Update Ticket\n3. View Tickets\n4. Exit")
  user_input = input("Please select one of our menu options: ")
  if user_input == "1":
    user_input1 = input("Please Enter ticket number: ")
    user_input2 = input("Customers name: ").title()
    user_input3 = input("Customers Issue: ")
    add_tacket(service_tickets, user_input1, user_input2, user_input3)
  elif user_input == "2":
    user_input1 = input("Please enter ticket number: ")
    user_input2 = input("What do you want to change status to: [OPEN/CLOSED] ").lower()
    update_ticket_status(service_tickets, user_input1, user_input2)
  elif user_input == "3":
    user_input1 = input("Open, Closed or Press Enter for all: ").lower()
    view_tickets(service_tickets, user_input1)
  elif user_input == "4":
    print("Thank you for using Service Ticket Handling Program")
    break
  else:
    print("Invalid input try again")
  
