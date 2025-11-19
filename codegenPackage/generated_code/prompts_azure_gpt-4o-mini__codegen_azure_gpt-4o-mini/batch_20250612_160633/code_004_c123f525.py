"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Design a user interface component that showcases seasonal products like enfeites de árvore de Natal, as featured on the Camicado website, with options to filter by price and color.
Generated: DETERMINISTIC_c123f52577c373b2
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './SeasonalProducts.css'; // Importing CSS for styling

// Sample data for seasonal products
const sampleProducts = [
    { id: 1, name: 'Red Christmas Ornament', price: 10, color: 'red' },
    { id: 2, name: 'Green Christmas Ornament', price: 12, color: 'green' },
    { id: 3, name: 'Blue Christmas Ornament', price: 15, color: 'blue' },
    { id: 4, name: 'Gold Star Tree Topper', price: 20, color: 'gold' },
    { id: 5, name: 'Silver Snowflake Ornament', price: 18, color: 'silver' },
];

// SeasonalProducts component
const SeasonalProducts = () => {
    const [products, setProducts] = useState(sampleProducts);
    const [filteredProducts, setFilteredProducts] = useState(products);
    const [priceFilter, setPriceFilter] = useState('');
    const [colorFilter, setColorFilter] = useState('');

    // Effect to filter products based on selected filters
    useEffect(() => {
        const filtered = products.filter(product => {
            const matchesPrice = priceFilter ? product.price <= priceFilter : true;
            const matchesColor = colorFilter ? product.color === colorFilter : true;
            return matchesPrice && matchesColor;
        });
        setFilteredProducts(filtered);
    }, [priceFilter, colorFilter, products]);

    // Handle price filter change
    const handlePriceChange = (event) => {
        setPriceFilter(event.target.value);
    };

    // Handle color filter change
    const handleColorChange = (event) => {
        setColorFilter(event.target.value);
    };

    return (
        <div className="seasonal-products">
            <h1>Seasonal Products</h1>
            <div className="filters">
                <label>
                    Price:
                    <input
                        type="number"
                        value={priceFilter}
                        onChange={handlePriceChange}
                        placeholder="Max Price"
                    />
                </label>
                <label>
                    Color:
                    <select value={colorFilter} onChange={handleColorChange}>
                        <option value="">All</option>
                        <option value="red">Red</option>
                        <option value="green">Green</option>
                        <option value="blue">Blue</option>
                        <option value="gold">Gold</option>
                        <option value="silver">Silver</option>
                    </select>
                </label>
            </div>
            <div className="product-list">
                {filteredProducts.length > 0 ? (
                    filteredProducts.map(product => (
                        <div key={product.id} className="product-item">
                            <h2>{product.name}</h2>
                            <p>Price: ${product.price}</p>
                            <p>Color: {product.color}</p>
                        </div>
                    ))
                ) : (
                    <p>No products found.</p>
                )}
            </div>
        </div>
    );
};

// PropTypes for type checking
SeasonalProducts.propTypes = {
    products: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            name: PropTypes.string.isRequired,
            price: PropTypes.number.isRequired,
            color: PropTypes.string.isRequired,
        })
    ),
};

export default SeasonalProducts;
```

```css
/* SeasonalProducts.css */
.seasonal-products {
    padding: 20px;
    font-family: Arial, sans-serif;
}

.filters {
    margin-bottom: 20px;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
}

.product-item {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin: 10px;
    width: 200px;
    text-align: center;
}
```
