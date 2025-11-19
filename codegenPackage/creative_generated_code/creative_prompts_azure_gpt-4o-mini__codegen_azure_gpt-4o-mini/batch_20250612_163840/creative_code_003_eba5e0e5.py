"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjya.com
Prompt: Generate a JavaScript function that alerts users to enable JavaScript for better experience on ethjya.com.
Generated: DETERMINISTIC_eba5e0e533a544cc
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled and alert the user if it is not.
 * This function is designed to be called on page load.
 */
function checkJavaScriptEnabled() {
    // Check if the JavaScript is enabled by using the 'navigator' object
    if (typeof navigator === 'undefined' || !navigator.javaEnabled()) {
        // Alert the user to enable JavaScript for a better experience
        alert("For a better experience on ethjya.com, please enable JavaScript in your browser.");
    }
}

// Add an event listener to call the function when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", checkJavaScriptEnabled);
```
