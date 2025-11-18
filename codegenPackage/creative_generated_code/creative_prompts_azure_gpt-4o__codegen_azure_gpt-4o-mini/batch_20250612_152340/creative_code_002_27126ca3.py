"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Generate JavaScript code to create a dynamic shopping cart system for a website selling Panasonic LED lights, ensuring it supports features like discount calculation and product filtering (e.g., "Đèn LED Âm Trần Panasonic" or "Đèn LED Diệt Khuẩn Panasonic").
Generated: DETERMINISTIC_27126ca38e16d0e3
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart Class to manage the shopping cart functionality
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold items in the cart
        this.discount = 0; // Discount percentage
    }

    // Method to add an item to the cart
    addItem(product) {
        if (!product || !product.id || !product.name || !product.price) {
            throw new Error('Invalid product. Please provide a valid product object.');
        }
        this.items.push(product);
    }

    // Method to remove an item from the cart by ID
    removeItem(productId) {
        const index = this.items.findIndex(item => item.id === productId);
        if (index === -1) {
            throw new Error('Product not found in cart.');
        }
        this.items.splice(index, 1);
    }

    // Method to apply a discount to the cart
    applyDiscount(discountPercentage) {
        if (discountPercentage < 0 || discountPercentage > 100) {
            throw new Error('Discount must be between 0 and 100.');
        }
        this.discount = discountPercentage;
    }

    // Method to calculate the total price of items in the cart
    calculateTotal() {
        const total = this.items.reduce((sum, item) => sum + item.price, 0);
        return total - (total * (this.discount / 100)); // Apply discount
    }

    // Method to get the items in the cart
    getItems() {
        return this.items;
    }

    // Method to filter products based on search criteria
    filterProducts(products, searchTerm) {
        return products.filter(product => product.name.includes(searchTerm));
    }
}

// Example usage:
const cart = new ShoppingCart();

// Sample products
const products = [
    { id: 1, name: 'Đèn LED Âm Trần Panasonic', price: 500000 },
    { id: 2, name: 'Đèn LED Diệt Khuẩn Panasonic', price: 700000 },
    { id: 3, name: 'Đèn LED Thông Minh', price: 600000 },
];

// Adding products to the cart
try {
    cart.addItem(products[0]);
    cart.addItem(products[1]);
    console.log('Items in cart:', cart.getItems());

    // Applying discount
    cart.applyDiscount(10);
    console.log('Total after discount:', cart.calculateTotal());

    // Filtering products
    const filteredProducts = cart.filterProducts(products, 'Đèn LED');
    console.log('Filtered products:', filteredProducts);

    // Removing an item
    cart.removeItem(1);
    console.log('Items in cart after removal:', cart.getItems());
} catch (error) {
    console.error('Error:', error.message);
}
```
