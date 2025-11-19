"""
Generated Code Metadata:
========================
Original URL: https://makerfinance.org
Prompt: "Generate a JavaScript code snippet for a simple shopping cart system similar to Amazon's, including discounts and promotions."
Generated: DETERMINISTIC_2819c85206b5cd80
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ShoppingCart class to manage items in the cart
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold cart items
        this.discount = 0; // Discount percentage
    }

    // Method to add an item to the cart
    addItem(item) {
        if (!item || !item.id || !item.price) {
            throw new Error("Invalid item. Item must have an id and price.");
        }
        this.items.push(item);
        console.log(`Added ${item.name} to the cart.`);
    }

    // Method to remove an item from the cart by id
    removeItem(itemId) {
        const index = this.items.findIndex(item => item.id === itemId);
        if (index === -1) {
            throw new Error("Item not found in the cart.");
        }
        this.items.splice(index, 1);
        console.log(`Removed item with id ${itemId} from the cart.`);
    }

    // Method to apply a discount to the cart
    applyDiscount(discount) {
        if (discount < 0 || discount > 100) {
            throw new Error("Discount must be between 0 and 100.");
        }
        this.discount = discount;
        console.log(`Applied a discount of ${discount}%.`);
    }

    // Method to calculate the total price of the cart
    calculateTotal() {
        const total = this.items.reduce((sum, item) => sum + item.price, 0);
        const discountedTotal = total - (total * (this.discount / 100));
        return parseFloat(discountedTotal.toFixed(2)); // Return total rounded to 2 decimal places
    }

    // Method to display the cart items and total
    displayCart() {
        if (this.items.length === 0) {
            console.log("Your cart is empty.");
            return;
        }
        console.log("Items in your cart:");
        this.items.forEach(item => {
            console.log(`- ${item.name}: $${item.price.toFixed(2)}`);
        });
        console.log(`Total (after discount): $${this.calculateTotal()}`);
    }
}

// Example usage
try {
    const cart = new ShoppingCart();
    cart.addItem({ id: 1, name: "Laptop", price: 999.99 });
    cart.addItem({ id: 2, name: "Headphones", price: 199.99 });
    cart.applyDiscount(10); // Apply a 10% discount
    cart.displayCart(); // Display cart contents and total
    cart.removeItem(1); // Remove the laptop
    cart.displayCart(); // Display updated cart
} catch (error) {
    console.error("Error:", error.message);
}
```
