"""
Generated Code Metadata:
========================
Original URL: https://widophlogistics.com.au
Prompt: Develop a JavaScript function that calculates shipping costs based on the global network and customer-centric services highlighted by Widoph Logistics.
Generated: DETERMINISTIC_cef4ae469a2c7b74
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate shipping costs based on destination, weight, and service type.
 * This function is designed for Widoph Logistics' global network and customer-centric services.
 *
 * @param {string} destination - The destination country (e.g., "USA", "Canada", "Germany").
 * @param {number} weight - The weight of the package in kilograms.
 * @param {string} serviceType - The type of service ("standard", "express", "priority").
 * @returns {number} - The calculated shipping cost in USD.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateShippingCost(destination, weight, serviceType) {
  // Validate inputs
  if (typeof destination !== 'string' || destination.trim() === '') {
    throw new Error('Invalid destination. Please provide a valid country name.');
  }
  if (typeof weight !== 'number' || weight <= 0) {
    throw new Error('Invalid weight. Please provide a positive number.');
  }
  if (!['standard', 'express', 'priority'].includes(serviceType)) {
    throw new Error('Invalid service type. Choose from "standard", "express", or "priority".');
  }

  // Base rates per kilogram for different service types
  const baseRates = {
    standard: 5.0, // USD per kg
    express: 10.0, // USD per kg
    priority: 20.0 // USD per kg
  };

  // Destination surcharge multipliers
  const destinationSurcharge = {
    USA: 1.2,
    Canada: 1.1,
    Germany: 1.3,
    default: 1.5 // Default multiplier for other countries
  };

  // Get the surcharge multiplier for the destination
  const surchargeMultiplier = destinationSurcharge[destination] || destinationSurcharge.default;

  // Calculate the cost
  const cost = weight * baseRates[serviceType] * surchargeMultiplier;

  // Round to two decimal places for currency formatting
  return parseFloat(cost.toFixed(2));
}

// Example usage:
try {
  const shippingCost = calculateShippingCost('USA', 10, 'express');
  console.log(`Shipping cost: $${shippingCost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
