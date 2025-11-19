"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ravitechworld.com
Prompt: How can I enable JavaScript in my browser to access web applications effectively?
Generated: DETERMINISTIC_c997b564f0d31502
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled in the browser
function checkJavaScriptEnabled() {
    // Create a div element to test JavaScript functionality
    const testDiv = document.createElement('div');
    testDiv.id = 'js-test';

    // Set a property that should only be set if JavaScript is enabled
    testDiv.innerHTML = 'JavaScript is enabled!';

    // Append the test div to the body
    document.body.appendChild(testDiv);

    // Check if the test div is correctly updated
    if (testDiv.innerHTML === 'JavaScript is enabled!') {
        console.log('JavaScript is enabled in this browser.');
    } else {
        console.error('JavaScript is not enabled in this browser.');
    }

    // Remove the test div after testing
    document.body.removeChild(testDiv);
}

// Execute the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    try {
        checkJavaScriptEnabled();
    } catch (error) {
        // Log any errors that occur during the check
        console.error('An error occurred while checking JavaScript status:', error);
    }
});
```
