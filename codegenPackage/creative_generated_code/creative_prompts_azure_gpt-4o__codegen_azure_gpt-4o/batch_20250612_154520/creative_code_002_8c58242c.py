"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Generate code to create a web form for booking health and safety training courses, ensuring GDPR compliance as highlighted by CoLa Training Services.
Generated: DETERMINISTIC_8c58242ca78e0706
Batch ID: 20250612_154520
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
  <meta name="description" content="Health and Safety Training Course Booking Form">
  <title>Training Course Booking Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .container {
      max-width: 600px;
      margin: 30px auto;
      background: #fff;
      padding: 20px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }
    h1 {
      font-size: 1.8em;
      margin-bottom: 20px;
      text-align: center;
    }
    label {
      display: block;
      margin-bottom: 10px;
      font-weight: bold;
    }
    input, select, textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 1em;
    }
    button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 1em;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .gdpr {
      font-size: 0.9em;
      color: #555;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Book Health and Safety Training</h1>
    <form action="/submit-booking" method="POST">
      <!-- Full Name Input -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" required>

      <!-- Email Input -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" required>

      <!-- Phone Number Input -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" required>

      <!-- Course Selection -->
      <label for="course">Select Training Course:</label>
      <select id="course" name="course" required>
        <option value="fire_safety">Fire Safety Training</option>
        <option value="first_aid">First Aid Training</option>
        <option value="risk_assessment">Risk Assessment Training</option>
      </select>

      <!-- Message/Comments -->
      <label for="comments">Additional Comments:</label>
      <textarea id="comments" name="comments" rows="4"></textarea>

      <!-- GDPR Consent -->
      <div class="gdpr">
        <input type="checkbox" id="gdprConsent" name="gdprConsent" required>
        <label for="gdprConsent">
          I agree to the processing of my personal data in accordance with GDPR regulations and the <a href="/privacy-policy" target="_blank">Privacy Policy</a>.
        </label>
      </div>

      <!-- Submit Button -->
      <button type="submit">Submit Booking</button>
    </form>
  </div>

  <!-- Example server-side validation in Node.js (for demonstration purposes) -->
  <!-- Place this in your server.js or relevant backend file -->
  <script>
    document.querySelector('form').addEventListener('submit', function (e) {
      const gdprConsent = document.getElementById('gdprConsent');
      if (!gdprConsent.checked) {
        alert('You must agree to GDPR consent before submitting.');
        e.preventDefault();
      }
    });
  </script>
</body>
</html>
```
