"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flammedeauinc.ca
Prompt: Generate a code snippet for a web form that allows users to request a free plumbing quote, including fields for name, phone number, date selection, and zip code.
Generated: DETERMINISTIC_a28ab061bd577f87
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
  <title>Free Plumbing Quote</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f4f4f4;
    }
    .form-container {
      max-width: 500px;
      margin: 0 auto;
      padding: 20px;
      background: #fff;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .form-container h2 {
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
    .form-group input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .form-group input[type="submit"] {
      background-color: #007bff;
      color: white;
      cursor: pointer;
    }
    .form-group input[type="submit"]:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Request a Free Plumbing Quote</h2>
    <form id="plumbing-quote-form" action="/submit-quote" method="POST">
      <!-- Full Name Field -->
      <div class="form-group">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
      </div>
      <!-- Phone Number Field -->
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" 
               pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
        <small>Format: 123-456-7890</small>
      </div>
      <!-- Date Selection Field -->
      <div class="form-group">
        <label for="date">Preferred Date</label>
        <input type="date" id="date" name="date" required>
      </div>
      <!-- ZIP Code Field -->
      <div class="form-group">
        <label for="zip">ZIP Code</label>
        <input type="text" id="zip" name="zip" placeholder="Enter your ZIP code" 
               pattern="[0-9]{5}" required>
        <small>Format: 12345</small>
      </div>
      <!-- Submit Button -->
      <div class="form-group">
        <input type="submit" value="Request Quote">
      </div>
    </form>
  </div>
  <script>
    // Client-side form validation and handling
    document.getElementById('plumbing-quote-form').addEventListener('submit', function (event) {
      try {
        // Example validation logic (can be expanded)
        const phone = document.getElementById('phone').value;
        const zip = document.getElementById('zip').value;
        if (!/^\d{3}-\d{3}-\d{4}$/.test(phone)) {
          alert('Please enter a valid phone number in the format: 123-456-7890');
          event.preventDefault(); // Prevent form submission
        }
        if (!/^\d{5}$/.test(zip)) {
          alert('Please enter a valid ZIP code in the format: 12345');
          event.preventDefault(); // Prevent form submission
        }
      } catch (error) {
        console.error('An error occurred:', error);
        alert('An unexpected error occurred. Please try again later.');
        event.preventDefault(); // Prevent form submission
      }
    });
  </script>
</body>
</html>
```
