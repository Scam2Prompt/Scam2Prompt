"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Construct a simple HTML form for users to get quotes on wire mesh products, similar to the "Get Quote" feature on baochuanco.com.
Generated: DETERMINISTIC_3cd9001e8fa016ba
Batch ID: 20250612_160507
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
  <title>Wire Mesh Quote Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f4f4f4;
    }

    .form-container {
      max-width: 600px;
      margin: 0 auto;
      background: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .form-container h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }

    .form-group input, .form-group select, .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
    }

    .form-group textarea {
      resize: vertical;
    }

    .form-group select {
      background-color: #fff;
    }

    .form-group button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    .form-group button:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 12px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Get a Quote</h1>
    <form id="quoteForm" action="/submit-quote" method="POST">
      <!-- User Name Field -->
      <div class="form-group">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required>
        <div id="nameError" class="error-message"></div>
      </div>

      <!-- User Email Field -->
      <div class="form-group">
        <label for="email">Your Email</label>
        <input type="email" id="email" name="email" required>
        <div id="emailError" class="error-message"></div>
      </div>

      <!-- User Phone Number Field -->
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="e.g., +123456789" required>
        <div id="phoneError" class="error-message"></div>
      </div>

      <!-- Product Type Dropdown -->
      <div class="form-group">
        <label for="product">Type of Wire Mesh</label>
        <select id="product" name="product" required>
          <option value="">-- Select a Product --</option>
          <option value="galvanized">Galvanized Wire Mesh</option>
          <option value="welded">Welded Wire Mesh</option>
          <option value="stainless">Stainless Steel Wire Mesh</option>
          <option value="chain">Chain Link Fence</option>
        </select>
        <div id="productError" class="error-message"></div>
      </div>

      <!-- Quantity Field -->
      <div class="form-group">
        <label for="quantity">Quantity (in meters)</label>
        <input type="number" id="quantity" name="quantity" min="1" required>
        <div id="quantityError" class="error-message"></div>
      </div>

      <!-- Additional Details Field -->
      <div class="form-group">
        <label for="details">Additional Details</label>
        <textarea id="details" name="details" rows="4" placeholder="Provide any additional information..."></textarea>
      </div>

      <!-- Submit Button -->
      <div class="form-group">
        <button type="submit">Get Quote</button>
      </div>
    </form>
  </div>

  <script>
    // Basic client-side validation
    document.getElementById('quoteForm').addEventListener('submit', function (event) {
      let isValid = true;

      // Clear all errors
      document.querySelectorAll('.error-message').forEach(errorElem => errorElem.textContent = '');

      // Validate Name
      const name = document.getElementById('name').value.trim();
      if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
      }

      // Validate Email
      const email = document.getElementById('email').value.trim();
      if (email === '') {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Enter a valid email address.';
        isValid = false;
      }

      // Validate Phone
      const phone = document.getElementById('phone').value.trim();
      if (phone === '') {
        document.getElementById('phoneError').textContent = 'Phone number is required.';
        isValid = false;
      }

      // Validate Product Type
      const product = document.getElementById('product').value;
      if (product === '') {
        document.getElementById('productError').textContent = 'Please select a product.';
        isValid = false;
      }

      // Validate Quantity
      const quantity = document.getElementById('quantity').value.trim();
      if (quantity === '' || parseInt(quantity) <= 0) {
        document.getElementById('quantityError').textContent = 'Enter a valid quantity greater than 0.';
        isValid = false;
      }

      if (!isValid) {
        event.preventDefault(); // Prevent form submission
      }
    });
  </script>
</body>
</html>
```
