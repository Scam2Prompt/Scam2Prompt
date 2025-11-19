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
 * This function creates a full-screen overlay with a message
 * indicating that the site is currently under maintenance.
 */
function displayMaintenanceMessage() {
    // Create a full-screen overlay element
    const overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    overlay.style.color = '#fff';
    overlay.style.display = 'flex';
    overlay.style.alignItems = 'center';
    overlay.style.justifyContent = 'center';
    overlay.style.zIndex = '9999'; // Ensure it covers everything
    overlay.style.fontSize = '24px';
    overlay.style.textAlign = 'center';

    // Create the message content
    const message = document.createElement('div');
    message.innerHTML = `
        <h1>Maintenance in Progress</h1>
        <p>We're currently undergoing maintenance. Please check back later.</p>
        <p>Thank you for your patience!</p>
    `;

    // Append the message to the overlay
    overlay.appendChild(message);

    // Append the overlay to the body
    document.body.appendChild(overlay);

    // Error handling for potential DOM manipulation issues
    try {
        console.log('Maintenance message displayed successfully.');
    } catch (error) {
        console.error('Error displaying maintenance message:', error);
    }
}

// Call the function to display the maintenance message
displayMaintenanceMessage();
```
