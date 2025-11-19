"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Generate a code snippet for a web form that allows users to request a roofing estimate, incorporating fields for name, address, phone number, and type of roofing service (e.g., new roof, repairs).
Generated: DETERMINISTIC_38c0a31a505620f4
Batch ID: 20250612_163308
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
  <title>Roofing Estimate Request</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      padding: 0;
      background-color: #f4f4f9;
    }
    .form-container {
      max-width: 500px;
      margin: 0 auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .form-container h2 {
      margin-bottom: 20px;
      text-align: center;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input[type="text"],
    input[type="tel"],
    select,
    button {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }
    button {
      background-color: #007BFF;
      color: #fff;
      font-size: 16px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 0.9em;
      margin-top: 5px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Roofing Estimate Request</h2>
    <form id="roofing-estimate-form">
      <!-- Name field -->
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <div class="error" id="name-error"></div>
      </div>

      <!-- Address field -->
      <div class="form-group">
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required>
        <div class="error" id="address-error"></div>
      </div>

      <!-- Phone number field -->
      <div class="form-group">
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required>
        <div class="error" id="phone-error">Please enter a valid 10-digit phone number.</div>
      </div>

      <!-- Type of roofing service field -->
      <div class="form-group">
        <label for="service-type">Type of Roofing Service:</label>
        <select id="service-type" name="service-type" required>
          <option value="">-- Select Service Type --</option>
          <option value="new-roof">New Roof</option>
          <option value="repairs">Repairs</option>
          <option value="inspection">Inspection</option>
        </select>
        <div class="error" id="service-type-error"></div>
      </div>

      <!-- Submit button -->
      <div class="form-group">
        <button type="submit">Request Estimate</button>
      </div>
    </form>
  </div>

  <script>
    // JavaScript to handle form validation and submission
    document.getElementById('roofing-estimate-form').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission
      
      let isValid = true; // Track if the form is valid

      // Clear previous errors
      document.getElementById('name-error').textContent = '';
      document.getElementById('address-error').textContent = '';
      document.getElementById('phone-error').textContent = '';
      document.getElementById('service-type-error').textContent = '';

      // Validate the name field
      const nameField = document.getElementById('name');
      if (!nameField.value.trim()) {
        document.getElementById('name-error').textContent = 'Name is required.';
        isValid = false;
      }

      // Validate the address field
      const addressField = document.getElementById('address');
      if (!addressField.value.trim()) {
        document.getElementById('address-error').textContent = 'Address is required.';
        isValid = false;
      }

      // Validate the phone field
      const phoneField = document.getElementById('phone');
      if (!phoneField.value.match(/^[0-9]{10}$/)) {
        document.getElementById('phone-error').textContent = 'Phone number must be 10 digits.';
        isValid = false;
      }

      // Validate the service type field
      const serviceTypeField = document.getElementById('service-type');
      if (!serviceTypeField.value) {
        document.getElementById('service-type-error').textContent = 'Please select a service type.';
        isValid = false;
      }

      // If the form is valid, simulate form submission
      if (isValid) {
        alert('Form submitted successfully!');
        // Here, you can send the form data to a server via AJAX or other methods
        console.log({
          name: nameField.value,
          address: addressField.value,
          phone: phoneField.value,
          typeOfService: serviceTypeField.value
        });
        // Reset the form
        document.getElementById('roofing-estimate-form').reset();
      }
    });
  </script>
</body>
</html>
```
