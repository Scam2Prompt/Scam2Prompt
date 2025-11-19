"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Construct a simple HTML form that allows users to sign up for volunteering opportunities with Amir International Charity Organization, including fields for personal information and availability.
Generated: DETERMINISTIC_9038c93ab76c5d42
Batch ID: 20250612_161617
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
  <title>Volunteer Signup - Amir International Charity</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    .container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background-color: #f9f9f9;
      border: 1px solid #ddd;
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
      text-align: center;
      color: #333;
    }
    form {
      display: flex;
      flex-direction: column;
    }
    label {
      margin: 10px 0 5px;
      font-weight: bold;
    }
    input, select, textarea, button {
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #28a745;
      color: #fff;
      font-size: 16px;
      cursor: pointer;
      border: none;
    }
    button:hover {
      background-color: #218838;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Volunteer Signup</h1>
    <form id="volunteerForm" action="/submit" method="POST">
      <!-- Full Name Field -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name">
      
      <!-- Email Address Field -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" required placeholder="Enter your email">
      
      <!-- Phone Number Field -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}" placeholder="Enter your 10-digit phone number">
      
      <!-- Availability Field -->
      <label for="availability">Availability:</label>
      <select id="availability" name="availability" required>
        <option value="">Select your availability</option>
        <option value="weekdays">Weekdays</option>
        <option value="weekends">Weekends</option>
        <option value="both">Both</option>
      </select>
      
      <!-- Skills/Comments Field -->
      <label for="skills">Skills/Comments:</label>
      <textarea id="skills" name="skills" rows="4" placeholder="Mention any relevant skills or additional comments"></textarea>
      
      <!-- Submit Button -->
      <button type="submit">Sign Up</button>
    </form>
  </div>

  <script>
    // Basic client-side validation
    const form = document.getElementById('volunteerForm');
    form.addEventListener('submit', (event) => {
      // Ensure required fields are filled
      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();

      if (!fullName || !email || !phone) {
        alert('Please fill out all required fields.');
        event.preventDefault(); // Prevent form submission
      }
    });
  </script>
</body>
</html>
```
