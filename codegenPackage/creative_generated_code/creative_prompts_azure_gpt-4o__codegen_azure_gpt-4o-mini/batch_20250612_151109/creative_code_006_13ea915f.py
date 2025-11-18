"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Write a React component to display a furniture product catalog, including items like "Bicama Siena" and "Estofado Desejos 3x2 lugares," with options to sort by price and category.
Generated: DETERMINISTIC_13ea915fb60e76a4
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';

// Sample data for furniture products
const initialProducts = [
    { id: 1, name: 'Bicama Siena', category: 'Beds', price: 500 },
    { id: 2, name: 'Estofado Desejos 3x2 lugares', category: 'Sofas', price: 1200 },
    { id: 3, name: 'Mesa de Jantar', category: 'Tables', price: 800 },
    { id: 4, name: 'Cadeira Elegante', category: 'Chairs', price: 250 },
    { id: 5, name: 'Armário Moderno', category: 'Cabinets', price: 1500 },
];

// Functional component for the product catalog
const ProductCatalog = () => {
    // State to hold products and sorting options
    const [products, setProducts] = useState(initialProducts);
    const [sortOption, setSortOption] = useState('name');

    // Function to handle sorting of products
    const handleSortChange = (event) => {
        const { value } = event.target;
        setSortOption(value);

        const sortedProducts = [...products].sort((a, b) => {
            if (value === 'price') {
                return a.price - b.price; // Sort by price
            } else {
                return a.name.localeCompare(b.name); // Sort by name
            }
        });

        setProducts(sortedProducts);
    };

    // Render the product catalog
    return (
        <div>
            <h1>Furniture Product Catalog</h1>
            <label htmlFor="sort">Sort by: </label>
            <select id="sort" value={sortOption} onChange={handleSortChange}>
                <option value="name">Name</option>
                <option value="price">Price</option>
            </select>
            <ul>
                {products.map((product) => (
                    <li key={product.id}>
                        <strong>{product.name}</strong> - {product.category} (${product.price})
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProductCatalog;
```
