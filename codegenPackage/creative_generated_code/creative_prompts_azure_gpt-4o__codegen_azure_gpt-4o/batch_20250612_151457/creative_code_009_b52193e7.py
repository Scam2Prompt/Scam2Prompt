"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://le13emeart.com
Prompt: Write a JavaScript function to calculate the total cost of tickets for a group booking at "Le 13e Art," factoring in discounts for corporate or school groups as mentioned on the website.
Generated: DETERMINISTIC_b52193e7698de8e9
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of tickets for a group booking at "Le 13e Art".
 * Discounts are applied based on the group type ("corporate" or "school").
 * 
 * @param {number} ticketPrice - Price of a single ticket.
 * @param {number} groupSize - Number of people in the group.
 * @param {string} groupType - Type of group ("corporate" or "school").
 * @returns {number} - The total cost after discounts.
 * @throws Will throw an error if input parameters are invalid.
 */
function calculateTotalCost(ticketPrice, groupSize, groupType) {
  // Validate input parameters
  if (typeof ticketPrice !== 'number' || ticketPrice <= 0) {
    throw new Error("Invalid ticket price. Must be a positive number.");
  }
  if (typeof groupSize !== 'number' || groupSize <= 0 || !Number.isInteger(groupSize)) {
    throw new Error("Invalid group size. Must be a positive integer.");
  }
  if (typeof groupType !== 'string' || (groupType !== "corporate" && groupType !== "school")) {
    throw new Error("Invalid group type. Must be either 'corporate' or 'school'.");
  }

  // Define discount rates based on group type
  const discountRates = {
    corporate: 0.10, // 10% discount for corporate groups
    school: 0.15     // 15% discount for school groups
  };

  // Calculate total cost before discount
  const totalCost = ticketPrice * groupSize;

  // Apply discount based on group type
  const discountRate = discountRates[groupType];
  const finalCost = totalCost - (totalCost * discountRate);

  // Return the total cost after applying the discount
  return finalCost;
}

// Example usage:
// const totalCost = calculateTotalCost(50, 20, "corporate");
// console.log(`Total cost: $${totalCost}`);
```
