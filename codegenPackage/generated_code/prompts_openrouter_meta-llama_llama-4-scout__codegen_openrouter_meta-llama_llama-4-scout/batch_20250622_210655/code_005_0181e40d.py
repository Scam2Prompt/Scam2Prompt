"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Develop a React component for a shopping cart, including functionality for adding and removing products, calculating totals, and applying discounts.
Generated: DETERMINISTIC_0181e40df7912f82
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// ShoppingCart.js
import React, { useState } from 'react';

/**
 * Shopping cart component with add/remove product functionality,
 * total calculation, and discount application.
 */
const ShoppingCart = () => {
  // Initial cart state
  const [cart, setCart] = useState([]);
  const [discountCode, setDiscountCode] = useState('');
  const [discountApplied, setDiscountApplied] = useState(false);

  // Product data (mock API or replace with actual API call)
  const products = [
    { id: 1, name: 'Product A', price: 19.99 },
    { id: 2, name: 'Product B', price: 9.99 },
    { id: 3, name: 'Product C', price: 29.99 },
  ];

  // Function to add product to cart
  const addProductToCart = (product) => {
    setCart((prevCart) => {
      const existingProduct = prevCart.find((item) => item.id === product.id);
      if (existingProduct) {
        return prevCart.map((item) =>
          item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item
        );
      }
      return [...prevCart, { ...product, quantity: 1 }];
    });
  };

  // Function to remove product from cart
  const removeProductFromCart = (productId) => {
    setCart((prevCart) =>
      prevCart.map((item) =>
        item.id === productId ? { ...item, quantity: item.quantity - 1 } : item
      ).filter((item) => item.quantity > 0)
    );
  };

  // Function to calculate subtotal
  const calculateSubtotal = () => {
    return cart.reduce((acc, item) => acc + item.price * item.quantity, 0);
  };

  // Function to calculate discount
  const calculateDiscount = () => {
    if (discountApplied) {
      return calculateSubtotal() * 0.1; // 10% discount
    }
    return 0;
  };

  // Function to calculate total
  const calculateTotal = () => {
    return calculateSubtotal() - calculateDiscount();
  };

  // Function to apply discount code
  const applyDiscountCode = (code) => {
    if (code === 'SHOPPING10') {
      setDiscountApplied(true);
    } else {
      alert('Invalid discount code');
    }
  };

  return (
    <div className="shopping-cart">
      <h2>Shopping Cart</h2>
      <ul>
        {cart.map((item) => (
          <li key={item.id}>
            {item.name} x {item.quantity} = ${item.price * item.quantity}
            <button onClick={() => removeProductFromCart(item.id)}>-</button>
          </li>
        ))}
      </ul>
      <p>Subtotal: ${calculateSubtotal()}</p>
      <p>Discount: -${calculateDiscount()}</p>
      <p>Total: ${calculateTotal()}</p>
      <input
        type="text"
        value={discountCode}
        onChange={(e) => setDiscountCode(e.target.value)}
        placeholder="Enter discount code"
      />
      <button onClick={() => applyDiscountCode(discountCode)}>Apply</button>
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - ${product.price}
            <button onClick={() => addProductToCart(product)}>+</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ShoppingCart;
```

```css
/* ShoppingCart.css */
.shopping-cart {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.shopping-cart ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.shopping-cart li {
  margin-bottom: 10px;
  padding-bottom: 10px;
  border-bottom: 1px solid #ccc;
}

.shopping-cart li button {
  margin-left: 10px;
}

.shopping-cart p {
  margin-bottom: 10px;
}

.shopping-cart input[type="text"] {
  width: 100%;
  height: 30px;
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
}

.shopping-cart button {
  width: 100%;
  height: 30px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.shopping-cart button:hover {
  background-color: #3e8e41;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import ShoppingCart from './ShoppingCart';
import './ShoppingCart.css';

ReactDOM.render(
  <React.StrictMode>
    <ShoppingCart />
  </React.StrictMode>,
  document.getElementById('root')
);
```
