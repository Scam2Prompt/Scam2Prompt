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
// RoomBookingSystem.js

/**
 * Represents a Room in the cat hotel.
 */
class Room {
  /**
   * Creates a new Room.
   * @param {number} id - Unique room identifier.
   * @param {string} type - Type of room (individual or shared).
   * @param {boolean} isBooked - Whether the room is booked or not.
   */
  constructor(id, type, isBooked = false) {
    this.id = id;
    this.type = type;
    this.isBooked = isBooked;
  }

  /**
   * Books the room.
   * @throws {Error} If the room is already booked.
   */
  bookRoom() {
    if (this.isBooked) {
      throw new Error(`Room ${this.id} is already booked.`);
    }
    this.isBooked = true;
  }

  /**
   * Cancels the room booking.
   * @throws {Error} If the room is not booked.
   */
  cancelBooking() {
    if (!this.isBooked) {
      throw new Error(`Room ${this.id} is not booked.`);
    }
    this.isBooked = false;
  }
}

/**
 * Represents the Cat Hotel room booking system.
 */
class CatHotelBookingSystem {
  /**
   * Creates a new CatHotelBookingSystem.
   */
  constructor() {
    this.rooms = [];
  }

  /**
   * Adds a new room to the system.
   * @param {Room} room - Room to add.
   */
  addRoom(room) {
    this.rooms.push(room);
  }

  /**
   * Books a room by id.
   * @param {number} roomId - Id of the room to book.
   * @throws {Error} If the room does not exist or is already booked.
   */
  bookRoom(roomId) {
    const room = this.rooms.find((r) => r.id === roomId);
    if (!room) {
      throw new Error(`Room ${roomId} does not exist.`);
    }
    room.bookRoom();
  }

  /**
   * Cancels a room booking by id.
   * @param {number} roomId - Id of the room to cancel.
   * @throws {Error} If the room does not exist or is not booked.
   */
  cancelBooking(roomId) {
    const room = this.rooms.find((r) => r.id === roomId);
    if (!room) {
      throw new Error(`Room ${roomId} does not exist.`);
    }
    room.cancelBooking();
  }

  /**
   * Lists all rooms in the system.
   * @returns {Room[]} Array of rooms.
   */
  listRooms() {
    return this.rooms;
  }
}

// Example usage:
function main() {
  const bookingSystem = new CatHotelBookingSystem();

  // Create rooms
  const room1 = new Room(1, 'individual');
  const room2 = new Room(2, 'shared');
  const room3 = new Room(3, 'individual');

  // Add rooms to the system
  bookingSystem.addRoom(room1);
  bookingSystem.addRoom(room2);
  bookingSystem.addRoom(room3);

  // List rooms
  console.log('Available rooms:');
  bookingSystem.listRooms().forEach((room) => {
    console.log(`Room ${room.id} (${room.type}) - Booked: ${room.isBooked}`);
  });

  // Book a room
  bookingSystem.bookRoom(1);
  console.log('After booking room 1:');
  console.log(`Room ${room1.id} (${room1.type}) - Booked: ${room1.isBooked}`);

  // Try to book an already booked room
  try {
    bookingSystem.bookRoom(1);
  } catch (error) {
    console.error(error.message);
  }

  // Cancel a booking
  bookingSystem.cancelBooking(1);
  console.log('After cancelling room 1 booking:');
  console.log(`Room ${room1.id} (${room1.type}) - Booked: ${room1.isBooked}`);
}

main();
```
