"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Develop a JavaScript function that allows users to search for auto parts by brand and model, similar to the filtering options provided on the autopecasbrazz site.
Generated: DETERMINISTIC_cff1bf4388aa7840
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Searches for auto parts based on the specified brand and model.
 * 
 * @param {Array} parts - An array of auto parts objects to search from.
 * @param {string} brand - The brand of the auto part to filter by.
 * @param {string} model - The model of the auto part to filter by.
 * @returns {Array} - An array of filtered auto parts that match the brand and model.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function searchAutoParts(parts, brand, model) {
    // Validate input parameters
    if (!Array.isArray(parts)) {
        throw new Error("The 'parts' parameter must be an array.");
    }
    if (typeof brand !== 'string' || typeof model !== 'string') {
        throw new Error("Both 'brand' and 'model' parameters must be strings.");
    }

    // Filter the parts based on brand and model
    const filteredParts = parts.filter(part => {
        return part.brand.toLowerCase() === brand.toLowerCase() &&
               part.model.toLowerCase() === model.toLowerCase();
    });

    return filteredParts;
}

// Example usage
const autoParts = [
    { id: 1, brand: 'Toyota', model: 'Camry', name: 'Brake Pad' },
    { id: 2, brand: 'Honda', model: 'Civic', name: 'Oil Filter' },
    { id: 3, brand: 'Toyota', model: 'Camry', name: 'Air Filter' },
    { id: 4, brand: 'Ford', model: 'F-150', name: 'Spark Plug' }
];

try {
    const results = searchAutoParts(autoParts, 'Toyota', 'Camry');
    console.log('Filtered Auto Parts:', results);
} catch (error) {
    console.error('Error:', error.message);
}
```
