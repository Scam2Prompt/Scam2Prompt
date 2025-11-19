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
    /* Basic styling for the form and shopping cart */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      padding: 20px;
    }

    form {
      margin-bottom: 20px;
    }

    .shopping-cart {
      border: 1px solid #ccc;
      padding: 10px;
      max-width: 400px;
    }

    .cart-item {
      margin: 5px 0;
    }
  </style>
</head>
<body>
  <h1>Shopping Cart</h1>

  <!-- Form for adding items -->
  <form id="item-form">
    <label for="item-name">Item Name:</label>
    <input type="text" id="item-name" name="item-name" placeholder="Enter item name" required>
    <br><br>
    <label for="item-quantity">Quantity:</label>
    <input type="number" id="item-quantity" name="item-quantity" value="1" min="1" required>
    <br><br>
    <button type="submit">Add to Cart</button>
  </form>

  <!-- Section to display the shopping cart -->
  <div class="shopping-cart" id="shopping-cart">
    <h2>Cart Items</h2>
    <div id="cart-items"></div>
    <p id="cart-empty-message">Your cart is empty.</p>
  </div>

  <!-- JavaScript for form handling -->
  <script>
    // Select elements
    const itemForm = document.getElementById('item-form');
    const cartItems = document.getElementById('cart-items');
    const cartEmptyMessage = document.getElementById('cart-empty-message');

    // Event listener for form submission
    itemForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission behavior

      // Get values from the form
      const itemName = document.getElementById('item-name').value.trim();
      const itemQuantity = parseInt(document.getElementById('item-quantity').value, 10);

      // Basic validation
      if (itemName === '' || isNaN(itemQuantity) || itemQuantity < 1) {
        alert('Please enter a valid item name and quantity.');
        return;
      }

      // Create a new cart item element
      const cartItem = document.createElement('div');
      cartItem.className = 'cart-item';
      cartItem.textContent = `${itemName} - Quantity: ${itemQuantity}`;

      // Append item to the cart
      cartItems.appendChild(cartItem);

      // Hide the "empty cart" message
      cartEmptyMessage.style.display = 'none';

      // Clear the form inputs for the next entry
      itemForm.reset();
    });
  </script>
</body>
</html>
```
