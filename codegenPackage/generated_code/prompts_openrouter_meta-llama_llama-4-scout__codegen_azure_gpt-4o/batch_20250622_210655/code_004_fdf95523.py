"""
Generated Code Metadata:
========================
Original URL: https://www.haim-lawyer.co.il
Prompt: Generate a code snippet for a simple contact form, similar to the one on the haim-lawyer.co.il website, that captures the user's name, email, phone number, and message.
Generated: DETERMINISTIC_fdf9552313d431ed
Batch ID: 20250622_210655
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
  <title>Contact Form</title>
  <style>
    /* Basic styling for the contact form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    .contact-form {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    .contact-form h2 {
      margin-bottom: 20px;
      font-size: 24px;
      text-align: center;
    }

    .contact-form label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .contact-form input,
    .contact-form textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    .contact-form button {
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    .contact-form button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <form class="contact-form" id="contactForm">
    <h2>Contact Us</h2>
    <!-- Name field -->
    <label for="name">Name</label>
    <input type="text" id="name" name="name" placeholder="Your name" required>

    <!-- Email field -->
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your email" required>

    <!-- Phone number field -->
    <label for="phone">Phone Number</label>
    <input type="tel" id="phone" name="phone" placeholder="Your phone number" required>

    <!-- Message field -->
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="5" placeholder="Your message" required></textarea>

    <!-- Submit button -->
    <button type="submit">Send Message</button>
  </form>

  <script>
    // JavaScript to handle form submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      // Capture form data
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const message = document.getElementById('message').value.trim();

      // Basic validation
      if (!name || !email || !phone || !message) {
        alert('Please fill out all fields.');
        return;
      }

      // Simulate form submission (replace with actual API call in production)
      console.log('Form submitted:', { name, email, phone, message });
      alert('Thank you for your message! We will get back to you soon.');

      // Reset the form
      document.getElementById('contactForm').reset();
    });
  </script>
</body>
</html>
```
