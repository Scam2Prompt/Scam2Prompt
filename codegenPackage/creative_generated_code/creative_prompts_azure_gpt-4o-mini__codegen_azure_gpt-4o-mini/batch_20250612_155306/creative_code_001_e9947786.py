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
 * Calculates the monthly lease payment for a domain name based on the total price.
 *
 * @param {number} totalPrice - The total price of the domain name.
 * @param {number} leaseDurationMonths - The duration of the lease in months.
 * @returns {number} - The monthly lease payment.
 * @throws {Error} - Throws an error if the parameters are invalid.
 */
function calculateMonthlyLeasePayment(totalPrice, leaseDurationMonths) {
    // Input validation
    if (typeof totalPrice !== 'number' || totalPrice <= 0) {
        throw new Error('Total price must be a positive number.');
    }
    if (typeof leaseDurationMonths !== 'number' || leaseDurationMonths <= 0) {
        throw new Error('Lease duration must be a positive number.');
    }

    // Calculate monthly lease payment
    const monthlyPayment = totalPrice / leaseDurationMonths;

    return parseFloat(monthlyPayment.toFixed(2)); // Round to two decimal places
}

// Example usage:
try {
    const totalPrice = 5000; // Total price of the domain name
    const leaseDurationMonths = 12; // Lease duration in months
    const monthlyPayment = calculateMonthlyLeasePayment(totalPrice, leaseDurationMonths);
    console.log(`The monthly lease payment is: $${monthlyPayment}`);
} catch (error) {
    console.error(`Error calculating monthly lease payment: ${error.message}`);
}
```
