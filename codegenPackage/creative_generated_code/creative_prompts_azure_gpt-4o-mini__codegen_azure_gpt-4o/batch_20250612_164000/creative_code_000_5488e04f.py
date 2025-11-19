"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lecarolee.it
Prompt: Generate a code snippet to create a web form for booking an agriturismo stay at Le Carolee, including fields for name, email, and dates of stay.
Generated: DETERMINISTIC_5488e04f0cc925b3
Batch ID: 20250612_164000
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
  <title>Le Carolee Booking Form</title>
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
      background-color: #f4f4f9;
    }
    .booking-form {
      background: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      max-width: 400px;
      width: 100%;
    }
    .booking-form h2 {
      margin-bottom: 20px;
      text-align: center;
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
    .form-group input[type="date"] {
      max-width: calc(50% - 10px);
      display: inline-block;
      margin-right: 10px;
    }
    .form-group input[type="date"]:last-child {
      margin-right: 0;
    }
    .submit-button {
      background-color: #4caf50;
      color: #ffffff;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      width: 100%;
      font-size: 16px;
    }
    .submit-button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <form class="booking-form" id="bookingForm">
    <h2>Book Your Stay at Le Carolee</h2>
    <!-- Name input field -->
    <div class="form-group">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" placeholder="Enter your full name" required />
    </div>
    
    <!-- Email input field -->
    <div class="form-group">
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email address" required />
    </div>

    <!-- Dates of stay input fields -->
    <div class="form-group">
      <label for="stay-dates">Dates of Stay:</label>
      <input type="date" id="startDate" name="startDate" required />
      <input type="date" id="endDate" name="endDate" required />
    </div>
    
    <!-- Submit button -->
    <button type="submit" class="submit-button">Submit Booking</button>
  </form>

  <script>
    // Attach event listener to the form to handle submission
    document.getElementById("bookingForm").addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent default form submission
      
      try {
        // Extract form data
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const startDate = document.getElementById("startDate").value;
        const endDate = document.getElementById("endDate").value;

        // Basic validation checks
        if (!name || !email || !startDate || !endDate) {
          alert("Please fill out all fields before submitting.");
          return;
        }

        // Validate date range
        if (new Date(startDate) >= new Date(endDate)) {
          alert("End date must be after the start date.");
          return;
        }

        // Mock form submission logic
        alert(`Booking confirmed for ${name} from ${startDate} to ${endDate}. Details will be sent to ${email}.`);
        
        // Reset the form after successful submission
        event.target.reset();
      } catch (error) {
        console.error("An error occurred while processing the booking:", error);
        alert("An unexpected error occurred. Please try again later.");
      }
    });
  </script>
</body>
</html>
```
