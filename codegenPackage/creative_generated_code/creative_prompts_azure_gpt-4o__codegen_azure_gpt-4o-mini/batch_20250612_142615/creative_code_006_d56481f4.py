"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: Write code to display a "No products found" message dynamically when a course platform has no available products.
Generated: DETERMINISTIC_d56481f4f7ceacea
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ProductList.js
import React from 'react';
import PropTypes from 'prop-types';

// Function to display a list of products
const ProductList = ({ products }) => {
    return (
        <div>
            {products.length === 0 ? (
                // Display message when no products are found
                <h2>No products found</h2>
            ) : (
                // Map through products and display each one
                <ul>
                    {products.map((product) => (
                        <li key={product.id}>{product.name}</li>
                    ))}
                </ul>
            )}
        </div>
    );
};

// PropTypes for validating props
ProductList.propTypes = {
    products: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            name: PropTypes.string.isRequired,
        })
    ).isRequired,
};

export default ProductList;

// Example usage of ProductList component
// App.js
import React from 'react';
import ProductList from './ProductList';

const App = () => {
    // Example products array (can be fetched from an API)
    const products = []; // Empty array simulating no available products

    return (
        <div>
            <h1>Course Products</h1>
            <ProductList products={products} />
        </div>
    );
};

export default App;
```
