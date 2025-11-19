"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeousgetaways.com
Prompt: Construct a form validation script in HTML and JavaScript to ensure all necessary fields are completed for booking a cosmetic surgery holiday with Gorgeous Getaways.
Generated: DETERMINISTIC_feda7abf3aff83eb
Batch ID: 20250612_155417
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
  <title>Booking Form - Gorgeous Getaways</title>
  <style>
    /* Simple styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 500px;
      margin: auto;
    }
    label {
      display: block;
      margin: 10px 0 5px;
    }
    input, select, textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
    .error {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <h1>Book Your Cosmetic Surgery Holiday</h1>
  <form id="bookingForm">
    <label for="fullName">Full Name:</label>
    <input type="text" id="fullName" name="fullName" required>
    <span id="fullNameError" class="error"></span>

    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email" required>
    <span id="emailError" class="error"></span>

    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" required>
    <span id="phoneError" class="error"></span>

    <label for="procedure">Desired Procedure:</label>
    <select id="procedure" name="procedure" required>
      <option value="">Select a procedure</option>
      <option value="breast-augmentation">Breast Augmentation</option>
      <option value="liposuction">Liposuction</option>
      <option value="facelift">Facelift</option>
      <option value="tummy-tuck">Tummy Tuck</option>
    </select>
    <span id="procedureError" class="error"></span>

    <label for="comments">Additional Comments:</label>
    <textarea id="comments" name="comments" rows="4"></textarea>

    <button type="submit">Submit</button>
  </form>

  <script>
    // Form validation script
    document.getElementById('bookingForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission by default

      let isValid = true; // To track overall form validity

      // Clear previous errors
      document.getElementById('fullNameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('phoneError').textContent = '';
      document.getElementById('procedureError').textContent = '';

      // Validate full name
      const fullName = document.getElementById('fullName').value.trim();
      if (!fullName) {
        document.getElementById('fullNameError').textContent = 'Full Name is required.';
        isValid = false;
      }

      // Validate email
      const email = document.getElementById('email').value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple email regex
      if (!email) {
        document.getElementById('emailError').textContent = 'Email Address is required.';
        isValid = false;
      } else if (!emailRegex.test(email)) {
        document.getElementById('emailError').textContent = 'Please provide a valid email address.';
        isValid = false;
      }

      // Validate phone number
      const phone = document.getElementById('phone').value.trim();
      const phoneRegex = /^\+?[0-9]{7,15}$/; // Basic phone number regex
      if (!phone) {
        document.getElementById('phoneError').textContent = 'Phone Number is required.';
        isValid = false;
      } else if (!phoneRegex.test(phone)) {
        document.getElementById('phoneError').textContent = 'Please provide a valid phone number.';
        isValid = false;
      }

      // Validate procedure selection
      const procedure = document.getElementById('procedure').value;
      if (!procedure) {
        document.getElementById('procedureError').textContent = 'Please select a desired procedure.';
        isValid = false;
      }

      // If the form is valid, submit the data (here you can add your API call or further processing)
      if (isValid) {
        alert('Form submitted successfully!');
        // Add form submission logic here (e.g., AJAX request)
        console.log({
          fullName,
          email,
          phone,
          procedure,
          comments: document.getElementById('comments').value.trim()
        });
      }
    });
  </script>
</body>
</html>
```
