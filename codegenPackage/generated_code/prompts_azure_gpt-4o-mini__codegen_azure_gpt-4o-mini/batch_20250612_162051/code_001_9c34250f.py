"""
Generated Code Metadata:
========================
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Write a JavaScript function that displays a maintenance message on a webpage, inspired by the service maintenance notice on nasiniacademyhairextension.it.
Generated: DETERMINISTIC_9c34250f6257bb2e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a maintenance message on the webpage.
 * This function creates a full-screen overlay with a message
 * indicating that the site is currently under maintenance.
 */
function displayMaintenanceMessage() {
    // Create a full-screen overlay div
    const overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.8)'; // Semi-transparent black
    overlay.style.color = '#ffffff'; // White text
    overlay.style.display = 'flex';
    overlay.style.flexDirection = 'column';
    overlay.style.alignItems = 'center';
    overlay.style.justifyContent = 'center';
    overlay.style.zIndex = '1000'; // Ensure it is on top of other content
    overlay.style.fontFamily = 'Arial, sans-serif';
    overlay.style.textAlign = 'center';

    // Create the maintenance message
    const message = document.createElement('h1');
    message.textContent = 'We are currently undergoing maintenance';
    message.style.margin = '0';

    // Create a sub-message for additional information
    const subMessage = document.createElement('p');
    subMessage.textContent = 'We apologize for the inconvenience. Please check back later.';
    subMessage.style.marginTop = '10px';

    // Append the message and sub-message to the overlay
    overlay.appendChild(message);
    overlay.appendChild(subMessage);

    // Append the overlay to the body
    document.body.appendChild(overlay);

    // Optional: Add a listener to remove the overlay on click (for testing purposes)
    overlay.addEventListener('click', () => {
        document.body.removeChild(overlay);
    });
}

// Call the function to display the maintenance message
displayMaintenanceMessage();
```
