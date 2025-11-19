"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.com
Prompt: Generate a JavaScript function that calculates the total cost for a group tour package to Gunung Bromo, including Jeep rental and accommodation at a homestay.
Generated: DETERMINISTIC_65a2f0a962f378e5
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
 * Calculates the total cost for a group tour package to Gunung Bromo.
 * 
 * @param {number} numberOfPeople - The total number of participants in the tour.
 * @param {number} jeepRentalCost - The cost of renting a Jeep for the tour.
 * @param {number} accommodationCostPerNight - The cost of accommodation at a homestay per night.
 * @param {number} numberOfNights - The number of nights for the accommodation.
 * @returns {number} The total cost of the tour package.
 * @throws {Error} Throws an error if any of the input values are invalid.
 */
function calculateTourCost(numberOfPeople, jeepRentalCost, accommodationCostPerNight, numberOfNights) {
    // Validate input parameters
    if (typeof numberOfPeople !== 'number' || numberOfPeople <= 0) {
        throw new Error('Invalid number of people. It must be a positive number.');
    }
    if (typeof jeepRentalCost !== 'number' || jeepRentalCost < 0) {
        throw new Error('Invalid Jeep rental cost. It cannot be negative.');
    }
    if (typeof accommodationCostPerNight !== 'number' || accommodationCostPerNight < 0) {
        throw new Error('Invalid accommodation cost per night. It cannot be negative.');
    }
    if (typeof numberOfNights !== 'number' || numberOfNights <= 0) {
        throw new Error('Invalid number of nights. It must be a positive number.');
    }

    // Calculate the total cost components
    const totalJeepCost = jeepRentalCost; // Assuming the cost covers the entire group
    const totalAccommodationCost = accommodationCostPerNight * numberOfNights * numberOfPeople;

    // Calculate the total cost
    const totalCost = totalJeepCost + totalAccommodationCost;

    return totalCost;
}

// Example usage:
// const totalCost = calculateTourCost(5, 500, 150, 2);
// console.log('Total Tour Cost:', totalCost);
```
