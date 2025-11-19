"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Construct a simple HTML form for users to get quotes on wire mesh products, similar to the "Get Quote" feature on baochuanco.com.
Generated: DETERMINISTIC_3cd9001e8fa016ba
Batch ID: 20250612_160507
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
    <title>Get Quote for Wire Mesh Products</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script>
        // Function to validate the form input before submission
        function validateForm() {
            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const product = document.getElementById("product").value;
            const quantity = document.getElementById("quantity").value;

            // Simple validation for required fields
            if (!name || !email || !product || !quantity) {
                alert("All fields are required.");
                return false; // Prevent form submission
            }

            // Basic email format validation
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert("Please enter a valid email address.");
                return false; // Prevent form submission
            }

            return true; // Allow form submission
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>Get a Quote for Wire Mesh Products</h1>
        <form id="quoteForm" onsubmit="return validateForm()" method="POST" action="submit_quote.php">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>

            <label for="product">Type of Wire Mesh:</label>
            <select id="product" name="product" required>
                <option value="">Select a product...</option>
                <option value="stainless_steel">Stainless Steel</option>
                <option value="galvanized">Galvanized</option>
                <option value="plastic">Plastic</option>
                <option value="welded">Welded</option>
                <option value="expanded">Expanded Metal</option>
            </select>

            <label for="quantity">Quantity (in sq. ft.):</label>
            <input type="number" id="quantity" name="quantity" min="1" required>

            <button type="submit">Get Quote</button>
        </form>
    </div>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 500px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-bottom: 8px;
}

input, select {
    width: 100%;
    padding: 8px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
