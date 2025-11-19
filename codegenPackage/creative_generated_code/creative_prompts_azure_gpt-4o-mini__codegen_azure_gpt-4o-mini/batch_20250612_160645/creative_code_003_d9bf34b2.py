"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rembytservis02.ru
Prompt: Develop a simple web form in HTML/CSS for users to submit their requests for selling laptops and computers, referencing the service details provided on the site.
Generated: DETERMINISTIC_d9bf34b232e56e38
Batch ID: 20250612_160645
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
    <title>Sell Your Laptop/Computer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Request to Sell Your Laptop/Computer</h1>
        <form id="sellForm" action="submit_request.php" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>

            <label for="deviceType">Device Type:</label>
            <select id="deviceType" name="deviceType" required>
                <option value="" disabled selected>Select your device</option>
                <option value="laptop">Laptop</option>
                <option value="desktop">Desktop Computer</option>
            </select>

            <label for="deviceModel">Device Model:</label>
            <input type="text" id="deviceModel" name="deviceModel" required>

            <label for="condition">Condition:</label>
            <textarea id="condition" name="condition" rows="4" required placeholder="Describe the condition of your device"></textarea>

            <label for="price">Expected Selling Price:</label>
            <input type="number" id="price" name="price" min="0" required>

            <button type="submit">Submit Request</button>
        </form>
    </div>

    <script src="script.js"></script>
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
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
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

```javascript
// script.js
document.getElementById('sellForm').addEventListener('submit', function(event) {
    // Perform any client-side validation or processing here
    // For example, you can check for specific conditions before allowing the submission
    const price = document.getElementById('price').value;

    if (price < 0) {
        alert('Expected selling price cannot be negative.');
        event.preventDefault(); // Stop the form from submitting
    }
});
```

```php
<?php
// submit_request.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Capture and sanitize form data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $deviceType = filter_input(INPUT_POST, 'deviceType', FILTER_SANITIZE_STRING);
    $deviceModel = filter_input(INPUT_POST, 'deviceModel', FILTER_SANITIZE_STRING);
    $condition = filter_input(INPUT_POST, 'condition', FILTER_SANITIZE_STRING);
    $price = filter_input(INPUT_POST, 'price', FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);

    // Basic validation
    if (!$name || !$email || !$deviceType || !$deviceModel || !$condition || $price < 0) {
        die("Invalid input data. Please go back and try again.");
    }

    // Simulate request processing (e.g., save to database or send email)
    // Note: Use prepared statements for database operations to prevent SQL injection
    // For now, we will just print the data as an example
    echo "Request received successfully!";
    echo "Name: $name, Email: $email, Device Type: $deviceType, Device Model: $deviceModel, Condition: $condition, Price: $price";
} else {
    // If not submitted, redirect to form
    header("Location: index.html");
    exit();
}
?>
```
