"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacerealestatevt.com
Prompt: Develop a simple web form using HTML and JavaScript that allows users to sign up for market updates from Pace Real Estate in Northern Vermont.
Generated: DETERMINISTIC_a659aea18619ac2d
Batch ID: 20250612_164213
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
  <title>Sign Up for Market Updates - Pace Real Estate</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }
    form {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }
    h2 {
      text-align: center;
      margin-bottom: 20px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input[type="text"],
    input[type="email"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
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
      font-size: 16px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 14px;
      margin-bottom: 10px;
    }
    .success {
      color: green;
      font-size: 14px;
      margin-top: 10px;
      text-align: center;
    }
  </style>
</head>
<body>
  <form id="signupForm">
    <h2>Sign Up for Market Updates</h2>
    <div class="error" id="errorMessage"></div>
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" placeholder="Enter your full name" required>

    <label for="email">Email Address</label>
    <input type="email" id="email" name="email" placeholder="Enter your email" required>

    <button type="submit">Sign Up</button>
    <div class="success" id="successMessage"></div>
  </form>

  <script>
    // JavaScript code for form validation and submission handling
    document.getElementById('signupForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the form from submitting normally

      const name = document.getElementById('name').value.trim(); // Get and trim name input
      const email = document.getElementById('email').value.trim(); // Get and trim email input
      const errorMessage = document.getElementById('errorMessage'); // Error message container
      const successMessage = document.getElementById('successMessage'); // Success message container

      errorMessage.textContent = ''; // Clear previous error message
      successMessage.textContent = ''; // Clear previous success message

      // Basic validation
      if (name === '' || email === '') {
        errorMessage.textContent = 'Please fill in all required fields.';
        return;
      }

      if (!validateEmail(email)) {
        errorMessage.textContent = 'Please enter a valid email address.';
        return;
      }

      // Simulate successful submission
      successMessage.textContent = 'Thank you for signing up! You will now receive market updates.';
      document.getElementById('signupForm').reset(); // Reset the form
    });

    /**
     * Validates an email address format using regex.
     * @param {string} email - The email address to validate.
     * @returns {boolean} True if valid, false otherwise.
     */
    function validateEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  </script>
</body>
</html>
```
