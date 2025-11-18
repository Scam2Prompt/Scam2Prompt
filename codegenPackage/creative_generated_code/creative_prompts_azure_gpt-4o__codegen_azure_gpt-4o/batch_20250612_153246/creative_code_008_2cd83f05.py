"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duct-split.com
Prompt: Write JavaScript code to implement a search functionality for the "duct-split.com" website, allowing users to filter Gree air conditioners by cooling capacity, inverter type, and price range.
Generated: DETERMINISTIC_2cd83f058d359002
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Search functionality for "duct-split.com" website to filter Gree air conditioners
// by cooling capacity, inverter type, and price range.

// Sample dataset for air conditioners
const airConditioners = [
  { id: 1, name: "Gree AC Model X", coolingCapacity: "1.5 Ton", inverter: true, price: 450 },
  { id: 2, name: "Gree AC Model Y", coolingCapacity: "2 Ton", inverter: false, price: 650 },
  { id: 3, name: "Gree AC Model Z", coolingCapacity: "1 Ton", inverter: true, price: 300 },
  { id: 4, name: "Gree AC Model W", coolingCapacity: "2 Ton", inverter: true, price: 700 },
  { id: 5, name: "Gree AC Model V", coolingCapacity: "1.5 Ton", inverter: false, price: 500 },
];

// Function to filter air conditioners based on user criteria
/**
 * Filters air conditioners based on cooling capacity, inverter type, and price range.
 * @param {string} coolingCapacity - Desired cooling capacity (e.g., "1 Ton", "1.5 Ton", "2 Ton").
 * @param {boolean|null} inverter - Desired inverter type (true for inverter, false for non-inverter, null for any).
 * @param {Object} priceRange - Price range object with `min` and `max` properties.
 * @returns {Array} - Filtered list of air conditioners.
 */
function searchAirConditioners(coolingCapacity, inverter, priceRange) {
  // Validate input parameters
  if (priceRange && (typeof priceRange.min !== 'number' || typeof priceRange.max !== 'number')) {
    throw new Error("Price range must contain valid `min` and `max` values.");
  }
  
  // Filter the air conditioners based on criteria
  return airConditioners.filter((ac) => {
    const matchesCoolingCapacity = coolingCapacity ? ac.coolingCapacity === coolingCapacity : true;
    const matchesInverter = inverter !== null ? ac.inverter === inverter : true;
    const matchesPrice = priceRange
      ? ac.price >= priceRange.min && ac.price <= priceRange.max
      : true;

    return matchesCoolingCapacity && matchesInverter && matchesPrice;
  });
}

// Example usage:
try {
  const coolingCapacity = "1.5 Ton"; // User-selected cooling capacity
  const inverter = true; // User-selected inverter type
  const priceRange = { min: 400, max: 600 }; // User-selected price range
  
  const results = searchAirConditioners(coolingCapacity, inverter, priceRange);
  console.log("Filtered Air Conditioners:", results);
} catch (error) {
  console.error("Error filtering air conditioners:", error.message);
}
```
