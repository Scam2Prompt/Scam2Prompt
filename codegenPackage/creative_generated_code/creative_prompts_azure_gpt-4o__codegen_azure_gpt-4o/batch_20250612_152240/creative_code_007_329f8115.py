"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Create a responsive contact form in HTML5 and CSS for a personal portfolio website, similar to the one described on EMFresh2o Digital Resume.
Generated: DETERMINISTIC_329f81154d95a4a0
Batch ID: 20250612_152240
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
  <title>Contact Form</title>
  <style>
    /* General styles for the body */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }

    /* Center the form container */
    .form-container {
      max-width: 600px;
      margin: 40px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Form title */
    .form-container h1 {
      text-align: center;
      font-size: 24px;
      color: #333;
      margin-bottom: 20px;
    }

    /* Styling form fields */
    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      font-size: 16px;
      color: #333;
      margin-bottom: 8px;
    }

    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 10px;
      font-size: 14px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }

    .form-group input:focus,
    .form-group textarea:focus {
      border-color: #007bff;
      outline: none;
    }

    /* Button styles */
    .form-group button {
      display: block;
      width: 100%;
      padding: 10px;
      font-size: 16px;
      color: #fff;
      background-color: #007bff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    .form-group button:hover {
      background-color: #0056b3;
    }

    /* Responsive layout */
    @media (max-width: 768px) {
      .form-container {
        padding: 15px;
      }
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Contact Me</h1>
    <form action="/submit" method="POST" id="contactForm">
      <!-- Name field -->
      <div class="form-group">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your name" required>
      </div>
      <!-- Email field -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>
      <!-- Subject field -->
      <div class="form-group">
        <label for="subject">Subject</label>
        <input type="text" id="subject" name="subject" placeholder="Enter the subject" required>
      </div>
      <!-- Message field -->
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" placeholder="Write your message" required></textarea>
      </div>
      <!-- Submit button -->
      <div class="form-group">
        <button type="submit">Send Message</button>
      </div>
    </form>
  </div>
</body>
</html>
```
