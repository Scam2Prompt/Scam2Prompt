"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://friendtech-5tt.pages.dev
Prompt: Write JavaScript code to detect if a user is on a mobile browser and display instructions for adding a webpage to the home screen, similar to the functionality described on friend.tech.
Generated: DETERMINISTIC_bc9c9de0ba75344d
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to detect if the user is on a mobile device
function isMobileDevice() {
    return /Mobi|Android/i.test(navigator.userAgent);
}

// Function to check if the webpage is running in a standalone mode (added to home screen)
function isInStandaloneMode() {
    return window.matchMedia('(display-mode: standalone)').matches || 
           window.navigator.standalone;
}

// Function to display instructions for adding to home screen
function displayAddToHomeScreenInstructions() {
    // Create a div element for instructions
    const instructionDiv = document.createElement('div');
    instructionDiv.style.position = 'fixed';
    instructionDiv.style.bottom = '20px';
    instructionDiv.style.left = '50%';
    instructionDiv.style.transform = 'translateX(-50%)';
    instructionDiv.style.backgroundColor = '#fff';
    instructionDiv.style.padding = '20px';
    instructionDiv.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.2)';
    instructionDiv.style.zIndex = '1000';

    // Set the content of the instructions
    instructionDiv.innerHTML = `
        <h2>Add to Home Screen</h2>
        <p>For a better experience, add this page to your home screen.</p>
        <p>On iOS: Tap the 'Share' icon and then select 'Add to Home Screen'.</p>
        <p>On Android: Tap the menu icon (three dots) and then select 'Add to Home Screen'.</p>
        <button id="close-instruction">Close</button>
    `;

    // Append the instructions to the body
    document.body.appendChild(instructionDiv);

    // Add event listener to close button
    document.getElementById('close-instruction').onclick = function() {
        instructionDiv.remove();
    };
}

// Main function to initialize mobile detection and display instructions
function init() {
    try {
        // Check if on mobile device and not in standalone mode
        if (isMobileDevice() && !isInStandaloneMode()) {
            displayAddToHomeScreenInstructions();
        }
    } catch (error) {
        console.error("An error occurred while checking the device:", error);
    }
}

// Run the initialization function on DOMContentLoaded
document.addEventListener('DOMContentLoaded', init);
```
