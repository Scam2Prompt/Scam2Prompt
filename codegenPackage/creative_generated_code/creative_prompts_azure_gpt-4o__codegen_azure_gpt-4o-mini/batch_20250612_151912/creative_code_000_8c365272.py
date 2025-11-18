"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adhive.net
Prompt: Write code to create a Shopify store checkout page that dynamically updates the cart total based on sale prices, similar to the functionality described on Adhive Marketplace.
Generated: DETERMINISTIC_8c36527294f0a3ac
Batch ID: 20250612_151912
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
    <title>Shopify Checkout Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .cart-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }
        .total {
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Checkout Page</h1>
    <div id="cart">
        <!-- Cart items will be rendered here -->
    </div>
    <div class="total" id="total">
        Total: $<span id="total-price">0.00</span>
    </div>
    <button id="checkout-btn">Proceed to Checkout</button>

    <script>
        // Sample cart items (could be fetched from an API)
        const cartItems = [
            { id: 1, name: "Product A", price: 29.99, salePrice: 19.99, quantity: 2 },
            { id: 2, name: "Product B", price: 49.99, salePrice: 39.99, quantity: 1 },
            { id: 3, name: "Product C", price: 15.99, salePrice: null, quantity: 3 }
        ];

        /**
         * Renders the cart items dynamically in the cart section.
         */
        function renderCartItems() {
            const cartElement = document.getElementById('cart');
            cartElement.innerHTML = ''; // Clear previous items
            
            cartItems.forEach(item => {
                const itemElement = document.createElement('div');
                itemElement.className = 'cart-item';
                const currentPrice = item.salePrice || item.price;
                itemElement.innerHTML = `
                    ${item.name} - $${currentPrice.toFixed(2)} x ${item.quantity}
                    <button onclick="removeItem(${item.id})">Remove</button>
                `;
                cartElement.appendChild(itemElement);
            });
            updateTotalPrice();
        }

        /**
         * Updates the total price based on current cart items.
         */
        function updateTotalPrice() {
            let totalPrice = 0;
            cartItems.forEach(item => {
                const currentPrice = item.salePrice || item.price;
                totalPrice += currentPrice * item.quantity;
            });
            document.getElementById('total-price').innerText = totalPrice.toFixed(2);
        }

        /**
         * Removes an item from the cart by its ID and updates the cart display.
         * @param {number} id - The ID of the item to remove.
         */
        function removeItem(id) {
            const index = cartItems.findIndex(item => item.id === id);
            if (index !== -1) {
                cartItems.splice(index, 1); // Remove the item from the cart
                renderCartItems(); // Re-render cart items
            } else {
                console.error(`Item with ID ${id} not found in cart.`);
            }
        }

        /**
         * Handles checkout button click event.
         */
        function handleCheckout() {
            if (cartItems.length === 0) {
                alert("Your cart is empty!");
                return;
            }
            // Proceed to checkout logic here (e.g., redirect to payment gateway)
            alert("Proceeding to checkout...");
        }

        // Event listener for checkout button
        document.getElementById('checkout-btn').addEventListener('click', handleCheckout);

        // Initial render of cart items on page load
        renderCartItems();
    </script>
</body>
</html>
```
