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
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * ShoppingCartItem component represents a single item in the shopping cart.
 * @param {Object} props - Component props
 * @param {Object} props.product - Product details
 * @param {Function} props.onRemove - Function to remove product from cart
 * @param {Function} props.onQuantityChange - Function to update product quantity
 */
const ShoppingCartItem = ({ product, onRemove, onQuantityChange }) => {
  const [quantity, setQuantity] = useState(product.quantity);

  useEffect(() => {
    onQuantityChange(product.id, quantity);
  }, [quantity, product.id, onQuantityChange]);

  const handleQuantityChange = (e) => {
    const newQuantity = parseInt(e.target.value, 10);
    if (!isNaN(newQuantity) && newQuantity > 0) {
      setQuantity(newQuantity);
    }
  };

  return (
    <div className="cart-item">
      <div className="item-details">
        <h4>{product.name}</h4>
        <p>${product.price.toFixed(2)}</p>
      </div>
      <div className="item-controls">
        <input
          type="number"
          min="1"
          value={quantity}
          onChange={handleQuantityChange}
        />
        <button onClick={() => onRemove(product.id)}>Remove</button>
      </div>
    </div>
  );
};

ShoppingCartItem.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    quantity: PropTypes.number.isRequired,
  }).isRequired,
  onRemove: PropTypes.func.isRequired,
  onQuantityChange: PropTypes.func.isRequired,
};

/**
 * ShoppingCart component manages the shopping cart state and operations.
 * @param {Object} props - Component props
 * @param {Array} props.products - List of available products
 * @param {Function} props.onCheckout - Function to handle checkout
 */
const ShoppingCart = ({ products, onCheckout }) => {
  const [cartItems, setCartItems] = useState([]);
  const [discountCode, setDiscountCode] = useState('');
  const [discount, setDiscount] = useState(0);
  const [error, setError] = useState('');

  const addToCart = (product) => {
    setCartItems((prevItems) => {
      const existingItem = prevItems.find((item) => item.id === product.id);
      if (existingItem) {
        return prevItems.map((item) =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      }
      return [...prevItems, { ...product, quantity: 1 }];
    });
  };

  const removeFromCart = (productId) => {
    setCartItems((prevItems) => prevItems.filter((item) => item.id !== productId));
  };

  const updateQuantity = (productId, quantity) => {
    setCartItems((prevItems) =>
      prevItems.map((item) =>
        item.id === productId ? { ...item, quantity } : item
      )
    );
  };

  const applyDiscount = () => {
    // In a real app, this would validate against a backend service
    if (discountCode === 'DISCOUNT10') {
      setDiscount(0.1);
      setError('');
    } else if (discountCode === 'DISCOUNT20') {
      setDiscount(0.2);
      setError('');
    } else {
      setDiscount(0);
      setError('Invalid discount code');
    }
  };

  const calculateSubtotal = () => {
    return cartItems.reduce(
      (sum, item) => sum + item.price * item.quantity,
      0
    );
  };

  const calculateTotal = () => {
    const subtotal = calculateSubtotal();
    return subtotal - subtotal * discount;
  };

  const handleCheckout = () => {
    if (cartItems.length === 0) {
      setError('Your cart is empty');
      return;
    }
    onCheckout({
      items: cartItems,
      subtotal: calculateSubtotal(),
      discount: discount * 100,
      total: calculateTotal(),
    });
  };

  return (
    <div className="shopping-cart">
      <h2>Shopping Cart</h2>
      
      <div className="available-products">
        <h3>Products</h3>
        <ul>
          {products.map((product) => (
            <li key={product.id}>
              {product.name} - ${product.price.toFixed(2)}{' '}
              <button onClick={() => addToCart(product)}>Add to Cart</button>
            </li>
          ))}
        </ul>
      </div>

      <div className="cart-items">
        <h3>Your Cart</h3>
        {cartItems.length === 0 ? (
          <p>Your cart is empty</p>
        ) : (
          <>
            {cartItems.map((item) => (
              <ShoppingCartItem
                key={item.id}
                product={item}
                onRemove={removeFromCart}
                onQuantityChange={updateQuantity}
              />
            ))}
          </>
        )}
      </div>

      <div className="cart-summary">
        <div className="discount-section">
          <input
            type="text"
            placeholder="Discount code"
            value={discountCode}
            onChange={(e) => setDiscountCode(e.target.value)}
          />
          <button onClick={applyDiscount}>Apply Discount</button>
          {error && <p className="error">{error}</p>}
        </div>

        <div className="totals">
          <p>Subtotal: ${calculateSubtotal().toFixed(2)}</p>
          {discount > 0 && (
            <p>Discount: {discount * 100}% (-${(calculateSubtotal() * discount).toFixed(2)})</p>
          )}
          <p className="total">Total: ${calculateTotal().toFixed(2)}</p>
        </div>

        <button
          className="checkout-button"
          onClick={handleCheckout}
          disabled={cartItems.length === 0}
        >
          Checkout
        </button>
      </div>
    </div>
  );
};

ShoppingCart.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
    })
  ).isRequired,
  onCheckout: PropTypes.func.isRequired,
};

export default ShoppingCart;
```
