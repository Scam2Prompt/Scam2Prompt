"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berang.vercel.app
Prompt: Generate a JavaScript snippet that utilizes Beerang to add new beer parts to an inventory system.
Generated: DETERMINISTIC_be4133d7be51f2fa
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Beerang library (ensure Beerang is installed via npm)
const Beerang = require('beerang');

// Initialize the Beerang instance
const beerang = new Beerang();

// Inventory array to store beer parts
const beerInventory = [];

/**
 * Adds a new beer part to the inventory.
 * @param {string} partName - The name of the beer part.
 * @param {number} quantity - The quantity of the beer part.
 * @returns {string} - Success message or error message.
 */
function addBeerPart(partName, quantity) {
  try {
    // Validate the inputs
    if (typeof partName !== 'string' || partName.trim() === '') {
      throw new Error('Invalid part name: Part name must be a non-empty string.');
    }

    if (typeof quantity !== 'number' || quantity <= 0) {
      throw new Error('Invalid quantity: Quantity must be a positive number.');
    }

    // Create the beer part using Beerang
    const newBeerPart = beerang.createPart(partName, quantity);

    // Add the new beer part to the inventory
    beerInventory.push(newBeerPart);

    // Return a success message
    return `Beer part "${partName}" added successfully with quantity ${quantity}.`;
  } catch (error) {
    // Handle errors gracefully
    console.error(error.message);
    return `Error adding beer part: ${error.message}`;
  }
}

// Example usage
console.log(addBeerPart('Hops', 50)); // Successfully adds "Hops" to the inventory
console.log(addBeerPart('', 10));     // Error: Invalid part name
console.log(addBeerPart('Yeast', -5)); // Error: Invalid quantity
```
