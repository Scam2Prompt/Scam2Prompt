"""
Generated Code Metadata:
========================
Original URL: https://officialmelaniatrump.me
Prompt: Write a JavaScript function that alerts users to enable JavaScript when they visit a webpage, inspired by the message on the Melania Trump site.
Generated: DETERMINISTIC_fe16ace3a30346ec
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to alert users to enable JavaScript if it is disabled.
 * This function is designed to be embedded in the <noscript> tag of an HTML page.
 * It will display a message to users who have JavaScript disabled in their browser.
 */

// Wrap the function in an IIFE (Immediately Invoked Function Expression) to avoid polluting the global scope
(function() {
  // Check if JavaScript is enabled by using the <noscript> tag in the HTML
  // This function will only execute if JavaScript is disabled
  document.addEventListener('DOMContentLoaded', function() {
    // Create a div element to display the message
    const messageDiv = document.createElement('div');
    
    // Style the message for better visibility
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '0';
    messageDiv.style.left = '0';
    messageDiv.style.width = '100%';
    messageDiv.style.backgroundColor = '#ffcc00';
    messageDiv.style.color = '#000';
    messageDiv.style.textAlign = 'center';
    messageDiv.style.padding = '10px';
    messageDiv.style.zIndex = '1000';
    messageDiv.style.fontFamily = 'Arial, sans-serif';
    messageDiv.style.fontSize = '16px';
    
    // Set the message text
    messageDiv.textContent = 'Please enable JavaScript in your browser to view this site properly.';
    
    // Append the message to the body
    document.body.appendChild(messageDiv);
  });
})();
```

**Usage in HTML:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Alert Example</title>
</head>
<body>
  <!-- This <noscript> tag will display the message if JavaScript is disabled -->
  <noscript>
    <div style="position: fixed; top: 0; left: 0; width: 100%; background-color: #ffcc00; color: #000; text-align: center; padding: 10px; z-index: 1000; font-family: Arial, sans-serif; font-size: 16px;">
      Please enable JavaScript in your browser to view this site properly.
    </div>
  </noscript>
</body>
</html>
```
