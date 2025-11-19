"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://widophlogistics.com.au
Prompt: Develop a JavaScript function that calculates shipping costs based on the global network and customer-centric services highlighted by Widoph Logistics.
Generated: DETERMINISTIC_cef4ae469a2c7b74
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate shipping costs based on global network and customer-centric services.
 * @param {number} weight - The weight of the package in kilograms.
 * @param {string} destination - The destination country.
 * @param {boolean} expedited - Whether expedited shipping is requested.
 * @returns {number} - The calculated shipping cost.
 */
function calculateShippingCost(weight, destination, expedited) {
  // Validate the inputs
  if (typeof weight !== 'number' || weight <= 0) {
    throw new Error('Invalid weight. Weight must be a positive number.');
  }
  if (typeof destination !== 'string' || destination.trim() === '') {
    throw new Error('Invalid destination. Destination must be a non-empty string.');
  }
  if (typeof expedited !== 'boolean') {
    throw new Error('Invalid expedited flag. Expedited must be a boolean.');
  }

  // Base cost per kilogram
  const baseCostPerKg = 5.0;

  // Destination multiplier (simulated values for global network)
  const destinationMultipliers = {
    'North America': 1.2,
    'Europe': 1.5,
    'Asia': 1.7,
    'Australia': 1.8,
    'Africa': 1.6,
    'South America': 1.4,
    'Other': 2.0,
  };

  // Determine destination multiplier
  const region = getRegion(destination);
  const destinationMultiplier =
    destinationMultipliers[region] || destinationMultipliers['Other'];

  // Expedited multiplier
  const expeditedMultiplier = expedited ? 1.5 : 1.0;

  // Calculate shipping cost
  const shippingCost =
    weight * baseCostPerKg * destinationMultiplier * expeditedMultiplier;

  // Return the rounded shipping cost
  return Math.round(shippingCost * 100) / 100; // Round to 2 decimal places
}

/**
 * Helper function to map a destination to a region.
 * This simulates Widoph Logistics' global network classification.
 * @param {string} destination - The destination country.
 * @returns {string} - The region associated with the destination.
 */
function getRegion(destination) {
  const regions = {
    'USA': 'North America',
    'Canada': 'North America',
    'Mexico': 'North America',
    'Germany': 'Europe',
    'France': 'Europe',
    'UK': 'Europe',
    'China': 'Asia',
    'Japan': 'Asia',
    'India': 'Asia',
    'Australia': 'Australia',
    'South Africa': 'Africa',
    'Brazil': 'South America',
    'Argentina': 'South America',
  };

  // Normalize the destination string to handle casing
  const normalizedDestination = destination.trim().toLowerCase();

  // Find the region or default to 'Other'
  for (const [country, region] of Object.entries(regions)) {
    if (country.toLowerCase() === normalizedDestination) {
      return region;
    }
  }

  return 'Other'; // Default region for unclassified destinations
}

// Example usage:
try {
  const cost = calculateShippingCost(10, 'Germany', true);
  console.log(`Shipping cost: $${cost}`);
} catch (error) {
  console.error(`Error calculating shipping cost: ${error.message}`);
}
```
