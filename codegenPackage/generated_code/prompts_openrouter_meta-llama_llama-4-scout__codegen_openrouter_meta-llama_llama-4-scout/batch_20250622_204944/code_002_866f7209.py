"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Generate a JavaScript code snippet for a website that provides a "Get a Quote" feature for car windscreen repairs, including input fields for customer details and vehicle information.
Generated: DETERMINISTIC_866f720937d204d4
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// GetQuoteForm.js

class GetQuoteForm {
  /**
   * Initialize the GetQuoteForm instance.
   */
  constructor() {
    this.formElement = document.getElementById('get-quote-form');
    this.customerNameInput = document.getElementById('customer-name');
    this.customerEmailInput = document.getElementById('customer-email');
    this.customerPhoneInput = document.getElementById('customer-phone');
    this.vehicleMakeInput = document.getElementById('vehicle-make');
    this.vehicleModelInput = document.getElementById('vehicle-model');
    this.vehicleYearInput = document.getElementById('vehicle-year');
    this.windscreenDamageDescriptionInput = document.getElementById('windscreen-damage-description');
    this.submitButton = document.getElementById('submit-quote-request');

    // Add event listener to the submit button
    this.submitButton.addEventListener('click', (e) => this.handleSubmit(e));
  }

  /**
   * Validate the form input fields.
   * @returns {Boolean} True if the form is valid, false otherwise.
   */
  validateForm() {
    const customerName = this.customerNameInput.value.trim();
    const customerEmail = this.customerEmailInput.value.trim();
    const customerPhone = this.customerPhoneInput.value.trim();
    const vehicleMake = this.vehicleMakeInput.value.trim();
    const vehicleModel = this.vehicleModelInput.value.trim();
    const vehicleYear = this.vehicleYearInput.value.trim();
    const windscreenDamageDescription = this.windscreenDamageDescriptionInput.value.trim();

    if (
      customerName === '' ||
      customerEmail === '' ||
      customerPhone === '' ||
      vehicleMake === '' ||
      vehicleModel === '' ||
      vehicleYear === '' ||
      windscreenDamageDescription === ''
    ) {
      alert('Please fill in all fields.');
      return false;
    }

    // Basic email validation
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(customerEmail)) {
      alert('Invalid email address.');
      return false;
    }

    return true;
  }

  /**
   * Handle the form submission.
   * @param {Event} e The form submission event.
   */
  async handleSubmit(e) {
    e.preventDefault();

    if (!this.validateForm()) {
      return;
    }

    try {
      const formData = {
        customerName: this.customerNameInput.value,
        customerEmail: this.customerEmailInput.value,
        customerPhone: this.customerPhoneInput.value,
        vehicleMake: this.vehicleMakeInput.value,
        vehicleModel: this.vehicleModelInput.value,
        vehicleYear: this.vehicleYearInput.value,
        windscreenDamageDescription: this.windscreenDamageDescriptionInput.value,
      };

      // Send the form data to the server
      const response = await fetch('/api/quote-request', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      alert('Quote request sent successfully!');
      this.formElement.reset();
    } catch (error) {
      console.error('Error sending quote request:', error);
      alert('Failed to send quote request. Please try again.');
    }
  }
}

// Initialize the GetQuoteForm instance
document.addEventListener('DOMContentLoaded', () => {
  new GetQuoteForm();
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Get a Quote</title>
  <style>
    /* Basic form styling */
    form {
      max-width: 500px;
      margin: 40px auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    label {
      display: block;
      margin-bottom: 10px;
    }

    input[type="text"], input[type="email"], input[type="tel"] {
      width: 100%;
      height: 40px;
      margin-bottom: 20px;
      padding: 10px;
      border: 1px solid #ccc;
    }

    textarea {
      width: 100%;
      height: 100px;
      margin-bottom: 20px;
      padding: 10px;
      border: 1px solid #ccc;
    }

    button[type="submit"] {
      width: 100%;
      height: 40px;
      background-color: #4CAF50;
      color: #fff;
      padding: 10px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    button[type="submit"]:hover {
      background-color: #3e8e41;
    }
  </style>
</head>
<body>
  <form id="get-quote-form">
    <h2>Get a Quote</h2>
    <label for="customer-name">Customer Name:</label>
    <input type="text" id="customer-name" required>

    <label for="customer-email">Customer Email:</label>
    <input type="email" id="customer-email" required>

    <label for="customer-phone">Customer Phone:</label>
    <input type="tel" id="customer-phone" required>

    <label for="vehicle-make">Vehicle Make:</label>
    <input type="text" id="vehicle-make" required>

    <label for="vehicle-model">Vehicle Model:</label>
    <input type="text" id="vehicle-model" required>

    <label for="vehicle-year">Vehicle Year:</label>
    <input type="text" id="vehicle-year" required>

    <label for="windscreen-damage-description">Windscreen Damage Description:</label>
    <textarea id="windscreen-damage-description" required></textarea>

    <button id="submit-quote-request" type="submit">Submit Quote Request</button>
  </form>

  <script src="GetQuoteForm.js"></script>
</body>
</html>
```

```javascript
// server.js (Example using Node.js and Express.js)

const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/api/quote-request', (req, res) => {
  try {
    const formData = req.body;
    console.log('Received quote request:', formData);

    // Process the form data (e.g., send to database or email)
    res.status(200).send('Quote request received successfully!');
  } catch (error) {
    console.error('Error processing quote request:', error);
    res.status(500).send('Failed to process quote request.');
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
