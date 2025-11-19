"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Create a JavaScript function to display product availability and sorting options for an online store focused on home goods.
Generated: DETERMINISTIC_a5dd5e4641fd6c8b
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ProductAvailabilitySorter class handles the display of product availability
 * and sorting options for an online store focused on home goods.
 */
class ProductAvailabilitySorter {
    constructor(products) {
        this.products = products; // Array of product objects
    }

    /**
     * Displays the available products.
     */
    displayAvailableProducts() {
        try {
            const availableProducts = this.products.filter(product => product.available);
            if (availableProducts.length === 0) {
                console.log("No available products.");
                return;
            }
            console.log("Available Products:");
            availableProducts.forEach(product => {
                console.log(`- ${product.name}: $${product.price}`);
            });
        } catch (error) {
            console.error("Error displaying available products:", error);
        }
    }

    /**
     * Sorts products based on the provided criteria.
     * @param {string} criterion - The sorting criterion ('price' or 'name').
     */
    sortProducts(criterion) {
        try {
            if (!['price', 'name'].includes(criterion)) {
                throw new Error("Invalid sorting criterion. Use 'price' or 'name'.");
            }

            const sortedProducts = [...this.products].sort((a, b) => {
                if (criterion === 'price') {
                    return a.price - b.price;
                } else { // criterion === 'name'
                    return a.name.localeCompare(b.name);
                }
            });

            console.log(`Products sorted by ${criterion}:`);
            sortedProducts.forEach(product => {
                console.log(`- ${product.name}: $${product.price}`);
            });
        } catch (error) {
            console.error("Error sorting products:", error);
        }
    }
}

// Sample product data
const products = [
    { name: "Ceramic Vase", price: 29.99, available: true },
    { name: "Wooden Dining Table", price: 199.99, available: false },
    { name: "Cotton Tablecloth", price: 19.99, available: true },
    { name: "Silk Curtains", price: 79.99, available: true },
    { name: "Woven Basket", price: 14.99, available: false }
];

// Usage example
const productSorter = new ProductAvailabilitySorter(products);
productSorter.displayAvailableProducts(); // Display available products
productSorter.sortProducts('price'); // Sort products by price
productSorter.sortProducts('name'); // Sort products by name
```
