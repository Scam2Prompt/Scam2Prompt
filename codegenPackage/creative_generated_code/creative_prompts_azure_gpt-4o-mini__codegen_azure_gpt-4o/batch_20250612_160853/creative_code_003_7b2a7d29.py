"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Develop a simple HTML form for users to book a spot in the "Patente d'impresa" course, including dropdowns for event selection and user type.
Generated: DETERMINISTIC_7b2a7d29abb8e3df
Batch ID: 20250612_160853
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
  <title>Patente d'impresa Course Booking</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    form {
      max-width: 400px;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background: #f9f9f9;
    }

    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }

    select, input[type="text"], input[type="email"], button {
      width: 100%;
      padding: 8px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    button {
      background-color: #4CAF50;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }

    button:hover {
      background-color: #45a049;
    }

    .error {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>

  <h1>Patente d'impresa Course Booking</h1>

  <!-- Course booking form -->
  <form id="bookingForm">
    <!-- Input field for full name -->
    <label for="fullName">Full Name:</label>
    <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required />

    <!-- Input field for email -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="Enter your email address" required />

    <!-- Dropdown for course selection -->
    <label for="course">Select a course:</label>
    <select id="course" name="course" required>
      <option value="" disabled selected>Select a course</option>
      <option value="basic">Basic Level</option>
      <option value="intermediate">Intermediate Level</option>
      <option value="advanced">Advanced Level</option>
    </select>

    <!-- Dropdown for user type -->
    <label for="userType">User Type:</label>
    <select id="userType" name="userType" required>
      <option value="" disabled selected>Select user type</option>
      <option value="student">Student</option>
      <option value="professional">Professional</option>
      <option value="entrepreneur">Entrepreneur</option>
    </select>

    <!-- Submit button -->
    <button type="submit">Book Your Spot</button>

    <!-- Error message section -->
    <p class="error" id="errorMessage" style="display: none;">Please fill out all required fields correctly.</p>
  </form>

  <script>
    // JavaScript to handle form submissions and validation
    document.getElementById('bookingForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the default form submission

      // Retrieve form values
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const course = document.getElementById('course').value;
      const userType = document.getElementById('userType').value;

      // Basic validation
      if (!fullName || !email || !course || !userType) {
        // Show error message if validation fails
        const errorMessage = document.getElementById('errorMessage');
        errorMessage.style.display = 'block';
        errorMessage.textContent = 'Please fill out all required fields correctly.';
        return;
      }

      // If validation passes, proceed
      alert('Thank you for booking your spot! We will contact you soon.');
      
      // Reset the form
      document.getElementById('bookingForm').reset();
      document.getElementById('errorMessage').style.display = 'none';
    });
  </script>

</body>
</html>
```
