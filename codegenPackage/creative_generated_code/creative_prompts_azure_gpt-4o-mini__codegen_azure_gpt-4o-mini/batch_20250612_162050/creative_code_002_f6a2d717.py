"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingoficecream.com
Prompt: Write a JavaScript function to calculate the total sales for a snow cone truck based on different flavors and prices.
Generated: DETERMINISTIC_f6a2d717caa80028
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total sales from a snow cone truck based on various flavors and their associated sales.
 * 
 * @param {Object} sales - An object representing the sales data.
 * @param {Object} sales.flavors - An object where keys are flavor names and values are their prices.
 * @param {Object} sales.quantity - An object where keys are flavor names and values are the quantity sold.
 * @returns {number} - The total sales amount.
 * @throws {Error} - Throws an error if the sales data is not formatted correctly.
 */
function calculateTotalSales(sales) {
    // Validate the input data structure
    if (!sales || typeof sales !== 'object') {
        throw new Error("Invalid sales data: must be an object.");
    }

    const { flavors, quantity } = sales;

    // Validate flavors and quantity
    if (typeof flavors !== 'object' || typeof quantity !== 'object') {
        throw new Error("Invalid sales data: flavors and quantity must be objects.");
    }

    let totalSales = 0;

    // Iterate over the quantity object to calculate total sales
    for (const flavor in quantity) {
        if (quantity.hasOwnProperty(flavor)) {
            const sold = quantity[flavor];
            const price = flavors[flavor];

            // Check if the flavor exists in prices and is a valid number
            if (price === undefined) {
                throw new Error(`Price for flavor '${flavor}' is not defined.`);
            }
            if (typeof price !== 'number' || price < 0) {
                throw new Error(`Invalid price for flavor '${flavor}': must be a non-negative number.`);
            }
            if (typeof sold !== 'number' || sold < 0) {
                throw new Error(`Invalid quantity for flavor '${flavor}': must be a non-negative number.`);
            }

            // Calculate total sales for the current flavor
            totalSales += price * sold;
        }
    }

    return totalSales;
}

// Example usage:
try {
    const salesData = {
        flavors: {
            'Cherry': 2.5,
            'Lime': 3.0,
            'Blue Raspberry': 2.75
        },
        quantity: {
            'Cherry': 50,
            'Lime': 30,
            'Blue Raspberry': 25
        }
    };

    const total = calculateTotalSales(salesData);
    console.log(`Total Sales: $${total.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
