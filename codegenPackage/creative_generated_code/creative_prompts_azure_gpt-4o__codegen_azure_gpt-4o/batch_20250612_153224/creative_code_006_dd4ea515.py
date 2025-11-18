"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byamed.net
Prompt: Write code for a responsive form that captures client inquiries, including fields for preferred contact method and service of interest, as seen on ByAmed.net.
Generated: DETERMINISTIC_dd4ea51506828da6
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
  <meta name="description" content="Responsive inquiry form for ByAmed.net">
  <title>Client Inquiry Form</title>
  <style>
    /* General styles */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }

    .form-container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background-color: #ffffff;
      border: 1px solid #ddd;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .form-container h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input, select, textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    textarea {
      resize: vertical;
    }

    .radio-group {
      display: flex;
      gap: 10px;
    }

    .radio-group input {
      margin-right: 5px;
    }

    .submit-btn {
      width: 100%;
      padding: 10px;
      background-color: #007bfc;
      color: #ffffff;
      font-size: 18px;
      font-weight: bold;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .submit-btn:hover {
      background-color: #005bb5;
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
    <h2>Client Inquiry Form</h2>
    <form id="inquiry-form">
      <!-- Full Name -->
      <div class="form-group">
        <label for="full-name">Full Name</label>
        <input type="text" id="full-name" name="full_name" required>
        <span id="name-error" class="error"></span>
      </div>

      <!-- Email -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" required>
        <span id="email-error" class="error"></span>
      </div>

      <!-- Preferred Contact Method -->
      <div class="form-group">
        <label>Preferred Contact Method</label>
        <div class="radio-group">
          <label>
            <input type="radio" name="contact_method" value="Email" required>Email
          </label>
          <label>
            <input type="radio" name="contact_method" value="Phone" required>Phone
          </label>
        </div>
        <span id="contact-error" class="error"></span>
      </div>

      <!-- Service of Interest -->
      <div class="form-group">
        <label for="service-interest">Service of Interest</label>
        <select id="service-interest" name="service_interest" required>
          <option value="">-- Select Service --</option>
          <option value="Consultation">Consultation</option>
          <option value="Treatment">Treatment</option>
          <option value="Follow-up">Follow-up</option>
        </select>
        <span id="service-error" class="error"></span>
      </div>

      <!-- Message -->
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        <span id="message-error" class="error"></span>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="submit-btn">Submit Inquiry</button>
      <div id="form-success" class="success"></div>
    </form>
  </div>

  <script>
    // JavaScript for form validation and submission
    document.getElementById('inquiry-form').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent default form submission

      let hasError = false;

      // Clear previous errors
      document.querySelectorAll('.error').forEach(error => error.textContent = '');
      document.getElementById('form-success').textContent = '';

      // Validation logic
      const fullName = document.getElementById('full-name').value.trim();
      const email = document.getElementById('email').value.trim();
      const contactMethod = document.querySelector('input[name="contact_method"]:checked');
      const serviceInterest = document.getElementById('service-interest').value;
      const message = document.getElementById('message').value.trim();

      if (fullName === '') {
        document.getElementById('name-error').textContent = 'Full name is required.';
        hasError = true;
      }

      if (email === '' || !/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('email-error').textContent = 'Valid email is required.';
        hasError = true;
      }

      if (!contactMethod) {
        document.getElementById('contact-error').textContent = 'Contact method is required.';
        hasError = true;
      }

      if (serviceInterest === '') {
        document.getElementById('service-error').textContent = 'Service of interest is required.';
        hasError = true;
      }

      if (message === '') {
        document.getElementById('message-error').textContent = 'Message is required.';
        hasError = true;
      }

      // If no errors, display success message (simulate submission)
      if (!hasError) {
        document.getElementById('form-success').textContent = 'Inquiry submitted successfully!';
        document.getElementById('inquiry-form').reset(); // Reset form
      }
    });
  </script>
</body>
</html>
```
