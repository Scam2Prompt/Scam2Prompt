"""
Generated Code Metadata:
========================
Original URL: https://firstbaptistnj.org
Prompt: Develop a web form for planning a visit to a church, incorporating elements from the First Baptist Church's visitor engagement strategies.
Generated: DETERMINISTIC_03a989c713eb66bd
Batch ID: 20250612_163912
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
  <title>Church Visit Planning Form</title>
  <style>
    /* Basic styling for the form */
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
      margin-top: 10px;
      font-weight: bold;
    }

    input, select, textarea {
      margin-top: 5px;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    button {
      margin-top: 20px;
      padding: 10px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
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
    <h1>Plan Your Visit</h1>
    <form id="visitForm">
      <!-- Full Name Field -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" required>
      <span class="error" id="nameError"></span>

      <!-- Email Field -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" required>
      <span class="error" id="emailError"></span>

      <!-- Phone Number Field -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" required>
      <span class="error" id="phoneError"></span>

      <!-- Visit Date Field -->
      <label for="visitDate">Preferred Visit Date:</label>
      <input type="date" id="visitDate" name="visitDate" required>
      <span class="error" id="dateError"></span>

      <!-- Service Time Dropdown -->
      <label for="serviceTime">Preferred Service Time:</label>
      <select id="serviceTime" name="serviceTime" required>
        <option value="">Select a time</option>
        <option value="morning">Morning Service (9:00 AM)</option>
        <option value="afternoon">Afternoon Service (12:00 PM)</option>
        <option value="evening">Evening Service (6:00 PM)</option>
      </select>
      <span class="error" id="serviceTimeError"></span>

      <!-- Additional Notes -->
      <label for="notes">Additional Notes or Questions:</label>
      <textarea id="notes" name="notes" rows="4"></textarea>

      <!-- Submit Button -->
      <button type="submit">Submit</button>
    </form>
  </div>

  <script>
    // JavaScript for form validation and submission
    document.getElementById('visitForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('phoneError').textContent = '';
      document.getElementById('dateError').textContent = '';
      document.getElementById('serviceTimeError').textContent = '';

      // Validate form fields
      let isValid = true;

      const fullName = document.getElementById('fullName').value.trim();
      if (!fullName) {
        document.getElementById('nameError').textContent = 'Full Name is required.';
        isValid = false;
      }

      const email = document.getElementById('email').value.trim();
      if (!email || !email.includes('@')) {
        document.getElementById('emailError').textContent = 'Valid Email Address is required.';
        isValid = false;
      }

      const phone = document.getElementById('phone').value.trim();
      if (!phone || phone.length < 10) {
        document.getElementById('phoneError').textContent = 'Valid Phone Number is required.';
        isValid = false;
      }

      const visitDate = document.getElementById('visitDate').value.trim();
      if (!visitDate) {
        document.getElementById('dateError').textContent = 'Preferred Visit Date is required.';
        isValid = false;
      }

      const serviceTime = document.getElementById('serviceTime').value.trim();
      if (!serviceTime) {
        document.getElementById('serviceTimeError').textContent = 'Preferred Service Time is required.';
        isValid = false;
      }

      // If all fields are valid, submit the form
      if (isValid) {
        alert('Thank you for planning your visit! We look forward to seeing you.');
        // Here, you can add code to send the form data to a server via AJAX or another method
        document.getElementById('visitForm').reset(); // Reset the form
      }
    });
  </script>
</body>
</html>
```
