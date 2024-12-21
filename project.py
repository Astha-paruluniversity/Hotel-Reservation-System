#Hotel Reservation System
total_rooms = 10
rooms = [{"room_id": i + 1, "status": "available"} for i in range(total_rooms)]

# Display current room statuses
def display_rooms():
    print("\nRoom Status:")
    for room in rooms:
        print("Room {room['room_id']}: {room['status']}")

# Check available rooms
def check_availability():
    available_rooms = [room['room_id'] for room in rooms if room['status'] == "available"]
    if available_rooms:
        print("\nAvailable Rooms:", available_rooms)
    else:
        print("\nNo rooms available.")

# Book a room by ID
def book_room(room_id):
    if room_id <= 0 or room_id > len(rooms):
        print("\nInvalid room ID.")
        return
    room = rooms[room_id - 1]
    if room['status'] == "available":
        room['status'] = "booked"
        print("\nRoom {room_id} has been successfully booked.")
    else:
        print("\nRoom {room_id} is already booked.")

# Cancel room booking by ID
def cancel_booking(room_id):
    if room_id <= 0 or room_id > len(rooms):
        print("\nInvalid room ID.")
        return
    room = rooms[room_id - 1]
    if room['status'] == "booked":
        room['status'] = "available"
        print("\nBooking for Room {room_id} has been successfully canceled.")
    else:
        print("\nRoom {room_id} is not booked yet.")

# Main program loop
def main():
    while True:
        print("\nHotel Room Booking System")
        print("1. Check Availability")
        print("2. Book a Room")
        print("3. Cancel a Booking")
        print("4. Display Room Status")
        print("5. Exit")
        
        choice = input("Please choose an option (1-5): ")
        
        if choice == "1":
            check_availability()
        elif choice == "2":
            try:
                room_id = int(input("\nEnter room ID to book: "))
                book_room(room_id)
            except ValueError:
                print("\nInvalid input. Please enter a valid room ID.")
        elif choice == "3":
            try:
                room_id = int(input("\nEnter room ID to cancel booking: "))
                cancel_booking(room_id)
            except ValueError:
                print("\nInvalid input. Please enter a valid room ID.")
        elif choice == "4":
            display_rooms()
        elif choice == "5":
            print("\nThank you for using the Hotel Booking System!")
            break
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()
