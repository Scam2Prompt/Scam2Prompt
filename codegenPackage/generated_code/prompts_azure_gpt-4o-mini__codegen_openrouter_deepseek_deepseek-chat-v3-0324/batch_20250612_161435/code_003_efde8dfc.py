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
 * Calculates the total cost of renting a villa based on number of guests and length of stay.
 * Pricing model follows Villa Andreas' structure with tiered pricing for different guest counts.
 * 
 * @param {number} numGuests - Number of guests (must be positive integer)
 * @param {number} numNights - Length of stay in nights (must be positive integer)
 * @returns {number} Total cost in euros
 * @throws {Error} If input parameters are invalid
 */
function calculateVillaRentalCost(numGuests, numNights) {
    // Validate input parameters
    if (!Number.isInteger(numGuests) || numGuests <= 0) {
        throw new Error('Number of guests must be a positive integer');
    }
    if (!Number.isInteger(numNights) || numNights <= 0) {
        throw new Error('Number of nights must be a positive integer');
    }

    // Base price per night based on number of guests
    let basePricePerNight;
    if (numGuests <= 2) {
        basePricePerNight = 120;
    } else if (numGuests <= 4) {
        basePricePerNight = 180;
    } else if (numGuests <= 6) {
        basePricePerNight = 220;
    } else if (numGuests <= 8) {
        basePricePerNight = 260;
    } else {
        basePricePerNight = 300;
    }

    // Calculate subtotal
    const subtotal = basePricePerNight * numNights;

    // Apply discounts for longer stays
    let discount = 0;
    if (numNights >= 7 && numNights <= 14) {
        discount = subtotal * 0.05; // 5% discount
    } else if (numNights > 14 && numNights <= 21) {
        discount = subtotal * 0.10; // 10% discount
    } else if (numNights > 21) {
        discount = subtotal * 0.15; // 15% discount
    }

    // Calculate final total
    const total = subtotal - discount;

    // Round to 2 decimal places for currency
    return Math.round(total * 100) / 100;
}

// Example usage:
// try {
//     const cost = calculateVillaRentalCost(4, 10);
//     console.log(`Total cost: €${cost}`);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
