"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage.vercel.app
Prompt: Write a function in TypeScript that calculates the total cost in ETH for purchasing a specified number of pixels on the Starknet Homepage.
Generated: DETERMINISTIC_27ecf9b7b3d6bb2f
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Importing necessary libraries for handling BigNumber calculations
import { BigNumber } from 'bignumber.js';

/**
 * Calculates the total cost in ETH for purchasing a specified number of pixels on the Starknet Homepage.
 * 
 * @param {number} numberOfPixels - The number of pixels to purchase.
 * @param {number} costPerPixel - The cost of a single pixel in ETH.
 * @returns {string} - The total cost in ETH formatted as a string.
 * @throws {Error} - Throws an error if the number of pixels or cost per pixel is negative.
 */
function calculateTotalCostInETH(numberOfPixels: number, costPerPixel: number): string {
    // Input validation
    if (numberOfPixels < 0) {
        throw new Error("Number of pixels cannot be negative.");
    }
    if (costPerPixel < 0) {
        throw new Error("Cost per pixel cannot be negative.");
    }

    // Utilizing BigNumber for accurate calculations
    const totalCost = new BigNumber(numberOfPixels).multipliedBy(costPerPixel);

    // Return the total cost as a string with 18 decimal places for ETH precision
    return totalCost.toFixed(18);
}

// Example usage
try {
    const pixelsToPurchase = 1000; // Number of pixels to purchase
    const pricePerPixel = 0.01; // Cost per pixel in ETH
    const totalCost = calculateTotalCostInETH(pixelsToPurchase, pricePerPixel);
    console.log(`Total cost for ${pixelsToPurchase} pixels: ${totalCost} ETH`);
} catch (error) {
    console.error(`Error calculating total cost: ${(error as Error).message}`);
}
```
