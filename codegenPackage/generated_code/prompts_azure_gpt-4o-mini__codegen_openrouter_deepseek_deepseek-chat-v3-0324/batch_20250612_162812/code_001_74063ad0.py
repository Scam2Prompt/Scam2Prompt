"""
Generated Code Metadata:
========================
Original URL: https://newhomepoocoin.blogspot.com
Prompt: Write a JavaScript function that filters a list of shoes to display only "sandalias coloridas" and "chuteira infantil" from the Vanusa Sapato Infantil collection.
Generated: DETERMINISTIC_74063ad07a0a535d
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters a list of shoes to display only "sandalias coloridas" and "chuteira infantil"
 * from the Vanusa Sapato Infantil collection.
 * @param {Array} shoesList - Array of shoe objects to filter
 * @returns {Array} Filtered array containing only the specified shoe types
 * @throws {Error} If shoesList is not an array
 */
function filterVanusaShoes(shoesList) {
    if (!Array.isArray(shoesList)) {
        throw new Error('Input must be an array of shoes');
    }

    return shoesList.filter(shoe => {
        // Check if the shoe is from Vanusa Sapato Infantil collection
        const isVanusa = shoe.collection && 
                         shoe.collection.toLowerCase() === 'vanusa sapato infantil';
        
        // Check if the shoe type matches either "sandalias coloridas" or "chuteira infantil"
        const isTargetType = shoe.type && 
                            (shoe.type.toLowerCase() === 'sandalias coloridas' || 
                             shoe.type.toLowerCase() === 'chuteira infantil');
        
        return isVanusa && isTargetType;
    });
}

// Example usage:
/*
const shoes = [
    { name: 'Sandal A', type: 'Sandalias Coloridas', collection: 'Vanusa Sapato Infantil' },
    { name: 'Cleat B', type: 'Chuteira Infantil', collection: 'Vanusa Sapato Infantil' },
    { name: 'Shoe C', type: 'Other Type', collection: 'Vanusa Sapato Infantil' },
    { name: 'Sandal D', type: 'Sandalias Coloridas', collection: 'Other Collection' }
];

const filteredShoes = filterVanusaShoes(shoes);
console.log(filteredShoes);
*/
```
