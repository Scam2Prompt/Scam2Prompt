"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Write code to create a "Contact Us" form for a church website, including fields for name, email, message, and a dropdown for selecting the type of inquiry, inspired by ChurchProWeb's contact page design.
Generated: DETERMINISTIC_1e196df2c2357826
Batch ID: 20250612_153224
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
  <title>Contact Us - Church Website</title>
  <style>
    /* Basic styling for the contact form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }

    .contact-form-container {
      max-width: 600px;
      margin: 50px auto;
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
    }

    label {
      display: block;
      margin-bottom: 6px;
      font-weight: bold;
    }

    input,
    select,
    textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
      font-size: 16px;
    }

    button {
      width: 100%;
      padding: 10px;
      background-color: #5cb85c;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover {
      background-color: #4cae4c;
    }

    .error-message {
      color: red;
      font-size: 14px;
    }

    .success-message {
      color: green;
      font-size: 14px;
    }
  </style>
</head>

<body>
  <div class="contact-form-container">
    <h1>Contact Us</h1>
    <form id="contactForm">
      <!-- Name field -->
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" placeholder="Your full name" required>
      <span class="error-message" id="nameError"></span>

      <!-- Email field -->
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" placeholder="Your email address" required>
      <span class="error-message" id="emailError"></span>

      <!-- Type of inquiry dropdown -->
      <label for="inquiryType">Type of Inquiry:</label>
      <select id="inquiryType" name="inquiryType" required>
        <option value="">Select an option</option>
        <option value="General">General Inquiry</option>
        <option value="Prayer">Prayer Request</option>
        <option value="Event">Event Information</option>
        <option value="Volunteer">Volunteering</option>
      </select>
      <span class="error-message" id="inquiryError"></span>

      <!-- Message field -->
      <label for="message">Message:</label>
      <textarea id="message" name="message" rows="5" placeholder="Type your message here..." required></textarea>
      <span class="error-message" id="messageError"></span>

      <!-- Submit button -->
      <button type="submit">Submit</button>
    </form>
    <div id="formResponse"></div>
  </div>

  <script>
    // Handle form submission
    document.getElementById('contactForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent default form submission

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('inquiryError').textContent = '';
      document.getElementById('messageError').textContent = '';

      let hasError = false;

      // Basic validation
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const inquiryType = document.getElementById('inquiryType').value;
      const message = document.getElementById('message').value.trim();

      if (!name) {
        document.getElementById('nameError').textContent = 'Name is required.';
        hasError = true;
      }

      if (!email || !/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Valid email is required.';
        hasError = true;
      }

      if (!inquiryType) {
        document.getElementById('inquiryError').textContent = 'Please select an inquiry type.';
        hasError = true;
      }

      if (!message) {
        document.getElementById('messageError').textContent = 'Message cannot be empty.';
        hasError = true;
      }

      // If there are no errors, simulate successful submission
      if (!hasError) {
        document.getElementById('formResponse').innerHTML =
          '<p class="success-message">Thank you for contacting us! We will get back to you soon.</p>';
        document.getElementById('contactForm').reset(); // Reset form fields
      }
    });
  </script>
</body>

</html>
```
