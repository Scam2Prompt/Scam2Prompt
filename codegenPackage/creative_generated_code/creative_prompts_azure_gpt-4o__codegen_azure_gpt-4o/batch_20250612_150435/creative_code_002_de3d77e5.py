"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gombke.pages.dev
Prompt: Generate a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "You need to enable JavaScript to run this app," similar to the GOMBLE Wallet Checker website.
Generated: DETERMINISTIC_de3d77e5b226f71e
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled and display a message if it's not.
 * This check is mostly done by using the <noscript> HTML tag.
 * The JavaScript portion here ensures proper handling when JS is enabled.
 */

// Function to display a message if JavaScript is disabled (fallback for <noscript>)
function checkJavaScriptEnabled() {
  try {
    // Select the placeholder element where the "JS Disabled" message might be shown
    const noJsMessage = document.getElementById('no-js-message');

    // If the message exists (added via <noscript>), remove it since JS is enabled
    if (noJsMessage) {
      noJsMessage.style.display = 'none';
    }
  } catch (error) {
    // Log error to console if any unexpected issue occurs
    console.error('An error occurred while checking JavaScript status:', error);
  }
}

// Call the function on page load
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```

```html
<!-- Example HTML usage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Check</title>
  <style>
    /* Style for the no-JS message */
    #no-js-message {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">You need to enable JavaScript to run this app.</div>
  </noscript>

  <script src="script.js"></script>
</body>
</html>
```
