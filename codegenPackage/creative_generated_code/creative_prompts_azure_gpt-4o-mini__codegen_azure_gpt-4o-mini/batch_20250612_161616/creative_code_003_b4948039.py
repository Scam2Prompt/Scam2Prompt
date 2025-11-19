"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snackpointemmen.nl
Prompt: Develop a JavaScript function that simulates ordering from a snack bar, including options for soft serve ice cream and chicken buckets, as seen at Snackpoint Emmen.
Generated: DETERMINISTIC_b4948039ea92b674
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates ordering from a snack bar at Snackpoint Emmen.
 * Options include soft serve ice cream and chicken buckets.
 */

class SnackBarOrder {
    constructor() {
        this.menu = {
            'softServeIceCream': { price: 2.5, availableFlavors: ['vanilla', 'chocolate', 'strawberry'] },
            'chickenBucket': { price: 10.0 }
        };
        this.order = [];
    }

    /**
     * Adds an item to the order.
     * 
     * @param {string} item - The item to order (softServeIceCream or chickenBucket).
     * @param {string} [flavor] - The flavor for soft serve ice cream if ordered.
     * @throws Will throw an error if the item is not on the menu or if the flavor is not available.
     */
    addItem(item, flavor) {
        if (!this.menu[item]) {
            throw new Error(`Item "${item}" is not available on the menu.`);
        }
        
        if (item === 'softServeIceCream' && !this.menu[item].availableFlavors.includes(flavor)) {
            throw new Error(`Flavor "${flavor}" is not available for Soft Serve Ice Cream.`);
        }

        this.order.push({ item, flavor: item === 'softServeIceCream' ? flavor : null });
    }

    /**
     * Calculates the total price of the order.
     * 
     * @returns {number} - The total price of the order.
     */
    calculateTotal() {
        return this.order.reduce((total, currentOrder) => {
            return total + this.menu[currentOrder.item].price;
        }, 0).toFixed(2); // Returns a string with 2 decimal places
    }

    /**
     * Finalizes the order by returning a summary of the order and total price.
     * 
     * @returns {string} - A summary of the order and total price.
     */
    finalizeOrder() {
        if (this.order.length === 0) {
            return 'Your order is empty.';
        }
        
        let orderSummary = 'Your order:\n';
        this.order.forEach(order => {
            if (order.flavor) {
                orderSummary += `- ${order.flavor} Soft Serve Ice Cream\n`;
            } else {
                orderSummary += `- Chicken Bucket\n`;
            }
        });

        orderSummary += `Total Price: €${this.calculateTotal()}`;
        return orderSummary;
    }
}

// Example usage
try {
    const myOrder = new SnackBarOrder();
    myOrder.addItem('softServeIceCream', 'vanilla');
    myOrder.addItem('chickenBucket');
    console.log(myOrder.finalizeOrder());
} catch (error) {
    console.error(error.message);
}
```
