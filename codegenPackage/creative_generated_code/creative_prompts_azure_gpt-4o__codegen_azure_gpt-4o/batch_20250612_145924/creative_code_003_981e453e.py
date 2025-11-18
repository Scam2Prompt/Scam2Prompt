"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origina-predictor.vercel.app
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "You need to enable JavaScript to run this app," similar to the "Predictor" app.
Generated: DETERMINISTIC_981e453ee8deaf79
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled and display a message if it's disabled.
 * Since JavaScript is required to run this function, it effectively checks if JavaScript is enabled.
 * If JavaScript were disabled, the fallback message created in `<noscript>` tags would be displayed instead.
 */
function checkJavaScriptEnabled() {
    // Create a message container
    const messageContainer = document.createElement('div');
    messageContainer.id = 'js-check-message';
    messageContainer.style.display = 'none'; // It's initially hidden unless needed
    messageContainer.style.fontFamily = 'Arial, sans-serif';
    messageContainer.style.color = 'red';
    messageContainer.style.padding = '10px';
    messageContainer.style.backgroundColor = '#ffe6e6';
    messageContainer.style.border = '1px solid #ff9999';
    messageContainer.style.margin = '10px 0';
    messageContainer.textContent = 'You need to enable JavaScript to run this app.';
  
    // Append the message container to the body
    document.body.appendChild(messageContainer);

    // Simulate the behavior when JavaScript is enabled
    // Hide any noscript fallback messages (if present) because JavaScript is running
    const noscriptElements = document.querySelectorAll('noscript');
    noscriptElements.forEach((element) => {
        element.style.display = 'none';
    });
}

// Execute the function once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);

/*
 * Fallback message for users who have JavaScript disabled.
 * This `<noscript>` block will only be displayed when JavaScript is disabled.
 * You can insert this block manually in your HTML file.
 * Example:
 * <noscript>
 *   <div style="font-family: Arial, sans-serif; color: red; padding: 10px; background-color: #ffe6e6; border: 1px solid #ff9999; margin: 10px 0;">
 *     You need to enable JavaScript to run this app.
 *   </div>
 * </noscript>
 */
```
