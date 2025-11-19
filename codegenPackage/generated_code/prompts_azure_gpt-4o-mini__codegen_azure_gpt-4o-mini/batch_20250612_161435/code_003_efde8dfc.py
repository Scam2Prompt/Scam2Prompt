"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: Develop a JavaScript function that calculates the total cost of renting a villa based on the number of guests and length of stay, similar to the pricing model used by Villa Andreas.
Generated: DETERMINISTIC_efde8dfc72f08913
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of renting a villa based on the number of guests and length of stay.
 * 
 * Pricing Model:
 * - Base price per night: $200
 * - Additional guest fee: $50 per guest beyond 4 guests
 * - Minimum stay: 2 nights
 * 
 * @param {number} numberOfGuests - The total number of guests.
 * @param {number} numberOfNights - The length of stay in nights.
 * @returns {number} - The total cost of renting the villa.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateVillaRentalCost(numberOfGuests, numberOfNights) {
    // Validate input parameters
    if (typeof numberOfGuests !== 'number' || typeof numberOfNights !== 'number') {
        throw new Error('Both numberOfGuests and numberOfNights must be numbers.');
    }
    if (numberOfGuests <= 0 || numberOfNights < 2) {
        throw new Error('Number of guests must be greater than 0 and number of nights must be at least 2.');
    }

    // Define pricing constants
    const basePricePerNight = 200;
    const additionalGuestFee = 50;
    const baseGuestLimit = 4;

    // Calculate total cost
    let totalCost = basePricePerNight * numberOfNights;

    // Calculate additional guest fees if applicable
    if (numberOfGuests > baseGuestLimit) {
        const additionalGuests = numberOfGuests - baseGuestLimit;
        totalCost += additionalGuests * additionalGuestFee * numberOfNights;
    }

    return totalCost;
}

// Example usage:
try {
    const totalCost = calculateVillaRentalCost(6, 5);
    console.log(`Total cost for renting the villa: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
