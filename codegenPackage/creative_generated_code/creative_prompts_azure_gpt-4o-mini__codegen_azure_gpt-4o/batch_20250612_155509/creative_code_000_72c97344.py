"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qwaliconnect.com
Prompt: Generate a code snippet for a contact form that captures user input similar to the one described on Qwali Connect's contact page.
Generated: DETERMINISTIC_72c9734497e38c72
Batch ID: 20250612_155509
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
    /* Basic styling for the contact form */
    .contact-form {
      max-width: 500px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
    }

    .contact-form h1 {
      text-align: center;
    }

    .contact-form label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .contact-form input,
    .contact-form textarea,
    .contact-form button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 3px;
      font-size: 16px;
    }

    .contact-form button {
      background-color: #007BFF;
      color: #fff;
      border: none;
      cursor: pointer;
    }

    .contact-form button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <form class="contact-form" id="contactForm">
    <h1>Contact Us</h1>
    
    <!-- Name field -->
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required placeholder="Your full name">

    <!-- Email field -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required placeholder="Your email address">

    <!-- Subject field -->
    <label for="subject">Subject:</label>
    <input type="text" id="subject" name="subject" required placeholder="Subject of your message">

    <!-- Message field -->
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="5" required placeholder="Your message"></textarea>

    <!-- Submit button -->
    <button type="submit">Send Message</button>
  </form>

  <script>
    // Attach event listener to the form for submission handling
    document.getElementById('contactForm').addEventListener('submit', async function(event) {
      event.preventDefault(); // Prevent default form submission

      // Gather form data
      const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value
      };

      // Basic validation (example)
      if (!formData.name || !formData.email || !formData.subject || !formData.message) {
        alert('Please fill in all fields.');
        return;
      }

      try {
        // Simulate form submission (replace with actual API endpoint if needed)
        const response = await fetch('/api/contact', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        });

        if (!response.ok) {
          throw new Error('Failed to submit the form. Please try again.');
        }

        // Notify the user of the successful form submission
        alert('Your message has been sent successfully!');
        document.getElementById('contactForm').reset(); // Reset form fields
      } catch (error) {
        // Handle errors and notify the user
        alert(`Error: ${error.message}`);
      }
    });
  </script>
</body>
</html>
```
