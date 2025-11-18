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

```python
# Flask-based backend code for filtering and sorting products in a web application
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Product A", "price": 30.0, "category": "Electronics"},
    {"id": 2, "name": "Product B", "price": 20.0, "category": "Books"},
    {"id": 3, "name": "Product C", "price": 50.0, "category": "Electronics"},
    {"id": 4, "name": "Product D", "price": 15.0, "category": "Books"},
]


@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to get filtered and sorted products.
    Query Params:
    - filter_by_category: Filter products by category (e.g., 'Electronics').
    - sort_by: Sort products by a key (e.g., 'price', 'name').
    - order: Sort order ('asc' for ascending, 'desc' for descending).
    """
    try:
        # Get query params
        filter_by_category = request.args.get('filter_by_category')
        sort_by = request.args.get('sort_by', 'id')  # Default sorting by 'id'
        order = request.args.get('order', 'asc')  # Default sorting order is ascending

        # Start with all products
        filtered_products = products

        # Apply category filter if provided
        if filter_by_category:
            filtered_products = [
                product for product in filtered_products
                if product['category'].lower() == filter_by_category.lower()
            ]

        # Perform sorting if 'sort_by' is a valid key
        if sort_by in products[0]:
            reverse = order.lower() == 'desc'
            filtered_products = sorted(filtered_products, key=lambda p: p[sort_by], reverse=reverse)

        # Return the filtered and sorted products
        return jsonify({"success": True, "data": filtered_products}), 200

    except Exception as e:
        # Return error response in case of an exception
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

```javascript
// React-based frontend component for filtering and sorting products
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [category, setCategory] = useState('');
  const [sortBy, setSortBy] = useState('id');
  const [order, setOrder] = useState('asc');
  const [error, setError] = useState(null);

  // Fetch products from the backend
  const fetchProducts = async () => {
    try {
      const response = await axios.get('/products', {
        params: {
          filter_by_category: category,
          sort_by: sortBy,
          order: order,
        },
      });
      setProducts(response.data.data);
    } catch (err) {
      setError(err.message);
    }
  };

  // Fetch products on component mount and whenever filters/sorting change
  useEffect(() => {
    fetchProducts();
  }, [category, sortBy, order]);

  return (
    <div>
      <h1>Product List</h1>

      {/* Error display */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Filtering options */}
      <div>
        <label>
          Filter by Category:
          <select value={category} onChange={(e) => setCategory(e.target.value)}>
            <option value="">All</option>
            <option value="Electronics">Electronics</option>
            <option value="Books">Books</option>
          </select>
        </label>
      </div>

      {/* Sorting options */}
      <div>
        <label>
          Sort by:
          <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
            <option value="id">ID</option>
            <option value="price">Price</option>
            <option value="name">Name</option>
          </select>
        </label>
        <label>
          Order:
          <select value={order} onChange={(e) => setOrder(e.target.value)}>
            <option value="asc">Ascending</option>
            <option value="desc">Descending</option>
          </select>
        </label>
      </div>

      {/* Product list display */}
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - ${product.price} ({product.category})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
```
