"""
Generated Code Metadata:
========================
Original URL: https://swapfinderbp.github.io
Prompt: Write a JavaScript code to handle errors or display a message when JavaScript is disabled, similar to the one on the SwapFinderBP website.
Generated: DETERMINISTIC_7a011ebb3f4065b4
Batch ID: 20250622_211454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a noscript element
    const noscriptElement = document.createElement('noscript');
    
    // Create a message element
    const messageElement = document.createElement('div');
    messageElement.textContent = 'Please enable JavaScript to use this website.';
    messageElement.style.color = 'red';
    messageElement.style.fontWeight = 'bold';
    messageElement.style.textAlign = 'center';
    messageElement.style.padding = '1em';
    messageElement.style.backgroundColor = '#f0f0f0';
    messageElement.style.border = '1px solid #ccc';
    messageElement.style.borderRadius = '5px';
    messageElement.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.2)';
    
    // Append message element to noscript element
    noscriptElement.appendChild(messageElement);
    
    // Check if JavaScript is enabled by trying to access document.body
    try {
        // If JavaScript is enabled, this line will execute without errors
        document.body.appendChild(noscriptElement);
        
        // If the noscript element is still present, JavaScript is disabled
        if (document.body.contains(noscriptElement)) {
            // Remove the noscript element
            document.body.removeChild(noscriptElement);
            
            // Display the message
            messageElement.style.position = 'fixed';
            messageElement.style.top = '0';
            messageElement.style.left = '0';
            messageElement.style.width = '100%';
            messageElement.style.zIndex = '1000';
            document.body.appendChild(messageElement);
        }
    } catch (error) {
        // Handle any unexpected errors
        console.error('An unexpected error occurred:', error);
    }
}

// Call the function to check if JavaScript is enabled
checkJavaScriptEnabled();
```
