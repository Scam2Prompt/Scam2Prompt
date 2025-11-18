"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Develop a JavaScript function to calculate the total cost of a dumpster rental based on the pricing details provided for regions like Brampton, Burlington, and Toronto on Purple Dumpster's website.
Generated: DETERMINISTIC_12a543804d3acfc3
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
 * Function to calculate the total cost of a dumpster rental.
 * Pricing data is based on the regions and their rates.
 * The function considers base price, weight surcharge, and additional fees.
 *
 * @param {string} region - The rental region (e.g., 'Brampton', 'Burlington', 'Toronto').
 * @param {number} weight - The weight in tons (used to calculate surcharge if applicable).
 * @param {number} days - The number of rental days (used to calculate extra day charges if applicable).
 * @returns {number} - The total cost of the dumpster rental.
 * @throws {Error} - Throws an error if the region is invalid or input data is incorrect.
 */

// Define pricing data for regions
const pricingData = {
  Brampton: {
    basePrice: 300,
    extraDayFee: 30,       // Fee for additional days
    weightLimit: 3,        // Weight limit in tons
    weightSurcharge: 50,   // Per ton over the weight limit
  },
  Burlington: {
    basePrice: 320,
    extraDayFee: 35,
    weightLimit: 3.5,
    weightSurcharge: 55,
  },
  Toronto: {
    basePrice: 280,
    extraDayFee: 25,
    weightLimit: 2.5,
    weightSurcharge: 60,
  },
};

function calculateDumpsterRentalCost(region, weight, days) {
  // Validate inputs
  if (!pricingData[region]) {
    throw new Error(`Invalid region: ${region}. Valid regions are Brampton, Burlington, Toronto.`);
  }
  if (typeof weight !== 'number' || weight < 0) {
    throw new Error(`Invalid weight: ${weight}. Weight must be a positive number.`);
  }
  if (typeof days !== 'number' || days <= 0) {
    throw new Error(`Invalid days: ${days}. Days must be a positive integer.`);
  }

  // Get region-specific pricing details
  const { basePrice, extraDayFee, weightLimit, weightSurcharge } = pricingData[region];

  // Calculate weight surcharge (if any)
  const weightOverage = Math.max(0, weight - weightLimit);
  const weightSurchargeTotal = weightOverage * weightSurcharge;

  // Calculate extra day fee (if any)
  const extraDaysFeeTotal = days > 7 ? (days - 7) * extraDayFee : 0;

  // Calculate total cost
  const totalCost = basePrice + weightSurchargeTotal + extraDaysFeeTotal;

  return totalCost;
}

// Example Usage:
// console.log(calculateDumpsterRentalCost("Brampton", 4, 10)); // Output: 440
// console.log(calculateDumpsterRentalCost("Toronto", 2, 5));   // Output: 280
// console.log(calculateDumpsterRentalCost("Burlington", 3, 8)); // Output: 355
```
