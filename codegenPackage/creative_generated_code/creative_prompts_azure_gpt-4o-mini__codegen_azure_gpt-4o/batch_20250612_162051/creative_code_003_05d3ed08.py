"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerfivesolar.com
Prompt: Develop a simple web form that collects user information for solar consultation, similar to the form provided by PowerFive Solar, ensuring it captures property type and roof type.
Generated: DETERMINISTIC_05d3ed08e3c9da22
Batch ID: 20250612_162051
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
  <title>Solar Consultation Form</title>
  <style>
    /* Basic styling for form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .form-container {
      max-width: 500px;
      margin: auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, select, button {
      width: 100%;
      padding: 10px;
      margin: 5px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
    .error {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Solar Consultation Form</h2>
    <form id="solarConsultationForm">
      <!-- Full Name -->
      <div class="form-group">
        <label for="fullName">Full Name</label>
        <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
      </div>

      <!-- Email -->
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>

      <!-- Phone -->
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
      </div>

      <!-- Property Type -->
      <div class="form-group">
        <label for="propertyType">Property Type</label>
        <select id="propertyType" name="propertyType" required>
          <option value="" disabled selected>Select property type</option>
          <option value="residential">Residential</option>
          <option value="commercial">Commercial</option>
          <option value="industrial">Industrial</option>
          <option value="other">Other</option>
        </select>
      </div>

      <!-- Roof Type -->
      <div class="form-group">
        <label for="roofType">Roof Type</label>
        <select id="roofType" name="roofType" required>
          <option value="" disabled selected>Select roof type</option>
          <option value="flat">Flat</option>
          <option value="pitched">Pitched</option>
          <option value="metal">Metal</option>
          <option value="tile">Tile</option>
          <option value="other">Other</option>
        </select>
      </div>

      <!-- Submit Button -->
      <button type="submit">Submit</button>
      <div id="formError" class="error"></div>
    </form>
  </div>

  <!-- JavaScript -->
  <script>
    // Handle form submission
    document.getElementById('solarConsultationForm').addEventListener('submit', function(event) {
      event.preventDefault();

      // Clear previous error message
      const errorDiv = document.getElementById('formError');
      errorDiv.textContent = '';

      try {
        // Gather form data
        const fullName = document.getElementById('fullName').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const propertyType = document.getElementById('propertyType').value.trim();
        const roofType = document.getElementById('roofType').value.trim();

        // Basic validation
        if (!fullName || !email || !phone || !propertyType || !roofType) {
          throw new Error('All fields are required.');
        }

        // Log data to the console (or send it to a server via AJAX)
        console.log({
          fullName: fullName,
          email: email,
          phone: phone,
          propertyType: propertyType,
          roofType: roofType
        });

        // Display success message or redirect (production app might redirect or send data to a server)
        alert('Form submitted successfully!');
        event.target.reset(); // Clear the form after submission
      } catch (error) {
        // Handle validation error
        errorDiv.textContent = error.message;
      }
    });
  </script>
</body>
</html>
```
