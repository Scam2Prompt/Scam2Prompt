"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btccetc.com
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled on a mobile browser for the BTC Pledge site.
Generated: DETERMINISTIC_cb08218f902d10b2
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled on a mobile browser
function isJavaScriptEnabled() {
    // Create a temporary <noscript> element
    const noScriptElement = document.createElement('noscript');
    
    // Append the element to the body (it won't be visible)
    document.body.appendChild(noScriptElement);
    
    // Check if the <noscript> element has been added to the body
    const isEnabled = noScriptElement.offsetHeight === 0;
    
    // Remove the <noscript> element from the body
    document.body.removeChild(noScriptElement);
    
    return isEnabled;
}

// Function to execute when the page loads
function onDocumentReady() {
    // Check if the user is on a mobile device
    const isMobile = /Mobi|Android/i.test(navigator.userAgent);
    
    // Check if JavaScript is enabled
    if (isMobile) {
        if (isJavaScriptEnabled()) {
            console.log("JavaScript is enabled on this mobile browser.");
            // Additional logic for when JavaScript is enabled can go here
        } else {
            console.warn("JavaScript is disabled on this mobile browser. Please enable it for better functionality.");
            // You can redirect users or show a message here
        }
    } else {
        console.log("This is not a mobile browser.");
    }
}

// Execute onDocumentReady once the DOM is fully loaded
document.addEventListener("DOMContentLoaded", onDocumentReady);
```
