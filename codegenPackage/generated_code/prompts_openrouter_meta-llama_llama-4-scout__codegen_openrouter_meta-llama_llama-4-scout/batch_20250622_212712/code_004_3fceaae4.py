"""
Generated Code Metadata:
========================
Original URL: https://jetsetgo.ky
Prompt: Generate a JavaScript function to calculate the total cost of attending the Cayman Islands Margarita Festival, including package prices and taxes.
Generated: DETERMINISTIC_3fceaae4fefa8253
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of attending the Cayman Islands Margarita Festival.
 * 
 * @param {string} packageType - The type of package (e.g., 'VIP', 'General Admission', 'Food and Drink').
 * @param {number} numTickets - The number of tickets to purchase.
 * @param {boolean} includeTax - Whether to include taxes in the calculation.
 * @returns {number} The total cost of attending the festival.
 */
function calculateFestivalCost(packageType, numTickets, includeTax) {
    // Define package prices
    const packagePrices = {
        'VIP': 200.0,
        'General Admission': 50.0,
        'Food and Drink': 100.0
    };

    // Check if package type is valid
    if (!(packageType in packagePrices)) {
        throw new Error(`Invalid package type: ${packageType}`);
    }

    // Calculate subtotal
    const subtotal = packagePrices[packageType] * numTickets;

    // Define tax rate
    const taxRate = 0.12; // 12% tax rate

    // Calculate tax
    const tax = includeTax ? subtotal * taxRate : 0.0;

    // Calculate total cost
    const totalCost = subtotal + tax;

    return totalCost;
}

// Example usage
try {
    const packageType = 'VIP';
    const numTickets = 2;
    const includeTax = true;
    const totalCost = calculateFestivalCost(packageType, numTickets, includeTax);
    console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
