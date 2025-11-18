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
 * 
 * @param {number} numAdults - The number of adult passengers.
 * @param {number} numChildren - The number of child passengers.
 * @param {number} numInfants - The number of infant passengers.
 * @param {Object} pricing - An object containing the pricing details.
 * @param {number} pricing.adultPrice - The price of one adult ticket.
 * @param {number} pricing.childPrice - The price of one child ticket.
 * @param {number} pricing.infantPrice - The price of one infant ticket.
 * @returns {number} - The total cost of the flight tickets.
 * @throws {Error} - Throws an error if invalid inputs are provided.
 */
function calculateTotalCost(numAdults, numChildren, numInfants, pricing) {
  // Input validation
  if (
    typeof numAdults !== 'number' || numAdults < 0 ||
    typeof numChildren !== 'number' || numChildren < 0 ||
    typeof numInfants !== 'number' || numInfants < 0 ||
    typeof pricing !== 'object' || pricing === null ||
    typeof pricing.adultPrice !== 'number' || pricing.adultPrice < 0 ||
    typeof pricing.childPrice !== 'number' || pricing.childPrice < 0 ||
    typeof pricing.infantPrice !== 'number' || pricing.infantPrice < 0
  ) {
    throw new Error("Invalid input. Please ensure all arguments are valid numbers and pricing is a valid object.");
  }

  // Calculate total cost
  const totalCost =
    (numAdults * pricing.adultPrice) +
    (numChildren * pricing.childPrice) +
    (numInfants * pricing.infantPrice);

  return totalCost;
}

// Example usage
try {
  const pricingModel = {
    adultPrice: 200,   // Cost per adult ticket
    childPrice: 150,   // Cost per child ticket
    infantPrice: 50    // Cost per infant ticket
  };

  const totalCost = calculateTotalCost(2, 1, 1, pricingModel);
  console.log(`Total cost: $${totalCost}`); // Output: Total cost: $600
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
