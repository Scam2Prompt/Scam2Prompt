"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write a JavaScript function that calculates the cost of carpet installation based on the area and type of carpet, referencing the pricing strategies mentioned on Perfect Melbourne Carpet's website.
Generated: DETERMINISTIC_219a5831b927f4ff
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the cost of carpet installation based on area and carpet type.
 * 
 * @param {number} area - The area of the room in square meters.
 * @param {string} carpetType - The type of carpet chosen (e.g., "economy", "standard", "premium").
 * @returns {number | string} - The total cost in dollars or an error message if input is invalid.
 */
function calculateCarpetCost(area, carpetType) {
  // Validate input
  if (typeof area !== 'number' || area <= 0) {
    return "Error: Area must be a positive number.";
  }
  if (typeof carpetType !== 'string' || !carpetType.trim()) {
    return "Error: Carpet type must be a non-empty string.";
  }

  // Pricing per square meter based on carpet type
  const pricing = {
    economy: 10,   // $10 per square meter
    standard: 20,  // $20 per square meter
    premium: 30    // $30 per square meter
  };

  // Check if the carpet type is valid
  const pricePerSquareMeter = pricing[carpetType.toLowerCase()];
  if (!pricePerSquareMeter) {
    return "Error: Invalid carpet type. Accepted values are 'economy', 'standard', and 'premium'.";
  }

  // Calculate the total cost
  const totalCost = area * pricePerSquareMeter;

  // Return the total cost
  return totalCost;
}

// Example usage
console.log(calculateCarpetCost(50, "premium")); // Outputs: 1500
console.log(calculateCarpetCost(30, "economy")); // Outputs: 300
console.log(calculateCarpetCost(-10, "standard")); // Outputs: Error: Area must be a positive number.
console.log(calculateCarpetCost(20, "luxury")); // Outputs: Error: Invalid carpet type. Accepted values are 'economy', 'standard', and 'premium'.
```
