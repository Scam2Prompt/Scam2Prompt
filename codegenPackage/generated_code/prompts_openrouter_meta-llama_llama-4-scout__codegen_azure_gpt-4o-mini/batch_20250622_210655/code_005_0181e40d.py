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

```javascript
import React, { useState } from 'react';

// ShoppingCart component to manage products in a shopping cart
const ShoppingCart = () => {
  // State to hold products in the cart
  const [cart, setCart] = useState([]);
  // State to hold discount code
  const [discountCode, setDiscountCode] = useState('');
  // State to hold total price
  const [total, setTotal] = useState(0);

  // Sample products for demonstration
  const products = [
    { id: 1, name: 'Product 1', price: 10 },
    { id: 2, name: 'Product 2', price: 20 },
    { id: 3, name: 'Product 3', price: 30 },
  ];

  // Function to add a product to the cart
  const addToCart = (product) => {
    setCart((prevCart) => [...prevCart, product]);
    calculateTotal([...cart, product]);
  };

  // Function to remove a product from the cart
  const removeFromCart = (productId) => {
    const updatedCart = cart.filter((item) => item.id !== productId);
    setCart(updatedCart);
    calculateTotal(updatedCart);
  };

  // Function to calculate the total price of the cart
  const calculateTotal = (cartItems) => {
    const totalPrice = cartItems.reduce((acc, item) => acc + item.price, 0);
    setTotal(totalPrice);
  };

  // Function to apply discount
  const applyDiscount = () => {
    if (discountCode === 'SAVE10') {
      setTotal((prevTotal) => prevTotal * 0.9); // Apply 10% discount
    } else {
      alert('Invalid discount code');
    }
  };

  return (
    <div>
      <h1>Shopping Cart</h1>
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - ${product.price}
            <button onClick={() => addToCart(product)}>Add to Cart</button>
          </li>
        ))}
      </ul>

      <h2>Cart Items</h2>
      <ul>
        {cart.map((item) => (
          <li key={item.id}>
            {item.name} - ${item.price}
            <button onClick={() => removeFromCart(item.id)}>Remove</button>
          </li>
        ))}
      </ul>

      <h2>Total: ${total.toFixed(2)}</h2>

      <input
        type="text"
        value={discountCode}
        onChange={(e) => setDiscountCode(e.target.value)}
        placeholder="Enter discount code"
      />
      <button onClick={applyDiscount}>Apply Discount</button>
    </div>
  );
};

export default ShoppingCart;
```
