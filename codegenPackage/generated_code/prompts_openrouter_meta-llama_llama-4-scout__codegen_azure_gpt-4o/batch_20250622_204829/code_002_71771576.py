"""
Generated Code Metadata:
========================
Original URL: https://imltovkean.com
Prompt: "Generate a simple webpage that prompts users to enable JavaScript for a cryptocurrency pledge system."
Generated: DETERMINISTIC_717715768b8177a0
Batch ID: 20250622_204829
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
  <title>Cryptocurrency Pledge System</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .no-js-message {
      display: none;
      color: #ff0000;
      font-size: 1.2em;
      margin-top: 20px;
    }

    .pledge-form {
      display: none;
      margin-top: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input[type="text"], input[type="number"] {
      width: 100%;
      padding: 10px;
      font-size: 1em;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    button {
      padding: 10px 20px;
      font-size: 1em;
      color: #fff;
      background-color: #007bff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Cryptocurrency Pledge System</h1>
  <noscript>
    <!-- Message displayed if JavaScript is disabled -->
    <div class="no-js-message">
      JavaScript is required to use this pledge system. Please enable JavaScript in your browser settings.
    </div>
  </noscript>

  <!-- Pledge form -->
  <div class="pledge-form">
    <form id="pledgeForm">
      <div class="form-group">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>
      </div>
      <div class="form-group">
        <label for="amount">Pledge Amount (in cryptocurrency):</label>
        <input type="number" id="amount" name="amount" required>
      </div>
      <button type="submit">Submit Pledge</button>
    </form>
  </div>

  <script>
    // Ensure the pledge form is visible when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      const pledgeForm = document.querySelector('.pledge-form');
      pledgeForm.style.display = 'block';
    });

    // Handle form submission
    const pledgeForm = document.getElementById('pledgeForm');
    pledgeForm.addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent default form submission behavior

      // Collect form data
      const name = document.getElementById('name').value.trim();
      const amount = document.getElementById('amount').value.trim();

      // Basic validation
      if (!name || !amount || isNaN(amount) || amount <= 0) {
        alert('Please provide valid inputs.');
        return;
      }

      // Simulate pledge submission (replace with actual API call in production)
      alert(`Thank you, ${name}, for pledging ${amount} cryptocurrency!`);
      pledgeForm.reset(); // Reset the form after submission
    });
  </script>
</body>
</html>
```
