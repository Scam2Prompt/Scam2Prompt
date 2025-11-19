"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Design a simple HTML form for users to submit their medical certificates and registration documents to the AAVE gliding club.
Generated: DETERMINISTIC_be78b720ddae3a97
Batch ID: 20250612_155142
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
  <title>AAVE Gliding Club - Document Submission</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background: #f7f7f7;
    }
    .container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
      text-align: center;
      color: #333;
    }
    form {
      display: flex;
      flex-direction: column;
    }
    label {
      margin-top: 15px;
      font-weight: bold;
    }
    input[type="text"],
    input[type="file"],
    input[type="email"],
    button {
      margin-top: 8px;
      padding: 10px;
      width: 100%;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }
    button {
      background-color: #007bff;
      color: white;
      cursor: pointer;
      border: none;
      transition: background-color 0.3s;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>AAVE Gliding Club Document Submission</h1>
    <form id="documentSubmissionForm" action="/submit-documents" method="POST" enctype="multipart/form-data">
      <!-- User's full name -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>

      <!-- User's email -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email address" required>

      <!-- Medical certificate upload -->
      <label for="medicalCertificate">Upload Medical Certificate:</label>
      <input type="file" id="medicalCertificate" name="medicalCertificate" accept=".pdf,.jpg,.jpeg,.png" required>

      <!-- Registration document upload -->
      <label for="registrationDocument">Upload Registration Document:</label>
      <input type="file" id="registrationDocument" name="registrationDocument" accept=".pdf,.jpg,.jpeg,.png" required>

      <!-- Submit button -->
      <button type="submit">Submit Documents</button>

      <div id="formErrors" class="error"></div>
    </form>
  </div>

  <script>
    // JavaScript for basic client-side validation
    document.getElementById('documentSubmissionForm').addEventListener('submit', function (event) {
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const medicalCertificate = document.getElementById('medicalCertificate').files.length;
      const registrationDocument = document.getElementById('registrationDocument').files.length;
      const formErrors = document.getElementById('formErrors');

      // Clear previous error messages
      formErrors.textContent = '';

      // Validate inputs
      if (!fullName || !email || medicalCertificate === 0 || registrationDocument === 0) {
        event.preventDefault(); // Prevent form submission
        formErrors.textContent = 'Please fill out all fields and upload all required documents.';
      }
    });
  </script>
</body>
</html>
```
