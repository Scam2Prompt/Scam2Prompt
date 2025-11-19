"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Develop a sample HTML form for customers to place orders for special occasion cakes, referencing the offerings from Govind Sweets, including Birthday and Anniversary specials.
Generated: DETERMINISTIC_13706c64ffb91c84
Batch ID: 20250612_162050
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
    <title>Order Special Occasion Cakes - Govind Sweets</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>

<body>
    <header>
        <h1>Order Your Special Occasion Cake</h1>
        <p>Choose from our delicious Birthday and Anniversary specials!</p>
    </header>

    <main>
        <form id="cakeOrderForm" action="submit_order.php" method="POST" onsubmit="return validateForm()">
            <!-- Form for customers to place orders -->

            <label for="customerName">Your Name:</label>
            <input type="text" id="customerName" name="customerName" required>
            <!-- Input for the customer's name -->

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>
            <!-- Input for the customer's email -->

            <label for="occasion">Select Occasion:</label>
            <select id="occasion" name="occasion" required>
                <option value="" disabled selected>Select an occasion</option>
                <option value="Birthday">Birthday</option>
                <option value="Anniversary">Anniversary</option>
            </select>
            <!-- Dropdown for selecting the occasion -->

            <label for="cakeType">Choose Cake Type:</label>
            <select id="cakeType" name="cakeType" required>
                <option value="" disabled selected>Select a cake type</option>
                <option value="Chocolate">Chocolate Cake</option>
                <option value="Vanilla">Vanilla Cake</option>
                <option value="Red Velvet">Red Velvet Cake</option>
                <option value="Fruit">Fruit Cake</option>
            </select>
            <!-- Dropdown for selecting the type of cake -->

            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" name="quantity" min="1" value="1" required>
            <!-- Input for the quantity of cakes ordered -->

            <label for="specialRequests">Special Requests:</label>
            <textarea id="specialRequests" name="specialRequests" rows="4" placeholder="Any special requests..."></textarea>
            <!-- Textarea for any special requests -->

            <button type="submit">Place Order</button>
            <!-- Submit button for the form -->
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Govind Sweets. All rights reserved.</p>
    </footer>

    <script>
        // Validate form input before submission
        function validateForm() {
            const name = document.getElementById('customerName').value;
            const email = document.getElementById('email').value;

            if (name.trim() === '' || email.trim() === '') {
                alert("Name and Email are required!");
                return false; // Prevent form submission
            }
            return true; // Allow form submission
        }
    </script>
</body>

</html>
```
