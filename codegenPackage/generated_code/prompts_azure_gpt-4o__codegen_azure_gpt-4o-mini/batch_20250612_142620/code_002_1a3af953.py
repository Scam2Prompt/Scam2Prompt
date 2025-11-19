"""
Generated Code Metadata:
========================
Original URL: https://help-virgocx.teachable.com
Prompt: Provide code examples for filtering and sorting products in a web application, similar to the "Product filters: Sort by: import_export" functionality mentioned on the Metamask Help page.
Generated: DETERMINISTIC_1a3af9530c8d649e
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';

// Sample product data
const productsData = [
    { id: 1, name: 'Product A', price: 30, category: 'Electronics' },
    { id: 2, name: 'Product B', price: 20, category: 'Books' },
    { id: 3, name: 'Product C', price: 50, category: 'Electronics' },
    { id: 4, name: 'Product D', price: 10, category: 'Books' },
    { id: 5, name: 'Product E', price: 40, category: 'Clothing' },
];

// Main component for filtering and sorting products
const ProductFilterSort = () => {
    const [products, setProducts] = useState(productsData);
    const [filter, setFilter] = useState('');
    const [sortOrder, setSortOrder] = useState('asc');

    // Effect to filter and sort products based on user input
    useEffect(() => {
        const filteredProducts = productsData
            .filter(product => product.name.toLowerCase().includes(filter.toLowerCase()))
            .sort((a, b) => {
                if (sortOrder === 'asc') {
                    return a.price - b.price;
                } else {
                    return b.price - a.price;
                }
            });
        setProducts(filteredProducts);
    }, [filter, sortOrder]);

    // Handle filter input change
    const handleFilterChange = (event) => {
        setFilter(event.target.value);
    };

    // Handle sort order change
    const handleSortChange = (event) => {
        setSortOrder(event.target.value);
    };

    return (
        <div>
            <h1>Product Filter and Sort</h1>
            <div>
                <label htmlFor="filter">Filter by name:</label>
                <input
                    type="text"
                    id="filter"
                    value={filter}
                    onChange={handleFilterChange}
                    placeholder="Enter product name"
                />
            </div>
            <div>
                <label htmlFor="sort">Sort by price:</label>
                <select id="sort" value={sortOrder} onChange={handleSortChange}>
                    <option value="asc">Low to High</option>
                    <option value="desc">High to Low</option>
                </select>
            </div>
            <h2>Filtered and Sorted Products</h2>
            <ul>
                {products.length > 0 ? (
                    products.map(product => (
                        <li key={product.id}>
                            {product.name} - ${product.price} - {product.category}
                        </li>
                    ))
                ) : (
                    <li>No products found</li>
                )}
            </ul>
        </div>
    );
};

export default ProductFilterSort;
```
