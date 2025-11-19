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
 * ProductAvailability.js
 * 
 * Displays product availability and sorting options for an online store focused on home goods.
 */

// Define product class
class Product {
    /**
     * @param {string} name - Product name
     * @param {number} price - Product price
     * @param {string} availability - Product availability (In Stock, Out of Stock, Pre-Order)
     */
    constructor(name, price, availability) {
        this.name = name;
        this.price = price;
        this.availability = availability;
    }
}

// Define product availability and sorting options class
class ProductAvailability {
    /**
     * @param {Product[]} products - Array of products
     */
    constructor(products) {
        this.products = products;
    }

    /**
     * Display product availability
     */
    displayAvailability() {
        console.log("Product Availability:");
        this.products.forEach((product, index) => {
            console.log(`${index + 1}. ${product.name} - ${product.availability} - $${product.price}`);
        });
    }

    /**
     * Sort products by price (ascending or descending)
     * @param {string} order - Sorting order (asc, desc)
     */
    sortByPrice(order) {
        if (order !== "asc" && order !== "desc") {
            throw new Error("Invalid sorting order. Please use 'asc' or 'desc'.");
        }

        try {
            this.products.sort((a, b) => {
                if (order === "asc") {
                    return a.price - b.price;
                } else {
                    return b.price - a.price;
                }
            });
            this.displayAvailability();
        } catch (error) {
            console.error("Error sorting products:", error.message);
        }
    }

    /**
     * Sort products by name (ascending or descending)
     * @param {string} order - Sorting order (asc, desc)
     */
    sortByName(order) {
        if (order !== "asc" && order !== "desc") {
            throw new Error("Invalid sorting order. Please use 'asc' or 'desc'.");
        }

        try {
            this.products.sort((a, b) => {
                if (order === "asc") {
                    return a.name.localeCompare(b.name);
                } else {
                    return b.name.localeCompare(a.name);
                }
            });
            this.displayAvailability();
        } catch (error) {
            console.error("Error sorting products:", error.message);
        }
    }
}

// Example usage
function main() {
    // Create products
    const product1 = new Product("Chair", 50, "In Stock");
    const product2 = new Product("Table", 100, "Out of Stock");
    const product3 = new Product("Lamp", 20, "Pre-Order");

    // Create product availability and sorting options
    const products = [product1, product2, product3];
    const productAvailability = new ProductAvailability(products);

    // Display initial product availability
    productAvailability.displayAvailability();

    // Sort products by price (ascending)
    console.log("\nSorting by price (ascending):");
    productAvailability.sortByPrice("asc");

    // Sort products by name (descending)
    console.log("\nSorting by name (descending):");
    productAvailability.sortByName("desc");
}

main();
```
