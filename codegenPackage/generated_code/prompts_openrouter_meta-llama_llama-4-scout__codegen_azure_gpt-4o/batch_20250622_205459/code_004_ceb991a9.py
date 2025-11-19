"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Write a JavaScript function to calculate the cost of transporting goods based on the type of freight and incoterms used by Kalgate Technology.
Generated: DETERMINISTIC_ceb991a92c472f6e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of transporting goods based on freight type and incoterms.
 * @param {string} freightType - Type of freight (e.g., "air", "sea", "land").
 * @param {string} incoterm - Incoterm used (e.g., "EXW", "FOB", "CIF").
 * @param {number} weight - Weight of the goods in kilograms.
 * @param {number} distance - Distance to be transported in kilometers.
 * @returns {number} - Total transportation cost in USD.
 * @throws {Error} - Throws an error if invalid inputs are provided.
 */
function calculateTransportCost(freightType, incoterm, weight, distance) {
  // Validate inputs
  if (typeof freightType !== 'string' || typeof incoterm !== 'string') {
    throw new Error('Freight type and incoterm must be strings.');
  }
  if (typeof weight !== 'number' || weight <= 0) {
    throw new Error('Weight must be a positive number.');
  }
  if (typeof distance !== 'number' || distance <= 0) {
    throw new Error('Distance must be a positive number.');
  }

  // Base rates per kilometer per kilogram for different freight types
  const freightRates = {
    air: 0.5, // USD per km per kg
    sea: 0.2, // USD per km per kg
    land: 0.3, // USD per km per kg
  };

  // Additional cost multipliers based on incoterms
  const incotermMultipliers = {
    EXW: 1.1, // Ex Works
    FOB: 1.2, // Free On Board
    CIF: 1.3, // Cost, Insurance, and Freight
  };

  // Check if freight type and incoterm are valid
  if (!freightRates[freightType]) {
    throw new Error(`Invalid freight type: ${freightType}. Valid options are "air", "sea", "land".`);
  }
  if (!incotermMultipliers[incoterm]) {
    throw new Error(`Invalid incoterm: ${incoterm}. Valid options are "EXW", "FOB", "CIF".`);
  }

  // Calculate base cost
  const baseCost = weight * distance * freightRates[freightType];

  // Apply incoterm multiplier
  const totalCost = baseCost * incotermMultipliers[incoterm];

  // Return the total cost rounded to two decimal places
  return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
  const cost = calculateTransportCost('air', 'FOB', 100, 500);
  console.log(`Total transportation cost: $${cost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
