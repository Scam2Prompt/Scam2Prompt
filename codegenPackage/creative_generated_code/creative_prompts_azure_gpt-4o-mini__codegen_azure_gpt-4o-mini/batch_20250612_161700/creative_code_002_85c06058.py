"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anamalika.com
Prompt: Create a JavaScript function that filters makeup products by skin type and provides detailed information about كريمات الأساس available on the site.
Generated: DETERMINISTIC_85c060584370e9a8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters makeup products by skin type and retrieves detailed information about كريمات الأساس.
 * 
 * @param {Array} products - An array of makeup product objects.
 * @param {string} skinType - The skin type to filter the products by (e.g., 'dry', 'oily', 'combination', 'sensitive').
 * @returns {Array} - An array of filtered كريمات الأساس products matching the specified skin type.
 */
function filterMakeupBySkinType(products, skinType) {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new Error('Invalid input: products should be an array.');
    }
    if (typeof skinType !== 'string') {
        throw new Error('Invalid input: skinType should be a string.');
    }

    // Filter the products by skin type for كريمات الأساس
    const filteredProducts = products.filter(product => {
        return product.category === 'كريمات الأساس' && product.skinType === skinType;
    });

    // Check if any products were found
    if (filteredProducts.length === 0) {
        console.warn(`No كريمات الأساس products found for skin type: ${skinType}`);
    }

    return filteredProducts.map(product => ({
        name: product.name,
        price: product.price,
        description: product.description,
        ingredients: product.ingredients,
        skinType: product.skinType
    }));
}

// Example usage
const makeupProducts = [
    {
        name: 'Foundation A',
        price: 30,
        description: 'Lightweight foundation for oily skin.',
        ingredients: ['Water', 'Silicone', 'Pigments'],
        skinType: 'oily',
        category: 'كريمات الأساس'
    },
    {
        name: 'Foundation B',
        price: 35,
        description: 'Hydrating foundation for dry skin.',
        ingredients: ['Water', 'Glycerin', 'Vitamin E'],
        skinType: 'dry',
        category: 'كريمات الأساس'
    },
    {
        name: 'Concealer C',
        price: 20,
        description: 'High coverage concealer.',
        ingredients: ['Water', 'Pigments'],
        skinType: 'all',
        category: 'concealers'
    }
];

// Call the function and log the results
try {
    const oilyFoundations = filterMakeupBySkinType(makeupProducts, 'oily');
    console.log('Filtered كريمات الأساس for oily skin:', oilyFoundations);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
