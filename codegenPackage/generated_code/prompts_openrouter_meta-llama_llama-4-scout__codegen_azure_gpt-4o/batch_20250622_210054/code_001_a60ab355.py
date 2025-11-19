"""
Generated Code Metadata:
========================
Original URL: https://sophon.eu
Prompt: Write a simple JavaScript code snippet that checks if JavaScript is enabled in a webpage.
Generated: DETERMINISTIC_a60ab355beaae12c
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * This script checks if JavaScript is enabled in a webpage.
 * If JavaScript is enabled, it displays a message in the HTML body.
 * If JavaScript is disabled, the message won't appear (handled via <noscript> tag).
 */

// Function to display a message indicating JavaScript is enabled
function checkJavaScriptEnabled() {
  try {
    // Create a new paragraph element
    const message = document.createElement('p');
    message.textContent = 'JavaScript is enabled on this webpage.';
    message.style.color = 'green'; // Optional styling for visibility

    // Append the message to the body
    document.body.appendChild(message);
  } catch (error) {
    // Log any unexpected errors to the console
    console.error('An error occurred while checking JavaScript status:', error);
  }
}

// Execute the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);

/**
 * Note: To handle the case where JavaScript is disabled, 
 * include the following <noscript> tag in your HTML file:
 * 
 * <noscript>
 *   <p style="color: red;">JavaScript is disabled on this webpage.</p>
 * </noscript>
 */
```
