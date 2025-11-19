"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lestersplace.com
Prompt: Generate a code snippet for a web application that allows users to contact assisted living facilities like Lester's Place, including fields for name, phone number, and message.
Generated: DETERMINISTIC_a5021ad33a88559d
Batch ID: 20250612_161353
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
    <title>Contact Assisted Living Facility</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <div class="container">
        <h1>Contact Lester's Place</h1>
        <form id="contactForm" action="/send-message" method="POST">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" placeholder="123-456-7890">

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Send Message</button>
        </form>
        <div id="responseMessage" class="hidden"></div>
    </div>

    <script>
        // Add an event listener to the form submission
        document.getElementById('contactForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this); // Gather form data

            try {
                // Send the form data to the server
                const response = await fetch(this.action, {
                    method: this.method,
                    body: formData,
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`); // Handle non-200 responses
                }

                const result = await response.json(); // Parse JSON response
                document.getElementById('responseMessage').innerText = result.message; // Show success message
                document.getElementById('responseMessage').classList.remove('hidden'); // Display message
                this.reset(); // Reset form fields
            } catch (error) {
                console.error('Error:', error); // Log the error for debugging
                document.getElementById('responseMessage').innerText = 'An error occurred. Please try again later.'; // Show error message
                document.getElementById('responseMessage').classList.remove('hidden'); // Display message
            }
        });
    </script>
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
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"],
input[type="tel"],
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 15px;
}

button {
    background-color: #5cb85c;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

.hidden {
    display: none;
}
``` 

```javascript
// Sample server-side code (Node.js with Express)
// This would be in your server file (e.g., server.js)

const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.urlencoded({ extended: true })); // Middleware to parse URL-encoded data

// Endpoint to handle form submissions
app.post('/send-message', (req, res) => {
    const { name, phone, message } = req.body;

    // Validate inputs
    if (!name || !phone || !message) {
        return res.status(400).json({ message: 'All fields are required.' });
    }

    // Here, you would typically send the message to a database or an email
    console.log(`Received message from ${name} (${phone}): ${message}`);

    // Send back a success response
    res.json({ message: 'Your message has been sent successfully!' });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
