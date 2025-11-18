"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a warning message if it is disabled.
Generated: DETERMINISTIC_11dfdc564930f674
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled in the browser
 * and display a warning message if it is disabled.
 *
 * Note: JavaScript being disabled cannot be detected while it is running,
 * so this function works in conjunction with a <noscript> block.
 */

// This function will be executed only if JavaScript is enabled.
// The warning message for JavaScript being disabled is typically handled
// through <noscript> HTML tags.

// Example usage: Include this function in your script and ensure
// there's a <noscript> warning in your HTML page.

function checkJavaScriptEnabled() {
  try {
    // Find the <noscript> warning element by its ID
    const noScriptWarning = document.getElementById('no-js-warning');

    // If the <noscript> warning exists, remove it since JavaScript is enabled
    if (noScriptWarning) {
      noScriptWarning.style.display = 'none'; // Hide the warning
    }
  } catch (error) {
    console.error('An error occurred while checking JavaScript status:', error);
  }
}

/**
 * Example usage:
 * Add the following <noscript> block to your HTML to show a warning when JavaScript is disabled:
 * 
 * <noscript>
 *   <div id="no-js-warning" style="color: red; font-weight: bold;">
 *     Warning: JavaScript is disabled in your browser. Please enable it for a better experience.
 *   </div>
 * </noscript>
 */

// Ensure the function runs after DOM content is loaded
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```
