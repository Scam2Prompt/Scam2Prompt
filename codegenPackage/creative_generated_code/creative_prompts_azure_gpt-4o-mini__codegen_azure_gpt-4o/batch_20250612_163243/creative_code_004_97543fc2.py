"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Write a sample HTML form for an online store that collects user information for ordering diving equipment, inspired by the registration process on acula.com.ua.
Generated: DETERMINISTIC_97543fc2f81719b4
Batch ID: 20250612_163243
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
  <title>Diving Equipment Order Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 500px;
      margin: auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
    }
    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }
    input, select, textarea, button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    button {
      background-color: #007BFF;
      color: white;
      font-size: 16px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 14px;
      margin-bottom: 15px;
    }
  </style>
</head>
<body>

  <h1>Order Diving Equipment</h1>
  <form id="orderForm">
    <!-- Error message container -->
    <div id="errorMsg" class="error" style="display: none;"></div>

    <!-- Collect user's personal information -->
    <label for="fullName">Full Name:</label>
    <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>

    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email" placeholder="Enter your email address" required>

    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>

    <!-- Collect shipping details -->
    <label for="address">Shipping Address:</label>
    <textarea id="address" name="address" placeholder="Enter your shipping address" rows="3" required></textarea>

    <label for="city">City:</label>
    <input type="text" id="city" name="city" placeholder="Enter your city" required>

    <label for="country">Country:</label>
    <select id="country" name="country" required>
      <option value="">Select your country</option>
      <option value="US">United States</option>
      <option value="CA">Canada</option>
      <option value="UK">United Kingdom</option>
      <option value="AU">Australia</option>
      <option value="UA">Ukraine</option>
      <!-- Add more countries as needed -->
    </select>

    <!-- Collect details about the diving equipment -->
    <label for="equipment">Diving Equipment:</label>
    <textarea id="equipment" name="equipment" placeholder="List the diving equipment you want to order" rows="5" required></textarea>

    <label for="quantity">Quantity:</label>
    <input type="number" id="quantity" name="quantity" placeholder="Enter quantity" min="1" required>

    <!-- Submit button -->
    <button type="submit">Place Order</button>
  </form>

  <script>
    // JavaScript for basic form validation
    document.getElementById('orderForm').addEventListener('submit', function(event) {
      const errorMsg = document.getElementById('errorMsg');
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const address = document.getElementById('address').value.trim();
      const city = document.getElementById('city').value.trim();
      const country = document.getElementById('country').value;
      const equipment = document.getElementById('equipment').value.trim();
      const quantity = document.getElementById('quantity').value;

      // Clear previous error message
      errorMsg.textContent = '';
      errorMsg.style.display = 'none';

      // Validate form fields
      if (!fullName || !email || !phone || !address || !city || !country || !equipment || !quantity || quantity <= 0) {
        event.preventDefault();
        errorMsg.textContent = 'Please fill out all fields correctly.';
        errorMsg.style.display = 'block';
      }
    });
  </script>

</body>
</html>
```
