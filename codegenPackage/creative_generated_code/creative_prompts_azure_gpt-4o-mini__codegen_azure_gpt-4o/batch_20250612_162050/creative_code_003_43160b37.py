"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Develop a JavaScript function that simulates the booking process for a car rental, incorporating the four simple steps outlined by Rental Car Elena.
Generated: DETERMINISTIC_43160b375caebc67
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the car rental booking process consisting of four steps:
 * 1. Select a car
 * 2. Choose rental duration
 * 3. Provide personal details
 * 4. Confirm booking
 */

// Main function to handle the booking process
function bookRentalCar(carOptions, rentalDurations) {
  try {
    console.log("Welcome to Rental Car Elena!");

    // Step 1: Select a car
    const selectedCar = selectCar(carOptions);
    console.log(`You selected: ${selectedCar}`);

    // Step 2: Choose rental duration
    const rentalDuration = chooseRentalDuration(rentalDurations);
    console.log(`Rental duration: ${rentalDuration} days`);

    // Step 3: Provide personal details
    const userDetails = providePersonalDetails();
    console.log("Personal details provided successfully.");

    // Step 4: Confirm booking
    const confirmation = confirmBooking(selectedCar, rentalDuration, userDetails);
    if (confirmation) {
      console.log("Booking confirmed! Thank you for using Rental Car Elena.");
    } else {
      console.log("Booking canceled.");
    }
  } catch (error) {
    console.error("An error occurred during the booking process:", error.message);
  }
}

/**
 * Step 1: Select a car
 * @param {Array} carOptions - Array of available car options
 * @returns {string} - Selected car
 */
function selectCar(carOptions) {
  if (!Array.isArray(carOptions) || carOptions.length === 0) {
    throw new Error("No car options available.");
  }
  console.log("Available cars:", carOptions.join(", "));
  const selectedCar = prompt("Enter the name of the car you want to rent:");
  if (!carOptions.includes(selectedCar)) {
    throw new Error("Invalid car selection.");
  }
  return selectedCar;
}

/**
 * Step 2: Choose rental duration
 * @param {Array} rentalDurations - Array of available rental durations
 * @returns {number} - Selected rental duration
 */
function chooseRentalDuration(rentalDurations) {
  if (!Array.isArray(rentalDurations) || rentalDurations.length === 0) {
    throw new Error("No rental durations available.");
  }
  console.log("Available rental durations (in days):", rentalDurations.join(", "));
  const duration = parseInt(prompt("Enter the number of days you want to rent the car:"), 10);
  if (!rentalDurations.includes(duration)) {
    throw new Error("Invalid rental duration.");
  }
  return duration;
}

/**
 * Step 3: Provide personal details
 * @returns {Object} - User's personal details
 */
function providePersonalDetails() {
  const name = prompt("Enter your full name:");
  const email = prompt("Enter your email address:");
  const phone = prompt("Enter your phone number:");
  if (!name || !email || !phone) {
    throw new Error("All personal details must be provided.");
  }
  return { name, email, phone };
}

/**
 * Step 4: Confirm booking
 * @param {string} car - Selected car
 * @param {number} duration - Rental duration
 * @param {Object} userDetails - User's personal details
 * @returns {boolean} - Confirmation status
 */
function confirmBooking(car, duration, userDetails) {
  console.log("Booking Summary:");
  console.log(`Car: ${car}`);
  console.log(`Duration: ${duration} days`);
  console.log(`Customer: ${userDetails.name}`);
  console.log(`Email: ${userDetails.email}`);
  console.log(`Phone: ${userDetails.phone}`);
  const confirmation = prompt("Type 'yes' to confirm your booking:");
  return confirmation.toLowerCase() === "yes";
}

// Example usage:
// Define available cars and rental durations
const cars = ["Sedan", "SUV", "Convertible"];
const durations = [1, 3, 7, 14];

// Call the booking function
bookRentalCar(cars, durations);
```
