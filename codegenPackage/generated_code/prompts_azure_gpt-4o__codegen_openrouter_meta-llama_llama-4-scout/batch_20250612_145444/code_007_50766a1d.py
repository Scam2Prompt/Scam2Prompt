"""
Generated Code Metadata:
========================
Original URL: https://morpho-frontend.pages.dev
Prompt: Develop a JavaScript snippet to display a warning message if JavaScript is disabled in a Morpho-based app.
Generated: DETERMINISTIC_50766a1d11192944
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled
function checkJavascriptEnabled() {
    // Create a noscript element
    const noscriptElement = document.createElement('noscript');
    
    // Create a warning message element
    const warningMessageElement = document.createElement('div');
    warningMessageElement.textContent = 'Warning: JavaScript is disabled. Please enable JavaScript to use this app.';
    warningMessageElement.style.color = 'red';
    warningMessageElement.style.fontWeight = 'bold';
    warningMessageElement.style.padding = '10px';
    warningMessageElement.style.textAlign = 'center';

    // Append the warning message to the noscript element
    noscriptElement.appendChild(warningMessageElement);

    // Append the noscript element to the body
    document.body.appendChild(noscriptElement);

    // Check if the noscript element is still present
    // If JavaScript is enabled, this element will be removed from the DOM
    try {
        // Try to access the noscript element
        const noscriptCheck = document.querySelector('noscript');
        
        // If the noscript element is still present, JavaScript is disabled
        if (noscriptCheck) {
            // Display the warning message
            warningMessageElement.style.display = 'block';
        } else {
            // If JavaScript is enabled, remove the noscript element
            noscriptElement.remove();
        }
    } catch (error) {
        // Handle any errors that occur during the check
        console.error('Error checking JavaScript status:', error);
    }
}

// Call the function to check JavaScript status
checkJavascriptEnabled();
```
