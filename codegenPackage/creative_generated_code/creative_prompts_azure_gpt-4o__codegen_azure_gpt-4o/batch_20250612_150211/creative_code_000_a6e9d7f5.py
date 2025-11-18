"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cxconnect1-dss.coinbase.co.za
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message prompting them to enable it, similar to the behavior on the Coinbase domain details page.
Generated: DETERMINISTIC_a6e9d7f596d49baa
Batch ID: 20250612_150211
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
  <title>JavaScript Detection</title>
  <style>
    /* Message styling for when JavaScript is disabled */
    #js-disabled-message {
      display: none;
      text-align: center;
      font-family: Arial, sans-serif;
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      padding: 1rem;
      margin: 2rem;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <!-- Message displayed when JavaScript is disabled -->
  <noscript>
    <div id="js-disabled-message">
      <p><strong>JavaScript is disabled on your browser.</strong></p>
      <p>Please enable JavaScript to experience all features of this website.</p>
    </div>
  </noscript>

  <!-- Main content that requires JavaScript -->
  <div id="main-content">
    <h1>Welcome to Our Website</h1>
    <p>This content will only be visible if JavaScript is enabled.</p>
  </div>

  <script>
    // Ensure the main content is visible if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      try {
        const mainContent = document.getElementById('main-content');
        if (mainContent) {
          mainContent.style.display = 'block';
        }
      } catch (error) {
        // Log any unexpected errors
        console.error('An error occurred while detecting JavaScript:', error);
      }
    });
  </script>
</body>
</html>
```
