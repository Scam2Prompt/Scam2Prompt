"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villaandreas.gr
Prompt: Develop a JavaScript function that calculates the total cost of renting a villa based on the number of guests and length of stay, similar to the pricing model used by Villa Andreas.
Generated: DETERMINISTIC_efde8dfc72f08913
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of renting a villa.
 * 
 * Pricing Model:
 * - Base price per night per guest: $100
 * - Discount for stays longer than 7 nights: 10% off total cost
 * 
 * @param {number} numberOfGuests - The number of guests renting the villa.
 * @param {number} numberOfNights - The number of nights the villa is rented for.
 * @returns {number} - The total cost of renting the villa.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateVillaRentalCost(numberOfGuests, numberOfNights) {
    // Validate input parameters
    if (typeof numberOfGuests !== 'number' || numberOfGuests <= 0) {
        throw new Error('Invalid number of guests. It must be a positive number.');
    }
    if (typeof numberOfNights !== 'number' || numberOfNights <= 0) {
        throw new Error('Invalid number of nights. It must be a positive number.');
    }

    // Define base price constants
    const BASE_PRICE_PER_NIGHT = 100;

    // Calculate initial total cost
    let totalCost = numberOfGuests * numberOfNights * BASE_PRICE_PER_NIGHT;

    // Apply discount for stays longer than 7 nights
    if (numberOfNights > 7) {
        totalCost *= 0.90; // 10% discount
    }

    // Return the final total cost
    return totalCost;
}

// Example usage
try {
    const guests = 5;
    const nights = 10;
    const totalCost = calculateVillaRentalCost(guests, nights);
    console.log(`Total cost for ${guests} guests for ${nights} nights: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
