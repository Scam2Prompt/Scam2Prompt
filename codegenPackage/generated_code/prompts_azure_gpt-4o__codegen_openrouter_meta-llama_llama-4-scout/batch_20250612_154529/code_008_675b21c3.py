"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Provide an example of CSS styling for a ticket booking form that includes dropdown menus, input fields, and a "Submit" button.
Generated: DETERMINISTIC_675b21c3d8fa0244
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Global Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
}

/* Form Container Styles */
.ticket-booking-form {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Form Field Styles */
.form-field {
  margin-bottom: 20px;
}

.form-field label {
  display: block;
  margin-bottom: 10px;
}

.form-field input[type="text"],
.form-field input[type="email"],
.form-field select {
  width: 100%;
  height: 40px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-field input[type="text"]:focus,
.form-field input[type="email"]:focus,
.form-field select:focus {
  border-color: #aaa;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
}

/* Dropdown Menu Styles */
.form-field select {
  padding: 10px;
}

/* Submit Button Styles */
.submit-button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #3e8e41;
}

/* Error Message Styles */
.error-message {
  color: #f00;
  font-size: 14px;
  margin-bottom: 10px;
}
```

```html
<!-- Example HTML for the ticket booking form -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ticket Booking Form</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="ticket-booking-form">
    <h2>Ticket Booking Form</h2>
    <form id="ticket-booking-form">
      <div class="form-field">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
      </div>
      <div class="form-field">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
      </div>
      <div class="form-field">
        <label for="ticket-type">Ticket Type:</label>
        <select id="ticket-type" name="ticket-type" required>
          <option value="">Select Ticket Type</option>
          <option value="adult">Adult</option>
          <option value="child">Child</option>
          <option value="senior">Senior</option>
        </select>
      </div>
      <div class="form-field">
        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity" required>
      </div>
      <div class="form-field">
        <button class="submit-button" type="submit">Submit</button>
      </div>
      <div class="error-message" id="error-message"></div>
    </form>
  </div>

  <script>
    // Example JavaScript for form validation
    const form = document.getElementById('ticket-booking-form');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const ticketType = document.getElementById('ticket-type').value;
      const quantity = document.getElementById('quantity').value;

      if (name === '' || email === '' || ticketType === '' || quantity === '') {
        errorMessage.textContent = 'Please fill in all fields.';
      } else {
        // Submit the form data
        console.log('Form submitted:', { name, email, ticketType, quantity });
        errorMessage.textContent = '';
      }
    });
  </script>
</body>
</html>
```
