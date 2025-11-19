"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Create a JavaScript function to display product availability and sorting options for an online store focused on home goods.
Generated: DETERMINISTIC_a5dd5e4641fd6c8b
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ProductAvailabilityAndSorting class to manage product availability and sorting options.
 */
class ProductAvailabilityAndSorting {
    constructor(products) {
        // Initialize with an array of products
        this.products = products;
    }

    /**
     * Displays the availability of products.
     * @returns {void}
     */
    displayAvailability() {
        try {
            console.log("Product Availability:");
            this.products.forEach(product => {
                if (product.available) {
                    console.log(`${product.name}: In Stock`);
                } else {
                    console.log(`${product.name}: Out of Stock`);
                }
            });
        } catch (error) {
            console.error("Error displaying product availability:", error);
        }
    }

    /**
     * Sorts products based on the specified criteria.
     * @param {string} criteria - The criteria to sort by (e.g., 'price', 'name').
     * @returns {Array} - Sorted array of products.
     */
    sortProducts(criteria) {
        try {
            const sortedProducts = [...this.products]; // Create a shallow copy of the products array

            sortedProducts.sort((a, b) => {
                if (criteria === 'price') {
                    return a.price - b.price; // Sort by price
                } else if (criteria === 'name') {
                    return a.name.localeCompare(b.name); // Sort by name
                } else {
                    throw new Error("Invalid sorting criteria. Use 'price' or 'name'.");
                }
            });

            return sortedProducts;
        } catch (error) {
            console.error("Error sorting products:", error);
            return this.products; // Return unsorted products in case of error
        }
    }

    /**
     * Displays sorted products based on the specified criteria.
     * @param {string} criteria - The criteria to sort by (e.g., 'price', 'name').
     * @returns {void}
     */
    displaySortedProducts(criteria) {
        const sortedProducts = this.sortProducts(criteria);
        console.log(`Sorted Products by ${criteria}:`);
        sortedProducts.forEach(product => {
            console.log(`${product.name} - $${product.price.toFixed(2)} - ${product.available ? 'In Stock' : 'Out of Stock'}`);
        });
    }
}

// Example usage:
const products = [
    { name: "Sofa", price: 499.99, available: true },
    { name: "Coffee Table", price: 149.99, available: false },
    { name: "Dining Chair", price: 89.99, available: true },
    { name: "Lamp", price: 39.99, available: true }
];

const store = new ProductAvailabilityAndSorting(products);
store.displayAvailability();
store.displaySortedProducts('price');
store.displaySortedProducts('name');
```
