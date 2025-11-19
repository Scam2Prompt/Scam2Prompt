"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opticalize.com
Prompt: Design a simple HTML form that collects user information for scheduling an eye examination, reflecting the services provided by Optic Alizé in Burkina Faso.
Generated: DETERMINISTIC_56a192b69cacb009
Batch ID: 20250612_164304
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
  <title>Eye Examination Appointment Form | Optic Alizé</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .form-container {
      max-width: 600px;
      margin: 50px auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .form-container h1 {
      text-align: center;
      color: #333;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    .form-group input, .form-group select, .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }
    .form-group input[type="submit"] {
      background-color: #008cba;
      color: #fff;
      border: none;
      cursor: pointer;
    }
    .form-group input[type="submit"]:hover {
      background-color: #005f75;
    }
    .error-message {
      color: red;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Schedule an Eye Examination</h1>
    <form id="appointmentForm" action="/submit" method="POST">
      <!-- Name field -->
      <div class="form-group">
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
      </div>

      <!-- Email field -->
      <div class="form-group">
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>

      <!-- Phone field -->
      <div class="form-group">
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
      </div>

      <!-- Preferred Date field -->
      <div class="form-group">
        <label for="date">Preferred Appointment Date:</label>
        <input type="date" id="date" name="date" required>
      </div>

      <!-- Service type field -->
      <div class="form-group">
        <label for="service">Type of Service:</label>
        <select id="service" name="service" required>
          <option value="">Select a service</option>
          <option value="eye_exam">Eye Examination</option>
          <option value="glasses_fitting">Glasses Fitting</option>
          <option value="contact_lenses">Contact Lenses Consultation</option>
        </select>
      </div>

      <!-- Additional notes field -->
      <div class="form-group">
        <label for="notes">Additional Notes (Optional):</label>
        <textarea id="notes" name="notes" rows="4" placeholder="Provide additional details, if any"></textarea>
      </div>

      <!-- Submit button -->
      <div class="form-group">
        <input type="submit" value="Submit Appointment Request">
      </div>
    </form>
  </div>
</body>
</html>
```
