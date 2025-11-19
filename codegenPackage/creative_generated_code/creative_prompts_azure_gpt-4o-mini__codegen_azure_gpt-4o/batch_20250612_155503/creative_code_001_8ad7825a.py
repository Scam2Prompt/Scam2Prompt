"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thresholdsummer.org
Prompt: Write a JavaScript function that calculates the registration fees for the Threshold Summer Meeting based on the purchase date and applies discounts for early registration.
Generated: DETERMINISTIC_8ad7825aa7bfddcc
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate registration fees for the Threshold Summer Meeting
 * based on purchase date and apply early registration discounts.
 *
 * @param {Date} purchaseDate - The date when the registration was made.
 * @returns {number} - The calculated registration fee.
 * @throws {Error} - Throws an error if purchaseDate is invalid.
 */
function calculateRegistrationFee(purchaseDate) {
  // Validate input
  if (!(purchaseDate instanceof Date) || isNaN(purchaseDate)) {
    throw new Error('Invalid purchase date. Expected a valid Date object.');
  }

  // Define constants for fee structure
  const baseFee = 150; // Base registration fee in USD
  const earlyBirdDiscount = 0.2; // 20% discount for early registration
  const earlyBirdDeadline = new Date('2023-06-01'); // Early registration deadline

  let finalFee = baseFee;

  // Check if the registration qualifies for the early bird discount
  if (purchaseDate < earlyBirdDeadline) {
    finalFee -= baseFee * earlyBirdDiscount; // Apply discount
  }

  return finalFee;
}

// Example usage:
try {
  const purchaseDate = new Date('2023-05-15');
  const fee = calculateRegistrationFee(purchaseDate);
  console.log(`The registration fee is: $${fee}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
