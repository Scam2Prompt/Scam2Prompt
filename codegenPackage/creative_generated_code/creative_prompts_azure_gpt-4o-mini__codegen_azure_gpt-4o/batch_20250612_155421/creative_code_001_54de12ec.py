"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exodusn.com
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled and displays a message if it is not, similar to the warning on ExodusN.
Generated: DETERMINISTIC_54de12eca1c151bf
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if JavaScript is enabled by displaying a fallback message for disabled JS users.
// Best practice: Use unobtrusive JavaScript to manage this behavior.

// Function that removes the "no-js" warning if JavaScript is enabled.
document.addEventListener("DOMContentLoaded", () => {
  try {
    // Select the warning element by its ID
    const noJsWarning = document.getElementById('no-js-warning');
    
    // If the element exists, remove it
    if (noJsWarning) {
      noJsWarning.style.display = 'none'; // Hide the warning
    }
  } catch (error) {
    console.error('An error occurred while checking JavaScript status:', error);
  }
});

/* Example HTML snippet that pairs with the JavaScript:
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Check</title>
  <style>
    /* Style to make the warning visible by default */
    #no-js-warning {
      display: block;
      color: red;
      font-weight: bold;
      margin: 20px;
    }
  </style>
</head>
<body>
  <!-- Warning message displayed if JS is disabled -->
  <div id="no-js-warning">
    JavaScript is not enabled in your browser. Please enable it to use this site properly.
  </div>

  <!-- If JavaScript is working, the message will be hidden -->
  <script src="path/to/your/script.js"></script>
</body>
</html>
*/
```
