"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Write JavaScript code to implement a dynamic pricing calculator for services, including optional add-ons like 24-hour delivery, as offered on YourPalmReading.com.
Generated: DETERMINISTIC_2c5f21a2bd0f8f06
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Dynamic Pricing Calculator for YourPalmReading.com

// Function to calculate total price based on service and add-ons selected
function calculateTotalPrice(basePrice, addOns) {
    // Validate inputs
    if (typeof basePrice !== 'number' || basePrice < 0) {
        throw new Error('Base price must be a non-negative number.');
    }
    if (!Array.isArray(addOns)) {
        throw new Error('Add-ons must be provided as an array.');
    }

    // Initialize total price with the base price
    let totalPrice = basePrice;

    // Iterate over add-ons to calculate additional costs
    addOns.forEach(addOn => {
        if (typeof addOn.price !== 'number' || addOn.price < 0) {
            throw new Error(`Invalid price for add-on: ${addOn.name}. Must be a non-negative number.`);
        }
        totalPrice += addOn.price;
    });

    return totalPrice.toFixed(2); // Return total price formatted to 2 decimal places
}

// Example usage of the pricing calculator
try {
    const baseServicePrice = 50; // Base price for palm reading service
    const selectedAddOns = [
        { name: '24-Hour Delivery', price: 15 }, // Additional cost for expedited delivery
        { name: 'Detailed Report', price: 10 } // Additional cost for a detailed report
    ];

    const totalCost = calculateTotalPrice(baseServicePrice, selectedAddOns);
    console.log(`Total Price: $${totalCost}`); // Output the total price
} catch (error) {
    console.error(`Error calculating total price: ${error.message}`);
}
```
