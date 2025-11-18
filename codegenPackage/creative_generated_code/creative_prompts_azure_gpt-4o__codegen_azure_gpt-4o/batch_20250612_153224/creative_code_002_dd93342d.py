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
/**
 * Dynamic Pricing Calculator for Wholesale Metallic Stickers
 * 
 * This script calculates the cost of an order based on quantity, type of sticker,
 * and shipping destination. It factors in base costs, volume discounts, and 
 * international shipping fees.
 */

// Constants for pricing
const BASE_PRICE_PER_STICKER = 0.5; // Base price per sticker in USD
const VOLUME_DISCOUNTS = [
  { minQty: 100, discount: 0.05 }, // 5% discount for 100+ stickers
  { minQty: 500, discount: 0.10 }, // 10% discount for 500+ stickers
  { minQty: 1000, discount: 0.15 }, // 15% discount for 1000+ stickers
];
const SHIPPING_RATES = {
  domestic: 10.0, // Flat domestic shipping rate in USD
  international: 25.0, // Flat international shipping rate in USD
};

/**
 * Function to calculate the total cost for an order
 * @param {number} quantity - Number of stickers ordered
 * @param {string} shippingType - Shipping type: 'domestic' or 'international'
 * @returns {object} - An object containing the breakdown of costs and total price
 */
function calculateOrderCost(quantity, shippingType) {
  // Input validation
  if (typeof quantity !== "number" || quantity <= 0) {
    throw new Error("Invalid quantity. Quantity must be a positive number.");
  }

  if (!["domestic", "international"].includes(shippingType)) {
    throw new Error("Invalid shipping type. Must be 'domestic' or 'international'.");
  }

  // Calculate base sticker cost
  let baseCost = quantity * BASE_PRICE_PER_STICKER;

  // Apply volume discount
  let discountRate = 0;
  for (const discount of VOLUME_DISCOUNTS) {
    if (quantity >= discount.minQty) {
      discountRate = discount.discount;
    }
  }
  const discountAmount = baseCost * discountRate;
  const stickerCostAfterDiscount = baseCost - discountAmount;

  // Calculate shipping cost
  const shippingCost = SHIPPING_RATES[shippingType];

  // Calculate total cost
  const totalCost = stickerCostAfterDiscount + shippingCost;

  // Return detailed cost breakdown
  return {
    baseCost,
    discountRate: discountRate * 100, // Convert to percentage
    discountAmount,
    stickerCostAfterDiscount,
    shippingCost,
    totalCost,
  };
}

// Example usage
try {
  const orderSummary = calculateOrderCost(750, "international");
  console.log("Order Summary:", orderSummary);
} catch (error) {
  console.error("Error:", error.message);
}
```
