"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-echo.pages.dev
Prompt: Create a JavaScript-based landing page that includes an early access signup form and social media follow buttons, similar to the Echo Beta website.
Generated: DETERMINISTIC_279059db6c7c63b5
Batch ID: 20250612_153225
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://facebook.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://instagram.com": {
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
  <meta name="description" content="Sign up for early access to our platform and follow us on social media.">
  <title>Early Access Landing Page</title>
  <style>
    /* Basic styles for the landing page */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      text-align: center;
      background-color: #f4f4f4;
      color: #333;
    }

    header {
      background-color: #6200ea;
      color: #fff;
      padding: 20px 0;
    }

    header h1 {
      margin: 0;
    }

    main {
      padding: 40px 20px;
    }

    .signup-form {
      max-width: 400px;
      margin: 0 auto;
      background: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .signup-form input,
    .signup-form button {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      border-radius: 5px;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }

    .signup-form button {
      background-color: #6200ea;
      color: #fff;
      border: none;
      cursor: pointer;
    }

    .signup-form button:hover {
      background-color: #4500b5;
    }

    .social-buttons a {
      text-decoration: none;
      margin: 0 10px;
      color: #fff;
      padding: 10px 20px;
      border-radius: 5px;
      display: inline-block;
    }

    .social-buttons a.facebook {
      background-color: #3b5998;
    }

    .social-buttons a.twitter {
      background-color: #1da1f2;
    }

    .social-buttons a.instagram {
      background-color: #e4405f;
    }
  </style>
</head>
<body>
  <header>
    <h1>Welcome to Echo Beta</h1>
    <p>Be the first to experience our new platform.</p>
  </header>

  <main>
    <!-- Early Access Signup Form -->
    <section>
      <div class="signup-form">
        <h2>Sign Up for Early Access</h2>
        <form id="signupForm">
          <input type="text" id="name" name="name" placeholder="Your Name" required>
          <input type="email" id="email" name="email" placeholder="Your Email" required>
          <button type="submit">Sign Up</button>
        </form>
        <p id="formMessage" style="color: green; display: none;">Thank you for signing up!</p>
      </div>
    </section>

    <!-- Social Media Follow Buttons -->
    <section>
      <h2>Follow Us on Social Media</h2>
      <div class="social-buttons">
        <a href="https://facebook.com" class="facebook" target="_blank">Facebook</a>
        <a href="https://twitter.com" class="twitter" target="_blank">Twitter</a>
        <a href="https://instagram.com" class="instagram" target="_blank">Instagram</a>
      </div>
    </section>
  </main>

  <footer>
    <p>&copy; 2023 Echo Beta. All rights reserved.</p>
  </footer>

  <script>
    // Handle form submission and display a success message
    document.getElementById('signupForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent default form submission behavior

      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();

      if (!name || !email) {
        alert('Please fill out both fields.');
        return; // Exit if validation fails
      }

      // Simulate form submission (you can replace this with actual API call)
      console.log('Form submitted:', { name, email });

      // Show success message and reset the form
      document.getElementById('formMessage').style.display = 'block';
      document.getElementById('signupForm').reset();
    });

    // Error handling can be added for actual API calls if required
  </script>
</body>
</html>
```
