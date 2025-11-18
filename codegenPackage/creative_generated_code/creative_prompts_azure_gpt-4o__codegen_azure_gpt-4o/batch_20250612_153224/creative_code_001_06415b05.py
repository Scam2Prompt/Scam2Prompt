"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Generate code to create a contact form for a handyman service website, allowing users to input their name, email, and service request (e.g., plumbing, electrical work, or appliance repair). Include validation for phone numbers like `620 365 080`.
Generated: DETERMINISTIC_06415b0594e23a2e
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
  <title>Handyman Service Contact Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    form {
      max-width: 400px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      background-color: #f9f9f9;
    }

    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }

    input, select, textarea, button {
      width: 100%;
      margin-bottom: 15px;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    button {
      cursor: pointer;
      background-color: #4CAF50;
      color: white;
      font-size: 16px;
      border: none;
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
  <h1>Handyman Service Contact Form</h1>
  <form id="contactForm">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" placeholder="Your name" required>
    <span class="error" id="nameError"></span>

    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your email" required>
    <span class="error" id="emailError"></span>

    <label for="phone">Phone</label>
    <input type="text" id="phone" name="phone" placeholder="e.g., 620 365 080" required>
    <span class="error" id="phoneError"></span>

    <label for="service">Service Request</label>
    <select id="service" name="service" required>
      <option value="">Select a service</option>
      <option value="plumbing">Plumbing</option>
      <option value="electrical">Electrical Work</option>
      <option value="appliance_repair">Appliance Repair</option>
    </select>
    <span class="error" id="serviceError"></span>

    <label for="message">Additional Information</label>
    <textarea id="message" name="message" placeholder="Describe your issue..." rows="4"></textarea>

    <button type="submit">Submit</button>
  </form>

  <script>
    // Validate phone numbers in the format '620 365 080'
    function validatePhone(phone) {
      const phoneRegex = /^\d{3} \d{3} \d{3}$/;
      return phoneRegex.test(phone);
    }

    // Form submission handler
    document.getElementById('contactForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form submission
      let isValid = true;

      // Clear any previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('phoneError').textContent = '';
      document.getElementById('serviceError').textContent = '';

      // Name validation
      const name = document.getElementById('name').value.trim();
      if (!name) {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
      }

      // Email validation
      const email = document.getElementById('email').value.trim();
      if (!email) {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!email.includes('@')) {
        document.getElementById('emailError').textContent = 'Enter a valid email address.';
        isValid = false;
      }

      // Phone validation
      const phone = document.getElementById('phone').value.trim();
      if (!phone) {
        document.getElementById('phoneError').textContent = 'Phone number is required.';
        isValid = false;
      } else if (!validatePhone(phone)) {
        document.getElementById('phoneError').textContent = 'Enter a valid phone number (e.g., 620 365 080).';
        isValid = false;
      }

      // Service validation
      const service = document.getElementById('service').value;
      if (!service) {
        document.getElementById('serviceError').textContent = 'Please select a service.';
        isValid = false;
      }

      // If valid, log the form data (can be sent to a server)
      if (isValid) {
        const formData = {
          name,
          email,
          phone,
          service,
          message: document.getElementById('message').value.trim()
        };
        console.log('Form submitted:', formData);
        alert('Thank you for your request! We will get back to you soon.');
      }
    });
  </script>
</body>
</html>
```
