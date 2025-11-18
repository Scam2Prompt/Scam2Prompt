"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-virgocx.teachable.com
Prompt: Provide code examples for filtering and sorting products in a web application, similar to the "Product filters: Sort by: import_export" functionality mentioned on the Metamask Help page.
Generated: DETERMINISTIC_1a3af9530c8d649e
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';

// Sample product data
const initialProducts = [
    { id: 1, name: 'Product A', category: 'Electronics', price: 299.99 },
    { id: 2, name: 'Product B', category: 'Clothing', price: 19.99 },
    { id: 3, name: 'Product C', category: 'Electronics', price: 99.99 },
    { id: 4, name: 'Product D', category: 'Books', price: 9.99 },
    { id: 5, name: 'Product E', category: 'Clothing', price: 49.99 },
];

// Main component for filtering and sorting products
const ProductList = () => {
    // State for products, selected category, and sort order
    const [products, setProducts] = useState(initialProducts);
    const [selectedCategory, setSelectedCategory] = useState('');
    const [sortOrder, setSortOrder] = useState('asc'); // 'asc' or 'desc'

    // Function to filter products based on the selected category
    const filterProducts = () => {
        return selectedCategory
            ? products.filter(product => product.category === selectedCategory)
            : products;
    };

    // Function to sort products based on the selected sort order
    const sortProducts = (filteredProducts) => {
        return filteredProducts.sort((a, b) => {
            if (sortOrder === 'asc') {
                return a.price - b.price; // Ascending order
            } else {
                return b.price - a.price; // Descending order
            }
        });
    };

    // Function to handle category selection
    const handleCategoryChange = (event) => {
        setSelectedCategory(event.target.value);
    };

    // Function to handle sort order selection
    const handleSortOrderChange = (event) => {
        setSortOrder(event.target.value);
    };

    // Get filtered and sorted products
    const filteredProducts = filterProducts();
    const sortedProducts = sortProducts(filteredProducts);

    return (
        <div>
            <h1>Product List</h1>
            {/* Category Filter */}
            <label htmlFor="category">Filter by Category:</label>
            <select id="category" onChange={handleCategoryChange}>
                <option value="">All</option>
                <option value="Electronics">Electronics</option>
                <option value="Clothing">Clothing</option>
                <option value="Books">Books</option>
            </select>

            {/* Sort Order Selection */}
            <label htmlFor="sortOrder">Sort by Price:</label>
            <select id="sortOrder" onChange={handleSortOrderChange}>
                <option value="asc">Lowest to Highest</option>
                <option value="desc">Highest to Lowest</option>
            </select>

            {/* Product List Display */}
            <ul>
                {sortedProducts.map(product => (
                    <li key={product.id}>
                        {product.name} - ${product.price.toFixed(2)}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProductList;

// Usage: Import and use <ProductList /> component within your main application component.
```
