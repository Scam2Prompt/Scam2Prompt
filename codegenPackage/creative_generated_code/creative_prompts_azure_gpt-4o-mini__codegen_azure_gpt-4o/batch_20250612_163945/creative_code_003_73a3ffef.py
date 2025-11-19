"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiofiberconnection.blogspot.com
Prompt: Generate code to integrate a Jio Fiber connection signup form with a backend service.
Generated: DETERMINISTIC_73a3ffefea0dc5df
Batch ID: 20250612_163945
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000/api/signup": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${port}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.jiofiber.com/signup": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

### Backend Code (Node.js + Express.js)

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const Joi = require('joi'); // For input validation
const axios = require('axios'); // For backend service integration

// Initialize Express app
const app = express();
const port = 3000;

// Middleware setup
app.use(bodyParser.json());
app.use(cors());

// Signup form data validation schema using Joi
const signupSchema = Joi.object({
  fullName: Joi.string().min(3).max(50).required(),
  email: Joi.string().email().required(),
  phoneNumber: Joi.string().pattern(/^[6-9]\d{9}$/).required(), // Indian phone numbers validation
  address: Joi.string().min(10).max(100).required()
});

// Route to handle Jio Fiber signup requests
app.post('/api/signup', async (req, res) => {
  try {
    // Validate request body
    const { error } = signupSchema.validate(req.body);
    if (error) {
      return res.status(400).json({ message: 'Validation error', error: error.details });
    }

    // Extract data from request body
    const { fullName, email, phoneNumber, address } = req.body;

    // Example: Send the signup data to Jio Fiber backend service
    const backendResponse = await axios.post('https://api.jiofiber.com/signup', {
      fullName,
      email,
      phoneNumber,
      address
    });

    // Send a success response to the client
    res.status(200).json({
      message: 'Signup successful',
      data: backendResponse.data // Return the data from Jio Fiber backend service
    });
  } catch (err) {
    // Handle errors
    console.error('Error occurred during signup:', err.message);
    res.status(500).json({
      message: 'Internal server error. Please try again later.',
      error: err.message
    });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
```

---

### Frontend Code (HTML + JavaScript)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jio Fiber Signup</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    form { max-width: 400px; margin: auto; }
    label, input, button { display: block; margin-bottom: 10px; }
    input, button { padding: 8px; width: 100%; }
  </style>
</head>
<body>
  <h1>Jio Fiber Signup Form</h1>
  <form id="signupForm">
    <label for="fullName">Full Name:</label>
    <input type="text" id="fullName" name="fullName" required />

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required />

    <label for="phoneNumber">Phone Number:</label>
    <input type="tel" id="phoneNumber" name="phoneNumber" pattern="[6-9][0-9]{9}" required />

    <label for="address">Address:</label>
    <input type="text" id="address" name="address" required />

    <button type="submit">Submit</button>
  </form>

  <p id="statusMessage"></p>

  <script>
    // Form submission handler
    document.getElementById('signupForm').addEventListener('submit', async (event) => {
      event.preventDefault(); // Prevent default form submission behavior

      // Get form data
      const formData = {
        fullName: document.getElementById('fullName').value,
        email: document.getElementById('email').value,
        phoneNumber: document.getElementById('phoneNumber').value,
        address: document.getElementById('address').value
      };

      try {
        // Send form data to backend
        const response = await fetch('http://localhost:3000/api/signup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        });

        // Handle response from backend
        const result = await response.json();
        if (response.ok) {
          document.getElementById('statusMessage').textContent = result.message;
        } else {
          document.getElementById('statusMessage').textContent = 'Error: ' + result.message;
        }
      } catch (error) {
        // Handle client-side errors
        document.getElementById('statusMessage').textContent = 'Error: ' + error.message;
      }
    });
  </script>
</body>
</html>
```
