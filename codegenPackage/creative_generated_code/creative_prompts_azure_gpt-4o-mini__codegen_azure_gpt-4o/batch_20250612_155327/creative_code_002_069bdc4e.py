"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Create a JavaScript code example that simulates the inventory management for industrial brushes, including features for standard and custom products as highlighted on the VIRCOMEM site.
Generated: DETERMINISTIC_069bdc4e7603c4ef
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Inventory Management System for Industrial Brushes
 * Features include management of standard and custom products.
 * This code follows best practices, includes error handling, and is production-ready.
 */

// Inventory class to manage brushes
class Inventory {
    constructor() {
        this.standardProducts = [];
        this.customProducts = [];
    }

    /**
     * Add a standard product to the inventory.
     * @param {Object} product - An object representing the standard product.
     */
    addStandardProduct(product) {
        // Validation for product input
        if (!product.id || !product.name || !product.quantity || product.quantity < 0) {
            throw new Error('Invalid product details for standard product.');
        }
        this.standardProducts.push({ ...product });
    }

    /**
     * Add a custom product to the inventory.
     * @param {Object} product - An object representing the custom product.
     */
    addCustomProduct(product) {
        // Validation for product input
        if (!product.id || !product.name || !product.quantity || product.quantity < 0 || !product.customSpecs) {
            throw new Error('Invalid product details for custom product.');
        }
        this.customProducts.push({ ...product });
    }

    /**
     * Update the quantity of a product in inventory.
     * @param {string} productId - The ID of the product to update.
     * @param {number} newQuantity - The new quantity to set.
     */
    updateProductQuantity(productId, newQuantity) {
        if (newQuantity < 0) {
            throw new Error('Quantity cannot be negative.');
        }

        let productFound = false;

        // Update standard products
        this.standardProducts.forEach(product => {
            if (product.id === productId) {
                product.quantity = newQuantity;
                productFound = true;
            }
        });

        // Update custom products
        this.customProducts.forEach(product => {
            if (product.id === productId) {
                product.quantity = newQuantity;
                productFound = true;
            }
        });

        if (!productFound) {
            throw new Error('Product not found in inventory.');
        }
    }

    /**
     * Get the details of a product by ID.
     * @param {string} productId - The ID of the product to retrieve.
     * @returns {Object} The product details.
     */
    getProductDetails(productId) {
        // Search standard products
        const standardProduct = this.standardProducts.find(product => product.id === productId);
        if (standardProduct) return standardProduct;

        // Search custom products
        const customProduct = this.customProducts.find(product => product.id === productId);
        if (customProduct) return customProduct;

        throw new Error('Product not found in inventory.');
    }

    /**
     * List all products in inventory.
     * @returns {Object} An object containing arrays of standard and custom products.
     */
    listAllProducts() {
        return {
            standardProducts: this.standardProducts,
            customProducts: this.customProducts
        };
    }
}

// Example usage of Inventory class
try {
    const inventory = new Inventory();

    // Add standard products
    inventory.addStandardProduct({ id: 's1', name: 'Standard Brush A', quantity: 100 });
    inventory.addStandardProduct({ id: 's2', name: 'Standard Brush B', quantity: 50 });

    // Add custom products
    inventory.addCustomProduct({
        id: 'c1',
        name: 'Custom Brush X',
        quantity: 20,
        customSpecs: { material: 'Steel', size: 'Large' }
    });

    inventory.addCustomProduct({
        id: 'c2',
        name: 'Custom Brush Y',
        quantity: 10,
        customSpecs: { material: 'Plastic', size: 'Small' }
    });

    // Update product quantity
    inventory.updateProductQuantity('s1', 120);

    // Get product details
    console.log('Product Details:', inventory.getProductDetails('c1'));

    // List all products
    console.log('Inventory:', inventory.listAllProducts());
} catch (error) {
    console.error('Error:', error.message);
}
```
