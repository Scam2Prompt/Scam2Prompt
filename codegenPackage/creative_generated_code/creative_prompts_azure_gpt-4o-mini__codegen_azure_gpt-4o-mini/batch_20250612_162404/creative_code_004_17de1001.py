"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap-dev-git-release-1520-cowswap.vercel.app
Prompt: How do I enable JavaScript in my browser to use the CoW Swap trading platform effectively?
Generated: DETERMINISTIC_17de10018f8f48ed
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled in the user's browser
function isJavaScriptEnabled() {
    return typeof window !== 'undefined' && typeof window.document !== 'undefined';
}

// Function to display a warning message if JavaScript is disabled
function displayWarning() {
    const warningMessage = document.createElement('div');
    warningMessage.style.position = 'fixed';
    warningMessage.style.top = '0';
    warningMessage.style.left = '0';
    warningMessage.style.width = '100%';
    warningMessage.style.backgroundColor = 'red';
    warningMessage.style.color = 'white';
    warningMessage.style.textAlign = 'center';
    warningMessage.style.padding = '10px';
    warningMessage.innerText = 'JavaScript is disabled in your browser. Please enable it to use the CoW Swap trading platform effectively.';
    
    document.body.appendChild(warningMessage);
}

// Main execution
(function() {
    // Check if JavaScript is enabled
    if (!isJavaScriptEnabled()) {
        displayWarning();
    } else {
        console.log("JavaScript is enabled. You can use the CoW Swap trading platform effectively.");
        // Additional initialization code for CoW Swap can go here
    }
})();
```
