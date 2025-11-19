"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Create a JavaScript function to sort a list of toys by category, including "Brinquedos de Cowboy", "Brinquedos de Pedal", and "Brinquedos Eletrônicos".
Generated: DETERMINISTIC_5531eca1bc548d57
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts an array of toys by their category.
 * Categories include: "Brinquedos de Cowboy", "Brinquedos de Pedal", "Brinquedos Eletrônicos"
 * 
 * @param {Array} toys - Array of toy objects with a 'category' property
 * @returns {Array} Sorted array of toys by category
 * @throws {Error} If input is not an array or toys lack category property
 */
function sortToysByCategory(toys) {
    if (!Array.isArray(toys)) {
        throw new Error('Input must be an array');
    }

    // Define category order
    const categoryOrder = {
        'Brinquedos de Cowboy': 1,
        'Brinquedos de Pedal': 2,
        'Brinquedos Eletrônicos': 3
    };

    return toys.map(toy => {
        if (!toy.category) {
            throw new Error('Toy object must have a category property');
        }
        return toy;
    }).sort((a, b) => {
        const categoryA = categoryOrder[a.category] || Infinity;
        const categoryB = categoryOrder[b.category] || Infinity;
        return categoryA - categoryB;
    });
}

// Example usage:
// const sortedToys = sortToysByCategory([
//     { name: "Boneca", category: "Brinquedos Eletrônicos" },
//     { name: "Cavalo de Pau", category: "Brinquedos de Cowboy" },
//     { name: "Triciclo", category: "Brinquedos de Pedal" }
// ]);
// console.log(sortedToys);
```
