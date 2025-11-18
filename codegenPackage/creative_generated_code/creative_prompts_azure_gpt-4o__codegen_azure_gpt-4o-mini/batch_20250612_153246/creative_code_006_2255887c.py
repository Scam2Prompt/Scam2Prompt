"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Write code for a newsletter subscription form that integrates with an e-commerce site, similar to Gvika's "Newsletter" feature.
Generated: DETERMINISTIC_2255887c301795be
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!-- Newsletter Subscription Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter Subscription</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="newsletter-container">
        <h2>Subscribe to Our Newsletter</h2>
        <form id="newsletterForm" action="/subscribe" method="POST">
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="you@example.com">

            <button type="submit">Subscribe</button>
        </form>
        <div id="responseMessage" class="hidden"></div> <!-- Message display area -->
    </div>

    <script>
        document.getElementById('newsletterForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const email = document.getElementById('email').value;
            const responseMessage = document.getElementById('responseMessage');

            // Clear previous messages
            responseMessage.classList.add('hidden');

            // Validate email format
            if (!validateEmail(email)) {
                responseMessage.textContent = 'Please enter a valid email address.';
                responseMessage.classList.remove('hidden');
                return;
            }

            // Send subscription request to the server
            fetch('/subscribe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                return response.json();
            })
            .then(data => {
                // Handle success response
                if (data.success) {
                    responseMessage.textContent = 'Thank you for subscribing!';
                } else {
                    responseMessage.textContent = 'Subscription failed. Please try again later.';
                }
                responseMessage.classList.remove('hidden');
            })
            .catch(error => {
                // Handle errors gracefully
                console.error('There was a problem with the fetch operation:', error);
                responseMessage.textContent = 'An error occurred. Please try again later.';
                responseMessage.classList.remove('hidden');
            });
        });

        // Function to validate email format
        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple regex for email validation
            return re.test(String(email).toLowerCase());
        }
    </script>
</body>
</html>
```

```css
/* styles.css - Basic styling for the newsletter subscription form */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.newsletter-container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
    text-align: center;
}

input[type="email"] {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.hidden {
    display: none;
}

#responseMessage {
    color: red;
    text-align: center;
    margin-top: 10px;
}
```

```javascript
// server.js - Node.js Express server for handling newsletter subscriptions

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Simulated database (for demonstration)
let subscribers = [];

// Subscribe endpoint
app.post('/subscribe', (req, res) => {
    const { email } = req.body;

    // Basic validation
    if (!email || !validateEmail(email)) {
        return res.status(400).json({ success: false, message: 'Invalid email address' });
    }

    // Check for duplicate subscriptions
    if (subscribers.includes(email)) {
        return res.status(409).json({ success: false, message: 'Email already subscribed' });
    }

    // Simulate adding to database
    subscribers.push(email);

    // Respond with success
    return res.status(200).json({ success: true });
});

// Function to validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple regex for email validation
    return re.test(String(email).toLowerCase());
}

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
