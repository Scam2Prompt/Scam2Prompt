"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bot22.cc
Prompt: How can I enable JavaScript in my browser to use the features of the BOT website?
Generated: DETERMINISTIC_1fb63e715fe2c60b
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to help users enable JavaScript in their browser
function enableJavaScriptInstructions() {
    // Create a message element to display instructions
    const messageElement = document.createElement('div');
    messageElement.style.border = '1px solid #f00';
    messageElement.style.backgroundColor = '#ffe6e6';
    messageElement.style.padding = '10px';
    messageElement.style.margin = '20px';
    messageElement.style.borderRadius = '5px';
    
    // Instructions text
    const instructions = `
        <h3>How to Enable JavaScript in Your Browser</h3>
        <p>Please follow the instructions for your browser:</p>
        <ul>
            <li><strong>Google Chrome:</strong> 
                <ol>
                    <li>Click the three-dot menu in the top right corner.</li>
                    <li>Go to <strong>Settings</strong>.</li>
                    <li>Scroll down and click on <strong>Privacy and security</strong>.</li>
                    <li>Select <strong>Site settings</strong>.</li>
                    <li>Under <strong>Content</strong>, click <strong>JavaScript</strong>.</li>
                    <li>Toggle the switch to <strong>Allowed (recommended)</strong>.</li>
                </ol>
            </li>
            <li><strong>Mozilla Firefox:</strong>
                <ol>
                    <li>Click the three horizontal lines in the top right corner.</li>
                    <li>Select <strong>Options</strong>.</li>
                    <li>In the left menu, click on <strong>Privacy & Security</strong>.</li>
                    <li>Scroll down to the <strong>Permissions</strong> section.</li>
                    <li>Check the box next to <strong>Enable JavaScript</strong>.</li>
                </ol>
            </li>
            <li><strong>Microsoft Edge:</strong>
                <ol>
                    <li>Click the three-dot menu in the top right corner.</li>
                    <li>Go to <strong>Settings</strong>.</li>
                    <li>Click on <strong>Cookies and site permissions</strong>.</li>
                    <li>Under <strong>Site permissions</strong>, select <strong>JavaScript</strong>.</li>
                    <li>Toggle the switch to <strong>Allowed</strong>.</li>
                </ol>
            </li>
            <li><strong>Safari:</strong>
                <ol>
                    <li>Click on <strong>Safari</strong> in the menu bar.</li>
                    <li>Select <strong>Preferences</strong>.</li>
                    <li>Go to the <strong>Security</strong> tab.</li>
                    <li>Check the box next to <strong>Enable JavaScript</strong>.</li>
                </ol>
            </li>
        </ul>
        <p>After enabling JavaScript, please refresh the page to access all features.</p>
    `;
    
    // Set the inner HTML of the message element
    messageElement.innerHTML = instructions;

    // Append the message to the body of the document
    document.body.appendChild(messageElement);
}

// Check if JavaScript is enabled and display the instructions if not
if (!window.navigator.javaEnabled()) {
    enableJavaScriptInstructions();
}
```
