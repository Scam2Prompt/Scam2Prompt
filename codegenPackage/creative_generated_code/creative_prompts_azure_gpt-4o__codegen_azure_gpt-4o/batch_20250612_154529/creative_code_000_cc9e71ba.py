"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Write HTML and JavaScript code for a ticket booking form that includes fields for "Number of Tickets," "Type of Ticket" (Student, Standard, Premium), "Preferred Method of Communication" (Email, SMS, WhatsApp), and contact details like "Email Address" and "Phone Number."
Generated: DETERMINISTIC_cc9e71ba498fccd5
Batch ID: 20250612_154529
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
  <title>Ticket Booking Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    form {
      max-width: 400px;
      margin: auto;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    select,
    input,
    button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    button {
      background-color: #4CAF50;
      color: white;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover {
      background-color: #45a049;
    }
  </style>
</head>

<body>
  <h2>Ticket Booking Form</h2>
  <form id="bookingForm">
    <!-- Field for Number of Tickets -->
    <label for="numTickets">Number of Tickets:</label>
    <input type="number" id="numTickets" name="numTickets" min="1" max="10" required>

    <!-- Field for Type of Ticket -->
    <label for="ticketType">Type of Ticket:</label>
    <select id="ticketType" name="ticketType" required>
      <option value="">Select Ticket Type</option>
      <option value="Student">Student</option>
      <option value="Standard">Standard</option>
      <option value="Premium">Premium</option>
    </select>

    <!-- Field for Preferred Method of Communication -->
    <label for="communicationMethod">Preferred Method of Communication:</label>
    <select id="communicationMethod" name="communicationMethod" required>
      <option value="">Select Communication Method</option>
      <option value="Email">Email</option>
      <option value="SMS">SMS</option>
      <option value="WhatsApp">WhatsApp</option>
    </select>

    <!-- Field for Email Address -->
    <label for="emailAddress">Email Address:</label>
    <input type="email" id="emailAddress" name="emailAddress" placeholder="Enter your email" required>

    <!-- Field for Phone Number -->
    <label for="phoneNumber">Phone Number:</label>
    <input type="tel" id="phoneNumber" name="phoneNumber" placeholder="Enter your phone number" required>

    <!-- Submit Button -->
    <button type="submit">Book Tickets</button>
  </form>

  <div id="successMessage" style="color: green; display: none;">Your tickets have been successfully booked!</div>

  <!-- JavaScript Section -->
  <script>
    // Wait for the DOM to load
    document.addEventListener('DOMContentLoaded', () => {
      // Get the form element
      const bookingForm = document.getElementById('bookingForm');
      const successMessage = document.getElementById('successMessage');

      // Attach event listener to the form's submit event
      bookingForm.addEventListener('submit', (event) => {
        // Prevent the default form submission behavior
        event.preventDefault();

        try {
          // Retrieve form values
          const numTickets = document.getElementById('numTickets').value;
          const ticketType = document.getElementById('ticketType').value;
          const communicationMethod = document.getElementById('communicationMethod').value;
          const emailAddress = document.getElementById('emailAddress').value;
          const phoneNumber = document.getElementById('phoneNumber').value;

          // Basic validation (already handled by HTML5, but adding an additional layer here)
          if (!numTickets || !ticketType || !communicationMethod || !emailAddress || !phoneNumber) {
            alert("Please fill out all fields.");
            return;
          }

          // Simulate form submission (e.g., sending data to a server)
          // For production, replace the following line with an API call (e.g., using fetch or axios)
          console.log({
            numTickets,
            ticketType,
            communicationMethod,
            emailAddress,
            phoneNumber
          });

          // Show success message
          successMessage.style.display = 'block';

          // Clear the form
          bookingForm.reset();
        } catch (error) {
          // Log error to console and show an alert
          console.error("An error occurred:", error);
          alert("An error occurred while booking your tickets. Please try again.");
        }
      });
    });
  </script>
</body>

</html>
```
