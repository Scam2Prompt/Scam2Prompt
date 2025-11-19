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
 * Pricing model:
 * - Base rate per night: $200
 * - Additional guest fee (per guest per night beyond 4 guests): $50
 * - Discount for stays longer than 7 nights: 10% off total cost
 * 
 * @param {number} numGuests - The number of guests staying in the villa.
 * @param {number} numNights - The number of nights the villa is rented for.
 * @returns {number} - The total cost of the villa rental.
 * @throws {Error} - Throws an error if inputs are invalid (e.g., negative numbers or non-numeric values).
 */
function calculateVillaRentalCost(numGuests, numNights) {
    // Input validation
    if (typeof numGuests !== 'number' || typeof numNights !== 'number') {
        throw new Error("Both numGuests and numNights must be numbers.");
    }
    if (numGuests <= 0 || numNights <= 0) {
        throw new Error("Both numGuests and numNights must be positive numbers.");
    }

    // Constants for pricing
    const BASE_RATE_PER_NIGHT = 200; // Base rate for up to 4 guests
    const ADDITIONAL_GUEST_FEE = 50; // Fee per additional guest per night
    const DISCOUNT_THRESHOLD = 7; // Nights required for discount
    const DISCOUNT_RATE = 0.10; // 10% discount

    // Calculate base cost
    let baseCost = BASE_RATE_PER_NIGHT * numNights;

    // Calculate additional guest fees (if more than 4 guests)
    let additionalGuestFee = 0;
    if (numGuests > 4) {
        additionalGuestFee = (numGuests - 4) * ADDITIONAL_GUEST_FEE * numNights;
    }

    // Calculate total cost before discount
    let totalCost = baseCost + additionalGuestFee;

    // Apply discount for stays longer than the discount threshold
    if (numNights > DISCOUNT_THRESHOLD) {
        totalCost -= totalCost * DISCOUNT_RATE;
    }

    // Return the final total cost
    return totalCost;
}

// Example usage:
try {
    const totalCost = calculateVillaRentalCost(6, 10); // 6 guests, 10 nights
    console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
