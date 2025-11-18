"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://la-guarida.com.ar
Prompt: Develop a landing page for a digital campaign, including features such as call-to-action buttons and email subscription forms, inspired by La Guarida's services.
Generated: DETERMINISTIC_3859d1493904b19d
Batch ID: 20250612_155000
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
  <meta name="description" content="Landing page for a digital campaign inspired by La Guarida's services.">
  <title>La Guarida Campaign</title>
  
  <!-- Add modern, responsive CSS with minimal styling -->
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
      color: #333;
    }

    .container {
      max-width: 960px;
      margin: 0 auto;
      padding: 20px;
    }

    header {
      background-color: #444;
      color: white;
      padding: 20px;
      text-align: center;
    }

    header h1 {
      margin: 0;
      font-size: 2.5em;
    }

    .cta {
      margin: 40px 0;
      text-align: center;
    }

    .cta button {
      background-color: #0078d7;
      color: white;
      border: none;
      padding: 15px 30px;
      font-size: 1.2em;
      border-radius: 5px;
      cursor: pointer;
    }

    .cta button:hover {
      background-color: #005bb5;
    }

    .subscribe-form {
      background-color: white;
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      padding: 20px;
      text-align: center;
      margin: 20px auto;
    }

    .subscribe-form h2 {
      font-size: 1.5em;
      margin-bottom: 15px;
    }

    .subscribe-form input[type="email"] {
      width: 80%;
      padding: 10px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .subscribe-form button {
      background-color: #28a745;
      color: white;
      border: none;
      padding: 10px 20px;
      font-size: 1em;
      cursor: pointer;
      border-radius: 3px;
    }

    .subscribe-form button:hover {
      background-color: #218838;
    }

    footer {
      text-align: center;
      padding: 20px;
      background-color: #444;
      color: white;
      margin-top: 40px;
    }

    footer p {
      margin: 0;
    }
  </style>
</head>

<body>

  <!-- Header Section -->
  <header>
    <h1>Welcome to La Guarida Digital Campaign</h1>
  </header>

  <!-- Call-to-Action Section -->
  <div class="container">
    <div class="cta">
      <h2>Discover Our Exclusive Services</h2>
      <button onclick="handleCTAClick()">Learn More</button>
    </div>

    <!-- Email Subscription Form -->
    <div class="subscribe-form">
      <h2>Subscribe to Our Newsletter</h2>
      <form id="subscriptionForm" onsubmit="handleFormSubmit(event)">
        <input type="email" id="emailInput" name="email" placeholder="Enter your email address" required />
        <button type="submit">Subscribe</button>
      </form>
      <p id="successMessage" style="color: green; display: none;">Thank you for subscribing!</p>
      <p id="errorMessage" style="color: red; display: none;">Something went wrong. Please try again.</p>
    </div>
  </div>

  <!-- Footer Section -->
  <footer>
    <p>© 2023 La Guarida. All rights reserved.</p>
  </footer>

  <!-- JavaScript -->
  <script>
    /**
     * Handles click event for the "Learn More" button.
     */
    function handleCTAClick() {
      alert("Thank you for your interest! Visit our website for more information.");
    }

    /**
     * Handles form submission for the subscription.
     * @param {Event} event The form submission event.
     */
    function handleFormSubmit(event) {
      event.preventDefault(); // Prevent form from refreshing the page

      const emailInput = document.getElementById('emailInput');
      const successMessage = document.getElementById('successMessage');
      const errorMessage = document.getElementById('errorMessage');

      // Simple email validation
      if (emailInput.value.trim() === '' || !validateEmail(emailInput.value)) {
        alert('Please enter a valid email address.');
        return;
      }

      // Simulate form submission (in production, send this to a backend)
      try {
        // Simulated success response
        successMessage.style.display = 'block';
        errorMessage.style.display = 'none';
        emailInput.value = ''; // Clear input field
      } catch (e) {
        successMessage.style.display = 'none';
        errorMessage.style.display = 'block';
      }
    }

    /**
     * Validates email format.
     * @param {string} email The email address to validate.
     * @returns {boolean} True if valid, false otherwise.
     */
    function validateEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  </script>

</body>

</html>
```
