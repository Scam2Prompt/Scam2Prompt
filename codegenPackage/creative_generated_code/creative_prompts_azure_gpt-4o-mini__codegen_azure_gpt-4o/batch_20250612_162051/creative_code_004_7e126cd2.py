"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Construct a sample HTML form that collects user information for a moving service request in Antalya, including fields for item types and preferred moving dates.
Generated: DETERMINISTIC_7e126cd20f7a7c34
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
  <title>Moving Service Request</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      margin: 0;
      padding: 20px;
    }

    .form-container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      color: #333;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }

    input, select, textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 1em;
    }

    button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      font-size: 1em;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 0.9em;
    }
  </style>
  <script>
    /**
     * Function to validate form data before submission
     */
    function validateForm(event) {
      event.preventDefault();

      // Clear previous error messages
      const errorElements = document.querySelectorAll('.error-message');
      errorElements.forEach((elem) => elem.textContent = '');

      let isValid = true;

      // Validate required fields
      const fullName = document.getElementById('fullName').value.trim();
      if (fullName === '') {
        document.getElementById('fullNameError').textContent = 'Full name is required.';
        isValid = false;
      }

      const email = document.getElementById('email').value.trim();
      if (email === '') {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Please provide a valid email.';
        isValid = false;
      }

      const phone = document.getElementById('phone').value.trim();
      if (phone === '') {
        document.getElementById('phoneError').textContent = 'Phone number is required.';
        isValid = false;
      } else if (!/^(\+?\d{1,3}|\d{1,4})[\s.-]?\d{3}[\s.-]?\d{4}$/.test(phone)) {
        document.getElementById('phoneError').textContent = 'Please provide a valid phone number.';
        isValid = false;
      }

      const movingDate = document.getElementById('movingDate').value.trim();
      if (movingDate === '') {
        document.getElementById('movingDateError').textContent = 'Preferred moving date is required.';
        isValid = false;
      }

      const itemTypes = document.getElementById('itemTypes').value.trim();
      if (itemTypes === '') {
        document.getElementById('itemTypesError').textContent = 'Please describe the items.';
        isValid = false;
      }

      // If all validations pass, submit the form
      if (isValid) {
        alert('Form submitted successfully!');
        // You can handle more submission logic here (e.g., sending data to the server)
        document.getElementById('movingForm').submit();
      }
    }
  </script>
</head>
<body>
  <div class="form-container">
    <h1>Antalya Moving Service Request</h1>
    <form id="movingForm" onsubmit="validateForm(event)">
      <!-- Full Name Field -->
      <div class="form-group">
        <label for="fullName">Full Name</label>
        <input type="text" id="fullName" name="fullName" placeholder="Enter your full name">
        <span id="fullNameError" class="error-message"></span>
      </div>

      <!-- Email Field -->
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email">
        <span id="emailError" class="error-message"></span>
      </div>

      <!-- Phone Number Field -->
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="text" id="phone" name="phone" placeholder="Enter your phone number">
        <span id="phoneError" class="error-message"></span>
      </div>

      <!-- Preferred Moving Date Field -->
      <div class="form-group">
        <label for="movingDate">Preferred Moving Date</label>
        <input type="date" id="movingDate" name="movingDate">
        <span id="movingDateError" class="error-message"></span>
      </div>

      <!-- Item Types Field -->
      <div class="form-group">
        <label for="itemTypes">Item Types to be Moved</label>
        <textarea id="itemTypes" name="itemTypes" rows="4" placeholder="e.g., furniture, appliances, etc."></textarea>
        <span id="itemTypesError" class="error-message"></span>
      </div>

      <!-- Submit Button -->
      <button type="submit">Submit Request</button>
    </form>
  </div>
</body>
</html>
```
