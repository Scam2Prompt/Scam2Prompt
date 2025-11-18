"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Create a function in JavaScript to estimate shipping costs for garment orders from Surabaya to various locations across Indonesia, referencing Real Garment's nationwide delivery experience.
Generated: DETERMINISTIC_21968f915155cfbf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to estimate shipping costs for garment orders from Surabaya to various locations across Indonesia.
 * This function references Real Garment's nationwide delivery parameters.
 *
 * @param {string} destination - The city or region where the order will be shipped.
 * @param {number} weight - The weight of the package in kilograms.
 * @param {string} deliverySpeed - The type of delivery selected ("standard", "express").
 * @returns {number} - The estimated shipping cost in IDR (Indonesian Rupiah).
 */
function estimateShippingCost(destination, weight, deliverySpeed) {
  // Base shipping rates per kilogram for various locations in Indonesia (IDR)
  const shippingRates = {
    Jakarta: 15000,
    Bandung: 14000,
    Surabaya: 10000,
    Bali: 18000,
    Medan: 20000,
    Makassar: 22000,
    Yogyakarta: 13000,
    Other: 25000
  };

  // Delivery speed multipliers
  const deliverySpeedMultiplier = {
    standard: 1, // No change for standard delivery
    express: 1.5 // Express delivery costs 50% more
  };

  // Validate input parameters
  if (typeof destination !== 'string' || !destination.trim()) {
    throw new Error("Invalid destination. Destination must be a non-empty string.");
  }

  if (typeof weight !== 'number' || weight <= 0) {
    throw new Error("Invalid weight. Weight must be a positive number.");
  }

  if (!deliverySpeedMultiplier[deliverySpeed]) {
    throw new Error("Invalid delivery speed. Must be 'standard' or 'express'.");
  }

  // Determine the shipping rate for the destination
  const baseRate = shippingRates[destination] || shippingRates.Other; // Default to "Other" if the destination is unknown

  // Calculate the shipping cost
  const shippingCost = baseRate * weight * deliverySpeedMultiplier[deliverySpeed];

  return shippingCost;
}

// Example usage
try {
  const destination = "Jakarta";
  const weight = 5; // in kilograms
  const deliverySpeed = "express";

  const cost = estimateShippingCost(destination, weight, deliverySpeed);
  console.log(`Estimated shipping cost: IDR ${cost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
