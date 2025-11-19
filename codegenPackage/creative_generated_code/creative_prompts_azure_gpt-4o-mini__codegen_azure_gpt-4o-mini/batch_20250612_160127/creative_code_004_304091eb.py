"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonswallet.top
Prompt: Construct a sample HTML form for adding items to a shopping cart for track cycling equipment, reflecting the structure of the Velodrome Shop's checkout process.
Generated: DETERMINISTIC_304091eb1b9d069b
Batch ID: 20250612_160127
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
    <title>Velodrome Shop - Add to Cart</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Velodrome Shop</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="cart.html">Cart</a></li>
                <li><a href="contact.html">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <h2>Add Item to Cart</h2>
        <form id="addItemForm" action="/add-to-cart" method="POST" onsubmit="return validateForm()">
            <fieldset>
                <legend>Item Details</legend>
                
                <label for="itemName">Item Name:</label>
                <input type="text" id="itemName" name="itemName" required placeholder="Enter item name">
                
                <label for="itemCategory">Category:</label>
                <select id="itemCategory" name="itemCategory" required>
                    <option value="">Select a category</option>
                    <option value="bikes">Bikes</option>
                    <option value="helmets">Helmets</option>
                    <option value="apparel">Apparel</option>
                    <option value="accessories">Accessories</option>
                </select>
                
                <label for="itemQuantity">Quantity:</label>
                <input type="number" id="itemQuantity" name="itemQuantity" min="1" max="100" required value="1">
                
                <label for="itemPrice">Price ($):</label>
                <input type="number" id="itemPrice" name="itemPrice" step="0.01" required placeholder="Enter item price">

                <label for="itemDescription">Description:</label>
                <textarea id="itemDescription" name="itemDescription" rows="4" placeholder="Enter a brief description"></textarea>
            </fieldset>

            <button type="submit">Add to Cart</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Velodrome Shop. All rights reserved.</p>
    </footer>

    <script>
        // Function to validate form input before submission
        function validateForm() {
            const itemName = document.getElementById('itemName').value;
            const itemQuantity = document.getElementById('itemQuantity').value;

            if (itemName.trim() === "") {
                alert("Item name cannot be empty.");
                return false;
            }

            if (itemQuantity <= 0) {
                alert("Quantity must be at least 1.");
                return false;
            }

            return true; // Form is valid
        }
    </script>
</body>
</html>
```
