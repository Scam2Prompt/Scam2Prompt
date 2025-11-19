"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueseanice.com
Prompt: Develop a simple HTML form that allows users to submit inquiries about Blue Sea K-Beauty's skin care products, including fields for customer type (individual or spa owner).
Generated: DETERMINISTIC_2f6542180df32c65
Batch ID: 20250612_155421
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
  <title>Blue Sea K-Beauty Inquiry Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }
    .container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background: white;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 {
      text-align: center;
      color: #333;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, select, textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: white;
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
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Inquiry Form</h1>
    <form id="inquiryForm" action="/submit-inquiry" method="POST">
      
      <!-- Full Name Field -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" required>
      
      <!-- Email Field -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" required>
      
      <!-- Customer Type Field -->
      <label for="customerType">Customer Type:</label>
      <select id="customerType" name="customerType" required>
        <option value="" disabled selected>Select one</option>
        <option value="individual">Individual</option>
        <option value="spaOwner">Spa Owner</option>
      </select>
      
      <!-- Message Field -->
      <label for="message">Your Inquiry:</label>
      <textarea id="message" name="message" rows="6" required></textarea>
      
      <!-- Submit Button -->
      <button type="submit">Submit Inquiry</button>
    </form>
    <p class="error" id="errorMessage"></p>
  </div>

  <script>
    // JavaScript for form validation
    document.getElementById('inquiryForm').addEventListener('submit', function(event) {
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const customerType = document.getElementById('customerType').value;
      const message = document.getElementById('message').value.trim();
      const errorMessage = document.getElementById('errorMessage');

      // Clear previous error message
      errorMessage.textContent = '';

      // Basic validation
      if (!fullName || !email || !customerType || !message) {
        event.preventDefault();
        errorMessage.textContent = 'Please fill out all fields before submitting.';
      }
    });
  </script>
</body>
</html>
```
