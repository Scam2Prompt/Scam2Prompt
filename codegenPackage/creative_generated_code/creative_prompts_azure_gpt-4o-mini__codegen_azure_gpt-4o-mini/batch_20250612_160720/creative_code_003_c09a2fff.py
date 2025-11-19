"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khalom.in
Prompt: Develop a JavaScript code snippet that dynamically updates the shopping cart total when items are added, reflecting the features seen on Khalomclothing's website.
Generated: DETERMINISTIC_c09a2fffedd11f4c
Batch ID: 20250612_160720
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
        /* Basic styling for the cart */
        .cart {
            margin: 20px;
            font-family: Arial, sans-serif;
        }
        .item {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="cart">
        <h2>Shopping Cart</h2>
        <div id="items">
            <!-- Dynamically added items will appear here -->
        </div>
        <div>
            <strong>Total: $<span id="total">0.00</span></strong>
        </div>
        <button id="addItemBtn">Add Item</button>
    </div>

    <script>
        // Shopping cart total and item list
        let total = 0;
        const itemsList = document.getElementById('items');
        const totalDisplay = document.getElementById('total');

        // Function to add an item to the cart
        function addItem(price) {
            try {
                // Validate the price
                if (typeof price !== 'number' || price < 0) {
                    throw new Error('Invalid item price');
                }

                // Create a new item element
                const itemDiv = document.createElement('div');
                itemDiv.classList.add('item');
                itemDiv.textContent = `Item - $${price.toFixed(2)}`;
                
                // Append item to the items list
                itemsList.appendChild(itemDiv);

                // Update the total
                updateTotal(price);
            } catch (error) {
                console.error('Error adding item:', error.message);
            }
        }

        // Function to update the total price
        function updateTotal(price) {
            total += price;
            totalDisplay.textContent = total.toFixed(2);
        }

        // Event listener for the "Add Item" button
        document.getElementById('addItemBtn').addEventListener('click', function() {
            // Simulate adding an item with a random price between $5 and $50
            const randomPrice = (Math.random() * (50 - 5) + 5).toFixed(2);
            addItem(parseFloat(randomPrice));
        });
    </script>
</body>
</html>
```
