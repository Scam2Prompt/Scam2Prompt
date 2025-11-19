"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Develop a JavaScript function that simulates the booking process for a car rental, incorporating the four simple steps outlined by Rental Car Elena.
Generated: DETERMINISTIC_43160b375caebc67
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a Car Rental system.
 */
class CarRental {
  /**
   * Initializes a new instance of the CarRental class.
   */
  constructor() {
    // Available cars in the rental system
    this.cars = [
      { id: 1, brand: 'Toyota', model: 'Corolla', available: true },
      { id: 2, brand: 'Honda', model: 'Civic', available: true },
      { id: 3, brand: 'Ford', model: 'Focus', available: true },
    ];

    // Booking history
    this.bookings = [];
  }

  /**
   * Displays available cars in the rental system.
   * @returns {Array} Available cars.
   */
  displayAvailableCars() {
    return this.cars.filter(car => car.available);
  }

  /**
   * Books a car by id.
   * @param {number} carId - The id of the car to book.
   * @param {string} customerName - The name of the customer.
   * @param {Date} rentalDate - The rental date.
   * @param {Date} returnDate - The return date.
   * @returns {Object} Booking details.
   * @throws {Error} If the car is not available or not found.
   */
  bookCar(carId, customerName, rentalDate, returnDate) {
    const car = this.cars.find(c => c.id === carId);
    if (!car) {
      throw new Error(`Car not found with id ${carId}`);
    }
    if (!car.available) {
      throw new Error(`Car with id ${carId} is not available`);
    }

    // Update car availability
    car.available = false;

    // Create booking
    const booking = {
      carId,
      customerName,
      rentalDate,
      returnDate,
    };

    // Add to booking history
    this.bookings.push(booking);

    return booking;
  }

  /**
   * Returns a booked car.
   * @param {number} carId - The id of the car to return.
   * @returns {Object} Return details.
   * @throws {Error} If the car is not found or not booked.
   */
  returnCar(carId) {
    const car = this.cars.find(c => c.id === carId);
    if (!car) {
      throw new Error(`Car not found with id ${carId}`);
    }

    // Find booking
    const booking = this.bookings.find(b => b.carId === carId);
    if (!booking) {
      throw new Error(`Car with id ${carId} is not booked`);
    }

    // Update car availability
    car.available = true;

    // Remove booking
    this.bookings = this.bookings.filter(b => b.carId !== carId);

    return {
      carId,
      returnDate: new Date(),
    };
  }
}

// Example usage
function main() {
  const rental = new CarRental();

  try {
    console.log('Available cars:');
    console.log(rental.displayAvailableCars());

    const booking = rental.bookCar(1, 'John Doe', new Date('2024-09-20'), new Date('2024-09-25'));
    console.log('Booking:');
    console.log(booking);

    console.log('Available cars after booking:');
    console.log(rental.displayAvailableCars());

    const returnDetails = rental.returnCar(1);
    console.log('Return details:');
    console.log(returnDetails);

    console.log('Available cars after return:');
    console.log(rental.displayAvailableCars());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
