"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: "Develop a JavaScript code to calculate the cost of renting compressors and pumps for a specific period, considering the company's rates and services offered in Maringá, Londrina, and Campo Grande."
Generated: DETERMINISTIC_b3021bcdce7ab67e
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Compressor and Pump Rental Cost Calculator
 * 
 * This script calculates the cost of renting compressors and pumps for a specific period
 * based on the company's rates and services offered in Maringá, Londrina, and Campo Grande.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Rental rates per day for each city
const rentalRates = {
  Maringa: { compressor: 100, pump: 80 },
  Londrina: { compressor: 120, pump: 90 },
  CampoGrande: { compressor: 110, pump: 85 },
};

/**
 * Validates the input parameters.
 * @param {string} city - The city where the rental is taking place.
 * @param {number} days - The number of days for the rental.
 * @param {number} compressors - The number of compressors to rent.
 * @param {number} pumps - The number of pumps to rent.
 * @throws Will throw an error if any input is invalid.
 */
function validateInputs(city, days, compressors, pumps) {
  if (!rentalRates[city]) {
    throw new Error(`Invalid city: ${city}. Available cities are Maringa, Londrina, and CampoGrande.`);
  }
  if (typeof days !== 'number' || days <= 0) {
    throw new Error('Days must be a positive number.');
  }
  if (typeof compressors !== 'number' || compressors < 0) {
    throw new Error('Compressors must be a non-negative number.');
  }
  if (typeof pumps !== 'number' || pumps < 0) {
    throw new Error('Pumps must be a non-negative number.');
  }
}

/**
 * Calculates the total rental cost.
 * @param {string} city - The city where the rental is taking place.
 * @param {number} days - The number of days for the rental.
 * @param {number} compressors - The number of compressors to rent.
 * @param {number} pumps - The number of pumps to rent.
 * @returns {number} - The total rental cost.
 */
function calculateRentalCost(city, days, compressors, pumps) {
  validateInputs(city, days, compressors, pumps);

  const rates = rentalRates[city];
  const compressorCost = compressors * rates.compressor * days;
  const pumpCost = pumps * rates.pump * days;

  return compressorCost + pumpCost;
}

// Example usage
try {
  const city = 'Maringa'; // City name
  const days = 5; // Number of rental days
  const compressors = 2; // Number of compressors to rent
  const pumps = 3; // Number of pumps to rent

  const totalCost = calculateRentalCost(city, days, compressors, pumps);
  console.log(`The total rental cost in ${city} for ${days} days is: $${totalCost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
