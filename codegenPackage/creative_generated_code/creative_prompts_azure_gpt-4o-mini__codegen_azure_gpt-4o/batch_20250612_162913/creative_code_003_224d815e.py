"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Develop a simple HTML form to collect user feedback about their experience with First Crack Coffee Roasters' products.
Generated: DETERMINISTIC_224d815e78cf8d68
Batch ID: 20250612_162913
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
  <meta name="description" content="Feedback form for First Crack Coffee Roasters">
  <title>Feedback Form - First Crack Coffee Roasters</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }
    .container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1 {
      font-size: 24px;
      margin-bottom: 20px;
      text-align: center;
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    label {
      font-weight: bold;
    }
    input, textarea, button, select {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #007BFF;
      color: white;
      font-size: 16px;
      font-weight: bold;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 0.9em;
      margin-top: -10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Feedback Form</h1>
    <form id="feedbackForm">
      <!-- Full Name -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
      <div id="nameError" class="error"></div>

      <!-- Email Address -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email address" required>
      <div id="emailError" class="error"></div>

      <!-- Product Rating -->
      <label for="rating">Product Rating:</label>
      <select id="rating" name="rating" required>
        <option value="" disabled selected>Select a rating</option>
        <option value="1">1 - Very Dissatisfied</option>
        <option value="2">2 - Dissatisfied</option>
        <option value="3">3 - Neutral</option>
        <option value="4">4 - Satisfied</option>
        <option value="5">5 - Very Satisfied</option>
      </select>
      <div id="ratingError" class="error"></div>

      <!-- Comments -->
      <label for="comments">Comments:</label>
      <textarea id="comments" name="comments" rows="5" placeholder="Share your thoughts about our products"></textarea>

      <!-- Submit Button -->
      <button type="submit">Submit Feedback</button>
    </form>
  </div>

  <!-- JavaScript for Form Validation -->
  <script>
    document.getElementById('feedbackForm').addEventListener('submit', function(event) {
      // Prevent form submission
      event.preventDefault();

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('ratingError').textContent = '';

      // Form validation
      let isValid = true;

      const fullName = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const rating = document.getElementById('rating').value;

      // Validate full name
      if (fullName.length < 2) {
        document.getElementById('nameError').textContent = 'Full name must be at least 2 characters.';
        isValid = false;
      }

      // Validate email
      const emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
      if (!emailPattern.test(email)) {
        document.getElementById('emailError').textContent = 'Enter a valid email address.';
        isValid = false;
      }

      // Validate rating
      if (!rating) {
        document.getElementById('ratingError').textContent = 'Please select a rating.';
        isValid = false;
      }

      // If form is valid, display a success message
      if (isValid) {
        alert('Thank you for your feedback!');
        // Optionally, reset the form
        document.getElementById('feedbackForm').reset();
      }
    });
  </script>
</body>
</html>
```
