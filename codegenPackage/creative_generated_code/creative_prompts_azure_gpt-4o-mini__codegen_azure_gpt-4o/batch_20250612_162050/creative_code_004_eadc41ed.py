"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nellyservis.sk
Prompt: Construct a simple HTML form for customers to submit their requirements for window and door installations, similar to the request process at NellyServis.
Generated: DETERMINISTIC_eadc41ed7c9100f2
Batch ID: 20250612_162050
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
  <title>Window and Door Installation Request</title>
  <style>
    /* Styling for form */
    body {
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      margin: 0;
      padding: 20px;
    }
    .form-container {
      max-width: 600px;
      margin: auto;
      background: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    h2 {
      text-align: center;
      color: #333;
    }
    label {
      display: block;
      margin: 10px 0 5px;
      color: #555;
    }
    input, textarea, select, button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }
    button {
      background-color: #007BFF;
      color: #fff;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error-message {
      color: red;
      font-size: 0.875em;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Window and Door Installation Request Form</h2>
    <form id="installationRequestForm" action="/submit-request" method="POST">
      <!-- Customer Name -->
      <label for="name">Your Name:</label>
      <input type="text" id="name" name="name" placeholder="Enter your name" required>
      
      <!-- Customer Email -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email" required>
      
      <!-- Customer Phone -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
      
      <!-- Installation Type -->
      <label for="installationType">Type of Installation:</label>
      <select id="installationType" name="installationType" required>
        <option value="" disabled selected>Select an option</option>
        <option value="windows">Windows</option>
        <option value="doors">Doors</option>
        <option value="both">Both</option>
      </select>
      
      <!-- Requirements -->
      <label for="requirements">Additional Details / Requirements:</label>
      <textarea id="requirements" name="requirements" rows="4" placeholder="Describe any specific requirements or details here"></textarea>
      
      <!-- Submit Button -->
      <button type="submit">Submit Request</button>
      
      <!-- Error Message Area -->
      <div id="errorMessage" class="error-message"></div>
    </form>
  </div>

  <!-- Optional JavaScript for form validation -->
  <script>
    document.getElementById('installationRequestForm').addEventListener('submit', function(event) {
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const installationType = document.getElementById('installationType').value;
      const errorMessage = document.getElementById('errorMessage');

      // Clear previous error message
      errorMessage.textContent = '';

      // Basic validation
      if (!name || !email || !phone || !installationType) {
        errorMessage.textContent = 'Please fill in all required fields.';
        event.preventDefault(); // Prevent form submission
      }
    });
  </script>
</body>
</html>
```
