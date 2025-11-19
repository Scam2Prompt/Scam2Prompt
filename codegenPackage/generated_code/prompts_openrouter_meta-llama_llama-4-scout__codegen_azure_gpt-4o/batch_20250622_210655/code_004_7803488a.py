"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Create a web form using HTML and JavaScript that allows users to request a free consultation and price estimate for title insurance services, similar to the one provided on Superior Title Montana's website.
Generated: DETERMINISTIC_7803488aad2d092d
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
  <title>Title Insurance Consultation Form</title>
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
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      color: #333;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input, textarea, button {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
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

    .error {
      color: red;
      font-size: 14px;
    }

    .success {
      color: green;
      font-size: 16px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Request Free Consultation</h1>
    <form id="consultationForm">
      <div class="form-group">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
        <span class="error" id="nameError"></span>
      </div>
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email address" required>
        <span class="error" id="emailError"></span>
      </div>
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
        <span class="error" id="phoneError"></span>
      </div>
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="4" placeholder="Describe your needs" required></textarea>
        <span class="error" id="messageError"></span>
      </div>
      <button type="submit">Submit Request</button>
      <div class="success" id="successMessage"></div>
    </form>
  </div>

  <script>
    // JavaScript for form validation and submission
    document.getElementById('consultationForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form from submitting normally

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('phoneError').textContent = '';
      document.getElementById('messageError').textContent = '';
      document.getElementById('successMessage').textContent = '';

      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const message = document.getElementById('message').value.trim();

      let isValid = true;

      // Validate name
      if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
      }

      // Validate email
      if (email === '') {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Invalid email format.';
        isValid = false;
      }

      // Validate phone
      if (phone === '') {
        document.getElementById('phoneError').textContent = 'Phone number is required.';
        isValid = false;
      } else if (!/^\d{10}$/.test(phone)) {
        document.getElementById('phoneError').textContent = 'Invalid phone number format.';
        isValid = false;
      }

      // Validate message
      if (message === '') {
        document.getElementById('messageError').textContent = 'Message is required.';
        isValid = false;
      }

      // If all fields are valid, show success message
      if (isValid) {
        document.getElementById('successMessage').textContent = 'Your request has been submitted successfully!';
        // Optionally, you can send the data to a server using fetch or XMLHttpRequest here
        // Example:
        // fetch('/submit', {
        //   method: 'POST',
        //   headers: { 'Content-Type': 'application/json' },
        //   body: JSON.stringify({ name, email, phone, message })
        // }).then(response => response.json()).then(data => console.log(data));
      }
    });
  </script>
</body>
</html>
```
