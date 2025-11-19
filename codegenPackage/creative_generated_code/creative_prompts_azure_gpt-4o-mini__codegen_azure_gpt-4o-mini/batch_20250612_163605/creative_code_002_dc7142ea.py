"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cambridgesolution.com
Prompt: Write a JavaScript function that calculates the required quantities of ingredients based on the pack sizes offered by Cambridge Commodities.
Generated: DETERMINISTIC_dc7142eaaa231941
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the required quantities of ingredients based on the desired amount and pack sizes offered by Cambridge Commodities.
 * 
 * @param {number} desiredAmount - The total amount of the ingredient required (in grams).
 * @param {Array<number>} packSizes - An array of available pack sizes (in grams).
 * @returns {Object} - An object containing the optimal pack sizes and their respective quantities.
 * @throws {Error} - Throws an error if the desired amount is negative or if pack sizes are invalid.
 */
function calculateIngredientQuantities(desiredAmount, packSizes) {
    // Input validation
    if (desiredAmount < 0) {
        throw new Error("Desired amount must be a non-negative number.");
    }
    if (!Array.isArray(packSizes) || packSizes.length === 0) {
        throw new Error("Pack sizes must be a non-empty array.");
    }
    
    // Sort pack sizes in descending order to maximize the largest pack first
    packSizes.sort((a, b) => b - a);
    
    const result = {};
    
    // Calculate the required quantities of each pack size
    for (const packSize of packSizes) {
        if (packSize <= 0) {
            throw new Error(`Pack size must be a positive number, received: ${packSize}`);
        }

        // Calculate how many of this pack size are needed
        const quantity = Math.floor(desiredAmount / packSize);
        
        if (quantity > 0) {
            result[packSize] = quantity; // Store the quantity of this pack size
            desiredAmount -= quantity * packSize; // Reduce the remaining desired amount
        }
        
        if (desiredAmount === 0) {
            break; // If no amount is left, break the loop early
        }
    }

    // If there is still a desired amount left, it means the pack sizes couldn't cover it
    if (desiredAmount > 0) {
        throw new Error("The provided pack sizes are insufficient to cover the desired amount.");
    }

    return result;
}

// Example usage:
// const desiredAmount = 1500; // Desired amount in grams
// const packSizes = [500, 200, 50]; // Available pack sizes in grams
// try {
//     const quantities = calculateIngredientQuantities(desiredAmount, packSizes);
//     console.log(quantities); // Output the calculated quantities
// } catch (error) {
//     console.error(error.message); // Handle any errors
// }
```
