"""
Generated Code Metadata:
========================
Original URL: https://celestia.homes
Prompt: Create a JavaScript function to calculate the total cost of purchasing a property in Estepona, considering factors like price, taxes, and fees, as mentioned in Celestia Homes' brochures.
Generated: DETERMINISTIC_7fd69f3006d54f0e
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of purchasing a property in Estepona.
 * 
 * @param {number} propertyPrice - The base price of the property.
 * @param {number} taxRate - The applicable tax rate (as a decimal, e.g., 0.1 for 10%).
 * @param {number} fees - Additional fees associated with the purchase (e.g., notary fees, registration).
 * @returns {number} - The total cost of purchasing the property.
 * @throws {Error} - Throws an error if any input is invalid (negative values).
 */
function calculateTotalCost(propertyPrice, taxRate, fees) {
    // Validate inputs
    if (typeof propertyPrice !== 'number' || propertyPrice < 0) {
        throw new Error('Invalid property price. It must be a non-negative number.');
    }
    if (typeof taxRate !== 'number' || taxRate < 0) {
        throw new Error('Invalid tax rate. It must be a non-negative number.');
    }
    if (typeof fees !== 'number' || fees < 0) {
        throw new Error('Invalid fees. It must be a non-negative number.');
    }

    // Calculate tax amount
    const taxAmount = propertyPrice * taxRate;

    // Calculate total cost
    const totalCost = propertyPrice + taxAmount + fees;

    return totalCost;
}

// Example usage:
try {
    const propertyPrice = 300000; // Example property price
    const taxRate = 0.1; // Example tax rate (10%)
    const fees = 5000; // Example additional fees

    const totalCost = calculateTotalCost(propertyPrice, taxRate, fees);
    console.log(`The total cost of purchasing the property is: €${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
