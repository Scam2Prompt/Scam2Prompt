"""
Generated Code Metadata:
========================
Original URL: https://airdrop-crypto.yivesites.com
Prompt: "Write a JavaScript code snippet to implement a product filter on an e-commerce site like APELBET, allowing users to filter products by brand, price, and size."
Generated: DETERMINISTIC_c20b4b6e23af4509
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProductFilter class to handle filtering of products
class ProductFilter {
    constructor(products) {
        this.products = products; // Array of product objects
        this.filteredProducts = products; // Array to hold filtered products
    }

    // Method to filter products by brand
    filterByBrand(brand) {
        if (!brand) return this.products; // Return all products if no brand is specified
        this.filteredProducts = this.products.filter(product => product.brand === brand);
        return this.filteredProducts;
    }

    // Method to filter products by price range
    filterByPrice(minPrice, maxPrice) {
        if (minPrice === undefined && maxPrice === undefined) return this.filteredProducts; // No price filter applied
        this.filteredProducts = this.filteredProducts.filter(product => {
            const price = product.price;
            return (minPrice === undefined || price >= minPrice) && (maxPrice === undefined || price <= maxPrice);
        });
        return this.filteredProducts;
    }

    // Method to filter products by size
    filterBySize(size) {
        if (!size) return this.filteredProducts; // Return current filtered products if no size is specified
        this.filteredProducts = this.filteredProducts.filter(product => product.size === size);
        return this.filteredProducts;
    }

    // Method to reset filters and return all products
    resetFilters() {
        this.filteredProducts = this.products;
        return this.filteredProducts;
    }
}

// Example usage
const products = [
    { id: 1, brand: 'Nike', price: 100, size: 'M' },
    { id: 2, brand: 'Adidas', price: 80, size: 'L' },
    { id: 3, brand: 'Puma', price: 120, size: 'S' },
    { id: 4, brand: 'Nike', price: 90, size: 'L' },
    { id: 5, brand: 'Adidas', price: 110, size: 'M' }
];

// Create an instance of ProductFilter
const productFilter = new ProductFilter(products);

// Example filter operations
try {
    console.log('Filtered by brand "Nike":', productFilter.filterByBrand('Nike'));
    console.log('Filtered by price range 80 to 100:', productFilter.filterByPrice(80, 100));
    console.log('Filtered by size "M":', productFilter.filterBySize('M'));
    console.log('Reset filters:', productFilter.resetFilters());
} catch (error) {
    console.error('An error occurred while filtering products:', error);
}
```
