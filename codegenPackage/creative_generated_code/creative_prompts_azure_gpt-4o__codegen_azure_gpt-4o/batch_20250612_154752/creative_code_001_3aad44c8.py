"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarecrew-app.com
Prompt: Create a script that ensures a web application's core functionality, such as a shopping feature, works only when JavaScript is enabled, similar to the requirements on the Rarecrew app's "Shop" page.
Generated: DETERMINISTIC_3aad44c8ed504ce5
Batch ID: 20250612_154752
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
  <title>Shop Page</title>
  <style>
    /* Basic styling */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    .no-js-message {
      text-align: center;
      margin-top: 50px;
      color: red;
      font-weight: bold;
    }

    .shop-container {
      display: none; /* Hidden by default, shown when JS is enabled */
    }

    .shop-item {
      border: 1px solid #ddd;
      padding: 10px;
      margin: 10px;
      text-align: center;
    }
  </style>

  <noscript>
    <!-- Show a warning if JavaScript is disabled -->
    <style>
      .no-js-message {
        display: block !important;
      }

      .shop-container {
        display: none !important;
      }
    </style>
    <div class="no-js-message">
      JavaScript is required to use the shopping feature. Please enable JavaScript in your browser.
    </div>
  </noscript>
</head>

<body>
  <!-- Shop Content -->
  <div class="shop-container" id="shop-container">
    <h1>Welcome to Our Shop</h1>
    <div class="shop-item">
      <p>Item 1</p>
      <button onclick="addToCart(1)">Add to Cart</button>
    </div>
    <div class="shop-item">
      <p>Item 2</p>
      <button onclick="addToCart(2)">Add to Cart</button>
    </div>
    <div class="shop-item">
      <p>Item 3</p>
      <button onclick="addToCart(3)">Add to Cart</button>
    </div>
  </div>

  <script>
    /* Error handling and core functionality for the shop */

    // Show the shop container only if JavaScript is enabled
    const shopContainer = document.getElementById('shop-container');
    shopContainer.style.display = 'block';

    // Simulate adding items to the cart
    function addToCart(itemId) {
      try {
        // Perform the add-to-cart operation
        console.log(`Item ${itemId} added to cart.`);
        alert(`Item ${itemId} has been added to your cart!`);

        // Example: Send data to the server (could be an API call)
        // fetch('/api/add-to-cart', { method: 'POST', body: JSON.stringify({ itemId }) })
        //   .then(response => response.json())
        //   .then(data => console.log('Server Response:', data))
        //   .catch(error => console.error('Error adding to cart:', error));
      } catch (error) {
        // Handle any unexpected issues
        console.error('An error occurred:', error);
        alert('An error occurred while adding the item to the cart. Please try again.');
      }
    }
  </script>
</body>

</html>
```
