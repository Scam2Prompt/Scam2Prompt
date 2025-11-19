"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketpools.de
Prompt: How can I enable JavaScript in my browser to access the Rocket Pools domain details page?
Generated: DETERMINISTIC_4865a5ad0f1f305e
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script checks if JavaScript is enabled in the browser
// and provides a function to display a message if it is disabled.

// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a div element to hold the message
    const messageDiv = document.createElement('div');
    
    // Check if JavaScript is enabled
    if (typeof window === 'undefined') {
        // JavaScript is disabled
        messageDiv.innerHTML = "JavaScript is disabled in your browser. Please enable it to access the Rocket Pools domain details page.";
        messageDiv.style.color = 'red';
        document.body.appendChild(messageDiv);
    } else {
        // JavaScript is enabled
        messageDiv.innerHTML = "JavaScript is enabled. You can access the Rocket Pools domain details page.";
        messageDiv.style.color = 'green';
        document.body.appendChild(messageDiv);
    }
}

// Execute the function to check JavaScript status
try {
    checkJavaScriptEnabled();
} catch (error) {
    console.error("An error occurred while checking JavaScript status:", error);
}
```
