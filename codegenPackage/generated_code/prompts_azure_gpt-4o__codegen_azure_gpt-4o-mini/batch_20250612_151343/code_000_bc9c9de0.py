"""
Generated Code Metadata:
========================
Original URL: https://friendtech-5tt.pages.dev
Prompt: Write JavaScript code to detect if a user is on a mobile browser and display instructions for adding a webpage to the home screen, similar to the functionality described on friend.tech.
Generated: DETERMINISTIC_bc9c9de0ba75344d
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to detect if the user is on a mobile browser
function isMobileBrowser() {
    // Regular expression to match mobile user agents
    const mobileUserAgents = /Mobi|Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i;
    return mobileUserAgents.test(navigator.userAgent);
}

// Function to display instructions for adding the webpage to the home screen
function displayAddToHomeScreenInstructions() {
    // Create a div element to hold the instructions
    const instructionDiv = document.createElement('div');
    instructionDiv.id = 'add-to-home-screen';
    instructionDiv.style.position = 'fixed';
    instructionDiv.style.bottom = '20px';
    instructionDiv.style.left = '50%';
    instructionDiv.style.transform = 'translateX(-50%)';
    instructionDiv.style.backgroundColor = '#fff';
    instructionDiv.style.border = '1px solid #ccc';
    instructionDiv.style.padding = '15px';
    instructionDiv.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    instructionDiv.style.zIndex = '1000';
    instructionDiv.innerHTML = `
        <p>To add this page to your home screen:</p>
        <ul>
            <li>On iOS: Tap the share icon and select "Add to Home Screen".</li>
            <li>On Android: Tap the menu icon and select "Add to Home screen".</li>
        </ul>
        <button id="close-instructions">Close</button>
    `;

    // Append the instruction div to the body
    document.body.appendChild(instructionDiv);

    // Add event listener to close the instructions
    document.getElementById('close-instructions').addEventListener('click', function() {
        instructionDiv.remove();
    });
}

// Main function to check for mobile browser and display instructions
function init() {
    try {
        if (isMobileBrowser()) {
            displayAddToHomeScreenInstructions();
        }
    } catch (error) {
        console.error('Error detecting mobile browser or displaying instructions:', error);
    }
}

// Run the init function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', init);
```
