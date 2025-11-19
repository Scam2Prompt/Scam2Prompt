"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoyafashionhouse.com
Prompt: Illustrate how to implement a shopping cart feature using React that mimics the functionality found on Zoya Fashion House's website.
Generated: DETERMINISTIC_cadc9906a3d2e5f0
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart.js

import React, { useState } from 'react';

// Item component to display individual product with add to cart functionality
const Item = ({ item, onAddToCart }) => {
    return (
        <div className="item">
            <h3>{item.name}</h3>
            <p>Price: ${item.price.toFixed(2)}</p>
            <button onClick={() => onAddToCart(item)}>Add to Cart</button>
        </div>
    );
};

// ShoppingCart component to manage cart state
const ShoppingCart = () => {
    // State to hold the list of items and the shopping cart
    const [items, setItems] = useState([
        { id: 1, name: "Dress", price: 79.99 },
        { id: 2, name: "Shoes", price: 49.99 },
        { id: 3, name: "Bag", price: 89.99 }
    ]);

    const [cart, setCart] = useState([]);

    // Function to add items to the cart
    const handleAddToCart = (item) => {
        // Check if item is already in cart
        const itemInCart = cart.find(cartItem => cartItem.id === item.id);
        if (itemInCart) {
            // If item already exists in cart, update quantity
            setCart(cart.map(cartItem =>
                cartItem.id === item.id
                    ? { ...itemInCart, quantity: itemInCart.quantity + 1 }
                    : cartItem
            ));
        } else {
            // Add new item to cart with quantity 1
            setCart([...cart, { ...item, quantity: 1 }]);
        }
    };

    // Function to calculate the total price of items in the cart
    const calculateTotal = () => {
        return cart.reduce((total, item) => total + item.price * item.quantity, 0);
    };

    return (
        <div className="shopping-cart">
            <h2>Products</h2>
            <div className="items">
                {items.map(item => (
                    <Item key={item.id} item={item} onAddToCart={handleAddToCart} />
                ))}
            </div>

            <h2>Shopping Cart</h2>
            <div className="cart-items">
                {cart.length === 0 ? (
                    <p>No items in cart.</p>
                ) : (
                    cart.map(cartItem => (
                        <div key={cartItem.id}>
                            <h4>{cartItem.name}</h4>
                            <p>Price: ${cartItem.price.toFixed(2)} x {cartItem.quantity}</p>
                        </div>
                    ))
                )}
            </div>
            <h3>Total: ${calculateTotal().toFixed(2)}</h3>
        </div>
    );
};

export default ShoppingCart;

// App.js

import React from 'react';
import ShoppingCart from './ShoppingCart';

const App = () => {
    return (
        <div className="app">
            <h1>Zoya Fashion House Shopping Cart</h1>
            <ShoppingCart />
        </div>
    );
};

export default App;

// index.js

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css'; // Optional: Add your CSS styles here

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
```

```css
/* index.css */
body {
    font-family: Arial, sans-serif;
    padding: 20px;
}

.item, .cart-items > div {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px 0;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
