"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Generate a code snippet for a web form that allows users to submit their property information for a cash offer on their house, similar to the form on Metis Assets' website.
Generated: DETERMINISTIC_d49bfe253521700f
Batch ID: 20250612_162504
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
  <title>Property Information Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .form-container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
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
      margin-bottom: 5px;
      font-weight: bold;
    }
    .form-group input, .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .form-group textarea {
      resize: vertical;
    }
    .form-group button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    .form-group button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Get a Cash Offer</h1>
    <form id="propertyForm">
      <!-- Property Address -->
      <div class="form-group">
        <label for="address">Property Address</label>
        <input type="text" id="address" name="address" placeholder="Enter property address" required>
      </div>
      <!-- Owner Name -->
      <div class="form-group">
        <label for="ownerName">Owner Name</label>
        <input type="text" id="ownerName" name="ownerName" placeholder="Enter your name" required>
      </div>
      <!-- Contact Email -->
      <div class="form-group">
        <label for="email">Contact Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>
      <!-- Contact Phone -->
      <div class="form-group">
        <label for="phone">Contact Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
      </div>
      <!-- Property Details -->
      <div class="form-group">
        <label for="details">Property Details</label>
        <textarea id="details" name="details" rows="4" placeholder="Provide additional details about the property"></textarea>
      </div>
      <!-- Submit Button -->
      <div class="form-group">
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>

  <script>
    // JavaScript to handle form submission
    document.getElementById('propertyForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      // Collect form data
      const formData = {
        address: document.getElementById('address').value,
        ownerName: document.getElementById('ownerName').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        details: document.getElementById('details').value,
      };

      // Basic validation
      if (!formData.address || !formData.ownerName || !formData.email || !formData.phone) {
        alert('Please fill out all required fields.');
        return;
      }

      // Simulate form submission (replace with actual API call in production)
      console.log('Form submitted:', formData);
      alert('Thank you! Your property information has been submitted.');
      
      // Reset the form
      document.getElementById('propertyForm').reset();
    });
  </script>
</body>
</html>
```
