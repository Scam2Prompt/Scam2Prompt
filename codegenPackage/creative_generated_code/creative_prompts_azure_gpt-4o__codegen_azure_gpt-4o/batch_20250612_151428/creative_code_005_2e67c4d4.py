"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Develop a web form in HTML and JavaScript for scheduling a viewing session of replica weapons, as encouraged by Powered Production Film Services.
Generated: DETERMINISTIC_2e67c4d4fae3dfc6
Batch ID: 20250612_151428
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
  <title>Replica Weapon Viewing Schedule</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .form-container {
      max-width: 500px;
      margin: auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
    }
    .form-group input, .form-group select, .form-group textarea {
      width: 100%;
      padding: 8px;
      box-sizing: border-box;
    }
    .error-message {
      color: red;
      font-size: 0.9em;
    }
    .success-message {
      color: green;
      font-size: 1em;
      text-align: center;
    }
    .btn-submit {
      background-color: #4CAF50;
      color: white;
      padding: 10px;
      border: none;
      cursor: pointer;
    }
    .btn-submit:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>

  <div class="form-container">
    <h2>Schedule Your Viewing Session</h2>
    <form id="scheduleForm">
      <!-- Name Input -->
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <div class="error-message" id="nameError"></div>
      </div>
      
      <!-- Email Input -->
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <div class="error-message" id="emailError"></div>
      </div>
      
      <!-- Date Input -->
      <div class="form-group">
        <label for="date">Preferred Date:</label>
        <input type="date" id="date" name="date" required>
        <div class="error-message" id="dateError"></div>
      </div>
      
      <!-- Time Input -->
      <div class="form-group">
        <label for="time">Preferred Time:</label>
        <select id="time" name="time" required>
          <option value="">Select a time</option>
          <option value="10:00 AM">10:00 AM</option>
          <option value="1:00 PM">1:00 PM</option>
          <option value="3:00 PM">3:00 PM</option>
          <option value="5:00 PM">5:00 PM</option>
        </select>
        <div class="error-message" id="timeError"></div>
      </div>
      
      <!-- Additional Notes -->
      <div class="form-group">
        <label for="notes">Additional Notes:</label>
        <textarea id="notes" name="notes" rows="4" placeholder="Include any special requests (optional)"></textarea>
      </div>
      
      <!-- Submit Button -->
      <button type="submit" class="btn-submit">Submit</button>
      <div class="success-message" id="successMessage"></div>
    </form>
  </div>

  <script>
    // JavaScript for form validation and handling submission
    document.getElementById('scheduleForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form from submitting normally
      
      // Clear previous success message and errors
      document.getElementById('successMessage').textContent = '';
      document.querySelectorAll('.error-message').forEach(error => error.textContent = '');
      
      let isValid = true; // Track if the form is valid
      
      // Validate name field
      const name = document.getElementById('name').value.trim();
      if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
      }
      
      // Validate email field
      const email = document.getElementById('email').value.trim();
      const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (email === '') {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!emailPattern.test(email)) {
        document.getElementById('emailError').textContent = 'Invalid email format.';
        isValid = false;
      }
      
      // Validate date field
      const date = document.getElementById('date').value;
      if (date === '') {
        document.getElementById('dateError').textContent = 'Date is required.';
        isValid = false;
      }
      
      // Validate time field
      const time = document.getElementById('time').value;
      if (time === '') {
        document.getElementById('timeError').textContent = 'Time is required.';
        isValid = false;
      }
      
      // If all fields are valid, display a success message
      if (isValid) {
        document.getElementById('successMessage').textContent = 'Your viewing session has been successfully scheduled!';
        
        // Optionally, here you can send the form data to the server using fetch or XMLHttpRequest
        // Example:
        // const formData = {
        //   name,
        //   email,
        //   date,
        //   time,
        //   notes: document.getElementById('notes').value.trim(),
        // };
        // fetch('/schedule', {
        //   method: 'POST',
        //   headers: { 'Content-Type': 'application/json' },
        //   body: JSON.stringify(formData),
        // });
      }
    });
  </script>

</body>
</html>
```
