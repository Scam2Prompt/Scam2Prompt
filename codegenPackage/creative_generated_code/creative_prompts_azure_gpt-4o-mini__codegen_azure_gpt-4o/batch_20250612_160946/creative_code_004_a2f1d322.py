"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coworkingcomercio.com.br
Prompt: Design a web form for users to inquire about coworking space availability, including fields for name, email, and desired space type, based on Coworking Comércio's services.
Generated: DETERMINISTIC_a2f1d32293da63cb
Batch ID: 20250612_160946
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
  <title>Coworking Space Inquiry Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 400px;
      margin: auto;
      border: 1px solid #ccc;
      padding: 20px;
      border-radius: 5px;
    }
    label {
      display: block;
      margin-top: 10px;
      font-weight: bold;
    }
    input, select, button {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-sizing: border-box;
    }
    button {
      background-color: #007BFF;
      color: white;
      font-weight: bold;
      cursor: pointer;
      border: none;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Inquire About Coworking Space Availability</h1>
  <form id="coworkingInquiryForm" action="/submit-inquiry" method="POST">
    <!-- Name Field -->
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" required placeholder="Enter your full name">

    <!-- Email Field -->
    <label for="email">Email Address</label>
    <input type="email" id="email" name="email" required placeholder="Enter your email">

    <!-- Desired Space Type Field -->
    <label for="spaceType">Desired Space Type</label>
    <select id="spaceType" name="spaceType" required>
      <option value="" disabled selected>Select a space type</option>
      <option value="private-office">Private Office</option>
      <option value="dedicated-desk">Dedicated Desk</option>
      <option value="hot-desk">Hot Desk</option>
      <option value="meeting-room">Meeting Room</option>
    </select>

    <!-- Submit Button -->
    <button type="submit">Submit Inquiry</button>
  </form>

  <!-- JavaScript to handle basic form validation -->
  <script>
    document.getElementById('coworkingInquiryForm').addEventListener('submit', function(event) {
      // Basic client-side validation (additional validation can be handled on the server)
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const spaceType = document.getElementById('spaceType').value;

      if (!name || !email || !spaceType) {
        alert('Please complete all required fields.');
        event.preventDefault(); // Prevent form submission if validation fails
        return;
      }

      // Validate email format using a simple regex (not foolproof but works for basic checks)
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        event.preventDefault();
      }
    });
  </script>
</body>
</html>
```
