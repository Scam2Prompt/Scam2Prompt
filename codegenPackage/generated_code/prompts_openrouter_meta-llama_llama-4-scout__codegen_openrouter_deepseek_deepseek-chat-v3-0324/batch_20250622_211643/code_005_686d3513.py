"""
Generated Code Metadata:
========================
Original URL: https://mimihao.cc
Prompt: "Design a simple e-commerce shopping cart system in JavaScript that could be used for selling items like those on mimihao.cc, including support for multiple product categories."
Generated: DETERMINISTIC_686d3513a3279ee2
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple E-commerce Shopping Cart System
 * Supports multiple product categories and basic cart operations
 */

// Product Class
class Product {
    /**
     * @param {string} id - Unique identifier for the product
     * @param {string} name - Product name
     * @param {number} price - Product price
     * @param {string} category - Product category
     * @param {string} [image] - Optional product image URL
     */
    constructor(id, name, price, category, image = '') {
        this.id = id;
        this.name = name;
        this.price = price;
        this.category = category;
        this.image = image;
    }
}

// Cart Item Class
class CartItem {
    /**
     * @param {Product} product - The product being added to cart
     * @param {number} quantity - Quantity of the product
     */
    constructor(product, quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    /**
     * Calculates total price for this cart item
     * @returns {number} Total price
     */
    getTotalPrice() {
        return this.product.price * this.quantity;
    }
}

// Shopping Cart Class
class ShoppingCart {
    constructor() {
        this.items = [];
    }

    /**
     * Adds a product to the cart or updates quantity if already exists
     * @param {Product} product - Product to add
     * @param {number} [quantity=1] - Quantity to add
     */
    addItem(product, quantity = 1) {
        if (!(product instanceof Product)) {
            throw new Error('Invalid product');
        }

        if (quantity <= 0) {
            throw new Error('Quantity must be positive');
        }

        const existingItem = this.items.find(item => item.product.id === product.id);
        if (existingItem) {
            existingItem.quantity += quantity;
        } else {
            this.items.push(new CartItem(product, quantity));
        }
    }

    /**
     * Removes a product from the cart
     * @param {string} productId - ID of product to remove
     */
    removeItem(productId) {
        this.items = this.items.filter(item => item.product.id !== productId);
    }

    /**
     * Updates quantity of a product in the cart
     * @param {string} productId - ID of product to update
     * @param {number} newQuantity - New quantity
     */
    updateQuantity(productId, newQuantity) {
        if (newQuantity <= 0) {
            this.removeItem(productId);
            return;
        }

        const item = this.items.find(item => item.product.id === productId);
        if (item) {
            item.quantity = newQuantity;
        }
    }

    /**
     * Calculates total price of all items in cart
     * @returns {number} Total price
     */
    getTotalPrice() {
        return this.items.reduce((total, item) => total + item.getTotalPrice(), 0);
    }

    /**
     * Gets count of all items in cart
     * @returns {number} Total item count
     */
    getItemCount() {
        return this.items.reduce((count, item) => count + item.quantity, 0);
    }

    /**
     * Clears all items from cart
     */
    clearCart() {
        this.items = [];
    }

    /**
     * Gets all items in cart grouped by category
     * @returns {Object} Items grouped by category
     */
    getItemsByCategory() {
        return this.items.reduce((acc, item) => {
            const category = item.product.category;
            if (!acc[category]) {
                acc[category] = [];
            }
            acc[category].push(item);
            return acc;
        }, {});
    }
}

// E-commerce Store Class
class ECommerceStore {
    constructor() {
        this.products = [];
        this.cart = new ShoppingCart();
        this.categories = new Set();
    }

    /**
     * Adds a product to the store
     * @param {Product} product - Product to add
     */
    addProduct(product) {
        if (!(product instanceof Product)) {
            throw new Error('Invalid product');
        }

        this.products.push(product);
        this.categories.add(product.category);
    }

    /**
     * Gets all products in a specific category
     * @param {string} category - Category to filter by
     * @returns {Array} Products in category
     */
    getProductsByCategory(category) {
        return this.products.filter(product => product.category === category);
    }

    /**
     * Gets all available categories
     * @returns {Array} All categories
     */
    getAllCategories() {
        return Array.from(this.categories);
    }
}

// Example Usage
/*
// Create store instance
const store = new ECommerceStore();

// Add some products
store.addProduct(new Product('1', 'T-Shirt', 19.99, 'Clothing', 'tshirt.jpg'));
store.addProduct(new Product('2', 'Jeans', 49.99, 'Clothing', 'jeans.jpg'));
store.addProduct(new Product('3', 'Smartphone', 599.99, 'Electronics', 'phone.jpg'));
store.addProduct(new Product('4', 'Laptop', 999.99, 'Electronics', 'laptop.jpg'));

// Add items to cart
store.cart.addItem(store.products[0], 2);
store.cart.addItem(store.products[2], 1);

// Get cart summary
console.log('Total items:', store.cart.getItemCount());
console.log('Total price:', store.cart.getTotalPrice());
console.log('Items by category:', store.cart.getItemsByCategory());
*/
```
