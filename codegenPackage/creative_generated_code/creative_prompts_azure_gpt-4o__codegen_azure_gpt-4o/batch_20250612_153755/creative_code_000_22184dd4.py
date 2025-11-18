"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://account.coinbasenft.de
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it, similar to the behavior on the Coinbase NFT domain details page.
Generated: DETERMINISTIC_22184dd453586955
Batch ID: 20250612_153755
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
    /* Default message for when JavaScript is disabled */
    #js-disabled-message {
      display: block;
      font-family: Arial, sans-serif;
      color: red;
      text-align: center;
      padding: 20px;
    }

    /* Hide the message when JavaScript is enabled */
    .js-enabled #js-disabled-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <div id="js-disabled-message">
    It seems that JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
  </div>

  <script>
    /**
     * This script detects if JavaScript is enabled by dynamically adding a class
     * to the <body> element, which hides the fall-back message using CSS.
     */
    try {
      // Add the 'js-enabled' class to the <body> element to hide the message
      document.body.classList.add('js-enabled');
    } catch (error) {
      // Log any unexpected errors to the console
      console.error('An error occurred while detecting JavaScript status:', error);
    }
  </script>
</body>
</html>
```
