"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Design a simple HTML form that allows users to add items like "TINTA SPRAY VERNIZ" to a shopping cart, similar to the functionality seen on the Gala Games app.
Generated: DETERMINISTIC_fd40107fc8d386c1
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Cart</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .item input {
            padding: 10px;
            margin-right: 10px;
            flex-grow: 1;
        }
        .item button {
            padding: 10px 15px;
            border: none;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
            border-radius: 5px;
        }
        .item button:hover {
            background-color: #0056b3;
        }
        .cart {
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Add Item to Cart</h1>
    <form id="itemForm">
        <div class="item">
            <input type="text" id="itemName" placeholder="Enter item name" required>
            <button type="submit">Add to Cart</button>
        </div>
    </form>
    
    <div class="cart">
        <h2>Shopping Cart</h2>
        <ul id="cartList"></ul>
    </div>
</div>

<script>
    // Initialize an empty cart array
    const cart = [];

    // Get references to the form and the cart list
    const itemForm = document.getElementById('itemForm');
    const cartList = document.getElementById('cartList');

    // Function to add item to the cart
    function addItemToCart(itemName) {
        // Check if item already exists in the cart
        if (cart.includes(itemName)) {
            alert('Item already in cart!');
            return;
        }
        // Add item to the cart array
        cart.push(itemName);
        // Update the cart display
        displayCart();
    }

    // Function to display the cart contents
    function displayCart() {
        // Clear the current cart list
        cartList.innerHTML = '';
        // Populate the cart list with items
        cart.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            cartList.appendChild(li);
        });
    }

    // Event listener for form submission
    itemForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        const itemName = document.getElementById('itemName').value; // Get the item name
        addItemToCart(itemName); // Add the item to the cart
        itemForm.reset(); // Clear the input field
    });
</script>

</body>
</html>
```
