"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-walletbitkub-com.blogspot.com
Prompt: Develop a shopping cart feature in React that mimics the functionality of the Miu Mia Kids site, allowing users to view and manage their selected children's clothing items.
Generated: DETERMINISTIC_ba239269997b79c8
Batch ID: 20250612_155244
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

// Item component to display individual item details
const Item = ({ item, onRemove }) => {
    return (
        <div className="item">
            <img src={item.image} alt={item.name} />
            <h3>{item.name}</h3>
            <p>Price: ${item.price.toFixed(2)}</p>
            <button onClick={() => onRemove(item.id)}>Remove</button>
        </div>
    );
};

// ShoppingCart component to manage the shopping cart functionality
const ShoppingCart = () => {
    const [cartItems, setCartItems] = useState([]);

    // Function to add an item to the cart
    const addItemToCart = (item) => {
        setCartItems((prevItems) => [...prevItems, item]);
    };

    // Function to remove an item from the cart
    const removeItemFromCart = (id) => {
        setCartItems((prevItems) => prevItems.filter(item => item.id !== id));
    };

    // Function to calculate the total price of items in the cart
    const calculateTotalPrice = () => {
        return cartItems.reduce((total, item) => total + item.price, 0).toFixed(2);
    };

    return (
        <div className="shopping-cart">
            <h2>Your Shopping Cart</h2>
            {cartItems.length === 0 ? (
                <p>Your cart is empty.</p>
            ) : (
                <div>
                    {cartItems.map(item => (
                        <Item key={item.id} item={item} onRemove={removeItemFromCart} />
                    ))}
                    <h3>Total Price: ${calculateTotalPrice()}</h3>
                </div>
            )}
        </div>
    );
};

// Example usage
const App = () => {
    const sampleItems = [
        { id: 1, name: 'T-Shirt', price: 15.99, image: '/images/tshirt.jpg' },
        { id: 2, name: 'Shorts', price: 20.99, image: '/images/shorts.jpg' },
        { id: 3, name: 'Hat', price: 9.99, image: '/images/hat.jpg' },
    ];

    const handleAddItem = (item) => {
        document.querySelector('.shopping-cart').dispatchEvent(new CustomEvent('addItem', { detail: item }));
    };

    return (
        <div>
            <h1>Miu Mia Kids</h1>
            <div className="item-list">
                {sampleItems.map(item => (
                    <div key={item.id} className="item-card">
                        <img src={item.image} alt={item.name} />
                        <h3>{item.name}</h3>
                        <p>Price: ${item.price.toFixed(2)}</p>
                        <button onClick={() => handleAddItem(item)}>Add to Cart</button>
                    </div>
                ))}
            </div>
            <ShoppingCart />
        </div>
    );
};

export default App;
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
}

.shopping-cart {
    margin-top: 20px;
    border: 1px solid #ddd;
    padding: 10px;
}

.item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}

.item img {
    width: 50px;
    height: 50px;
    margin-right: 10px;
}

.item-card {
    border: 1px solid #ddd;
    padding: 10px;
    margin: 10px 0;
}

.item-card img {
    width: 100px;
    height: 100px;
}
``` 

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.css';

ReactDOM.render(<App />, document.getElementById('root'));
``` 

This code provides a clean, efficient shopping cart feature in React suitable for a children's clothing website. It includes components for displaying items, managing the cart, and calculating the total price, all while adhering to best practices in React development.
