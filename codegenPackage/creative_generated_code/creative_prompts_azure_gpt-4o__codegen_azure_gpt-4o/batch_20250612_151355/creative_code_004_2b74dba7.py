"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaks.xyz
Prompt: Generate HTML and CSS code for a responsive contact form, including fields for name, email, phone number, and message, inspired by the contact section on Ayoft's website.
Generated: DETERMINISTIC_2b74dba734fc706d
Batch ID: 20250612_151355
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
  <title>Responsive Contact Form</title>
  <style>
    /* Global styles */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    /* Contact form container */
    .contact-form-container {
      max-width: 600px;
      margin: 50px auto;
      background: #ffffff;
      border-radius: 8px;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
      padding: 20px;
    }

    /* Form heading */
    .contact-form-container h2 {
      text-align: center;
      color: #333333;
      margin-bottom: 20px;
    }

    /* Form group styling */
    .form-group {
      margin-bottom: 15px;
    }

    /* Labels */
    .form-group label {
      display: block;
      margin-bottom: 5px;
      color: #555555;
      font-weight: bold;
    }

    /* Input fields */
    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #cccccc;
      border-radius: 5px;
      font-size: 16px;
      color: #333333;
    }

    /* Textarea adjustments */
    .form-group textarea {
      resize: vertical;
      height: 100px;
    }

    /* Submit button */
    .form-group button {
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      border: none;
      border-radius: 5px;
      color: white;
      font-size: 16px;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    /* Button hover effect */
    .form-group button:hover {
      background-color: #0056b3;
    }

    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
      .contact-form-container {
        margin: 20px;
        padding: 15px;
      }
    }
  </style>
</head>
<body>
  <div class="contact-form-container">
    <!-- Contact form heading -->
    <h2>Contact Us</h2>
    <!-- Contact form -->
    <form action="/submit-form" method="POST">
      <!-- Name field -->
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" placeholder="Your Name" required>
      </div>
      <!-- Email field -->
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Your Email Address" required>
      </div>
      <!-- Phone number field -->
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="Your Phone Number" pattern="[0-9]{10}">
      </div>
      <!-- Message field -->
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" placeholder="Your Message" required></textarea>
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
