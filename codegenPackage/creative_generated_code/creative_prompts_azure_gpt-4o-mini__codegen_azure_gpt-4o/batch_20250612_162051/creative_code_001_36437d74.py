"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcelsolemos.com.br
Prompt: Generate a code snippet for a web form that allows users to inquire about orthodontic treatments and schedule an evaluation at Dr. Celso Lemos' clinic.
Generated: DETERMINISTIC_36437d74d1945e4a
Batch ID: 20250612_162051
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
  <title>Orthodontic Inquiry Form - Dr. Celso Lemos</title>
  <!-- Include a basic CSS stylesheet for styling the form -->
  <style>
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
      background: #ffffff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }
    h1 {
      text-align: center;
      color: #333;
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    input, textarea, button, select {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #007BFF;
      color: #fff;
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
      font-size: 1em;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Orthodontic Inquiry Form</h1>
    <!-- Web form for collecting inquiries and scheduling evaluations -->
    <form id="inquiryForm">
      <!-- Input field for user's full name -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" placeholder="Your full name" required>
      <span class="error" id="nameError"></span>

      <!-- Input field for user's email address -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" placeholder="Your email" required>
      <span class="error" id="emailError"></span>

      <!-- Input field for user's phone number -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" placeholder="Your phone number" required>
      <span class="error" id="phoneError"></span>

      <!-- Dropdown for selecting orthodontic services -->
      <label for="service">Select Service:</label>
      <select id="service" name="service" required>
        <option value="" disabled selected>Select a service</option>
        <option value="braces">Braces</option>
        <option value="aligners">Clear Aligners</option>
        <option value="consultation">General Consultation</option>
      </select>
      <span class="error" id="serviceError"></span>

      <!-- Textarea for additional comments -->
      <label for="comments">Additional Comments:</label>
      <textarea id="comments" name="comments" rows="5" placeholder="Any specific questions or concerns"></textarea>

      <!-- Input field for scheduling an appointment -->
      <label for="appointmentDate">Preferred Appointment Date:</label>
      <input type="date" id="appointmentDate" name="appointmentDate" required>
      <span class="error" id="dateError"></span>

      <!-- Submit button -->
      <button type="submit">Submit Inquiry</button>
      <span class="success" id="formSuccess"></span>
    </form>
  </div>

  <!-- JavaScript for basic form validation -->
  <script>
    document.getElementById('inquiryForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission
      
      // Clear previous messages
      document.querySelectorAll('.error').forEach(elem => elem.textContent = '');
      document.getElementById('formSuccess').textContent = '';

      // Basic validation
      let isValid = true;
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const service = document.getElementById('service').value.trim();
      const appointmentDate = document.getElementById('appointmentDate').value.trim();

      if (!fullName) {
        document.getElementById('nameError').textContent = 'Full Name is required.';
        isValid = false;
      }
      if (!email || !email.includes('@')) {
        document.getElementById('emailError').textContent = 'Valid Email is required.';
        isValid = false;
      }
      if (!phone || phone.length < 10) {
        document.getElementById('phoneError').textContent = 'Valid Phone Number is required.';
        isValid = false;
      }
      if (!service) {
        document.getElementById('serviceError').textContent = 'Please select a service.';
        isValid = false;
      }
      if (!appointmentDate) {
        document.getElementById('dateError').textContent = 'Appointment Date is required.';
        isValid = false;
      }

      // If valid, display success message and optionally send data to server
      if (isValid) {
        document.getElementById('formSuccess').textContent = 'Your inquiry has been submitted successfully!';
        // Add code here to send form data to the server via AJAX or Fetch API
      }
    });
  </script>
</body>
</html>
```
