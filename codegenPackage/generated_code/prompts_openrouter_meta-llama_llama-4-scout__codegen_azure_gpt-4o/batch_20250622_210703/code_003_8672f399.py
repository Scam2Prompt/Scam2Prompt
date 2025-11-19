"""
Generated Code Metadata:
========================
Original URL: https://grupoinmobiliariocrecer.com
Prompt: Create a simple web form using HTML and JavaScript to collect required documents for property evaluation, as mentioned in the Grupo Inmobiliario Crecer website (e.g., Formulario Persona Natural AFIANSA).
Generated: DETERMINISTIC_8672f3991d34c18e
Batch ID: 20250622_210703
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
  <title>Property Evaluation Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .container {
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

    input[type="text"],
    input[type="email"],
    input[type="file"],
    button {
      width: 100%;
      padding: 10px;
      margin: 5px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    button {
      background-color: #007BFF;
      color: white;
      border: none;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    .error {
      color: red;
      font-size: 0.9em;
    }

    .success {
      color: green;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Property Evaluation Form</h1>
    <form id="propertyForm">
      <!-- Full Name -->
      <div class="form-group">
        <label for="fullName">Full Name *</label>
        <input type="text" id="fullName" name="fullName" required>
        <span class="error" id="nameError"></span>
      </div>

      <!-- Email -->
      <div class="form-group">
        <label for="email">Email *</label>
        <input type="email" id="email" name="email" required>
        <span class="error" id="emailError"></span>
      </div>

      <!-- Required Documents -->
      <div class="form-group">
        <label for="documents">Upload Required Documents *</label>
        <input type="file" id="documents" name="documents" multiple required>
        <span class="error" id="documentsError"></span>
      </div>

      <!-- Submit Button -->
      <button type="submit">Submit</button>
      <span class="success" id="successMessage"></span>
    </form>
  </div>

  <script>
    // JavaScript for form validation and submission
    document.getElementById('propertyForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form submission

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('documentsError').textContent = '';
      document.getElementById('successMessage').textContent = '';

      // Get form values
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const documents = document.getElementById('documents').files;

      let isValid = true;

      // Validate Full Name
      if (fullName === '') {
        document.getElementById('nameError').textContent = 'Full Name is required.';
        isValid = false;
      }

      // Validate Email
      if (email === '') {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        isValid = false;
      }

      // Validate Documents
      if (documents.length === 0) {
        document.getElementById('documentsError').textContent = 'Please upload at least one document.';
        isValid = false;
      }

      // If all validations pass, show success message
      if (isValid) {
        document.getElementById('successMessage').textContent = 'Form submitted successfully!';
        // Here, you can add code to send the form data to a server using AJAX or another method
      }
    });
  </script>
</body>
</html>
```
