"""
Generated Code Metadata:
========================
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Write code to display a "No products found" message dynamically when an online course platform has no available products, similar to the rabbie-wall--extension-docs site.
Generated: DETERMINISTIC_816b6b229d662de0
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// NoProductsMessage.js
import React from 'react';

/**
 * Displays a "No products found" message when no products are available.
 *
 * @param {Object} props
 * @param {Boolean} props.hasProducts - Whether products are available.
 */
function NoProductsMessage({ hasProducts }) {
  if (hasProducts) {
    return null; // Render nothing if products are available
  }

  return (
    <div className="no-products-message">
      <p>No products found.</p>
    </div>
  );
}

export default NoProductsMessage;
```

```javascript
// ProductList.js
import React, { useState, useEffect } from 'react';
import NoProductsMessage from './NoProductsMessage';

/**
 * Fetches and displays a list of products.
 */
function ProductList() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('/api/products');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      {products.length === 0 ? (
        <NoProductsMessage hasProducts={false} />
      ) : (
        <ul>
          {products.map((product) => (
            <li key={product.id}>{product.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProductList;
```

```css
/* styles.css */
.no-products-message {
  text-align: center;
  padding: 20px;
}

.no-products-message p {
  font-size: 18px;
  color: #666;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import ProductList from './ProductList';

ReactDOM.render(
  <React.StrictMode>
    <ProductList />
  </React.StrictMode>,
  document.getElementById('root')
);
```
