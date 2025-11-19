"""
Generated Code Metadata:
========================
Original URL: https://mariberica.pt
Prompt: Develop a code snippet to implement a satisfaction survey questionnaire on a website, similar to the one used on Mar Ibérica's website.
Generated: DETERMINISTIC_7d295c4974c9c4f1
Batch ID: 20250622_210316
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
  <title>Satisfaction Survey</title>
  <style>
    /* Basic styling for the survey form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .survey-container {
      max-width: 600px;
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
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input[type="text"], textarea, select {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <div class="survey-container">
    <h1>Satisfaction Survey</h1>
    <form id="surveyForm">
      <!-- Name Field -->
      <div class="form-group">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>
        <span class="error" id="nameError"></span>
      </div>

      <!-- Email Field -->
      <div class="form-group">
        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>
        <span class="error" id="emailError"></span>
      </div>

      <!-- Satisfaction Rating -->
      <div class="form-group">
        <label for="rating">How satisfied are you with our service?</label>
        <select id="rating" name="rating" required>
          <option value="">Select an option</option>
          <option value="Very Satisfied">Very Satisfied</option>
          <option value="Satisfied">Satisfied</option>
          <option value="Neutral">Neutral</option>
          <option value="Dissatisfied">Dissatisfied</option>
          <option value="Very Dissatisfied">Very Dissatisfied</option>
        </select>
        <span class="error" id="ratingError"></span>
      </div>

      <!-- Comments Field -->
      <div class="form-group">
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4"></textarea>
      </div>

      <!-- Submit Button -->
      <button type="submit">Submit</button>
    </form>
  </div>

  <script>
    // JavaScript for form validation and submission
    document.getElementById('surveyForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('ratingError').textContent = '';

      // Validate form fields
      let isValid = true;

      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const rating = document.getElementById('rating').value;

      if (!name) {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
      }

      if (!email) {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Invalid email format.';
        isValid = false;
      }

      if (!rating) {
        document.getElementById('ratingError').textContent = 'Please select a satisfaction rating.';
        isValid = false;
      }

      // If all fields are valid, submit the form
      if (isValid) {
        alert('Thank you for your feedback!');
        // Here you can send the form data to the server using fetch or AJAX
        console.log({
          name: name,
          email: email,
          rating: rating,
          comments: document.getElementById('comments').value.trim()
        });
        // Reset the form
        document.getElementById('surveyForm').reset();
      }
    });
  </script>
</body>
</html>
```
