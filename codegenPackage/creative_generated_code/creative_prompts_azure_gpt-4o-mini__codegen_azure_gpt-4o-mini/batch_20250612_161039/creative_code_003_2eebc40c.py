"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Develop a simple HTML form that enables users to inquire about specific hardware products from APN Hardware, ensuring it captures essential contact details.
Generated: DETERMINISTIC_2eebc40c268a4e23
Batch ID: 20250612_161039
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
    <title>APN Hardware Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript for form handling -->
</head>
<body>
    <div class="container">
        <h1>Inquire About Our Hardware Products</h1>
        <form id="inquiryForm" method="POST" action="/submit-inquiry">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name">

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

            <label for="product">Product of Interest:</label>
            <input type="text" id="product" name="product" required placeholder="Enter the product name">

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" placeholder="Enter your message"></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="responseMessage"></div> <!-- Div to display response message -->
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the inquiry form */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('inquiryForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const formData = new FormData(this);

    // Send form data to the server
    fetch(this.action, {
        method: this.method,
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok'); // Throw an error for a bad response
        }
        return response.json(); // Parse the JSON response
    })
    .then(data => {
        // Display success message
        document.getElementById('responseMessage').innerText = 'Your inquiry has been submitted successfully!';
    })
    .catch(error => {
        // Display error message
        document.getElementById('responseMessage').innerText = 'There was an error submitting your inquiry: ' + error.message;
    });
});
```
