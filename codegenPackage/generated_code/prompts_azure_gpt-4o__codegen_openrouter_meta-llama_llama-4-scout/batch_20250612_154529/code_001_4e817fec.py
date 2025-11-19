"""
Generated Code Metadata:
========================
Original URL: https://www.tripocost.com
Prompt: Create a JavaScript function that mimics Tripocost's hotel search feature, allowing users to input destination, check-in and check-out dates, and the number of rooms and guests.
Generated: DETERMINISTIC_4e817fec3a37377e
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * HotelSearch class that mimics Tripocost's hotel search feature.
 */
class HotelSearch {
  /**
   * Constructor for HotelSearch.
   * @param {Object} hotels - Available hotels data.
   */
  constructor(hotels) {
    this.hotels = hotels;
  }

  /**
   * Searches for hotels based on user's input.
   * @param {string} destination - Destination name.
   * @param {Date} checkInDate - Check-in date.
   * @param {Date} checkOutDate - Check-out date.
   * @param {number} numRooms - Number of rooms.
   * @param {number} numGuests - Number of guests.
   * @returns {Object[]} Available hotels that match the search criteria.
   */
  searchHotels(destination, checkInDate, checkOutDate, numRooms, numGuests) {
    // Validate input parameters
    if (!destination || !checkInDate || !checkOutDate || numRooms <= 0 || numGuests <= 0) {
      throw new Error('Invalid search parameters');
    }

    // Filter hotels by destination
    const destinationHotels = this.hotels.filter(hotel => hotel.destination === destination);

    // Filter hotels by availability
    const availableHotels = destinationHotels.filter(hotel => {
      // Assume hotel.availability is an array of objects with checkIn and checkOut dates
      return hotel.availability.some(availability => {
        return (availability.checkIn <= checkInDate && availability.checkOut >= checkOutDate) ||
               (availability.checkIn >= checkInDate && availability.checkOut <= checkOutDate) ||
               (availability.checkIn <= checkInDate && availability.checkIn >= checkOutDate) ||
               (availability.checkOut >= checkOutDate && availability.checkOut <= checkInDate);
      });
    });

    // Filter hotels by number of rooms and guests
    const suitableHotels = availableHotels.filter(hotel => hotel.capacity >= numGuests && hotel.roomsAvailable >= numRooms);

    return suitableHotels;
  }
}

// Example usage:
const hotels = [
  {
    id: 1,
    name: 'Hotel A',
    destination: 'New York',
    capacity: 100,
    roomsAvailable: 50,
    availability: [
      { checkIn: new Date('2024-01-01'), checkOut: new Date('2024-01-31') },
      { checkIn: new Date('2024-03-01'), checkOut: new Date('2024-03-31') }
    ]
  },
  {
    id: 2,
    name: 'Hotel B',
    destination: 'New York',
    capacity: 50,
    roomsAvailable: 20,
    availability: [
      { checkIn: new Date('2024-01-15'), checkOut: new Date('2024-02-15') },
      { checkIn: new Date('2024-04-01'), checkOut: new Date('2024-04-30') }
    ]
  },
  {
    id: 3,
    name: 'Hotel C',
    destination: 'Los Angeles',
    capacity: 200,
    roomsAvailable: 100,
    availability: [
      { checkIn: new Date('2024-01-01'), checkOut: new Date('2024-12-31') }
    ]
  }
];

const hotelSearch = new HotelSearch(hotels);

try {
  const searchResults = hotelSearch.searchHotels('New York', new Date('2024-01-20'), new Date('2024-01-25'), 2, 4);
  console.log(searchResults);
} catch (error) {
  console.error(error.message);
}
```
