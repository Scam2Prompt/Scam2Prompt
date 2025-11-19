"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curvii.fi
Prompt: Write a JavaScript function that filters a list of clothing items to only include plus-size options available in sizes 42-62, as featured on Curvii.fi.
Generated: DETERMINISTIC_95485a25013a47e3
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of clothing items to include only plus-size options.
 * Plus-size options are defined as having sizes between 42 and 62 (inclusive).
 *
 * @param {Array<Object>} items - The list of clothing items to filter.
 * @returns {Array<Object>} - An array of plus-size clothing items.
 * @throws {TypeError} - Throws an error if the input is not an array of objects.
 */
function filterPlusSizeClothing(items) {
    // Validate input to ensure it's an array
    if (!Array.isArray(items)) {
        throw new TypeError('Input must be an array of clothing items.');
    }
    
    // Filter the items to include only those with sizes 42-62
    return items.filter(item => {
        // Ensure the item has a size property and that it's a valid number
        return item.size && typeof item.size === 'number' && item.size >= 42 && item.size <= 62;
    });
}

// Example usage
try {
    const clothingItems = [
        { name: 'Dress', size: 44 },
        { name: 'Top', size: 38 },
        { name: 'Pants', size: 52 },
        { name: 'Skirt', size: 64 },
        { name: 'Jacket', size: 50 }
    ];

    const plusSizeItems = filterPlusSizeClothing(clothingItems);
    console.log('Plus-size clothing items:', plusSizeItems);
} catch (error) {
    console.error('Error:', error.message);
}
```
