"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: Create a script that ensures a web application's core functionality, such as a shopping feature, works only when JavaScript is enabled, similar to the requirements on the Rarecrew app's "Shop" page.
Generated: DETERMINISTIC_3aad44c8ed504ce5
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shop Page</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none;
            color: red;
            font-weight: bold;
            margin: 20px;
        }
        /* Style for the main content when JavaScript is enabled */
        .js-enabled {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        JavaScript is required to use the shopping feature. Please enable JavaScript in your browser settings.
    </div>

    <!-- Main content of the shop page -->
    <div class="js-enabled" id="shop-content">
        <h1>Welcome to Our Shop</h1>
        <p>Here you can find amazing products!</p>
        <button id="add-to-cart">Add to Cart</button>
        <div id="cart-status"></div>
    </div>

    <script>
        // Function to initialize the shopping feature
        function initShoppingFeature() {
            const addToCartButton = document.getElementById('add-to-cart');
            const cartStatus = document.getElementById('cart-status');

            // Event listener for the "Add to Cart" button
            addToCartButton.addEventListener('click', function() {
                try {
                    // Simulate adding an item to the cart
                    cartStatus.textContent = 'Item added to cart!';
                } catch (error) {
                    console.error('Error adding item to cart:', error);
                    cartStatus.textContent = 'Failed to add item to cart. Please try again.';
                }
            });
        }

        // Function to show the appropriate content based on JavaScript availability
        function checkJavaScript() {
            const noJsMessage = document.getElementById('no-js-message');
            const shopContent = document.getElementById('shop-content');

            // If JavaScript is enabled, show the shop content and initialize features
            noJsMessage.style.display = 'none';
            shopContent.style.display = 'block';
            initShoppingFeature();
        }

        // Execute the check when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', checkJavaScript);
    </script>
</body>
</html>
```
