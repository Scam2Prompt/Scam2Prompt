"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonbd.com
Prompt: Write a JavaScript function that checks if JavaScript is enabled on a mobile browser and prompts the user to enable it if not.
Generated: DETERMINISTIC_c4477a5c9a4e60b6
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if JavaScript is enabled in the mobile browser.
 * If JavaScript is not enabled, prompts the user to enable it.
 */
function checkJavaScriptEnabled() {
    // Create a div element to test if JavaScript is enabled
    const testDiv = document.createElement('div');
    testDiv.setAttribute('id', 'js-enabled-test');
    testDiv.innerHTML = 'JavaScript is enabled';
    
    // Append the test div to the body
    document.body.appendChild(testDiv);

    // Check if the test element is present in the DOM
    if (document.getElementById('js-enabled-test')) {
        // JavaScript is enabled, remove the test div
        document.body.removeChild(testDiv);
    } else {
        // JavaScript is not enabled, prompt the user
        alert('JavaScript is disabled in your browser. Please enable it for a better experience.');
    }
}

// Call the function to perform the check
checkJavaScriptEnabled();
```
