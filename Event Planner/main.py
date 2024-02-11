from datetime import datetime, timedelta
import getpass

# Define existing event categories with numbers
event_categories = {
    '1': 'Birthday',
    '2': 'Wedding',
    '3': 'Conference',
    '4': 'Seminar',
    '5': 'Concert',
    '6': 'Party',
    '7': 'Workshop',
    '8': 'Meeting',
    '9': 'Networking',
    '10': 'Exhibition'
}

users = {
    'Maui': 'Pador',
    'user2': 'password2',
    'user3': 'password3',
    '1': '1',
}

# Login --Start--
def lgn_choices():
    print("Welcome to Cevent Event Planner")

    while True:
        print("Input your choice from 1-3")
        print("1.Login")
        print("2.Register")
        print("3.Exit")

        lgn_choice = input("Enter your choice: ")

        if lgn_choice == '1':
            return True
        elif lgn_choice == '2':
            main_reg()
        elif lgn_choice == '3':
            print("Exiting Program...")
            exit(0)
        else:
            print("Invalid Input")


def stm_login(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False


def main_login():
    print("Please input your credentials")

    while True:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        if stm_login(username, password):
            print("Login successful!")
            break
        else:
            print("Invalid username or password, please try again")


# Register start
def lgn_reg(username, password):
    if username in users:
        print("User already exists. Please try another username.")
    else:
        users[username] = password
        print("You have successfully registered")


def main_reg():
    print("Input your credentials here: ")

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        if password != confirm_password:
            print("Password doesn't match with the confirmation password")
        else:
            lgn_reg(username, password)
            break


# Register end


# CRUD function
# Main menu start

event_planner = {}


# Function to add an event to the planner
def add_event():
    print("Add Event:")

    # Display existing event categories
    print("Existing Event Categories:")
    for number, category in event_categories.items():
        print(f"{number}. {category}")

    # Prompt user to select a category
    category_number = input("Enter the number of the event category: ")

    # Validate category number
    if category_number not in event_categories:
        print("Invalid category number.")
        return

    # Get the selected category name
    event_type = event_categories[category_number]

    name = input("Enter the name of the event: ")
    venue = input("Enter the venue: ")

    # Prompt user to select the day of the week
    print("Select the day of the week:")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    print("5. Friday")
    print("6. Saturday")
    print("7. Sunday")
    day_choice = input("Enter your choice (1-7): ")

    # Map the choice to the corresponding day of the week
    day_mapping = {
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Saturday',
        '7': 'Sunday'
    }

    # Get the selected day of the week
    selected_day = day_mapping.get(day_choice)
    if not selected_day:
        print("Invalid choice for the day of the week.")
        return

    # Prompt user to select the time
    print("Select the time:")
    print("1. 6 AM")
    print("2. 12 PM")
    print("3. 6 PM")
    time_choice = input("Enter your choice (1-3): ")

    # Map the choice to the corresponding time
    time_mapping = {
        '1': '06:00:00',
        '2': '12:00:00',
        '3': '18:00:00'
    }

    # Get the selected time
    selected_time = time_mapping.get(time_choice)
    if not selected_time:
        print("Invalid choice for the time.")
        return

    # Combine the date, selected time, and format
    date_time_str = f"{selected_day} {selected_time}"

    # Check if the selected date and time are already reserved for another event
    for event in event_planner.values():
        if event['Date and Time'] == date_time_str:
            print("The selected date and time are already reserved for another event.")
            return

    special_guests = input("Enter the special guests (separated by commas if multiple): ").split(',')
    host_name = input("Enter the host name: ")

    event_planner[name] = {
        'Event Type': event_type,
        'Venue': venue,
        'Date and Time': date_time_str,
        'Special Guests': special_guests,
        'Host Name': host_name
    }
    print("Event added successfully!")


# Function to view all events in the planner
def view_events():
    if event_planner:
        print("Your events:")
        for name, details in event_planner.items():
            print("Event Name:", name)
            print("Event Type:", details['Event Type'])
            print("Venue:", details['Venue'])
            print("Date and Time:", details['Date and Time'])
            print("Special Guests:", ', '.join(details['Special Guests']))
            print("Host Name:", details['Host Name'])
            print()
    else:
        print("No events scheduled.")


# Function to update an event in the planner
def update_event(name):
    if name in event_planner:
        print("Update Event:")
        event_type = input("Enter the new type of event: ")
        venue = input("Enter the new venue: ")
        date_time = input("Enter the new date and time (MM/DD/YYYY HH:MM AM/PM): ")

        # Validate date and time
        if not validate_date_time(date_time):
            print("Invalid date and time format. Please enter in MM/DD/YYYY HH:MM AM/PM format.")
            return

        special_guests = input("Enter the new special guests (separated by commas if multiple): ").split(',')
        host_name = input("Enter the new host name: ")

        # Update event details
        event_planner[name]['Event Type'] = event_type
        event_planner[name]['Venue'] = venue
        event_planner[name]['Date and Time'] = date_time
        event_planner[name]['Special Guests'] = special_guests
        event_planner[name]['Host Name'] = host_name

        print(f"Event '{name}' updated successfully!")
    else:
        print(f"No event found with the name '{name}'.")


def validate_date_time(date_time):
    try:
        datetime.strptime(date_time, "%m/%d/%Y %I:%M %p")
        return True
    except ValueError:
        return False


def delete_event(name):
    if name in event_planner:
        del event_planner[name]
        print(f"Event '{name}' deleted successfully!")
    else:
        print(f"No event found with the name '{name}'.")


def main():
    print("Welcome to the Event Planner!")

    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. View Event")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_event()
        elif choice == '2':
            view_events()
        elif choice == '3':
            name = input("Enter the name of the event to update: ")
            update_event(name)
        elif choice == '4':
            name = input("Enter the name of the event to delete: ")
            delete_event(name)
        elif choice == '5':
            print("Thank you for using the Event Planner. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


lgn_choices()
main_login()
main()
