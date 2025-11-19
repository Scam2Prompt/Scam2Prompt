"""
Generated Code Metadata:
========================
Original URL: https://ethpai.com
Prompt: Generate HTML and JavaScript code for a simple pledge platform that requires JavaScript to be enabled.
Generated: DETERMINISTIC_8bcfac65d037e489
Batch ID: 20250622_211918
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
  <title>Pledge Platform</title>
  <style>
    /* Basic styling for the pledge platform */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .container {
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

    form {
      display: flex;
      flex-direction: column;
    }

    label {
      margin-bottom: 10px;
      font-weight: bold;
    }

    input[type="text"], input[type="email"], textarea {
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 4px;
      width: 100%;
    }

    button {
      padding: 10px 15px;
      background-color: #28a745;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background-color: #218838;
    }

    .message {
      margin-top: 20px;
      text-align: center;
      font-size: 1.2em;
      color: #28a745;
    }

    .no-js {
      text-align: center;
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js">JavaScript is required to use this platform. Please enable JavaScript in your browser.</div>
  </noscript>

  <div class="container">
    <h1>Make a Pledge</h1>
    <form id="pledgeForm">
      <label for="name">Your Name:</label>
      <input type="text" id="name" name="name" required placeholder="Enter your name">

      <label for="email">Your Email:</label>
      <input type="email" id="email" name="email" required placeholder="Enter your email">

      <label for="pledge">Your Pledge:</label>
      <textarea id="pledge" name="pledge" rows="4" required placeholder="Enter your pledge"></textarea>

      <button type="submit">Submit Pledge</button>
    </form>
    <div id="message" class="message"></div>
  </div>

  <script>
    // Wait for the DOM to load before executing JavaScript
    document.addEventListener('DOMContentLoaded', () => {
      const form = document.getElementById('pledgeForm');
      const messageDiv = document.getElementById('message');

      // Handle form submission
      form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the default form submission behavior

        // Retrieve form values
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const pledge = document.getElementById('pledge').value.trim();

        // Basic validation
        if (!name || !email || !pledge) {
          alert('Please fill out all fields.');
          return;
        }

        // Simulate successful submission
        messageDiv.textContent = `Thank you, ${name}, for your pledge!`;
        form.reset(); // Clear the form
      });
    });
  </script>
</body>
</html>
```
