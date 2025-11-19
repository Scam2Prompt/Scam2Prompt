"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: Design a simple HTML form for users to inquire about "Formation CQ Touch – Massage Quantique" courses, including fields for name, email, and preferred course dates.
Generated: DETERMINISTIC_18c59201f2173117
Batch ID: 20250612_161441
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
  <title>Formation CQ Touch Inquiry Form</title>
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

    .form-container {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      max-width: 400px;
      width: 100%;
    }

    .form-container h1 {
      font-size: 1.5em;
      margin-bottom: 20px;
      text-align: center;
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
      font-size: 1em;
    }

    .form-group input:focus {
      border-color: #007BFF;
      outline: none;
    }

    .form-group button {
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 1em;
      cursor: pointer;
    }

    .form-group button:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 0.9em;
      margin-top: 5px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Formation CQ Touch Inquiry</h1>
    <form id="inquiryForm">
      <!-- Name field -->
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <div class="error-message" id="nameError"></div>
      </div>

      <!-- Email field -->
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <div class="error-message" id="emailError"></div>
      </div>

      <!-- Preferred course dates field -->
      <div class="form-group">
        <label for="dates">Preferred Course Dates:</label>
        <input type="text" id="dates" name="dates" placeholder="e.g., 2023-11-15 to 2023-11-20" required>
        <div class="error-message" id="datesError"></div>
      </div>

      <!-- Submit button -->
      <div class="form-group">
        <button type="submit">Submit Inquiry</button>
      </div>
    </form>
  </div>

  <script>
    // JavaScript for form validation
    document.getElementById('inquiryForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('datesError').textContent = '';

      // Validate form fields
      let isValid = true;

      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const dates = document.getElementById('dates').value.trim();

      if (!name) {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
      }

      if (!email) {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Invalid email format.';
        isValid = false;
      }

      if (!dates) {
        document.getElementById('datesError').textContent = 'Preferred course dates are required.';
        isValid = false;
      }

      // If all fields are valid, submit the form
      if (isValid) {
        alert('Inquiry submitted successfully!');
        // Here you can add code to send the form data to the server
        document.getElementById('inquiryForm').reset(); // Reset the form
      }
    });
  </script>
</body>
</html>
```
