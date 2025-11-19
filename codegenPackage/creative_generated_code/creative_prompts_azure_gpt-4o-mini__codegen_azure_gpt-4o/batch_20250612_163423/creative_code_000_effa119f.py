"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Generate a code snippet for a web form that allows users to request a consultation with a personal injury law firm, including fields for name, contact information, and type of accident (e.g., car, motorcycle, pedestrian).
Generated: DETERMINISTIC_effa119fb6c093f9
Batch ID: 20250612_163423
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
  <title>Consultation Request Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 400px;
      margin: auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, select, textarea, button {
      width: 100%;
      margin-bottom: 15px;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      font-size: 16px;
      cursor: pointer;
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

  <h1>Request a Consultation</h1>
  <form id="consultation-form">
    <!-- Name field -->
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" placeholder="Enter your full name" required>
    <span class="error-message" id="name-error"></span>

    <!-- Contact Information field -->
    <label for="contact">Contact Information</label>
    <input type="email" id="contact" name="contact" placeholder="Enter your email or phone number" required>
    <span class="error-message" id="contact-error"></span>

    <!-- Type of accident field -->
    <label for="accident-type">Type of Accident</label>
    <select id="accident-type" name="accidentType" required>
      <option value="">Select an option</option>
      <option value="car">Car Accident</option>
      <option value="motorcycle">Motorcycle Accident</option>
      <option value="pedestrian">Pedestrian Accident</option>
    </select>
    <span class="error-message" id="accident-type-error"></span>

    <!-- Submit button -->
    <button type="submit">Submit</button>
  </form>

  <script>
    /**
     * JavaScript to handle form submission and basic validation
     */
    document.getElementById('consultation-form').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission

      // Clear previous error messages
      document.getElementById('name-error').textContent = '';
      document.getElementById('contact-error').textContent = '';
      document.getElementById('accident-type-error').textContent = '';

      let isValid = true;

      // Validate name
      const name = document.getElementById('name').value.trim();
      if (name === '') {
        document.getElementById('name-error').textContent = 'Name is required.';
        isValid = false;
      }

      // Validate contact information
      const contact = document.getElementById('contact').value.trim();
      if (contact === '') {
        document.getElementById('contact-error').textContent = 'Contact information is required.';
        isValid = false;
      }

      // Validate type of accident
      const accidentType = document.getElementById('accident-type').value;
      if (accidentType === '') {
        document.getElementById('accident-type-error').textContent = 'Please select the type of accident.';
        isValid = false;
      }

      // If all fields are valid, submit the form (mock submission in this case)
      if (isValid) {
        alert('Form submitted successfully!');
        // In production, you would send form data to the server here
      }
    });
  </script>

</body>
</html>
```
