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
 * Function to calculate the total cost of renting a villa.
 * 
 * @param {number} numGuests - The number of guests staying at the villa.
 * @param {number} numDays - The number of days the villa is being rented.
 * @returns {number} - The total cost of the rental.
 * 
 * Pricing model: 
 * - Base rate per day: $200
 * - Additional cost per guest beyond 2 guests: $50 per guest per day
 * - Discounts: 
 *   - 10% discount for stays longer than 7 days
 * 
 * Error Handling:
 * - Throws an error if input values are invalid (e.g., negative numbers).
 */
function calculateVillaRentalCost(numGuests, numDays) {
  // Input validation
  if (numGuests <= 0 || numDays <= 0 || !Number.isInteger(numGuests) || !Number.isInteger(numDays)) {
    throw new Error("Invalid input: numGuests and numDays must be positive integers.");
  }

  // Constants for pricing
  const BASE_RATE_PER_DAY = 200;
  const ADDITIONAL_GUEST_COST_PER_DAY = 50;
  const BASE_GUEST_COUNT = 2;
  const DISCOUNT_THRESHOLD_DAYS = 7;
  const DISCOUNT_RATE = 0.10;

  // Calculate base cost
  let totalBaseCost = BASE_RATE_PER_DAY * numDays;

  // Calculate additional guest cost if there are more than BASE_GUEST_COUNT guests
  let additionalGuestCost = 0;
  if (numGuests > BASE_GUEST_COUNT) {
    additionalGuestCost = (numGuests - BASE_GUEST_COUNT) * ADDITIONAL_GUEST_COST_PER_DAY * numDays;
  }

  // Combine base cost and additional guest cost
  let totalCost = totalBaseCost + additionalGuestCost;

  // Apply discount if the stay exceeds the discount threshold
  if (numDays > DISCOUNT_THRESHOLD_DAYS) {
    totalCost -= totalCost * DISCOUNT_RATE;
  }

  // Return the final total cost
  return totalCost;
}

// Example usage:
try {
  const totalCost = calculateVillaRentalCost(4, 10);
  console.log(`Total Cost: $${totalCost}`); // Should correctly calculate based on input
} catch (error) {
  console.error(error.message);
}
```
