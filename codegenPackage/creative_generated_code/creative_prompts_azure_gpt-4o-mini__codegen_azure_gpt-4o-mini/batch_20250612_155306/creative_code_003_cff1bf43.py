"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Develop a JavaScript function that allows users to search for auto parts by brand and model, similar to the filtering options provided on the autopecasbrazz site.
Generated: DETERMINISTIC_cff1bf4388aa7840
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to search for auto parts by brand and model.
 * @param {Array} parts - An array of auto parts to search from.
 * @param {string} brand - The brand of the auto part.
 * @param {string} model - The model of the auto part.
 * @returns {Array} - An array of filtered auto parts that match the specified brand and model.
 */
function searchAutoParts(parts, brand, model) {
    // Validate input parameters
    if (!Array.isArray(parts)) {
        throw new Error("The 'parts' parameter must be an array.");
    }
    if (typeof brand !== 'string' || typeof model !== 'string') {
        throw new Error("Both 'brand' and 'model' parameters must be strings.");
    }

    // Convert filters to lower case for case-insensitive matching
    const lowerCaseBrand = brand.toLowerCase();
    const lowerCaseModel = model.toLowerCase();

    // Filter the parts based on brand and model
    const filteredParts = parts.filter(part => {
        return part.brand.toLowerCase() === lowerCaseBrand && part.model.toLowerCase() === lowerCaseModel;
    });

    return filteredParts;
}

// Example usage
const autoParts = [
    { id: 1, brand: 'Toyota', model: 'Camry', partName: 'Brake Pad' },
    { id: 2, brand: 'Honda', model: 'Civic', partName: 'Air Filter' },
    { id: 3, brand: 'Toyota', model: 'Tacoma', partName: 'Oil Filter' },
    { id: 4, brand: 'Honda', model: 'Civic', partName: 'Brake Pad' },
];

// Search for Toyota Camry parts
try {
    const results = searchAutoParts(autoParts, 'Toyota', 'Camry');
    console.log('Search Results:', results);
} catch (error) {
    console.error('Error searching auto parts:', error.message);
}
```
