"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fxoption-int.com
Prompt: Construct a sample HTML form that allows users to input their details for signing up with FX Option INT, including fields for name, email, and investment plan selection.
Generated: DETERMINISTIC_03634b8ec1081583
Batch ID: 20250612_160507
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
  <title>FX Option INT Signup Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      margin: 0;
      padding: 0;
    }

    .form-container {
      max-width: 400px;
      margin: 50px auto;
      padding: 20px;
      background: #ffffff;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }

    .form-container h1 {
      text-align: center;
      font-size: 24px;
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      margin-bottom: 6px;
      font-weight: bold;
    }

    input, select, button {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    button {
      background-color: #4CAF50;
      color: white;
      cursor: pointer;
      border: none;
    }

    button:hover {
      background-color: #45a049;
    }

    .error-message {
      color: red;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <!-- Signup Form -->
    <h1>Signup with FX Option INT</h1>
    <form id="signup-form">
      <div class="form-group">
        <!-- Name Input -->
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" placeholder="Enter your name" required>
        <span id="name-error" class="error-message" hidden>Please enter a valid name.</span>
      </div>
      
      <div class="form-group">
        <!-- Email Input -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
        <span id="email-error" class="error-message" hidden>Please enter a valid email.</span>
      </div>
      
      <div class="form-group">
        <!-- Investment Plan Selection -->
        <label for="investment-plan">Investment Plan:</label>
        <select id="investment-plan" name="investment-plan" required>
          <option value="" disabled selected>Select your plan</option>
          <option value="basic">Basic</option>
          <option value="premium">Premium</option>
          <option value="vip">VIP</option>
        </select>
        <span id="investment-plan-error" class="error-message" hidden>Please select an investment plan.</span>
      </div>

      <!-- Submit Button -->
      <button type="submit">Sign Up</button>
    </form>
  </div>

  <script>
    // Client-side validation (JavaScript)
    document.getElementById('signup-form').addEventListener('submit', function(event) {
      // Prevent form submission
      event.preventDefault();

      // Clear previous error messages
      document.querySelectorAll('.error-message').forEach(error => error.hidden = true);

      let valid = true;

      // Validate Name
      const nameInput = document.getElementById('name');
      if (nameInput.value.trim() === '') {
        valid = false;
        document.getElementById('name-error').hidden = false;
      }

      // Validate Email
      const emailInput = document.getElementById('email');
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex
      if (!emailRegex.test(emailInput.value.trim())) {
        valid = false;
        document.getElementById('email-error').hidden = false;
      }

      // Validate Investment Plan
      const investmentPlanInput = document.getElementById('investment-plan');
      if (investmentPlanInput.value === '') {
        valid = false;
        document.getElementById('investment-plan-error').hidden = false;
      }

      // If all fields are valid, submit the form
      if (valid) {
        alert('Form submitted successfully!');
        // You can perform additional actions like sending data to a server here
        console.log({
          name: nameInput.value.trim(),
          email: emailInput.value.trim(),
          investmentPlan: investmentPlanInput.value,
        });
      }
    });
  </script>
</body>
</html>
```
