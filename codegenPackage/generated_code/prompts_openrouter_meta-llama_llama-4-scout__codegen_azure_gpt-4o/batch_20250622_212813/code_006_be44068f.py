"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Design a user interface component for a car repair shop website, allowing customers to select services (e.g., alignment, suspension) and schedule appointments online, inspired by Pneus ML's service offerings.
Generated: DETERMINISTIC_be44068f4e3dfd65
Batch ID: 20250622_212813
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
  <title>Car Repair Shop - Schedule Appointment</title>
  <link rel="stylesheet" href="styles.css">
  <script src="script.js" defer></script>
</head>
<body>
  <header>
    <h1>Car Repair Shop</h1>
    <p>Schedule your appointment online</p>
  </header>

  <main>
    <section id="service-selection">
      <h2>Select Services</h2>
      <form id="appointment-form">
        <!-- Service Selection -->
        <div>
          <label for="services">Choose a service:</label>
          <select id="services" name="services" required>
            <option value="" disabled selected>Select a service</option>
            <option value="alignment">Alignment</option>
            <option value="suspension">Suspension</option>
            <option value="oil-change">Oil Change</option>
            <option value="brake-repair">Brake Repair</option>
          </select>
        </div>

        <!-- Date Selection -->
        <div>
          <label for="appointment-date">Select a date:</label>
          <input type="date" id="appointment-date" name="appointment-date" required>
        </div>

        <!-- Time Selection -->
        <div>
          <label for="appointment-time">Select a time:</label>
          <input type="time" id="appointment-time" name="appointment-time" required>
        </div>

        <!-- Submit Button -->
        <button type="submit">Schedule Appointment</button>
      </form>
    </section>

    <!-- Confirmation Message -->
    <section id="confirmation-message" style="display: none;">
      <h2>Appointment Confirmed</h2>
      <p id="confirmation-details"></p>
    </section>
  </main>

  <footer>
    <p>&copy; 2023 Car Repair Shop. All rights reserved.</p>
  </footer>
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

header {
  background-color: #333;
  color: #fff;
  padding: 1rem;
  text-align: center;
}

main {
  padding: 2rem;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem;
  position: fixed;
  bottom: 0;
  width: 100%;
}

/* Form Styles */
form {
  background: #fff;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

form div {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

select, input, button {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
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

/* Confirmation Message */
#confirmation-message {
  background: #d4edda;
  color: #155724;
  padding: 1rem;
  border-radius: 5px;
  margin-top: 2rem;
}
```

```javascript
// script.js

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('appointment-form');
  const confirmationMessage = document.getElementById('confirmation-message');
  const confirmationDetails = document.getElementById('confirmation-details');

  // Handle form submission
  form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    try {
      // Get form values
      const service = document.getElementById('services').value;
      const date = document.getElementById('appointment-date').value;
      const time = document.getElementById('appointment-time').value;

      // Validate inputs
      if (!service || !date || !time) {
        alert('Please fill out all fields.');
        return;
      }

      // Display confirmation message
      confirmationDetails.textContent = `You have scheduled a ${service} service on ${date} at ${time}.`;
      confirmationMessage.style.display = 'block';

      // Reset form
      form.reset();
    } catch (error) {
      console.error('Error scheduling appointment:', error);
      alert('An error occurred while scheduling your appointment. Please try again.');
    }
  });
});
```
