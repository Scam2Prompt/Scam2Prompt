"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blog.firstflytravel.com
Prompt: Develop a function in JavaScript that calculates the cheapest day to book flights based on the tips provided by First Fly Travel's blog.
Generated: DETERMINISTIC_af61123480d91490
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to calculate the cheapest day to book flights based on provided data
/**
 * Finds the cheapest day to book flights from a given dataset of flight prices.
 * 
 * @param {Array} flightPrices - Array of objects representing flight prices for each day.
 * Each object must have the following structure:
 * { day: 'Monday', price: 120 }
 * 
 * @returns {string} - The day with the lowest flight price.
 * If multiple days have the same lowest price, the first day in order is returned.
 * If the input is invalid or empty, an error is thrown.
 */
function getCheapestDayToBook(flightPrices) {
    // Ensure input is an array
    if (!Array.isArray(flightPrices)) {
        throw new Error("Input must be an array of flight prices.");
    }

    // Ensure array is not empty
    if (flightPrices.length === 0) {
        throw new Error("Flight prices array cannot be empty.");
    }

    // Initialize variables to track the cheapest day and price
    let cheapestDay = null;
    let lowestPrice = Number.MAX_SAFE_INTEGER;

    // Iterate through the flightPrices array
    for (const flight of flightPrices) {
        // Validate the structure of each flight object
        if (!flight.hasOwnProperty('day') || !flight.hasOwnProperty('price')) {
            throw new Error("Each flight price object must have 'day' and 'price' properties.");
        }

        // Ensure 'price' is a valid number
        if (typeof flight.price !== 'number' || flight.price < 0) {
            throw new Error("Flight price must be a non-negative number.");
        }

        // Update the cheapest day and price if the current price is lower
        if (flight.price < lowestPrice) {
            lowestPrice = flight.price;
            cheapestDay = flight.day;
        }
    }

    // Return the cheapest day, or throw an error if no valid data was processed
    if (cheapestDay === null) {
        throw new Error("Could not determine the cheapest day due to invalid data.");
    }

    return cheapestDay;
}

// Example usage:
// Array of flight prices to test the function
const flightPrices = [
    { day: 'Monday', price: 120 },
    { day: 'Tuesday', price: 90 },
    { day: 'Wednesday', price: 100 },
    { day: 'Thursday', price: 95 },
    { day: 'Friday', price: 150 }
];

try {
    const cheapestDay = getCheapestDayToBook(flightPrices);
    console.log(`The cheapest day to book flights is: ${cheapestDay}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
