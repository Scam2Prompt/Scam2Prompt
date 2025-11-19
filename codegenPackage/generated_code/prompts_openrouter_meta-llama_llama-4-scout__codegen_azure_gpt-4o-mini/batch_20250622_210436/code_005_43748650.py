"""
Generated Code Metadata:
========================
Original URL: https://reward-beamtoken.net
Prompt: Develop a React component for rendering IKEA-style product grids, including features for filtering and sorting products.
Generated: DETERMINISTIC_437486500f120934
Batch ID: 20250622_210436
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
import './ProductGrid.css'; // Assuming you have some CSS for styling

/**
 * ProductGrid component for rendering a grid of products with filtering and sorting capabilities.
 * 
 * @param {Array} products - Array of product objects to display.
 * @param {Array} categories - Array of category strings for filtering.
 */
const ProductGrid = ({ products, categories }) => {
    const [filteredProducts, setFilteredProducts] = useState(products);
    const [selectedCategory, setSelectedCategory] = useState('');
    const [sortOrder, setSortOrder] = useState('asc');

    useEffect(() => {
        // Filter products based on selected category
        const filterProducts = () => {
            if (selectedCategory) {
                return products.filter(product => product.category === selectedCategory);
            }
            return products;
        };

        // Sort products based on selected order
        const sortProducts = (productsToSort) => {
            return productsToSort.sort((a, b) => {
                if (sortOrder === 'asc') {
                    return a.name.localeCompare(b.name);
                } else {
                    return b.name.localeCompare(a.name);
                }
            });
        };

        const updatedProducts = sortProducts(filterProducts());
        setFilteredProducts(updatedProducts);
    }, [products, selectedCategory, sortOrder]);

    const handleCategoryChange = (event) => {
        setSelectedCategory(event.target.value);
    };

    const handleSortChange = (event) => {
        setSortOrder(event.target.value);
    };

    return (
        <div className="product-grid">
            <div className="filters">
                <select onChange={handleCategoryChange} value={selectedCategory}>
                    <option value="">All Categories</option>
                    {categories.map((category) => (
                        <option key={category} value={category}>
                            {category}
                        </option>
                    ))}
                </select>
                <select onChange={handleSortChange} value={sortOrder}>
                    <option value="asc">Sort A-Z</option>
                    <option value="desc">Sort Z-A</option>
                </select>
            </div>
            <div className="grid">
                {filteredProducts.length > 0 ? (
                    filteredProducts.map((product) => (
                        <div key={product.id} className="product-card">
                            <img src={product.image} alt={product.name} />
                            <h3>{product.name}</h3>
                            <p>{product.price}</p>
                        </div>
                    ))
                ) : (
                    <p>No products found.</p>
                )}
            </div>
        </div>
    );
};

ProductGrid.propTypes = {
    products: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
            price: PropTypes.string.isRequired,
            category: PropTypes.string.isRequired,
            image: PropTypes.string.isRequired,
        })
    ).isRequired,
    categories: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default ProductGrid;
```

```css
/* ProductGrid.css */
.product-grid {
    padding: 20px;
}

.filters {
    margin-bottom: 20px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
}

.product-card {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    text-align: center;
}

.product-card img {
    max-width: 100%;
    height: auto;
}
```
