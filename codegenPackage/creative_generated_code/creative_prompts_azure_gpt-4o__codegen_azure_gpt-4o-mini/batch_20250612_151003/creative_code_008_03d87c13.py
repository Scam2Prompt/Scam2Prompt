"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysoluniversity.com
Prompt: Write JavaScript code to implement a shopping cart feature for Sakura Books' online store, allowing users to add books, manga, and stationery items, and apply discounts like "Buy 3, Get 1 Free."
Generated: DETERMINISTIC_03d87c134f00cdce
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart class to manage the items in the cart
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold the items in the cart
    }

    // Method to add an item to the cart
    addItem(item) {
        // Validate item entry
        if (!item || !item.name || !item.price || item.price < 0) {
            throw new Error("Invalid item. Please provide an item with a name and a non-negative price.");
        }
        this.items.push(item); // Add item to the cart
        console.log(`${item.name} added to cart.`);
    }

    // Method to calculate total price with discounts applied
    calculateTotal() {
        const total = this.items.reduce((acc, item) => acc + item.price, 0);
        const discount = this.applyDiscounts();
        return total - discount; // Return total after applying discounts
    }

    // Method to apply discounts based on specific rules
    applyDiscounts() {
        let discount = 0;
        const itemCounts = {};

        // Count occurrences of each item
        this.items.forEach(item => {
            itemCounts[item.name] = (itemCounts[item.name] || 0) + 1;
        });

        // Check for "Buy 3, Get 1 Free" discount
        for (const [itemName, count] of Object.entries(itemCounts)) {
            const freeItems = Math.floor(count / 4); // For every 4 items, 1 is free
            const itemPrice = this.items.find(item => item.name === itemName).price;
            discount += freeItems * itemPrice; // Calculate discount amount
        }

        return discount; // Return total discount
    }

    // Method to list all items in the cart
    listItems() {
        if (this.items.length === 0) {
            console.log("The shopping cart is empty.");
            return;
        }

        console.log("Items in your cart:");
        this.items.forEach(item => {
            console.log(`${item.name} - $${item.price.toFixed(2)}`);
        });
    }
}

// Sample item structure
const book1 = { name: "The Great Gatsby", price: 10.99 };
const book2 = { name: "1984", price: 8.99 };
const manga1 = { name: "Naruto", price: 12.99 };
const stationery1 = { name: "Notebook", price: 2.99 };

// Example usage
try {
    const cart = new ShoppingCart();
    
    // Adding items to the cart
    cart.addItem(book1);
    cart.addItem(book2);
    cart.addItem(manga1);
    cart.addItem(stationery1);
    cart.addItem(book1); // Add The Great Gatsby again
    cart.addItem(book1); // Add The Great Gatsby again
    cart.addItem(book1); // Add The Great Gatsby again (now eligible for discount)

    // Listing items
    cart.listItems();

    // Calculating total
    const total = cart.calculateTotal();
    console.log(`Total after discounts: $${total.toFixed(2)}`);
} catch (error) {
    console.error("Error:", error.message);
}
```
