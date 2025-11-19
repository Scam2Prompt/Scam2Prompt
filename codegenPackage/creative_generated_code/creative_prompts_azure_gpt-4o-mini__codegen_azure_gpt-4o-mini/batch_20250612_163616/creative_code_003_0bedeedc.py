"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Develop a JavaScript code to filter and display electronic products like monitors and printers based on user preferences, utilizing the structure seen on mixpelinfobrazz.
Generated: DETERMINISTIC_0bedeedcdb652659
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a class to represent an electronic product
class Product {
    constructor(name, type, brand, price) {
        this.name = name; // Name of the product
        this.type = type; // Type of the product (e.g., 'monitor', 'printer')
        this.brand = brand; // Brand of the product
        this.price = price; // Price of the product
    }
}

// Sample data: an array of electronic products
const products = [
    new Product('Ultra HD Monitor', 'monitor', 'BrandA', 299.99),
    new Product('Gaming Monitor', 'monitor', 'BrandB', 499.99),
    new Product('Laser Printer', 'printer', 'BrandC', 199.99),
    new Product('Inkjet Printer', 'printer', 'BrandD', 99.99),
    new Product('4K Monitor', 'monitor', 'BrandE', 399.99),
    new Product('Photo Printer', 'printer', 'BrandF', 159.99)
];

// Function to filter products based on user preferences
function filterProducts(preference) {
    try {
        // Check if preference is provided
        if (!preference || typeof preference !== 'object') {
            throw new Error('Invalid preference object. Please provide a valid filter.');
        }

        const { type, maxPrice } = preference;

        // Filter products based on type and max price
        const filteredProducts = products.filter(product => {
            const matchesType = type ? product.type === type : true;
            const matchesPrice = maxPrice ? product.price <= maxPrice : true;
            return matchesType && matchesPrice;
        });

        // Return filtered results
        return filteredProducts;
        
    } catch (error) {
        console.error(`Error filtering products: ${error.message}`);
        return []; // Return an empty array in case of error
    }
}

// Function to display filtered products
function displayProducts(filteredProducts) {
    if (filteredProducts.length === 0) {
        console.log('No products found matching the criteria.');
        return;
    }
    
    console.log('Filtered Products:');
    filteredProducts.forEach(product => {
        console.log(`- ${product.name} (${product.brand}): $${product.price.toFixed(2)}`);
    });
}

// User preferences for filtering
const userPreferences = {
    type: 'monitor', // User wishes to filter monitors
    maxPrice: 400 // User wants monitors that cost no more than $400
};

// Filtering and displaying products based on user preferences
const filteredProducts = filterProducts(userPreferences);
displayProducts(filteredProducts);
```
