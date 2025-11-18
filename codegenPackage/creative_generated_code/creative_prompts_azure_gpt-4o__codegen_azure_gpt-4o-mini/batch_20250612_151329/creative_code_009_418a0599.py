"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.insectshieldzoro.com
Prompt: Write a JavaScript function to filter product options for mosquito nets based on fitment type (e.g., Velcro, magnetic, sliding) and material (e.g., stainless steel, fiberglass), as described on the Insect Shield ZORO webpage.
Generated: DETERMINISTIC_418a0599fd3cd6b4
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters product options for mosquito nets based on fitment type and material.
 * 
 * @param {Array} products - The array of product objects to filter.
 * @param {string} fitmentType - The fitment type to filter by (e.g., 'Velcro', 'magnetic', 'sliding').
 * @param {string} material - The material to filter by (e.g., 'stainless steel', 'fiberglass').
 * @returns {Array} - An array of filtered products that match the specified criteria.
 * 
 * @throws {Error} - Throws an error if the products array is not an array or if the input types are invalid.
 */
function filterMosquitoNets(products, fitmentType, material) {
    // Input validation
    if (!Array.isArray(products)) {
        throw new Error('Invalid input: products must be an array.');
    }
    if (typeof fitmentType !== 'string' || typeof material !== 'string') {
        throw new Error('Invalid input: fitmentType and material must be strings.');
    }

    // Filter the products based on fitmentType and material
    return products.filter(product => {
        return product.fitmentType === fitmentType && product.material === material;
    });
}

// Example usage
const mosquitoNets = [
    { name: 'Net A', fitmentType: 'Velcro', material: 'stainless steel' },
    { name: 'Net B', fitmentType: 'magnetic', material: 'fiberglass' },
    { name: 'Net C', fitmentType: 'sliding', material: 'stainless steel' },
    { name: 'Net D', fitmentType: 'Velcro', material: 'fiberglass' },
];

// Filtering example
try {
    const filteredProducts = filterMosquitoNets(mosquitoNets, 'Velcro', 'stainless steel');
    console.log(filteredProducts);
} catch (error) {
    console.error(error.message);
}
```
