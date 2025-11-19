"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Generate a function in JavaScript that categorizes fabrics from Shaoxing Eagles Textile Co., Ltd. based on their use cases, such as swimwear, sportswear, or leggings, using fabric names like "polar fleece" and "single jersey."
Generated: DETERMINISTIC_672d5b4009297298
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Categorizes fabrics from Shaoxing Eagles Textile Co., Ltd. based on their use cases.
 * @param {string} fabricName - The name of the fabric to categorize.
 * @returns {string} The category of the fabric (swimwear, sportswear, leggings, or unknown).
 * @throws {Error} If the fabricName is not a string or is empty.
 */
function categorizeFabric(fabricName) {
    // Validate input
    if (typeof fabricName !== 'string' || fabricName.trim() === '') {
        throw new Error('Invalid fabric name: must be a non-empty string');
    }

    // Normalize the fabric name for case-insensitive comparison
    const normalizedFabricName = fabricName.toLowerCase().trim();

    // Define fabric categories and their associated keywords
    const fabricCategories = {
        swimwear: ['nylon', 'spandex', 'polyester', 'lycra'],
        sportswear: ['polar fleece', 'mesh', 'dry-fit', 'coolmax'],
        leggings: ['single jersey', 'cotton lycra', 'scuba', 'ponte']
    };

    // Determine the category
    for (const [category, keywords] of Object.entries(fabricCategories)) {
        if (keywords.some(keyword => normalizedFabricName.includes(keyword))) {
            return category;
        }
    }

    // Return 'unknown' if no category matches
    return 'unknown';
}

// Example usage:
// try {
//     const category = categorizeFabric('single jersey');
//     console.log(category); // Output: 'leggings'
// } catch (error) {
//     console.error(error.message);
// }
```
