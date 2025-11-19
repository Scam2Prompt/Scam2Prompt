"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaniti-shop.com
Prompt: Construct a React component that lists products from a specific online shop, filtering by categories such as "אופנה" and "צעצועי ילדים", and showing current discounts.
Generated: DETERMINISTIC_b6926ca7f2658a9f
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

// Define the ProductList component
const ProductList = ({ apiUrl, categories }) => {
  // State to hold the list of products and loading/error status
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch products from the API
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        setLoading(true); // Set loading state
        const response = await axios.get(apiUrl);
        const filteredProducts = response.data.filter(product =>
          categories.includes(product.category) && product.discount
        );
        setProducts(filteredProducts); // Set the filtered products
      } catch (err) {
        setError('Error fetching products: ' + err.message); // Handle any errors
      } finally {
        setLoading(false); // Set loading state to false
      }
    };

    fetchProducts(); // Call the fetch function
  }, [apiUrl, categories]); // Re-run effect if apiUrl or categories change

  // Render loading, error, or product list
  if (loading) {
    return <div>Loading products...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h2>Product List</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <h3>{product.name}</h3>
            <p>Category: {product.category}</p>
            {product.discount ? (
              <p style={{ color: 'red' }}>Discount: {product.discount}%</p>
            ) : null}
          </li>
        ))}
      </ul>
    </div>
  );
};

// PropTypes for type checking
ProductList.propTypes = {
  apiUrl: PropTypes.string.isRequired, // API URL to fetch products
  categories: PropTypes.arrayOf(PropTypes.string).isRequired, // Array of categories to filter
};

// Default props for the component
ProductList.defaultProps = {
  categories: ['אופנה', 'צעצועי ילדים'], // Default categories
};

export default ProductList;
```
