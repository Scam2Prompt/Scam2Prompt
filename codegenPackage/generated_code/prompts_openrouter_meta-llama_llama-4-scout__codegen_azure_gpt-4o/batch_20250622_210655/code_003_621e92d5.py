"""
Generated Code Metadata:
========================
Original URL: https://lhotel-des-chats.com
Prompt: Write a JavaScript code snippet to create a simple room booking system for a cat hotel, with options for individual and shared rooms.
Generated: DETERMINISTIC_621e92d5eae995ee
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Room Booking System for a Cat Hotel

// Define the Room class
class Room {
  constructor(id, type, capacity) {
    this.id = id; // Unique identifier for the room
    this.type = type; // Type of room: 'individual' or 'shared'
    this.capacity = capacity; // Maximum number of cats the room can accommodate
    this.bookedCats = []; // Array to store booked cats
  }

  // Method to check if the room has available space
  hasAvailability() {
    return this.bookedCats.length < this.capacity;
  }

  // Method to book a cat into the room
  bookCat(catName) {
    if (!this.hasAvailability()) {
      throw new Error(`Room ${this.id} is fully booked.`);
    }
    this.bookedCats.push(catName);
  }

  // Method to cancel a booking for a specific cat
  cancelBooking(catName) {
    const index = this.bookedCats.indexOf(catName);
    if (index === -1) {
      throw new Error(`Cat ${catName} is not booked in Room ${this.id}.`);
    }
    this.bookedCats.splice(index, 1);
  }

  // Method to get the current booking status
  getBookingStatus() {
    return {
      roomId: this.id,
      type: this.type,
      capacity: this.capacity,
      bookedCats: this.bookedCats,
      availableSlots: this.capacity - this.bookedCats.length,
    };
  }
}

// Define the CatHotel class
class CatHotel {
  constructor() {
    this.rooms = []; // Array to store all rooms in the hotel
  }

  // Method to add a new room to the hotel
  addRoom(id, type, capacity) {
    if (this.rooms.some((room) => room.id === id)) {
      throw new Error(`Room with ID ${id} already exists.`);
    }
    const newRoom = new Room(id, type, capacity);
    this.rooms.push(newRoom);
  }

  // Method to find a room by its ID
  findRoomById(id) {
    const room = this.rooms.find((room) => room.id === id);
    if (!room) {
      throw new Error(`Room with ID ${id} not found.`);
    }
    return room;
  }

  // Method to book a cat into a specific room
  bookCat(roomId, catName) {
    const room = this.findRoomById(roomId);
    room.bookCat(catName);
  }

  // Method to cancel a booking for a specific cat
  cancelBooking(roomId, catName) {
    const room = this.findRoomById(roomId);
    room.cancelBooking(catName);
  }

  // Method to get the booking status of all rooms
  getAllBookingStatuses() {
    return this.rooms.map((room) => room.getBookingStatus());
  }
}

// Example usage:

try {
  const hotel = new CatHotel();

  // Add rooms to the hotel
  hotel.addRoom(1, 'individual', 1); // Room 1: Individual room with capacity for 1 cat
  hotel.addRoom(2, 'shared', 3); // Room 2: Shared room with capacity for 3 cats

  // Book cats into rooms
  hotel.bookCat(1, 'Whiskers'); // Book Whiskers into Room 1
  hotel.bookCat(2, 'Mittens'); // Book Mittens into Room 2
  hotel.bookCat(2, 'Shadow'); // Book Shadow into Room 2

  // Cancel a booking
  hotel.cancelBooking(2, 'Mittens'); // Cancel Mittens' booking in Room 2

  // Get booking statuses
  console.log(hotel.getAllBookingStatuses());
} catch (error) {
  console.error(error.message); // Handle errors gracefully
}
```
