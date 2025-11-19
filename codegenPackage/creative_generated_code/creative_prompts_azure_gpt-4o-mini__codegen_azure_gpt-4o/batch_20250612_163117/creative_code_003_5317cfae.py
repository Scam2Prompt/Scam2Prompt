"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saltydazeusvi.com
Prompt: Develop a JavaScript function that calculates the total cost for a group booking on the Salt + Lime Express shuttle to Lime Out, based on the number of participants.
Generated: DETERMINISTIC_5317cfaebab34fbc
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost for a group booking on the Salt + Lime Express shuttle.
 * 
 * Pricing Details:
 * - Base price per participant: $25
 * - Discount for groups of 10 or more: 10% off total cost
 *
 * @param {number} numParticipants - The number of participants in the group.
 * @returns {number} The total cost for the group booking, or -1 if input is invalid.
 */
function calculateGroupBookingCost(numParticipants) {
  const BASE_PRICE_PER_PERSON = 25; // Base price per participant in dollars
  const DISCOUNT_THRESHOLD = 10; // Minimum number of participants required for a discount
  const DISCOUNT_RATE = 0.10; // Discount rate for groups of 10 or more

  try {
    // Validate input
    if (typeof numParticipants !== 'number' || numParticipants <= 0 || !Number.isInteger(numParticipants)) {
      throw new Error('Invalid input: numParticipants must be a positive integer.');
    }

    // Calculate total base cost
    const totalBaseCost = numParticipants * BASE_PRICE_PER_PERSON;

    // Apply discount if group size meets or exceeds the threshold
    const finalCost = numParticipants >= DISCOUNT_THRESHOLD 
      ? totalBaseCost * (1 - DISCOUNT_RATE) 
      : totalBaseCost;

    return finalCost;
  } catch (error) {
    console.error(error.message);
    return -1; // Return -1 to indicate an error in calculation
  }
}

// Example usage:
// console.log(calculateGroupBookingCost(5));  // Output: 125
// console.log(calculateGroupBookingCost(15)); // Output: 337.5
// console.log(calculateGroupBookingCost('five')); // Output: -1
```
