"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Write a JavaScript function that calculates the rental cost for different watersports equipment available at Coastal Boat Rentals, based on daily rates.
Generated: DETERMINISTIC_b2accfcf192cbcd0
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the rental cost for watersports equipment based on daily rates.
 * 
 * @param {string} equipment - The type of equipment to rent (e.g., "kayak", "paddleboard", "jet ski").
 * @param {number} days - The number of days for which the equipment is rented.
 * @returns {number} - The total rental cost.
 * @throws {Error} - Throws an error if the equipment type is invalid or if days is not a positive integer.
 */
function calculateRentalCost(equipment, days) {
    // Define daily rental rates for each type of equipment
    const rentalRates = {
        kayak: 30,        // Daily rate for kayak
        paddleboard: 40,  // Daily rate for paddleboard
        jetski: 100       // Daily rate for jet ski
    };

    // Validate the equipment type
    if (!rentalRates[equipment]) {
        throw new Error(`Invalid equipment type: ${equipment}. Please choose from ${Object.keys(rentalRates).join(", ")}.`);
    }

    // Validate the days parameter
    if (!Number.isInteger(days) || days <= 0) {
        throw new Error(`Invalid number of days: ${days}. It must be a positive integer.`);
    }

    // Calculate the total rental cost
    const totalCost = rentalRates[equipment] * days;

    return totalCost;
}

// Example usage
try {
    const equipment = "kayak"; // Type of equipment
    const rentalDays = 5;      // Number of rental days
    const cost = calculateRentalCost(equipment, rentalDays);
    console.log(`The total rental cost for ${rentalDays} days of ${equipment} is $${cost}.`);
} catch (error) {
    console.error(error.message);
}
```
