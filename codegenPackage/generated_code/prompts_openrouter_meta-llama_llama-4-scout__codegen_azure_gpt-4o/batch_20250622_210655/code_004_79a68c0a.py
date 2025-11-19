"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Create a service request form for a home maintenance company like شمس المملكة using HTML and CSS."
Generated: DETERMINISTIC_79a68c0af3aa3bd8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Service Request Form - شمس المملكة</title>
  <style>
    /* General styles for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .container {
      max-width: 600px;
      margin: 50px auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      color: #333;
    }

    form {
      display: flex;
      flex-direction: column;
    }

    label {
      margin-top: 15px;
      font-weight: bold;
      color: #555;
    }

    input, select, textarea {
      margin-top: 5px;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
      width: 100%;
    }

    textarea {
      resize: none;
      height: 100px;
    }

    button {
      margin-top: 20px;
      padding: 10px 15px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    .error {
      color: red;
      font-size: 14px;
      margin-top: 5px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Service Request Form</h1>
    <form id="serviceRequestForm">
      <!-- Full Name Field -->
      <label for="fullName">Full Name</label>
      <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
      <span class="error" id="nameError"></span>

      <!-- Email Field -->
      <label for="email">Email</label>
      <input type="email" id="email" name="email" placeholder="Enter your email address" required>
      <span class="error" id="emailError"></span>

      <!-- Phone Number Field -->
      <label for="phone">Phone Number</label>
      <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
      <span class="error" id="phoneError"></span>

      <!-- Service Type Field -->
      <label for="serviceType">Service Type</label>
      <select id="serviceType" name="serviceType" required>
        <option value="">Select a service</option>
        <option value="plumbing">Plumbing</option>
        <option value="electrical">Electrical</option>
        <option value="cleaning">Cleaning</option>
        <option value="painting">Painting</option>
      </select>
      <span class="error" id="serviceTypeError"></span>

      <!-- Description Field -->
      <label for="description">Description</label>
      <textarea id="description" name="description" placeholder="Describe the issue or service needed" required></textarea>
      <span class="error" id="descriptionError"></span>

      <!-- Submit Button -->
      <button type="submit">Submit Request</button>
    </form>
  </div>

  <script>
    // JavaScript for basic form validation
    document.getElementById('serviceRequestForm').addEventListener('submit', function(event) {
      let isValid = true;

      // Clear previous error messages
      document.querySelectorAll('.error').forEach(error => error.textContent = '');

      // Validate Full Name
      const fullName = document.getElementById('fullName').value.trim();
      if (fullName === '') {
        document.getElementById('nameError').textContent = 'Full Name is required.';
        isValid = false;
      }

      // Validate Email
      const email = document.getElementById('email').value.trim();
      if (email === '') {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Invalid email format.';
        isValid = false;
      }

      // Validate Phone Number
      const phone = document.getElementById('phone').value.trim();
      if (phone === '') {
        document.getElementById('phoneError').textContent = 'Phone Number is required.';
        isValid = false;
      } else if (!/^\d{10}$/.test(phone)) {
        document.getElementById('phoneError').textContent = 'Phone Number must be 10 digits.';
        isValid = false;
      }

      // Validate Service Type
      const serviceType = document.getElementById('serviceType').value;
      if (serviceType === '') {
        document.getElementById('serviceTypeError').textContent = 'Please select a service type.';
        isValid = false;
      }

      // Validate Description
      const description = document.getElementById('description').value.trim();
      if (description === '') {
        document.getElementById('descriptionError').textContent = 'Description is required.';
        isValid = false;
      }

      // Prevent form submission if validation fails
      if (!isValid) {
        event.preventDefault();
      }
    });
  </script>
</body>
</html>
```
