"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Design a user interface component (using HTML, CSS, and JavaScript) for a tire and wheel services website that allows users to select services (e.g., tire change, balancing, repair) and book appointments.
Generated: DETERMINISTIC_80a9457fe36204ea
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
  <title>Tire and Wheel Services Booking</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="booking-container">
    <h1>Tire and Wheel Services</h1>
    <form id="bookingForm">
      <!-- Service Selection -->
      <div class="form-group">
        <label for="service">Select Service:</label>
        <select id="service" name="service" required>
          <option value="" disabled selected>Select a service</option>
          <option value="tireChange">Tire Change</option>
          <option value="balancing">Balancing</option>
          <option value="repair">Repair</option>
        </select>
      </div>

      <!-- Appointment Date -->
      <div class="form-group">
        <label for="appointmentDate">Select Appointment Date:</label>
        <input type="date" id="appointmentDate" name="appointmentDate" required>
      </div>

      <!-- Appointment Time -->
      <div class="form-group">
        <label for="appointmentTime">Select Appointment Time:</label>
        <input type="time" id="appointmentTime" name="appointmentTime" required>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="submit-button">Book Appointment</button>
    </form>

    <!-- Confirmation Message -->
    <div id="confirmationMessage" class="hidden">
      <p>Your appointment has been successfully booked!</p>
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

.booking-container {
  max-width: 500px;
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

/* Form Styles */
.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

select, input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

button.submit-button {
  width: 100%;
  padding: 10px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

button.submit-button:hover {
  background-color: #0056b3;
}

/* Confirmation Message */
.hidden {
  display: none;
}

#confirmationMessage {
  margin-top: 20px;
  text-align: center;
  color: #28a745;
  font-weight: bold;
}
```

```javascript
// script.js

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
  const bookingForm = document.getElementById('bookingForm');
  const confirmationMessage = document.getElementById('confirmationMessage');

  // Handle form submission
  bookingForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    // Validate form inputs
    const service = document.getElementById('service').value;
    const appointmentDate = document.getElementById('appointmentDate').value;
    const appointmentTime = document.getElementById('appointmentTime').value;

    if (!service || !appointmentDate || !appointmentTime) {
      alert('Please fill out all fields before submitting.');
      return;
    }

    // Simulate booking process (e.g., send data to server)
    try {
      // Simulated server request (replace with actual API call if needed)
      console.log('Booking Details:', { service, appointmentDate, appointmentTime });

      // Show confirmation message
      confirmationMessage.classList.remove('hidden');
      bookingForm.reset(); // Reset the form
    } catch (error) {
      console.error('Error booking appointment:', error);
      alert('An error occurred while booking your appointment. Please try again.');
    }
  });
});
```
