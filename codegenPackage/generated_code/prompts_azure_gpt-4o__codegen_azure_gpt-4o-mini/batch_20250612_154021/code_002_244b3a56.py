"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Create a function in JavaScript that calculates the cost of a cocktail recipe using Yobugo's "Crema de leche Burgos" and "Pisco Afrutado Maracuyá."
Generated: DETERMINISTIC_244b3a568453c15b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a cocktail recipe using specified ingredients.
 * 
 * @param {number} cremaDeLecheBurgosQuantity - The quantity of "Crema de leche Burgos" in liters.
 * @param {number} piscoAfrutadoMaracuyaQuantity - The quantity of "Pisco Afrutado Maracuyá" in liters.
 * @returns {number} - The total cost of the cocktail.
 * @throws {Error} - Throws an error if the quantities are negative or not numbers.
 */
function calculateCocktailCost(cremaDeLecheBurgosQuantity, piscoAfrutadoMaracuyaQuantity) {
    // Prices per liter of the ingredients
    const cremaDeLecheBurgosPricePerLiter = 15.00; // Example price in currency
    const piscoAfrutadoMaracuyaPricePerLiter = 25.00; // Example price in currency

    // Validate input quantities
    if (typeof cremaDeLecheBurgosQuantity !== 'number' || cremaDeLecheBurgosQuantity < 0) {
        throw new Error('Invalid quantity for Crema de leche Burgos. It must be a non-negative number.');
    }
    if (typeof piscoAfrutadoMaracuyaQuantity !== 'number' || piscoAfrutadoMaracuyaQuantity < 0) {
        throw new Error('Invalid quantity for Pisco Afrutado Maracuyá. It must be a non-negative number.');
    }

    // Calculate the total cost
    const cremaDeLecheBurgosCost = cremaDeLecheBurgosQuantity * cremaDeLecheBurgosPricePerLiter;
    const piscoAfrutadoMaracuyaCost = piscoAfrutadoMaracuyaQuantity * piscoAfrutadoMaracuyáPricePerLiter;

    // Return the total cost
    return cremaDeLecheBurgosCost + piscoAfrutadoMaracuyaCost;
}

// Example usage
try {
    const totalCost = calculateCocktailCost(0.5, 0.3); // 0.5 liters of Crema de leche Burgos and 0.3 liters of Pisco Afrutado Maracuyá
    console.log(`Total cost of the cocktail: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
