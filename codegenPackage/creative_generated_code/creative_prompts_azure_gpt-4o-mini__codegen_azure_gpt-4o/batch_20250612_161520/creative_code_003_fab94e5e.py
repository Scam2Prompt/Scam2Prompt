"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mollinari.com.pl
Prompt: Develop a simple HTML form that collects user data for reservations at Mollinari, ensuring it includes fields for date, time, and number of guests.
Generated: DETERMINISTIC_fab94e5ea86a96c0
Batch ID: 20250612_161520
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
  <title>Mollinari Reservation Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    .reservation-form {
      background: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    .reservation-form h1 {
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

    .form-group input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .form-group input[type="submit"] {
      background-color: #007bff;
      color: white;
      cursor: pointer;
      border: none;
    }

    .form-group input[type="submit"]:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <form class="reservation-form" id="mollinari-reservation-form">
    <h1>Mollinari Reservation</h1>

    <!-- Field for the reservation date -->
    <div class="form-group">
      <label for="reservation-date">Reservation Date:</label>
      <input type="date" id="reservation-date" name="reservation-date" required>
    </div>

    <!-- Field for the reservation time -->
    <div class="form-group">
      <label for="reservation-time">Reservation Time:</label>
      <input type="time" id="reservation-time" name="reservation-time" required>
    </div>

    <!-- Field for the number of guests -->
    <div class="form-group">
      <label for="number-of-guests">Number of Guests:</label>
      <input type="number" id="number-of-guests" name="number-of-guests" min="1" max="20" required>
    </div>

    <!-- Submit button -->
    <div class="form-group">
      <input type="submit" value="Submit Reservation">
    </div>

    <!-- Placeholder for error messages -->
    <div id="error-message" class="error-message"></div>
  </form>

  <script>
    // JavaScript for form validation and error handling
    const form = document.getElementById('mollinari-reservation-form');
    const errorMessageDiv = document.getElementById('error-message');

    form.addEventListener('submit', function (event) {
      // Clear any previous error messages
      errorMessageDiv.textContent = '';

      // Collect form values
      const date = document.getElementById('reservation-date').value;
      const time = document.getElementById('reservation-time').value;
      const guests = document.getElementById('number-of-guests').value;

      // Validate the inputs
      if (!date || !time || !guests || guests <= 0) {
        event.preventDefault(); // Prevent form submission
        errorMessageDiv.textContent = 'Please ensure all fields are filled correctly.';
        return;
      }

      // Additional validation can be added here (e.g., date/time constraints)
    });
  </script>
</body>
</html>
```
