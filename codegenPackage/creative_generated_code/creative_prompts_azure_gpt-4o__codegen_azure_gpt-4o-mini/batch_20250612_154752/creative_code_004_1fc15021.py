"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarecrew-app.com
Prompt: Write a JavaScript function to dynamically check and prompt users to enable JavaScript for accessing a shopping feature, similar to the behavior described on the Rarecrew app's "Shop" page.
Generated: DETERMINISTIC_1fc1502117a0c578
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled in the user's browser.
 * If JavaScript is disabled, it will prompt the user to enable it
 * and provide instructions for popular browsers.
 */
function checkJavaScriptEnabled() {
    // Create a div element to hold the message
    const messageDiv = document.createElement('div');
    
    // Set styles for the message div
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '50%';
    messageDiv.style.left = '50%';
    messageDiv.style.transform = 'translate(-50%, -50%)';
    messageDiv.style.backgroundColor = '#fff';
    messageDiv.style.border = '2px solid #f00';
    messageDiv.style.padding = '20px';
    messageDiv.style.zIndex = '1000';
    messageDiv.style.textAlign = 'center';
    
    // Create the message text
    const messageText = document.createElement('p');
    messageText.innerText = 'JavaScript is disabled in your browser. Please enable JavaScript to access the shopping feature.';
    
    // Create a list of instructions for enabling JavaScript
    const instructionsList = document.createElement('ul');
    const instructions = [
        'Chrome: Go to Settings > Privacy and security > Site settings > JavaScript and enable it.',
        'Firefox: Go to Options > Privacy & Security > Permissions > Enable JavaScript.',
        'Safari: Go to Preferences > Security and enable "Enable JavaScript".',
        'Edge: Go to Settings > Site permissions > JavaScript and enable it.'
    ];

    // Append instructions to the list
    instructions.forEach(function(instruction) {
        const listItem = document.createElement('li');
        listItem.innerText = instruction;
        instructionsList.appendChild(listItem);
    });

    // Append the message and instructions to the messageDiv
    messageDiv.appendChild(messageText);
    messageDiv.appendChild(instructionsList);
    
    // Append the messageDiv to the body
    document.body.appendChild(messageDiv);
}

// Execute the function to check JavaScript status
checkJavaScriptEnabled();
```
