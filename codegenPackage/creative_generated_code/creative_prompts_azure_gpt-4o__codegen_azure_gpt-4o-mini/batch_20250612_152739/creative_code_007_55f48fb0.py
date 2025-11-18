"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Write JavaScript code to implement a dynamic shopping cart system for TiburonFishingReels.com, allowing users to add items like reel clamps and fasteners while updating the total cost in real-time.
Generated: DETERMINISTIC_55f48fb097d1f425
Batch ID: 20250612_152739
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
    <title>Tiburon Fishing Reels - Shopping Cart</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .cart-item {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        .cart-item input {
            width: 50px;
            margin-left: 10px;
        }
        .total {
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Tiburon Fishing Reels - Shopping Cart</h1>

    <div id="shopping-cart">
        <div class="cart-item">
            <label for="item-reel-clamp">Reel Clamp ($20):</label>
            <input type="number" id="item-reel-clamp" value="0" min="0" onchange="updateTotal()">
        </div>
        <div class="cart-item">
            <label for="item-fastener">Fastener ($5):</label>
            <input type="number" id="item-fastener" value="0" min="0" onchange="updateTotal()">
        </div>
        <div class="total" id="total-cost">Total: $0</div>
    </div>

    <script>
        /**
         * Updates the total cost based on the quantities of items added to the cart.
         * This function retrieves the values of each item, calculates the total,
         * and updates the total cost displayed on the webpage.
         */
        function updateTotal() {
            try {
                // Prices of the items
                const prices = {
                    reelClamp: 20,
                    fastener: 5
                };

                // Get quantities from input fields
                const reelClampQty = parseInt(document.getElementById('item-reel-clamp').value) || 0;
                const fastenerQty = parseInt(document.getElementById('item-fastener').value) || 0;

                // Calculate total cost
                const totalCost = (reelClampQty * prices.reelClamp) + (fastenerQty * prices.fastener);

                // Update the total cost display
                document.getElementById('total-cost').innerText = `Total: $${totalCost}`;
            } catch (error) {
                console.error('Error updating total cost:', error);
                alert('An error occurred while calculating the total cost. Please try again.');
            }
        }
    </script>

</body>
</html>
```
