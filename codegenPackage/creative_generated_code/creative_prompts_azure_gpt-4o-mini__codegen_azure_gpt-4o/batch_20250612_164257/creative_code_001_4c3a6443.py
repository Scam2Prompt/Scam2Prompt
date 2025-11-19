"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinswapse.blogspot.com
Prompt: Write a JavaScript function that filters an array of shoe types to include only "tenis de corrida" and "chuteira infantil" based on the categories found on the Poocoinswapse website.
Generated: DETERMINISTIC_4c3a64439fa02605
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters an array of shoe types to include only "tenis de corrida" and "chuteira infantil".
 * 
 * @param {Array<string>} shoeArray - The array of shoe types to be filtered.
 * @returns {Array<string>} - A new array containing only the filtered shoe types.
 */
function filterShoeTypes(shoeArray) {
    // Validate input
    if (!Array.isArray(shoeArray)) {
        throw new TypeError('Expected an array of strings as input.');
    }

    // Define allowed categories
    const allowedCategories = ["tenis de corrida", "chuteira infantil"];

    // Filter the array to include only the allowed categories
    const filteredShoes = shoeArray.filter(shoe => {
        if (typeof shoe !== 'string') {
            console.warn(`Invalid item found in array: ${shoe}. Expected a string.`);
            return false; // Skip invalid items
        }
        return allowedCategories.includes(shoe.toLowerCase());
    });

    return filteredShoes;
}

// Example usage:
// Input array contains various shoe types
const shoeTypes = [
    "Tenis de corrida", 
    "Chuteira infantil", 
    "Sandália", 
    "Sapato social", 
    "Chinelo", 
    "tenis de corrida"
];

try {
    const result = filterShoeTypes(shoeTypes);
    console.log('Filtered shoe types:', result); // Output: ['Tenis de corrida', 'Chuteira infantil', 'tenis de corrida']
} catch (error) {
    console.error('Error:', error.message);
}
```
