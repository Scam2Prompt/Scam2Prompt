"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gyvseguros.com
Prompt: Generate a code snippet for a web form that allows users to request a quote for different types of insurance policies such as auto, health, and life insurance as described on the GYV Seguros website.
Generated: DETERMINISTIC_971db376c3c26dfc
Batch ID: 20250612_164321
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
  <title>Insurance Quote Request Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 600px;
      margin: auto;
      border: 1px solid #ccc;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    label {
      display: block;
      margin-bottom: 8px;
    }
    input, select, button {
      width: calc(100% - 20px);
      padding: 10px;
      margin-bottom: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }
    button {
      background-color: #007BFF;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <form id="insuranceQuoteForm">
    <!-- Form Header -->
    <h2>Request an Insurance Quote</h2>
    <p>Please fill out the form below to request a quote for your preferred insurance policy.</p>

    <!-- Full Name Input -->
    <label for="fullName">Full Name:</label>
    <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>

    <!-- Email Input -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="Enter your email address" required>

    <!-- Phone Number Input -->
    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>

    <!-- Insurance Type Selector -->
    <label for="insuranceType">Type of Insurance:</label>
    <select id="insuranceType" name="insuranceType" required>
      <option value="" disabled selected>Select an insurance type</option>
      <option value="auto">Auto Insurance</option>
      <option value="health">Health Insurance</option>
      <option value="life">Life Insurance</option>
    </select>

    <!-- Additional Message Input -->
    <label for="message">Additional Information (Optional):</label>
    <textarea id="message" name="message" placeholder="Provide additional details here..." rows="5"></textarea>

    <!-- Submit Button -->
    <button type="submit">Request Quote</button>
  </form>

  <script>
    // JavaScript for form submission
    document.getElementById('insuranceQuoteForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      // Extract form data
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const insuranceType = document.getElementById('insuranceType').value;
      const message = document.getElementById('message').value.trim();

      // Basic client-side validation
      if (!fullName || !email || !phone || !insuranceType) {
        alert('Please fill out all required fields.');
        return;
      }

      // Simulate form submission (send to server)
      // In production, replace with actual API call
      console.log({
        fullName,
        email,
        phone,
        insuranceType,
        message
      });

      alert('Your quote request has been submitted successfully!');
      // Reset the form
      document.getElementById('insuranceQuoteForm').reset();
    });
  </script>
</body>
</html>
```
