"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Write a JavaScript function that displays a maintenance message on a webpage, inspired by the service maintenance notice on nasiniacademyhairextension.it.
Generated: DETERMINISTIC_9c34250f6257bb2e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Displays a maintenance message on the webpage.
 * This function creates a customizable overlay to notify users about ongoing maintenance.
 * 
 * Usage: Call `displayMaintenanceMessage()` when you need to show a maintenance notice.
 */
function displayMaintenanceMessage() {
    // Create an overlay element
    const overlay = document.createElement('div');
    overlay.id = 'maintenance-overlay';
    overlay.style.position = 'fixed';
    overlay.style.top = 0;
    overlay.style.left = 0;
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    overlay.style.color = '#fff';
    overlay.style.display = 'flex';
    overlay.style.justifyContent = 'center';
    overlay.style.alignItems = 'center';
    overlay.style.zIndex = 9999;

    // Create a message container
    const messageContainer = document.createElement('div');
    messageContainer.style.textAlign = 'center';
    messageContainer.style.padding = '20px';
    messageContainer.style.backgroundColor = '#222';
    messageContainer.style.borderRadius = '8px';
    messageContainer.style.boxShadow = '0px 0px 10px rgba(0, 0, 0, 0.5)';

    // Add the maintenance message
    const message = document.createElement('h1');
    message.textContent = 'We are currently performing maintenance.';
    message.style.marginBottom = '10px';

    const subMessage = document.createElement('p');
    subMessage.textContent = 'Please check back later. We apologize for the inconvenience.';
    subMessage.style.fontSize = '16px';

    // Add a close button
    const closeButton = document.createElement('button');
    closeButton.textContent = 'Close';
    closeButton.style.marginTop = '15px';
    closeButton.style.padding = '10px 20px';
    closeButton.style.border = 'none';
    closeButton.style.borderRadius = '4px';
    closeButton.style.backgroundColor = '#007BFF';
    closeButton.style.color = '#fff';
    closeButton.style.cursor = 'pointer';
    closeButton.style.fontSize = '16px';

    closeButton.addEventListener('click', () => {
        // Remove the overlay when the close button is clicked
        document.body.removeChild(overlay);
    });

    // Assemble the elements
    messageContainer.appendChild(message);
    messageContainer.appendChild(subMessage);
    messageContainer.appendChild(closeButton);
    overlay.appendChild(messageContainer);

    // Add the overlay to the body
    document.body.appendChild(overlay);
}

// Call the function to display the maintenance message
// Uncomment the line below to test
// displayMaintenanceMessage();
```
