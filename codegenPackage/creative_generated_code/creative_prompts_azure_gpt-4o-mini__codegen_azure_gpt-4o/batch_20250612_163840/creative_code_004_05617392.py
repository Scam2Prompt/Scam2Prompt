"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjya.com
Prompt: How do I create a fallback message for users without JavaScript on a BTC-related website?
Generated: DETERMINISTIC_056173925053ca10
Batch ID: 20250612_163840
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
  <title>Bitcoin Website</title>
  <style>
    /* Styling for the fallback message */
    .no-js-message {
      color: #ff0000; /* Red text for visibility */
      background-color: #fff8e6; /* Light background */
      padding: 15px;
      border: 1px solid #ffcc00; /* Yellow border */
      border-radius: 5px;
      text-align: center;
      font-family: Arial, sans-serif;
      font-size: 16px;
      margin: 20px auto;
      max-width: 600px;
    }

    /* Hide the fallback message by default */
    .no-js-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Fallback message for users without JavaScript -->
  <div class="no-js-message">
    It seems that you have disabled JavaScript or your browser does not support it.<br>
    Please enable JavaScript to view the Bitcoin-related features on our website.
  </div>

  <script>
    // JavaScript to hide the fallback message when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      const fallbackMessage = document.querySelector('.no-js-message');
      
      if (fallbackMessage) {
        // Hide the fallback message since JavaScript is enabled
        fallbackMessage.style.display = 'none';
      }
    });
  </script>

  <!-- Content of the website -->
  <div id="main-content">
    <h1>Welcome to the Bitcoin Website!</h1>
    <p>Explore the latest BTC prices and trends.</p>
  </div>
</body>
</html>
```
