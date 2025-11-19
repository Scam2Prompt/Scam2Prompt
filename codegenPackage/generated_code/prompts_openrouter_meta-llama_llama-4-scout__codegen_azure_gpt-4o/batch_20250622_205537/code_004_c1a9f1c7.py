"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocats.com
Prompt: Generate a sample intake form for a family law client, including fields for personal and case information, using HTML and CSS, inspired by the layout and content of the Majeli Avocat website.
Generated: DETERMINISTIC_c1a9f1c7f2e4295f
Batch ID: 20250622_205537
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
  <title>Family Law Client Intake Form</title>
  <style>
    /* General styles for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }

    .container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background-color: #fff;
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
      color: #555;
    }

    input, select, textarea {
      margin-top: 5px;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
      width: 100%;
      box-sizing: border-box;
    }

    textarea {
      resize: vertical;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .submit-btn {
      background-color: #007BFF;
      color: #fff;
      border: none;
      padding: 10px 15px;
      font-size: 16px;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .submit-btn:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Family Law Client Intake Form</h1>
    <form id="intakeForm">
      <!-- Personal Information Section -->
      <div class="form-group">
        <label for="fullName">Full Name *</label>
        <input type="text" id="fullName" name="fullName" required>
      </div>

      <div class="form-group">
        <label for="email">Email Address *</label>
        <input type="email" id="email" name="email" required>
      </div>

      <div class="form-group">
        <label for="phone">Phone Number *</label>
        <input type="tel" id="phone" name="phone" required>
      </div>

      <div class="form-group">
        <label for="address">Address *</label>
        <input type="text" id="address" name="address" required>
      </div>

      <!-- Case Information Section -->
      <div class="form-group">
        <label for="caseType">Type of Case *</label>
        <select id="caseType" name="caseType" required>
          <option value="">-- Select --</option>
          <option value="divorce">Divorce</option>
          <option value="childCustody">Child Custody</option>
          <option value="adoption">Adoption</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div class="form-group">
        <label for="caseDetails">Details of Your Case *</label>
        <textarea id="caseDetails" name="caseDetails" rows="5" required></textarea>
      </div>

      <div class="form-group">
        <label for="preferredContact">Preferred Contact Method *</label>
        <select id="preferredContact" name="preferredContact" required>
          <option value="">-- Select --</option>
          <option value="email">Email</option>
          <option value="phone">Phone</option>
        </select>
      </div>

      <!-- Submit Button -->
      <div class="form-group">
        <button type="submit" class="submit-btn">Submit</button>
      </div>
    </form>
  </div>

  <script>
    // Basic client-side validation
    document.getElementById('intakeForm').addEventListener('submit', function(event) {
      const form = event.target;
      let isValid = true;

      // Check required fields
      form.querySelectorAll('[required]').forEach(field => {
        if (!field.value.trim()) {
          isValid = false;
          field.style.borderColor = 'red';
        } else {
          field.style.borderColor = '#ccc';
        }
      });

      if (!isValid) {
        event.preventDefault();
        alert('Please fill out all required fields.');
      }
    });
  </script>
</body>
</html>
```
