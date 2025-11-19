"""
Generated Code Metadata:
========================
Original URL: https://anamalika.com
Prompt: Create a JavaScript function that filters makeup products by skin type and provides detailed information about كريمات الأساس available on the site.
Generated: DETERMINISTIC_85c060584370e9a8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters makeup products by skin type and retrieves detailed information
 * about foundation creams (كريمات الأساس).
 * 
 * @param {Array} products - Array of makeup product objects.
 * @param {string} skinType - The skin type to filter products by (e.g., 'oily', 'dry', 'combination').
 * @returns {Array} - An array of foundation cream products that match the specified skin type.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterFoundationBySkinType(products, skinType) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new Error('Invalid input: products must be an array.');
    }
    if (typeof skinType !== 'string') {
        throw new Error('Invalid input: skinType must be a string.');
    }

    // Filter products based on skin type and type of product
    const filteredProducts = products.filter(product => {
        return product.skinType === skinType && product.type === 'foundation';
    });

    // Check if any products were found
    if (filteredProducts.length === 0) {
        console.warn(`No foundation products found for skin type: ${skinType}`);
    }

    // Return detailed information about the filtered foundation products
    return filteredProducts.map(product => ({
        name: product.name,
        brand: product.brand,
        price: product.price,
        description: product.description,
        ingredients: product.ingredients,
        skinType: product.skinType,
    }));
}

// Example usage
const makeupProducts = [
    {
        name: 'Matte Foundation',
        brand: 'Brand A',
        price: 30,
        description: 'A long-lasting matte finish foundation.',
        ingredients: ['Water', 'Silica', 'Glycerin'],
        skinType: 'oily',
        type: 'foundation'
    },
    {
        name: 'Hydrating Foundation',
        brand: 'Brand B',
        price: 35,
        description: 'A hydrating foundation for dry skin.',
        ingredients: ['Water', 'Hyaluronic Acid', 'Glycerin'],
        skinType: 'dry',
        type: 'foundation'
    },
    {
        name: 'BB Cream',
        brand: 'Brand C',
        price: 25,
        description: 'A lightweight BB cream for combination skin.',
        ingredients: ['Water', 'Titanium Dioxide', 'Glycerin'],
        skinType: 'combination',
        type: 'bb cream'
    }
];

try {
    const filteredFoundations = filterFoundationBySkinType(makeupProducts, 'dry');
    console.log(filteredFoundations);
} catch (error) {
    console.error(error.message);
}
```
