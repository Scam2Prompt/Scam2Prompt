"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-hex.com
Prompt: Write a JavaScript function that calculates the total savings when purchasing multiple systems from Lenovo's Elite Tier, considering the extra 10% discount.
Generated: DETERMINISTIC_d4b8fc38dd316a0d
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate total savings when purchasing multiple systems 
 * from Lenovo's Elite Tier, considering an extra 10% discount.
 * 
 * @param {Array<number>} systemPrices - Array of individual system prices.
 * @param {number} discountPercentage - The base discount percentage (e.g., 20 for 20%).
 * @returns {number} - Total savings after applying both discounts.
 */
function calculateTotalSavings(systemPrices, discountPercentage) {
    // Input validation
    if (!Array.isArray(systemPrices) || systemPrices.some(price => typeof price !== 'number' || price < 0)) {
        throw new Error("Invalid input: systemPrices must be an array of non-negative numbers.");
    }
    if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 100) {
        throw new Error("Invalid input: discountPercentage must be a number between 0 and 100.");
    }

    // Base discount calculation (e.g., 20%)
    const baseDiscountRate = discountPercentage / 100;

    // Additional discount for Elite Tier systems (10%)
    const eliteDiscountRate = 0.10;

    // Total savings calculation
    let totalSavings = 0;
    for (const price of systemPrices) {
        const baseDiscount = price * baseDiscountRate; // Base discount amount
        const eliteDiscount = (price - baseDiscount) * eliteDiscountRate; // Extra discount on discounted price
        totalSavings += baseDiscount + eliteDiscount; // Add both discounts to total savings
    }

    return totalSavings;
}

// Example usage:
try {
    const systemPrices = [1500, 2000, 2500]; // Prices of systems in USD
    const baseDiscount = 20; // Base discount percentage
    const totalSavings = calculateTotalSavings(systemPrices, baseDiscount);
    console.log(`Total savings: $${totalSavings.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
