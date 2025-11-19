"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Generate a JavaScript function to validate and classify products for customs brokerage purposes in Bangladesh, taking into account tariffs and duty rates, as described in the Daimon Logistics services.
Generated: DETERMINISTIC_e8f67f3f9d60c84a
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates and classifies products for customs brokerage purposes in Bangladesh.
 * 
 * @param {Object} product - The product object to validate and classify.
 * @param {string} product.name - The name of the product.
 * @param {number} product.value - The declared value of the product in BDT.
 * @param {string} product.category - The category of the product (e.g., electronics, clothing).
 * @param {number} product.weight - The weight of the product in kilograms.
 * @returns {Object} - An object containing validation status and classification details.
 * @throws {Error} - Throws an error if the product data is invalid.
 */
function validateAndClassifyProduct(product) {
    // Validate input
    if (!product || typeof product !== 'object') {
        throw new Error('Invalid product data. Expected an object.');
    }
    if (typeof product.name !== 'string' || product.name.trim() === '') {
        throw new Error('Product name is required and must be a non-empty string.');
    }
    if (typeof product.value !== 'number' || product.value <= 0) {
        throw new Error('Product value must be a positive number.');
    }
    if (typeof product.category !== 'string' || product.category.trim() === '') {
        throw new Error('Product category is required and must be a non-empty string.');
    }
    if (typeof product.weight !== 'number' || product.weight <= 0) {
        throw new Error('Product weight must be a positive number.');
    }

    // Define tariff and duty rates based on product category
    const tariffRates = {
        electronics: 0.15, // 15% tariff for electronics
        clothing: 0.10,     // 10% tariff for clothing
        food: 0.05,         // 5% tariff for food
        // Add more categories as needed
    };

    // Classify product and calculate duties
    const category = product.category.toLowerCase();
    const tariffRate = tariffRates[category] || 0; // Default to 0 if category not found
    const duty = product.value * tariffRate;

    // Prepare the classification result
    const classificationResult = {
        isValid: true,
        classification: {
            name: product.name,
            category: category,
            value: product.value,
            weight: product.weight,
            tariffRate: tariffRate,
            duty: duty,
        },
    };

    return classificationResult;
}

// Example usage
try {
    const product = {
        name: 'Smartphone',
        value: 50000,
        category: 'Electronics',
        weight: 0.2,
    };

    const result = validateAndClassifyProduct(product);
    console.log('Product classification result:', result);
} catch (error) {
    console.error('Error validating product:', error.message);
}
```
