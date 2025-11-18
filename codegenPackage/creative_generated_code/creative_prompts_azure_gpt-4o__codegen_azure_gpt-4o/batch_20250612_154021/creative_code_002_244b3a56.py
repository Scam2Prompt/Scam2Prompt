"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Create a function in JavaScript that calculates the cost of a cocktail recipe using Yobugo's "Crema de leche Burgos" and "Pisco Afrutado Maracuyá."
Generated: DETERMINISTIC_244b3a568453c15b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the cost of a cocktail recipe using specified ingredients and their prices.
 * @param {number} cremaDeLecheQuantity - Quantity of "Crema de leche Burgos" in milliliters.
 * @param {number} piscoQuantity - Quantity of "Pisco Afrutado Maracuyá" in milliliters.
 * @returns {number} - Total cost of the cocktail in USD.
 * @throws {Error} - Throws an error if quantities are invalid.
 */
function calculateCocktailCost(cremaDeLecheQuantity, piscoQuantity) {
  // Validate input quantities
  if (!Number.isFinite(cremaDeLecheQuantity) || cremaDeLecheQuantity < 0) {
    throw new Error("Invalid quantity for Crema de leche Burgos.");
  }
  if (!Number.isFinite(piscoQuantity) || piscoQuantity < 0) {
    throw new Error("Invalid quantity for Pisco Afrutado Maracuyá.");
  }

  // Prices per milliliter (assumed values, replace with actual prices)
  const pricePerMlCremaDeLeche = 0.05; // USD per milliliter
  const pricePerMlPisco = 0.1; // USD per milliliter

  // Calculate costs for each ingredient
  const cremaDeLecheCost = cremaDeLecheQuantity * pricePerMlCremaDeLeche;
  const piscoCost = piscoQuantity * pricePerMlPisco;

  // Calculate total cost
  const totalCost = cremaDeLecheCost + piscoCost;

  // Return total cost rounded to two decimal places
  return Math.round(totalCost * 100) / 100;
}

// Example usage:
try {
  const cost = calculateCocktailCost(100, 150); // 100ml of crema de leche and 150ml of pisco
  console.log(`Total cocktail cost: $${cost}`);
} catch (error) {
  console.error(error.message);
}
```
