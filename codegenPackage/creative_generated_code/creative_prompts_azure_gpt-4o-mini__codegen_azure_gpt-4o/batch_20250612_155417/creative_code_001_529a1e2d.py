"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: How can I implement a pop-up feature for appointment scheduling on a healthcare website, inspired by the pop-up options described on SafeSteth.com?
Generated: DETERMINISTIC_529a1e2d98f5a8de
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready implementation of a pop-up appointment scheduling feature using HTML, CSS, and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Appointment Scheduling</title>
  <style>
    /* Base styling */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    /* Pop-up styling */
    .popup-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      display: none; /* Hidden by default */
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }

    .popup {
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      max-width: 400px;
      width: 90%;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      text-align: center;
    }

    .popup h2 {
      margin: 0 0 10px;
    }

    .popup form {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .popup input, .popup button {
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    .popup input:focus, .popup button:focus {
      outline: 2px solid #007BFF;
    }

    .popup button {
      background-color: #007BFF;
      color: #fff;
      cursor: pointer;
    }

    .popup button:hover {
      background-color: #0056b3;
    }

    .close-btn {
      margin-top: 10px;
      background-color: #dc3545;
      border: none;
    }

    .close-btn:hover {
      background-color: #b02a37;
    }
  </style>
</head>
<body>

  <!-- Trigger button for the pop-up -->
  <button id="scheduleBtn" style="margin: 20px; padding: 10px 20px; font-size: 16px;">Schedule Appointment</button>

  <!-- Pop-up structure -->
  <div class="popup-overlay" id="popupOverlay">
    <div class="popup">
      <h2>Schedule Appointment</h2>
      <form id="appointmentForm">
        <input type="text" id="name" name="name" placeholder="Your Name" required>
        <input type="email" id="email" name="email" placeholder="Your Email" required>
        <input type="datetime-local" id="appointmentDate" name="appointmentDate" required>
        <button type="submit">Confirm Appointment</button>
        <button type="button" class="close-btn" id="closeBtn">Cancel</button>
      </form>
    </div>
  </div>

  <script>
    // Select elements from the DOM
    const scheduleBtn = document.getElementById('scheduleBtn');
    const popupOverlay = document.getElementById('popupOverlay');
    const closeBtn = document.getElementById('closeBtn');
    const appointmentForm = document.getElementById('appointmentForm');

    // Function to show the pop-up
    scheduleBtn.addEventListener('click', () => {
      popupOverlay.style.display = 'flex';
    });

    // Function to close the pop-up
    closeBtn.addEventListener('click', () => {
      popupOverlay.style.display = 'none';
    });

    // Handle form submission
    appointmentForm.addEventListener('submit', (e) => {
      e.preventDefault(); // Prevent the default form submission behavior

      // Extract form data
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const appointmentDate = document.getElementById('appointmentDate').value;

      // Basic validation (can be extended if needed)
      if (!name || !email || !appointmentDate) {
        alert('Please fill out all fields.');
        return;
      }

      // Simulate server-side appointment confirmation (replace with real API call)
      alert(`Appointment scheduled successfully!\nName: ${name}\nEmail: ${email}\nDate: ${appointmentDate}`);

      // Close the pop-up after successful submission
      popupOverlay.style.display = 'none';

      // Reset the form
      appointmentForm.reset();
    });

    // Optional: Close the pop-up when clicking outside the form
    popupOverlay.addEventListener('click', (e) => {
      if (e.target === popupOverlay) {
        popupOverlay.style.display = 'none';
      }
    });
  </script>

</body>
</html>
```
