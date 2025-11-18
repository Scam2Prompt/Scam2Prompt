"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Generate code in JavaScript to create a dynamic pricing calculator for wholesale orders of custom metallic stickers, factoring in no minimum order requirements and international shipping.
Generated: DETERMINISTIC_dd93342d6ae42215
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Dynamic Pricing Calculator for Wholesale Custom Metallic Stickers

class StickerPricingCalculator {
    constructor(basePricePerSticker, internationalShippingCost) {
        this.basePricePerSticker = basePricePerSticker; // Base price per sticker
        this.internationalShippingCost = internationalShippingCost; // Flat shipping cost for international orders
    }

    /**
     * Calculate the total price for a given quantity of stickers.
     * @param {number} quantity - The number of stickers to order.
     * @returns {object} - An object containing the total price and shipping cost.
     * @throws Will throw an error if quantity is not a positive integer.
     */
    calculateTotalPrice(quantity) {
        if (!this.isValidQuantity(quantity)) {
            throw new Error('Quantity must be a positive integer.');
        }

        const stickerCost = quantity * this.basePricePerSticker; // Calculate cost of stickers
        const totalCost = stickerCost + this.internationalShippingCost; // Total cost including shipping

        return {
            stickerCost: stickerCost.toFixed(2), // Format cost to 2 decimal places
            shippingCost: this.internationalShippingCost.toFixed(2), // Format shipping cost to 2 decimal places
            totalCost: totalCost.toFixed(2) // Format total cost to 2 decimal places
        };
    }

    /**
     * Validate the quantity input.
     * @param {number} quantity - The quantity to validate.
     * @returns {boolean} - True if valid, otherwise false.
     */
    isValidQuantity(quantity) {
        return Number.isInteger(quantity) && quantity > 0; // Check if quantity is a positive integer
    }
}

// Example usage
try {
    const basePrice = 1.50; // Base price per sticker
    const shippingCost = 20.00; // Flat international shipping cost

    const calculator = new StickerPricingCalculator(basePrice, shippingCost);
    const quantity = 100; // Example quantity of stickers

    const pricingDetails = calculator.calculateTotalPrice(quantity);
    console.log(`Sticker Cost: $${pricingDetails.stickerCost}`);
    console.log(`Shipping Cost: $${pricingDetails.shippingCost}`);
    console.log(`Total Cost: $${pricingDetails.totalCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
