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
 * Calculates the total cost of a cocktail recipe using specified ingredients.
 * 
 * @param {number} cremaDeLecheQuantity - The quantity of "Crema de leche Burgos" in liters.
 * @param {number} piscoAfrutadoQuantity - The quantity of "Pisco Afrutado Maracuyá" in liters.
 * @returns {number} The total cost of the cocktail recipe.
 * @throws {Error} Throws an error if quantities are negative or not numbers.
 */
function calculateCocktailCost(cremaDeLecheQuantity, piscoAfrutadoQuantity) {
    // Price per liter for each ingredient
    const prices = {
        cremaDeLeche: 10.00, // Price of "Crema de leche Burgos" per liter
        piscoAfrutado: 25.00  // Price of "Pisco Afrutado Maracuyá" per liter
    };

    // Validate inputs
    if (typeof cremaDeLecheQuantity !== 'number' || typeof piscoAfrutadoQuantity !== 'number') {
        throw new Error("Both quantities must be numbers.");
    }
    if (cremaDeLecheQuantity < 0 || piscoAfrutadoQuantity < 0) {
        throw new Error("Quantities must not be negative.");
    }

    // Calculate total cost
    const totalCost = (cremaDeLecheQuantity * prices.cremaDeLeche) + 
                      (piscoAfrutadoQuantity * prices.piscoAfrutado);

    return parseFloat(totalCost.toFixed(2)); // Return total cost rounded to two decimal places
}

// Example usage
try {
    const cost = calculateCocktailCost(0.5, 1.0); // Example quantities
    console.log(`The total cost of the cocktail is: $${cost}`);
} catch (error) {
    console.error(`Error calculating cocktail cost: ${error.message}`);
}
```
