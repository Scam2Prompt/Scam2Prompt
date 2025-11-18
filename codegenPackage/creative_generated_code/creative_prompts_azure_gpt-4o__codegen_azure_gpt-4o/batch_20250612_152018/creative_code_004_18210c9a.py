"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Generate code to build a subscription form for receiving updates from Darul Raza, ensuring the form validates input fields like email and phone number.
Generated: DETERMINISTIC_18210c9ad54f5bf9
Batch ID: 20250612_152018
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
  <title>Darul Raza Subscription Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f5f5f5;
    }
    form {
      background: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }
    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }
    input[type="text"], input[type="email"], input[type="tel"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #007BFF;
      color: white;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 14px;
      margin-top: -10px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>

  <form id="subscriptionForm">
    <h2>Subscribe for Updates from Darul Raza</h2>
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" placeholder="Enter your full name" required>

    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Enter your email" required>

    <label for="phone">Phone Number</label>
    <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required pattern="^\+?[1-9]\d{1,14}$">

    <button type="submit">Subscribe</button>
    <div id="message" class="error"></div>
  </form>

  <script>
    // JavaScript for form validation and submission
    const form = document.getElementById('subscriptionForm');
    const messageElement = document.getElementById('message');

    form.addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent form submission

      // Clear previous error messages
      messageElement.textContent = '';

      // Retrieve form values
      const name = form.name.value.trim();
      const email = form.email.value.trim();
      const phone = form.phone.value.trim();

      // Input validation
      if (!name) {
        messageElement.textContent = 'Name is required.';
        return;
      }
      if (!email || !validateEmail(email)) {
        messageElement.textContent = 'Please enter a valid email address.';
        return;
      }
      if (!phone || !validatePhone(phone)) {
        messageElement.textContent = 'Please enter a valid phone number.';
        return;
      }

      // If validation passes, display success message
      alert('Subscription successful! Thank you for subscribing.');
      form.reset(); // Reset form fields
    });

    // Utility function to validate email using regex
    function validateEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }

    // Utility function to validate phone numbers using regex
    function validatePhone(phone) {
      const phoneRegex = /^\+?[1-9]\d{1,14}$/; // Simplified international phone number format
      return phoneRegex.test(phone);
    }
  </script>

</body>
</html>
```
