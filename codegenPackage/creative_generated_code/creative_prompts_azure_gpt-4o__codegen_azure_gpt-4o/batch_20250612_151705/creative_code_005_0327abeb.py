"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Create a web form using HTML and JavaScript for course registration, including fields for selecting sales training programs like those provided by Debridge Advisory.
Generated: DETERMINISTIC_0327abebd24e406b
Batch ID: 20250612_151705
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
  <title>Course Registration Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      margin: 0;
      padding: 20px;
    }

    .form-container {
      max-width: 500px;
      margin: auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
    }

    label {
      display: block;
      margin-bottom: 6px;
      font-weight: bold;
    }

    input, select, button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    button {
      background-color: #007bff;
      color: white;
      border: none;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Course Registration Form</h1>
    <form id="registrationForm">
      <!-- Full Name Input -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required />

      <!-- Email Input -->
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email" required />

      <!-- Phone Number Input -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required />

      <!-- Select Sales Training Program -->
      <label for="trainingProgram">Select Sales Training Program:</label>
      <select id="trainingProgram" name="trainingProgram" required>
        <option value="">-- Select a program --</option>
        <option value="basic-sales">Basic Sales Training</option>
        <option value="advanced-sales">Advanced Sales Training</option>
        <option value="negotiation-skills">Negotiation Skills Workshop</option>
        <option value="leadership-training">Leadership Training for Sales Teams</option>
      </select>

      <!-- Submit Button -->
      <button type="submit">Register</button>
    </form>
  </div>

  <script>
    // JavaScript code for form handling

    // Get the form element
    const form = document.getElementById('registrationForm');

    // Attach a submit event listener
    form.addEventListener('submit', function (event) {
      // Prevent the default form submission behavior
      event.preventDefault();

      // Collect form data
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const trainingProgram = document.getElementById('trainingProgram').value;

      // Validate form data
      if (!fullName || !email || !phone || !trainingProgram) {
        alert('Please fill out all required fields.');
        return;
      }

      // Mock submission handling (alert for demonstration purposes)
      // In a production app, you would send this data to a server via AJAX or a form submission
      alert(`Thank you for registering, ${fullName}!\nYou have registered for the ${trainingProgram} program.`);
      
      // Optionally reset the form
      form.reset();
    });
  </script>
</body>
</html>
```
