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
 * Calculate the total cost for a group booking of horse riding tours.
 * 
 * Pricing structure:
 * - Adult price: $50 per person
 * - Child price (under 12 years): $30 per child
 * - Discount: 10% off for groups larger than 10 people
 * 
 * @param {number} numAdults - Number of adults participating.
 * @param {number} numChildren - Number of children participating.
 * @returns {number} - Total cost for the booking.
 * @throws {Error} - Throws error if inputs are invalid.
 */
function calculateHorseRidingCost(numAdults, numChildren) {
  // Validate inputs
  if (!Number.isInteger(numAdults) || numAdults < 0) {
    throw new Error("Invalid number of adults. It must be a non-negative integer.");
  }
  if (!Number.isInteger(numChildren) || numChildren < 0) {
    throw new Error("Invalid number of children. It must be a non-negative integer.");
  }

  // Pricing constants
  const ADULT_PRICE = 50; // Cost per adult
  const CHILD_PRICE = 30; // Cost per child
  const GROUP_DISCOUNT_THRESHOLD = 10; // Minimum group size for discount
  const DISCOUNT_RATE = 0.10; // 10% discount

  // Calculate total participants
  const totalParticipants = numAdults + numChildren;

  // Calculate the total cost without discount
  const totalCostWithoutDiscount = (numAdults * ADULT_PRICE) + (numChildren * CHILD_PRICE);

  // Apply discount if the group size exceeds the threshold
  const totalCost = totalParticipants > GROUP_DISCOUNT_THRESHOLD
    ? totalCostWithoutDiscount * (1 - DISCOUNT_RATE)
    : totalCostWithoutDiscount;

  // Return the final total cost rounded to two decimal places
  return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
  const totalCost = calculateHorseRidingCost(8, 4); // 8 adults, 4 children
  console.log(`Total booking cost: $${totalCost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
