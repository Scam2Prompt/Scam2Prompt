"""
Generated Code Metadata:
========================
Original URL: https://hnu.co.id
Prompt: Create a JavaScript function that filters a list of herbal products based on their health benefits, particularly those related to boosting stamina and immune support as highlighted on HNU's website.
Generated: DETERMINISTIC_6c71ff932b34b885
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters a list of herbal products based on health benefits related to stamina and immune support.
 * @param {Array} products - Array of herbal product objects to filter.
 * @param {Array} benefitKeywords - Keywords to match against product benefits (e.g., ['stamina', 'immune']).
 * @returns {Array} Filtered array of products that match the specified health benefits.
 * @throws {Error} If products is not an array or benefitKeywords is not provided.
 */
function filterHerbalProducts(products, benefitKeywords) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array.');
    }
    if (!benefitKeywords || !Array.isArray(benefitKeywords)) {
        throw new Error('Benefit keywords must be provided as an array.');
    }

    // Normalize keywords to lowercase for case-insensitive matching
    const normalizedKeywords = benefitKeywords.map(keyword => keyword.toLowerCase());

    // Filter products that contain any of the specified keywords in their benefits
    return products.filter(product => {
        // Check if product has benefits and it's a string or array
        if (!product.benefits) return false;

        let benefitsText;
        if (Array.isArray(product.benefits)) {
            benefitsText = product.benefits.join(' ').toLowerCase();
        } else if (typeof product.benefits === 'string') {
            benefitsText = product.benefits.toLowerCase();
        } else {
            return false;
        }

        // Check if any keyword matches the product benefits
        return normalizedKeywords.some(keyword => benefitsText.includes(keyword));
    });
}

// Example usage:
// const products = [
//     { name: 'Herb A', benefits: 'Boosts stamina and energy levels' },
//     { name: 'Herb B', benefits: ['Supports immune system', 'Reduces inflammation'] },
//     { name: 'Herb C', benefits: 'Improves digestion' }
// ];
// const filtered = filterHerbalProducts(products, ['stamina', 'immune']);
// console.log(filtered);
```
