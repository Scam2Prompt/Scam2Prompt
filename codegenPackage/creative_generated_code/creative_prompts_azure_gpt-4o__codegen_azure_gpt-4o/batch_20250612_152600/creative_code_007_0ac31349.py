"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethcll.com
Prompt: Create a responsive web page using HTML, CSS, and JavaScript that allows users to pledge ETH and displays a warning if JavaScript is disabled.
Generated: DETERMINISTIC_0ac31349fd2eb281
Batch ID: 20250612_152600
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
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>ETH Pledge</title>
  <!-- Link to external CSS -->
  <style>
    /* Basic reset */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      color: #333;
    }

    /* Responsive container */
    .container {
      max-width: 600px;
      margin: 2rem auto;
      padding: 1rem;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    /* Heading styling */
    h1 {
      text-align: center;
      color: #444;
    }

    /* Input and button */
    .pledge-form {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .pledge-form input {
      padding: 0.75rem;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .pledge-form button {
      padding: 0.75rem;
      font-size: 1rem;
      color: #fff;
      background-color: #007bff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    .pledge-form button:hover {
      background-color: #0056b3;
    }

    /* Warning for disabled JavaScript */
    .no-js-warning {
      display: none;
      text-align: center;
      color: red;
      font-weight: bold;
    }

    .show-warning {
      display: block;
    }
  </style>
  <script>
    // If JavaScript is enabled, remove the warning
    document.addEventListener('DOMContentLoaded', () => {
      document.getElementById('no-js-warning').classList.remove('show-warning');
    });
  </script>
</head>
<body>
  <!-- Warning message for users with disabled JavaScript -->
  <noscript>
    <div id="no-js-warning" class="no-js-warning show-warning">
      Warning: JavaScript is disabled in your browser. This page requires JavaScript to function properly.
    </div>
  </noscript>

  <!-- Main container -->
  <div class="container">
    <h1>Pledge ETH</h1>
    <p>Enter the amount of ETH you'd like to pledge:</p>
    <!-- ETH Pledge Form -->
    <form id="pledge-form" class="pledge-form">
      <input type="number" step="0.0001" min="0" id="ethAmount" placeholder="Enter ETH amount" required>
      <button type="submit">Pledge</button>
    </form>
    <div id="confirmation-message" style="display: none; text-align: center; margin-top: 1rem;">
      Thanks for your pledge!
    </div>
  </div>

  <!-- JavaScript functionality -->
  <script>
    // Adding event for form handling
    document.getElementById('pledge-form').addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent page reload on form submission
      
      // Safely retrieve entered ETH amount
      const ethAmountInput = document.getElementById('ethAmount');
      const ethAmount = parseFloat(ethAmountInput.value);

      // Validate user input
      if (isNaN(ethAmount) || ethAmount <= 0) {
        alert('Please enter a valid ETH amount greater than 0.');
        return;
      }

      // Display confirmation message
      const confirmationMessage = document.getElementById('confirmation-message');
      confirmationMessage.textContent = `Thanks for pledging ${ethAmount} ETH!`;
      confirmationMessage.style.display = 'block';

      // Clear input field
      ethAmountInput.value = '';
    });
  </script>
</body>
</html>
```
