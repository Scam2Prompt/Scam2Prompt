"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plausivelsolucoes.online
Prompt: Develop a simple HTML form for users to register for courses on the Plausivel Soluções platform, including fields for name, email, and selected course.
Generated: DETERMINISTIC_b2709806575e2203
Batch ID: 20250612_160711
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
  <title>Course Registration</title>
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
    .form-container {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }
    .form-container h1 {
      font-size: 24px;
      margin-bottom: 20px;
      color: #333;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }
    .form-group input, .form-group select {
      width: 100%;
      padding: 10px;
      box-sizing: border-box;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .form-group input:focus, .form-group select:focus {
      border-color: #007bff;
      outline: none;
    }
    .form-group .error {
      color: red;
      font-size: 12px;
      margin-top: 5px;
    }
    .form-container button {
      background-color: #007bff;
      color: #fff;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
    }
    .form-container button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Course Registration</h1>
    <form id="registration-form">
      <!-- Name field -->
      <div class="form-group">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your name" required />
        <div class="error" id="name-error"></div>
      </div>
      <!-- Email field -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required />
        <div class="error" id="email-error"></div>
      </div>
      <!-- Course selection -->
      <div class="form-group">
        <label for="course">Select Course</label>
        <select id="course" name="course" required>
          <option value="">-- Choose a course --</option>
          <option value="web-development">Web Development</option>
          <option value="data-science">Data Science</option>
          <option value="machine-learning">Machine Learning</option>
        </select>
        <div class="error" id="course-error"></div>
      </div>
      <!-- Submit button -->
      <button type="submit">Register</button>
    </form>
  </div>

  <script>
    // Attach event listener for form submission
    const form = document.getElementById('registration-form');
    form.addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent default form submission behavior
      
      // Clear previous error messages
      document.getElementById('name-error').textContent = '';
      document.getElementById('email-error').textContent = '';
      document.getElementById('course-error').textContent = '';

      // Validate form fields
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const course = document.getElementById('course').value;

      let isValid = true;

      // Name validation
      if (name === '') {
        document.getElementById('name-error').textContent = 'Name is required.';
        isValid = false;
      }

      // Email validation
      if (email === '') {
        document.getElementById('email-error').textContent = 'Email is required.';
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('email-error').textContent = 'Invalid email format.';
        isValid = false;
      }

      // Course validation
      if (course === '') {
        document.getElementById('course-error').textContent = 'Please select a course.';
        isValid = false;
      }

      // If validation passes, submit the form data
      if (isValid) {
        alert('Registration successful!');
        // In production, you would typically send the data to a server here.
        form.reset(); // Reset the form
      }
    });
  </script>
</body>
</html>
```
