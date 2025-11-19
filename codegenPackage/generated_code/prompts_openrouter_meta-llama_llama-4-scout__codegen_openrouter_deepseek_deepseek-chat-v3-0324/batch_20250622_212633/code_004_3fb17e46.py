"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Create a JavaScript code to implement a product selection system for Paradigma ЖБИ, allowing users to choose products for different construction projects, such as civil, industrial, or railway construction.
Generated: DETERMINISTIC_3fb17e463e6fa8d8
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Selection System for Paradigma ЖБИ
 * Allows users to choose products for different construction projects
 */

// Product Database
const productDatabase = {
    civil: [
        { id: 'C001', name: 'Reinforced Concrete Slab', description: 'Standard slab for civil construction', price: 1200 },
        { id: 'C002', name: 'Precast Concrete Wall', description: 'Prefabricated wall panel', price: 950 },
        { id: 'C003', name: 'Concrete Beam', description: 'Load-bearing beam for structures', price: 1800 }
    ],
    industrial: [
        { id: 'I001', name: 'Heavy-Duty Column', description: 'Industrial-grade support column', price: 2500 },
        { id: 'I002', name: 'Industrial Floor Panel', description: 'High-strength flooring', price: 3200 },
        { id: 'I003', name: 'Crane Beam', description: 'Specialized beam for industrial facilities', price: 4100 }
    ],
    railway: [
        { id: 'R001', name: 'Railway Sleeper', description: 'Concrete sleeper for tracks', price: 150 },
        { id: 'R002', name: 'Bridge Girder', description: 'Railway bridge component', price: 3800 },
        { id: 'R003', name: 'Platform Slab', description: 'Station platform element', price: 2200 }
    ]
};

// Cart to store selected products
let shoppingCart = [];

/**
 * Get products by project type
 * @param {string} projectType - Type of construction project
 * @returns {Array} Array of products for the specified project type
 */
function getProductsByProjectType(projectType) {
    try {
        if (!productDatabase[projectType]) {
            throw new Error(`Invalid project type: ${projectType}`);
        }
        return productDatabase[projectType];
    } catch (error) {
        console.error('Error fetching products:', error.message);
        return [];
    }
}

/**
 * Add product to shopping cart
 * @param {string} projectType - Type of construction project
 * @param {string} productId - ID of the product to add
 * @returns {boolean} True if product was added successfully, false otherwise
 */
function addToCart(projectType, productId) {
    try {
        const products = getProductsByProjectType(projectType);
        const product = products.find(p => p.id === productId);
        
        if (!product) {
            throw new Error(`Product not found: ${productId}`);
        }
        
        shoppingCart.push({...product, projectType});
        return true;
    } catch (error) {
        console.error('Error adding to cart:', error.message);
        return false;
    }
}

/**
 * Remove product from shopping cart
 * @param {string} productId - ID of the product to remove
 * @returns {boolean} True if product was removed successfully, false otherwise
 */
function removeFromCart(productId) {
    try {
        const index = shoppingCart.findIndex(item => item.id === productId);
        if (index === -1) {
            throw new Error(`Product not found in cart: ${productId}`);
        }
        
        shoppingCart.splice(index, 1);
        return true;
    } catch (error) {
        console.error('Error removing from cart:', error.message);
        return false;
    }
}

/**
 * Calculate total price of items in cart
 * @returns {number} Total price of all items in cart
 */
function calculateTotal() {
    return shoppingCart.reduce((total, item) => total + item.price, 0);
}

/**
 * Clear the shopping cart
 */
function clearCart() {
    shoppingCart = [];
}

/**
 * Get all available project types
 * @returns {Array} Array of available project types
 */
function getProjectTypes() {
    return Object.keys(productDatabase);
}

// Export functions for use in other modules
module.exports = {
    getProductsByProjectType,
    addToCart,
    removeFromCart,
    calculateTotal,
    clearCart,
    getProjectTypes,
    getCart: () => [...shoppingCart] // Return copy of cart to prevent direct modification
};
```
