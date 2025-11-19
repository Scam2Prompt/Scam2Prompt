"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cloud-telephonie.net
Prompt: Generate a code snippet for a web form that collects user information like name, email, and phone number for a custom telephone quote.
Generated: DETERMINISTIC_845b2e39a393f245
Batch ID: 20250612_163945
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
    <title>Custom Telephone Quote Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JS for form handling -->
</head>
<body>
    <div class="container">
        <h1>Request a Custom Telephone Quote</h1>
        <form id="quoteForm" action="submit_quote.php" method="POST">
            <!-- Name input -->
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>

            <!-- Email input -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>

            <!-- Phone number input -->
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}" title="Please enter a valid 10-digit phone number.">
            </div>

            <!-- Submit button -->
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
    background-color: #f9f9f9;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 100%;
    padding: 8px;
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
document.getElementById('quoteForm').addEventListener('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Basic form validation
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();

    if (!name || !email || !phone) {
        alert('Please fill in all fields.');
        return;
    }

    // Optionally, further validation or data processing can be done here

    // Submit the form data using Fetch API
    fetch('submit_quote.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'name': name,
            'email': email,
            'phone': phone,
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then(data => {
        alert('Quote request submitted successfully!');
        // Clear the form
        document.getElementById('quoteForm').reset();
    })
    .catch((error) => {
        console.error('There was a problem with the fetch operation:', error);
        alert('An error occurred while submitting your request. Please try again later.');
    });
});
```

```php
<?php
// submit_quote.php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Collect and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);

    // Simple validation
    if (empty($name) || empty($email) || empty($phone)) {
        http_response_code(400);
        echo 'All fields are required.';
        exit;
    }

    // Here you would typically save the data to the database or send an email
    // For demonstration purposes, we're just returning a success message
    echo 'Quote request submitted successfully for ' . htmlspecialchars($name) . '!';
} else {
    // If the request is not POST, return a 405 Method Not Allowed error
    http_response_code(405);
    echo 'Method Not Allowed';
}
?>
```
