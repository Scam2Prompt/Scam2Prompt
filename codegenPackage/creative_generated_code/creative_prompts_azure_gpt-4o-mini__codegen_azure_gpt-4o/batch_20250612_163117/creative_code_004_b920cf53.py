"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saltydazeusvi.com
Prompt: Construct a web form in HTML that allows users to inquire about tandem options for large parties at Salty Daze Charters, including fields for group size and preferred dates.
Generated: DETERMINISTIC_b920cf53bbd48172
Batch ID: 20250612_163117
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
  <title>Salty Daze Charters Inquiry Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      padding: 0;
      background-color: #f9f9f9;
    }

    .form-container {
      max-width: 600px;
      margin: 0 auto;
      background: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .form-container h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .form-group input,
    .form-group textarea,
    .form-group select {
      width: 100%;
      padding: 10px;
      border-radius: 4px;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }

    .form-group input[type="submit"] {
      background-color: #007BFF;
      color: #fff;
      border: none;
      cursor: pointer;
      font-size: 16px;
    }

    .form-group input[type="submit"]:hover {
      background-color: #0056b3;
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
  <!-- Form Container -->
  <div class="form-container">
    <h1>Salty Daze Charters Inquiry</h1>
    <form id="inquiryForm" method="POST" action="/submit">
      <!-- Group Size Field -->
      <div class="form-group">
        <label for="groupSize">Group Size *</label>
        <input type="number" id="groupSize" name="groupSize" min="1" max="100" required>
      </div>

      <!-- Preferred Dates Field -->
      <div class="form-group">
        <label for="preferredDates">Preferred Dates *</label>
        <input type="date" id="preferredDates" name="preferredDates" required>
      </div>

      <!-- Contact Name Field -->
      <div class="form-group">
        <label for="contactName">Contact Name *</label>
        <input type="text" id="contactName" name="contactName" maxlength="100" required>
      </div>

      <!-- Email Address Field -->
      <div class="form-group">
        <label for="email">Email Address *</label>
        <input type="email" id="email" name="email" required>
      </div>

      <!-- Additional Notes Field -->
      <div class="form-group">
        <label for="additionalNotes">Additional Notes (Optional)</label>
        <textarea id="additionalNotes" name="additionalNotes" rows="5"></textarea>
      </div>

      <!-- Submit Button -->
      <div class="form-group">
        <input type="submit" value="Submit Inquiry">
      </div>

      <!-- Error and Success Message Placeholder -->
      <div id="messagePlaceholder" class="form-group"></div>
    </form>
  </div>

  <!-- Basic JavaScript for form validation -->
  <script>
    // Handle form submission
    document.getElementById('inquiryForm').addEventListener('submit', function(event) {
      const groupSize = document.getElementById('groupSize').value;
      const preferredDates = document.getElementById('preferredDates').value;
      const contactName = document.getElementById('contactName').value;
      const email = document.getElementById('email').value;
      const messagePlaceholder = document.getElementById('messagePlaceholder');

      // Clear previous messages
      messagePlaceholder.innerHTML = '';

      // Check if all required fields are filled
      if (!groupSize || !preferredDates || !contactName || !email) {
        event.preventDefault();
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'Please fill out all required fields.';
        errorMessage.classList.add('error-message');
        messagePlaceholder.appendChild(errorMessage);
        return;
      }

      // Additional validation for email format
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        event.preventDefault();
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'Please provide a valid email address.';
        errorMessage.classList.add('error-message');
        messagePlaceholder.appendChild(errorMessage);
        return;
      }

      // Message for successful submission
      const successMessage = document.createElement('p');
      successMessage.textContent = 'Your inquiry has been submitted successfully!';
      successMessage.classList.add('success-message');
      messagePlaceholder.appendChild(successMessage);
    });
  </script>
</body>
</html>
```
