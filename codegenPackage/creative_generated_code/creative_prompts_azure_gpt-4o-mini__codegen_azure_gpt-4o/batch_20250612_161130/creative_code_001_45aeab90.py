"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laptopshop.pe
Prompt: Write a JavaScript function to calculate the discounted price of laptops listed on LaptopShop, using the original and current prices provided.
Generated: DETERMINISTIC_45aeab908daef790
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the discounted price of laptops.
 * 
 * This function takes an array of laptop objects, each containing the original price and current price,
 * and calculates the discount percentage for each laptop. It returns an array with the laptop details
 * and the calculated discount percentage.
 * 
 * @param {Array} laptops - An array of laptop objects. Each object must have `originalPrice` and `currentPrice` properties.
 * @returns {Array} An array of laptop objects, including a new `discountPercentage` property.
 */
function calculateDiscountedPrices(laptops) {
    // Validate input
    if (!Array.isArray(laptops)) {
        throw new Error("Invalid input: laptops must be an array.");
    }

    return laptops.map((laptop) => {
        // Validate the structure of each laptop object
        if (typeof laptop.originalPrice !== "number" || typeof laptop.currentPrice !== "number") {
            throw new Error("Invalid laptop object: originalPrice and currentPrice must be numbers.");
        }

        if (laptop.originalPrice <= 0) {
            throw new Error("Invalid laptop object: originalPrice must be greater than 0.");
        }

        // Calculate discount percentage
        const discountPercentage = ((laptop.originalPrice - laptop.currentPrice) / laptop.originalPrice) * 100;

        // Ensure discount percentage is rounded to two decimal places
        const roundedDiscount = Math.round(discountPercentage * 100) / 100;

        // Return the laptop object with the new property
        return {
            ...laptop,
            discountPercentage: roundedDiscount
        };
    });
}

// Example usage:
const laptops = [
    { name: "Laptop A", originalPrice: 1000, currentPrice: 800 },
    { name: "Laptop B", originalPrice: 1500, currentPrice: 1200 },
    { name: "Laptop C", originalPrice: 2000, currentPrice: 1800 }
];

try {
    const discountedLaptops = calculateDiscountedPrices(laptops);
    console.log(discountedLaptops);
} catch (error) {
    console.error("Error calculating discounts:", error.message);
}
```
