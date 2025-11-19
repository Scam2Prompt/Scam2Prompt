"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Generate a code snippet for a web form that allows users to request a free measure and quote for cabinetry services, including fields for name, phone, email, and message.
Generated: DETERMINISTIC_56efb21599f66dce
Batch ID: 20250612_164115
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
  <title>Free Measure and Quote</title>
  <style>
    /* Basic styling for form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f9f9f9;
    }
    .form-container {
      max-width: 500px;
      margin: auto;
      background: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
      border-radius: 3px;
    }
    .form-group textarea {
      resize: vertical;
      height: 100px;
    }
    .submit-btn {
      display: inline-block;
      background-color: #007BFF;
      color: #fff;
      border: none;
      padding: 10px 20px;
      cursor: pointer;
      border-radius: 3px;
      text-align: center;
    }
    .submit-btn:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Request a Free Quote</h1>
    <form id="quoteForm">
      <!-- Name field -->
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
      </div>
      
      <!-- Phone field -->
      <div class="form-group">
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required
               title="Please enter a 10-digit phone number">
      </div>
      
      <!-- Email field -->
      <div class="form-group">
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required>
      </div>
      
      <!-- Message field -->
      <div class="form-group">
        <label for="message">Message:</label>
        <textarea id="message" name="message" placeholder="Tell us about your cabinetry needs..." required></textarea>
      </div>
      
      <!-- Submit button -->
      <button type="submit" class="submit-btn">Submit</button>
    </form>
  </div>

  <script>
    // Attach event listener to form submission
    document.getElementById('quoteForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission behavior

      // Gather form input values
      const name = document.getElementById('name').value;
      const phone = document.getElementById('phone').value;
      const email = document.getElementById('email').value;
      const message = document.getElementById('message').value;

      // Validate form fields (basic example)
      if (!name || !phone || !email || !message) {
        alert('All fields are required!');
        return;
      }

      // Simulate form submission (Replace this with actual API call or backend logic)
      alert(`Thank you, ${name}! Your request has been submitted successfully.`);
      
      // Clear the form after submission
      document.getElementById('quoteForm').reset();
    });
  </script>
</body>
</html>
```
