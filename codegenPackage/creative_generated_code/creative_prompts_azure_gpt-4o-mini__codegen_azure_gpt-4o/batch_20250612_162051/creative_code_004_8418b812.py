"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.efeotokurtarma.com.tr
Prompt: Illustrate how to implement a contact form in HTML that connects users to a towing service like Efem Oto Çekici, ensuring it highlights 24/7 support.
Generated: DETERMINISTIC_8418b8128ec43128
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/contact": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Contact Efem Oto Çekici - Your reliable 24/7 towing service provider">
  <title>Efem Oto Çekici - Contact Form</title>
  <style>
    /* Basic styling for the contact form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }

    .form-container {
      max-width: 600px;
      margin: 50px auto;
      background: #ffffff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      padding: 20px;
      border-radius: 8px;
    }

    .form-container h1 {
      text-align: center;
      color: #333333;
    }

    label {
      display: block;
      margin: 15px 0 5px;
      font-weight: bold;
    }

    input, textarea, button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #cccccc;
      border-radius: 4px;
      font-size: 16px;
    }

    button {
      background-color: #007BFF;
      color: #ffffff;
      border: none;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 14px;
    }

    .success-message {
      color: green;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Contact Efem Oto Çekici</h1>
    <p>We provide 24/7 towing services for your convenience.</p>
    <!-- Contact form -->
    <form id="contactForm" action="https://example.com/api/contact" method="POST">
      <label for="name">Full Name:</label>
      <input type="text" id="name" name="name" required placeholder="Enter your full name">

      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" required placeholder="Enter your email address">

      <label for="message">How can we assist you?</label>
      <textarea id="message" name="message" rows="4" required placeholder="Please describe your issue"></textarea>

      <button type="submit">Submit</button>
      <!-- Messages -->
      <p class="error-message" id="errorMessage" style="display: none;">An error occurred. Please try again.</p>
      <p class="success-message" id="successMessage" style="display: none;">Thank you for contacting us! We'll get back to you shortly.</p>
    </form>
  </div>

  <script>
    // JavaScript for handling form submission and showing error/success messages
    document.getElementById('contactForm').addEventListener('submit', async function(event) {
      event.preventDefault(); // Prevent the default form submission

      const form = event.target;
      const formData = new FormData(form);

      // Clear any existing messages
      const errorMessage = document.getElementById('errorMessage');
      const successMessage = document.getElementById('successMessage');
      errorMessage.style.display = 'none';
      successMessage.style.display = 'none';

      try {
        const response = await fetch(form.action, {
          method: form.method,
          body: formData
        });

        if (!response.ok) {
          throw new Error('Failed to submit the form.');
        }

        // Show success message
        successMessage.style.display = 'block';
      } catch (error) {
        // Show error message
        errorMessage.style.display = 'block';
      }
    });
  </script>
</body>
</html>
```
