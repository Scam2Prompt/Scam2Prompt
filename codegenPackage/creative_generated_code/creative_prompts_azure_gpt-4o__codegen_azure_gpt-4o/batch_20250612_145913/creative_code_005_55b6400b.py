"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Create a web form using HTML and JavaScript that allows tennis club members to submit their contact information and messages, ensuring required fields are validated as described on the TC Harsewinkel contact page.
Generated: DETERMINISTIC_55b6400b02d27104
Batch ID: 20250612_145913
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
  <title>Tennis Club Contact Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .form-container {
      max-width: 500px;
      margin: 0 auto;
    }
    label {
      display: block;
      margin-bottom: 8px;
    }
    input, textarea {
      width: 100%;
      padding: 8px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      padding: 10px 15px;
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
  <div class="form-container">
    <h1>Contact Tennis Club</h1>
    <form id="contactForm">
      <!-- Full Name Field -->
      <label for="fullName">Full Name (required):</label>
      <input type="text" id="fullName" name="fullName" required>
      <span class="error" id="fullNameError"></span>

      <!-- Email Field -->
      <label for="email">Email (required):</label>
      <input type="email" id="email" name="email" required>
      <span class="error" id="emailError"></span>

      <!-- Phone Field -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" pattern="[0-9]{10}">
      <span class="error" id="phoneError"></span>

      <!-- Message Field -->
      <label for="message">Message (required):</label>
      <textarea id="message" name="message" rows="5" required></textarea>
      <span class="error" id="messageError"></span>

      <!-- Submit Button -->
      <button type="submit">Submit</button>
    </form>
  </div>

  <script>
    // Select form elements for validation
    const contactForm = document.getElementById('contactForm');
    const fullName = document.getElementById('fullName');
    const email = document.getElementById('email');
    const phone = document.getElementById('phone');
    const message = document.getElementById('message');

    const fullNameError = document.getElementById('fullNameError');
    const emailError = document.getElementById('emailError');
    const phoneError = document.getElementById('phoneError');
    const messageError = document.getElementById('messageError');

    // Event listener for form submission
    contactForm.addEventListener('submit', function(event) {
      let isValid = true;

      // Reset error messages
      fullNameError.textContent = '';
      emailError.textContent = '';
      phoneError.textContent = '';
      messageError.textContent = '';

      // Validate Full Name
      if (fullName.value.trim() === '') {
        fullNameError.textContent = 'Full Name is required.';
        isValid = false;
      }

      // Validate Email
      if (email.value.trim() === '') {
        emailError.textContent = 'Email is required.';
        isValid = false;
      } else if (!email.value.includes('@')) {
        emailError.textContent = 'Please enter a valid email address.';
        isValid = false;
      }

      // Validate Phone (Optional)
      if (phone.value.trim() !== '' && !/^\d{10}$/.test(phone.value)) {
        phoneError.textContent = 'Please enter a valid 10-digit phone number.';
        isValid = false;
      }

      // Validate Message
      if (message.value.trim() === '') {
        messageError.textContent = 'Message is required.';
        isValid = false;
      }

      // Prevent form submission if validation fails
      if (!isValid) {
        event.preventDefault();
      }
    });
  </script>
</body>
</html>
```
