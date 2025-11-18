"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.sophon.am
Prompt: Write a JavaScript function to detect if JavaScript is disabled in a browser and display a warning message, similar to the functionality described on the cPanel login page.
Generated: DETERMINISTIC_681a5bf1d2db80bc
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to detect if JavaScript is disabled and display a warning message.
 * This function must be placed in the <body> of the HTML document for it to work.
 */
function detectJavaScriptDisabled() {
  // Check if the browser supports JavaScript
  if (!window || !document) {
    console.error("JavaScript environment not detected.");
    return;
  }

  // Create the warning message element
  const warningMessage = document.createElement('div');
  warningMessage.textContent = 'JavaScript is disabled in your browser. Please enable it for the best experience.';
  warningMessage.style.position = 'fixed';
  warningMessage.style.top = '0';
  warningMessage.style.left = '0';
  warningMessage.style.width = '100%';
  warningMessage.style.backgroundColor = '#ffcc00';
  warningMessage.style.color = '#000';
  warningMessage.style.padding = '10px';
  warningMessage.style.textAlign = 'center';
  warningMessage.style.zIndex = '1000';
  warningMessage.style.fontSize = '18px';
  warningMessage.style.fontFamily = 'Arial, sans-serif';
  warningMessage.style.display = 'none'; // Initially hidden

  // Append the message to the body
  document.body.appendChild(warningMessage);

  // Use a timeout to simulate detection of JavaScript being enabled
  setTimeout(() => {
    // If JavaScript is enabled, the warning message should not appear
    warningMessage.style.display = 'none';
  }, 0);

  // Fallback for browsers with JavaScript disabled
  document.write('<noscript><div style="position:fixed; top:0; left:0; width:100%; background-color:#ffcc00; color:#000; padding:10px; text-align:center; z-index:1000; font-size:18px; font-family:Arial, sans-serif;">JavaScript is disabled in your browser. Please enable it for the best experience.</div></noscript>');
}

// Call the function to ensure the warning message is handled
detectJavaScriptDisabled();
```
