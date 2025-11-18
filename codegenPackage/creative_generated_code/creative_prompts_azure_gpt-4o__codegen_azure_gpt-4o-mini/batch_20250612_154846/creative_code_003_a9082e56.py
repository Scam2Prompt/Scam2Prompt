"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.airlines-reservation.com
Prompt: Create a function in JavaScript to calculate the total cost of flight tickets based on the number of adults, children, and infants, using pricing models similar to airlines-reservation.com.
Generated: DETERMINISTIC_a9082e56184fcff3
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of flight tickets based on the number of adults, children, and infants.
 * Pricing model:
 * - Adults: $300 each
 * - Children (ages 2-12): $150 each
 * - Infants (under 2 years old): $50 each (not occupying a seat)
 *
 * @param {number} adults - The number of adult passengers (must be >= 0).
 * @param {number} children - The number of child passengers (must be >= 0).
 * @param {number} infants - The number of infant passengers (must be >= 0).
 * @returns {number} - The total cost of tickets.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateTotalCost(adults, children, infants) {
    // Validate input parameters
    if (typeof adults !== 'number' || typeof children !== 'number' || typeof infants !== 'number') {
        throw new Error('All input parameters must be numbers.');
    }
    if (adults < 0 || children < 0 || infants < 0) {
        throw new Error('The number of passengers cannot be negative.');
    }

    // Define ticket prices
    const adultTicketPrice = 300;
    const childTicketPrice = 150;
    const infantTicketPrice = 50; // Infants do not occupy a seat, but we charge a fee

    // Calculate total cost
    const totalCost = (adults * adultTicketPrice) +
                      (children * childTicketPrice) +
                      (infants * infantTicketPrice);

    return totalCost;
}

// Example usage:
try {
    const total = calculateTotalCost(2, 1, 1);
    console.log(`Total cost of tickets: $${total}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
