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
 * Function to calculate total sales for a snow cone truck.
 * @param {Array} salesData - Array of objects representing sales data. Each object should have:
 *                            - flavor: {string} name of the flavor.
 *                            - quantity: {number} number of snow cones sold for this flavor.
 *                            - price: {number} price per snow cone for this flavor.
 * @returns {number} - Total sales amount.
 */
function calculateTotalSales(salesData) {
    // Input validation: Ensure salesData is an array.
    if (!Array.isArray(salesData)) {
        throw new Error("Invalid input: salesData must be an array.");
    }

    // Initialize total sales to 0.
    let totalSales = 0;

    // Iterate over the sales data to calculate the total sales.
    for (const item of salesData) {
        // Validate the structure of each sales data item.
        if (
            typeof item.flavor !== "string" ||
            typeof item.quantity !== "number" ||
            typeof item.price !== "number"
        ) {
            throw new Error("Invalid sales data item structure.");
        }

        // Ensure quantity and price are non-negative.
        if (item.quantity < 0 || item.price < 0) {
            throw new Error(
                `Invalid data for flavor "${item.flavor}": quantity and price must be non-negative.`
            );
        }

        // Add the sales for this flavor to the total.
        totalSales += item.quantity * item.price;
    }

    // Return the total sales amount.
    return totalSales;
}

// Example usage:
const salesData = [
    { flavor: "Cherry", quantity: 10, price: 1.5 },
    { flavor: "Blue Raspberry", quantity: 8, price: 2 },
    { flavor: "Lemon", quantity: 12, price: 1.25 },
];

try {
    const total = calculateTotalSales(salesData);
    console.log(`Total Sales: $${total.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
