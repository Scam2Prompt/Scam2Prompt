"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioti.fi
Prompt: Generate a JavaScript function that calculates the monthly lease payment for a domain name based on a total price of $5,000, as mentioned on the symbioti.fi site.
Generated: DETERMINISTIC_e994778640856732
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the monthly lease payment for a domain name.
 * 
 * The calculation assumes a total price of $5,000 and a standard lease term 
 * of 12 months. It accounts for the possibility of interest rates or other
 * factors in the future, but currently assumes no added fees or interest.
 * 
 * @param {number} totalPrice - The total price of the domain name (default is $5,000).
 * @param {number} leaseTermMonths - The number of months for the lease term (default is 12).
 * @returns {number} - The calculated monthly payment.
 * @throws {Error} - Throws an error if the input values are invalid or non-positive.
 */
function calculateMonthlyLeasePayment(totalPrice = 5000, leaseTermMonths = 12) {
  // Validate inputs
  if (totalPrice <= 0 || leaseTermMonths <= 0) {
    throw new Error("Total price and lease term must be positive numbers.");
  }

  // Calculate the monthly payment
  const monthlyPayment = totalPrice / leaseTermMonths;

  // Round to two decimal places for currency formatting
  return parseFloat(monthlyPayment.toFixed(2));
}

// Example usage:
try {
  const monthlyPayment = calculateMonthlyLeasePayment();
  console.log(`Monthly Lease Payment: $${monthlyPayment}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
