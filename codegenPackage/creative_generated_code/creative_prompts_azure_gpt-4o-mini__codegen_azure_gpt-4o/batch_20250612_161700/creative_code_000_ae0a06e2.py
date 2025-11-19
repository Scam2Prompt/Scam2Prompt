"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mycoastalroofing.com
Prompt: Generate a code snippet for a web form that allows users to request a free roofing inspection from Coastal Roofing & Waterproofing.
Generated: DETERMINISTIC_ae0a06e22b2bff75
Batch ID: 20250612_161700
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
  <title>Free Roofing Inspection - Coastal Roofing & Waterproofing</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f4f4f9;
    }

    form {
      max-width: 500px;
      margin: 0 auto;
      background: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      color: #333333;
    }

    label {
      display: block;
      margin-top: 15px;
      font-weight: bold;
    }

    input, textarea, button {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border: 1px solid #cccccc;
      border-radius: 4px;
    }

    button {
      background-color: #007bff;
      color: #ffffff;
      border: none;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    .error {
      color: red;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <h1>Request a Free Roofing Inspection</h1>
  <form id="inspectionForm">
    <!-- Input for User's Name -->
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" placeholder="Enter your full name" required>
    <span class="error" id="nameError"></span>
    
    <!-- Input for User's Email -->
    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email" placeholder="Enter your email address" required>
    <span class="error" id="emailError"></span>
    
    <!-- Input for Phone Number -->
    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
    <span class="error" id="phoneError"></span>
    
    <!-- Textarea for Additional Information -->
    <label for="message">Additional Information:</label>
    <textarea id="message" name="message" rows="4" placeholder="Enter additional details (optional)"></textarea>
    
    <!-- Submit Button -->
    <button type="submit">Submit Request</button>
    <span class="error" id="formError"></span>
  </form>

  <script>
    // JavaScript for form validation and submission
    document.getElementById('inspectionForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form from submitting normally
      
      // Clear previous errors
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('phoneError').textContent = '';
      document.getElementById('formError').textContent = '';
      
      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      
      let isValid = true;
      
      // Validate name
      if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
      }
      
      // Validate email format
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        document.getElementById('emailError').textContent = 'Invalid email format.';
        isValid = false;
      }
      
      // Validate phone format (basic validation)
      const phoneRegex = /^[0-9\-+() ]{7,15}$/;
      if (!phoneRegex.test(phone)) {
        document.getElementById('phoneError').textContent = 'Invalid phone number.';
        isValid = false;
      }
      
      // If all validations pass, simulate form submission
      if (isValid) {
        alert('Thank you for your request! Our team will contact you shortly.');
        // Reset form fields
        document.getElementById('inspectionForm').reset();
      } else {
        document.getElementById('formError').textContent = 'Please fix the errors above and try again.';
      }
    });
  </script>
</body>
</html>
```
