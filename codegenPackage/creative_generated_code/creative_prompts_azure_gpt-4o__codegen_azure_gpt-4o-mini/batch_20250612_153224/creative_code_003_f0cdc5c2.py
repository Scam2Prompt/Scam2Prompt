"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Write a JavaScript function to calculate the total cost for a group booking of horse riding tours, factoring in the number of participants and children, as outlined on the Chile Horse Riding reservation form.
Generated: DETERMINISTIC_f0cdc5c2f600475f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost for a group booking of horse riding tours.
 * 
 * @param {number} adultPrice - The price per adult participant.
 * @param {number} childPrice - The price per child participant.
 * @param {number} numAdults - The total number of adult participants.
 * @param {number} numChildren - The total number of child participants.
 * @returns {number} - The total cost for the booking.
 * @throws {Error} - Throws an error if any of the input values are negative
 *                   or if the input types are incorrect.
 */
function calculateTotalCost(adultPrice, childPrice, numAdults, numChildren) {
    // Validate input types and values
    if (typeof adultPrice !== 'number' || typeof childPrice !== 'number' || 
        typeof numAdults !== 'number' || typeof numChildren !== 'number') {
        throw new Error('All parameters must be numbers.');
    }
    
    if (adultPrice < 0 || childPrice < 0 || numAdults < 0 || numChildren < 0) {
        throw new Error('Prices and participant numbers cannot be negative.');
    }

    // Calculate total cost
    const totalCost = (adultPrice * numAdults) + (childPrice * numChildren);

    return totalCost;
}

// Example usage
try {
    const adultPrice = 50; // price per adult
    const childPrice = 30; // price per child
    const numAdults = 3;   // number of adults
    const numChildren = 2; // number of children

    const total = calculateTotalCost(adultPrice, childPrice, numAdults, numChildren);
    console.log(`Total cost for the booking: $${total}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
