"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Write a JavaScript function to calculate fixed price solutions for legal and accounting services, reflecting the pricing model used by Carthew Chau & Co.
Generated: DETERMINISTIC_1e54cf9cfdee8351
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate fixed price solutions for legal and accounting services.
 * The pricing model is based on predefined service packages with fixed costs.
 * @param {string} serviceType - The type of service ('legal' or 'accounting').
 * @param {string} packageType - The package selected ('basic', 'standard', or 'premium').
 * @returns {number} - The fixed price of the selected service package.
 * @throws {Error} - Throws an error if the serviceType or packageType is invalid.
 */

function calculateFixedPrice(serviceType, packageType) {
  // Predefined pricing model for legal and accounting services
  const pricingModel = {
    legal: {
      basic: 500,
      standard: 1000,
      premium: 2000,
    },
    accounting: {
      basic: 300,
      standard: 700,
      premium: 1500,
    },
  };

  // Input validation
  if (!pricingModel[serviceType]) {
    throw new Error(`Invalid service type: ${serviceType}. Allowed types are 'legal' or 'accounting'.`);
  }

  if (!pricingModel[serviceType][packageType]) {
    throw new Error(
      `Invalid package type: ${packageType}. Allowed types for ${serviceType} are 'basic', 'standard', or 'premium'.`
    );
  }

  // Calculate and return the fixed price
  return pricingModel[serviceType][packageType];
}

/**
 * Example usage:
 * Uncomment the following lines to test the function.
 */

// console.log(calculateFixedPrice('legal', 'standard')); // Outputs: 1000
// console.log(calculateFixedPrice('accounting', 'premium')); // Outputs: 1500
// console.log(calculateFixedPrice('legal', 'basic')); // Outputs: 500

// Error handling test
// console.log(calculateFixedPrice('engineering', 'basic')); // Throws an error
// console.log(calculateFixedPrice('legal', 'gold')); // Throws an error
```
