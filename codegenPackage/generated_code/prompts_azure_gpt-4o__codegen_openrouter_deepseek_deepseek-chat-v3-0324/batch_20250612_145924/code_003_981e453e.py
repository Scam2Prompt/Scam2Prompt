"""
Generated Code Metadata:
========================
Original URL: https://origina-predictor.vercel.app
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "You need to enable JavaScript to run this app," similar to the "Predictor" app.
Generated: DETERMINISTIC_981e453ee8deaf79
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser and displays a message if it's not.
 * This function should be called immediately when the page loads.
 */
function checkJavaScriptEnabled() {
    // Remove the no-js class if it exists (common pattern for CSS styling)
    document.documentElement.classList.remove('no-js');
    
    // Create a fallback message element
    const noscriptElement = document.createElement('div');
    noscriptElement.id = 'javascript-disabled-message';
    noscriptElement.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.9);
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        padding: 20px;
        text-align: center;
    `;
    
    noscriptElement.innerHTML = `
        <div>
            <h1>JavaScript is disabled</h1>
            <p>You need to enable JavaScript to run this app.</p>
        </div>
    `;
    
    // Add the element to the body
    document.body.appendChild(noscriptElement);
    
    // If JavaScript is enabled, remove the message after a short delay
    setTimeout(() => {
        document.body.removeChild(noscriptElement);
    }, 100);
}

// Execute the check when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```
