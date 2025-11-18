"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Generate a function in JavaScript that categorizes fabrics from Shaoxing Eagles Textile Co., Ltd. based on their use cases, such as swimwear, sportswear, or leggings, using fabric names like "polar fleece" and "single jersey."
Generated: DETERMINISTIC_672d5b4009297298
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Categorizes fabrics based on their use cases.
 * 
 * @param {string} fabricName - The name of the fabric to be categorized.
 * @returns {string} - The category of the fabric (e.g., 'Swimwear', 'Sportswear', 'Leggings', or 'Unknown').
 */
function categorizeFabric(fabricName) {
    // Ensure input is a valid string
    if (typeof fabricName !== 'string' || fabricName.trim() === '') {
        throw new Error('Invalid fabric name. Please provide a valid string.');
    }

    // Normalize the fabric name to lowercase for consistent comparison
    const normalizedFabricName = fabricName.trim().toLowerCase();

    // Fabric categories mapping
    const fabricCategories = {
        swimwear: ['single jersey', 'spandex', 'nylon', 'polyester'],
        sportswear: ['mesh', 'interlock', 'quick-dry', 'microfiber'],
        leggings: ['polar fleece', 'lycra', 'double jersey', 'cotton blend']
    };

    // Iterate through the categories and return the matching category
    for (const category in fabricCategories) {
        if (fabricCategories[category].includes(normalizedFabricName)) {
            return category.charAt(0).toUpperCase() + category.slice(1); // Capitalize the category name
        }
    }

    // If no match is found, return 'Unknown'
    return 'Unknown';
}

// Example Usage
try {
    console.log(categorizeFabric('Polar Fleece')); // Output: Leggings
    console.log(categorizeFabric('Single Jersey')); // Output: Swimwear
    console.log(categorizeFabric('Mesh')); // Output: Sportswear
    console.log(categorizeFabric('Unknown Fabric')); // Output: Unknown
} catch (error) {
    console.error(error.message);
}
```
