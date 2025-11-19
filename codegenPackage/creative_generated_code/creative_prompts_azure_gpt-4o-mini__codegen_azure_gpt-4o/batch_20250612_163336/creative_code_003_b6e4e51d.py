"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startec.com.my
Prompt: How can I implement a contact form using HTML and JavaScript for a computer hardware store's website, inspired by the contact details provided by StarTec?
Generated: DETERMINISTIC_b6e4e51dfb38d398
Batch ID: 20250612_163336
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
  <title>Contact Form - Computer Hardware Store</title>
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
      background-color: #f9f9f9;
    }

    .contact-form {
      background: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    .contact-form h2 {
      margin-bottom: 10px;
      font-size: 24px;
      text-align: center;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
    }

    .form-group textarea {
      resize: vertical;
      height: 100px;
    }

    .form-group button {
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #ffffff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    .form-group button:hover {
      background-color: #0056b3;
    }

    .success-message,
    .error-message {
      text-align: center;
      margin-top: 15px;
      font-size: 14px;
    }

    .success-message {
      color: green;
    }

    .error-message {
      color: red;
    }
  </style>
</head>
<body>
  <div class="contact-form">
    <h2>Contact Us</h2>
    <form id="contactForm">
      <!-- Full Name Input -->
      <div class="form-group">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
      </div>

      <!-- Email Input -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>

      <!-- Message Input -->
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" placeholder="Write your message here..." required></textarea>
      </div>

      <!-- Submit Button -->
      <div class="form-group">
        <button type="submit">Submit</button>
      </div>

      <!-- Feedback Messages -->
      <div class="success-message" id="successMessage" style="display: none;">Your message has been sent successfully!</div>
      <div class="error-message" id="errorMessage" style="display: none;">Oops! Something went wrong. Please try again.</div>
    </form>
  </div>

  <script>
    // JavaScript to handle form submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();

      // Validate inputs
      if (!name || !email || !message) {
        document.getElementById('errorMessage').textContent = 'Please fill in all required fields.';
        document.getElementById('errorMessage').style.display = 'block';
        return;
      }

      // Mock send message logic (replace with actual server request if needed)
      try {
        // Simulate success response
        document.getElementById('successMessage').style.display = 'block';
        document.getElementById('errorMessage').style.display = 'none';

        // Reset the form
        document.getElementById('contactForm').reset();
      } catch (error) {
        // Handle error (e.g., network issues)
        document.getElementById('errorMessage').textContent = 'Failed to send your message. Please try again later.';
        document.getElementById('errorMessage').style.display = 'block';
        document.getElementById('successMessage').style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
