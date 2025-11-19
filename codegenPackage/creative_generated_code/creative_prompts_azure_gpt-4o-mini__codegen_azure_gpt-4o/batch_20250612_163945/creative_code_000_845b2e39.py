"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cloud-telephonie.net
Prompt: Generate a code snippet for a web form that collects user information like name, email, and phone number for a custom telephone quote.
Generated: DETERMINISTIC_845b2e39a393f245
Batch ID: 20250612_163945
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
  <title>Custom Telephone Quote</title>
  <style>
    /* Simple CSS for styling the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
    }
    form {
      max-width: 400px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input[type="text"], input[type="email"], input[type="tel"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      display: inline-block;
      padding: 10px 20px;
      color: #fff;
      background-color: #007BFF;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>

  <form id="quoteForm">
    <!-- Form Title -->
    <h2>Request a Custom Telephone Quote</h2>

    <!-- Name Field -->
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" required placeholder="Enter your full name">

    <!-- Email Field -->
    <label for="email">Email Address</label>
    <input type="email" id="email" name="email" required placeholder="Enter your email address">

    <!-- Phone Field -->
    <label for="phone">Phone Number</label>
    <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

    <!-- Submit Button -->
    <button type="submit">Get Quote</button>
  </form>

  <script>
    // JavaScript for form submission handling
    document.getElementById('quoteForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form from submitting traditionally

      // Collect form data
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();

      // Simple validation example
      if (!name || !email || !phone) {
        alert('Please fill out all fields.');
        return;
      }

      // Simulate successful form submission
      alert(`Thank you, ${name}! Your custom quote request has been submitted.`);
      
      // Normally, you would send the data to a server here, e.g., via fetch or XMLHttpRequest
      // Example placeholder for server logic:
      // fetch('/submit-quote', {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json' },
      //   body: JSON.stringify({ name, email, phone })
      // })
      // .then(response => response.json())
      // .then(data => console.log('Success:', data))
      // .catch(error => console.error('Error:', error));
    });
  </script>

</body>
</html>
```
