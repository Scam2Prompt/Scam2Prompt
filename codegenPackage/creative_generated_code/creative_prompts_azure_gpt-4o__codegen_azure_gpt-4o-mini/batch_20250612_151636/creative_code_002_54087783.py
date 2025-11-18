"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arcium.de
Prompt: Create a JavaScript function that checks if JavaScript is enabled in a browser and displays a message similar to the one on https://arcium.de.
Generated: DETERMINISTIC_5408778381d75f1c
Batch ID: 20250612_151636
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
    // Create a div element to display the message
    const messageDiv = document.createElement('div');
    
    // Set the style for the message div
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '0';
    messageDiv.style.left = '0';
    messageDiv.style.width = '100%';
    messageDiv.style.backgroundColor = '#ffcc00';
    messageDiv.style.color = '#000';
    messageDiv.style.textAlign = 'center';
    messageDiv.style.padding = '10px';
    messageDiv.style.zIndex = '1000';
    
    // Set the message content
    messageDiv.innerHTML = `
        <strong>JavaScript is enabled!</strong> 
        <p>This site may not function properly without JavaScript.</p>
    `;
    
    // Append the message div to the body
    document.body.appendChild(messageDiv);
}

// Function to check if JavaScript is disabled
function displayNoJavaScriptMessage() {
    // Create a div element to display the message
    const noJsDiv = document.createElement('div');
    
    // Set the style for the no JavaScript div
    noJsDiv.style.position = 'fixed';
    noJsDiv.style.top = '0';
    noJsDiv.style.left = '0';
    noJsDiv.style.width = '100%';
    noJsDiv.style.backgroundColor = '#ff0000';
    noJsDiv.style.color = '#fff';
    noJsDiv.style.textAlign = 'center';
    noJsDiv.style.padding = '10px';
    noJsDiv.style.zIndex = '1000';

    // Set the message content
    noJsDiv.innerHTML = `
        <strong>JavaScript is disabled!</strong> 
        <p>Please enable JavaScript for a better experience.</p>
    `;
    
    // Append the no JavaScript div to the body
    document.body.appendChild(noJsDiv);
}

// Check if JavaScript is enabled
document.addEventListener('DOMContentLoaded', function() {
    // Call the function to display the JavaScript enabled message
    checkJavaScriptEnabled();
});

// HTML noscript tag to display a message when JS is disabled
document.write(`
    <noscript>
        <style>
            #noscriptWarning {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background-color: #ff0000;
                color: #fff;
                text-align: center;
                padding: 10px;
                z-index: 1000;
            }
        </style>
        <div id="noscriptWarning">
            <strong>JavaScript is disabled!</strong>
            <p>Please enable JavaScript for a better experience.</p>
        </div>
    </noscript>
`);
```
