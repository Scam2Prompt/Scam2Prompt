"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.omninetwork.it
Prompt: How can I enable JavaScript in my browser to ensure proper functionality of Webmail services?
Generated: DETERMINISTIC_afdfa8c680f79816
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled in the browser
function isJavaScriptEnabled() {
    // Create a test element
    const testElement = document.createElement('div');
    testElement.innerHTML = '<script>window.jsEnabled = true;</script>';
    
    // Append the test element to the body
    document.body.appendChild(testElement);
    
    // Check if JavaScript is enabled by evaluating the variable
    const jsEnabled = window.jsEnabled === true;

    // Clean up the test element
    document.body.removeChild(testElement);
    
    return jsEnabled;
}

// Function to enable JavaScript instructions for the user
function enableJavaScriptInstructions() {
    if (!isJavaScriptEnabled()) {
        // Create a modal or notification to inform the user
        const message = `
            <div style="background-color: #ffcc00; padding: 20px; border-radius: 5px; text-align: center;">
                <h2>JavaScript is Disabled!</h2>
                <p>To ensure proper functionality of Webmail services, please enable JavaScript in your browser.</p>
                <ol>
                    <li>Go to your browser settings.</li>
                    <li>Look for the "Privacy and Security" section.</li>
                    <li>Find the settings related to JavaScript.</li>
                    <li>Enable JavaScript.</li>
                    <li>Refresh this page.</li>
                </ol>
            </div>
        `;

        // Append the message to the body
        document.body.innerHTML += message;
    }
}

// Execute the function to check and enable JavaScript instructions
enableJavaScriptInstructions();
```
