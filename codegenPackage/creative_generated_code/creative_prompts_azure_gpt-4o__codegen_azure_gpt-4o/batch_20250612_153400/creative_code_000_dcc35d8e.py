"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rdmerakyat.com
Prompt: Write code to create a subscription form for an architectural newsletter, similar to the one described on Études' website, and ensure it integrates with a backend service for managing 900+ subscribers.
Generated: DETERMINISTIC_dcc35d8e01af5264
Batch ID: 20250612_153400
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

### Frontend Code (HTML + CSS + JavaScript)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Architectural Newsletter Subscription</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="subscription-form-container">
    <h1>Subscribe to Our Architectural Newsletter</h1>
    <form id="subscription-form">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" placeholder="Your Name" required>

      <label for="email">Email:</label>
      <input type="email" id="email" name="email" placeholder="Your Email" required>

      <button type="submit">Subscribe</button>
    </form>
    <p id="response-message"></p>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f4f4f9;
}

.subscription-form-container {
  background: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 300px;
}

h1 {
  font-size: 1.5rem;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
}

input {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #cccccc;
  border-radius: 4px;
}

button {
  padding: 10px;
  background-color: #007BFF;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

#response-message {
  margin-top: 10px;
  color: #007BFF;
  font-size: 0.9rem;
}
```

```javascript
// script.js

// Add event listener to handle form submission
document.getElementById('subscription-form').addEventListener('submit', async function (event) {
  event.preventDefault(); // Prevent default form submission

  // Extract values from the form
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;

  try {
    // Send the subscription data to the backend via POST request
    const response = await fetch('/api/subscribe', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, email })
    });

    // Handle response from the server
    if (response.ok) {
      const data = await response.json();
      document.getElementById('response-message').textContent = data.message || 'Thank you for subscribing!';
    } else {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Failed to subscribe. Please try again.');
    }
  } catch (error) {
    // Display error message to the user
    document.getElementById('response-message').textContent = error.message;
  }
});
```

---

### Backend Code (Node.js + Express)

```javascript
// server.js

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Mock Database for Subscribers
const subscribers = [];

// Endpoint: Handle Subscription
app.post('/api/subscribe', (req, res) => {
  const { name, email } = req.body;

  // Validate input
  if (!name || !email) {
    return res.status(400).json({ message: 'Name and email are required.' });
  }

  // Check if email is already subscribed
  const isAlreadySubscribed = subscribers.some(subscriber => subscriber.email === email);
  if (isAlreadySubscribed) {
    return res.status(409).json({ message: 'Email is already subscribed.' });
  }

  // Add subscriber to the "database"
  subscribers.push({ name, email });

  // Respond with success message
  res.status(200).json({ message: 'Subscription successful!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Notes:
- Replace the mock array `subscribers` with a real database in production (e.g., MongoDB, PostgreSQL).
- Add HTTPS and authentication for enhanced security in production.
- Ensure API routes are well-documented for maintainability.
