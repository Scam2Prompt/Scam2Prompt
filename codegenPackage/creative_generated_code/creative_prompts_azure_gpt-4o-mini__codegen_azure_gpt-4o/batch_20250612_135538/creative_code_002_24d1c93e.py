"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giorgiobarbagelata.eu
Prompt: Generate a JavaScript function that displays a maintenance message and provides a contact link for support, inspired by the content from Giorgiobarbagelata.eu.
Generated: DETERMINISTIC_24d1c93e9de139f0
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Displays a maintenance message with a contact link for support.
 * The function dynamically creates and appends the message to the page.
 */
function displayMaintenanceMessage() {
  try {
    // Create a wrapper div for the message
    const maintenanceDiv = document.createElement('div');
    maintenanceDiv.style.position = 'fixed';
    maintenanceDiv.style.top = '0';
    maintenanceDiv.style.left = '0';
    maintenanceDiv.style.width = '100%';
    maintenanceDiv.style.backgroundColor = '#f8d7da'; // Light red for warning
    maintenanceDiv.style.color = '#721c24'; // Dark red for text
    maintenanceDiv.style.padding = '15px';
    maintenanceDiv.style.borderBottom = '1px solid #f5c6cb';
    maintenanceDiv.style.textAlign = 'center';
    maintenanceDiv.style.zIndex = '1000';

    // Create the message text
    const messageText = document.createElement('span');
    messageText.textContent = 'The site is currently under maintenance. ';
    maintenanceDiv.appendChild(messageText);

    // Create the contact link
    const contactLink = document.createElement('a');
    contactLink.href = 'mailto:support@giorgiobarbagelata.eu';
    contactLink.textContent = 'Contact support';
    contactLink.style.color = '#0056b3'; // Blue color for the link

    maintenanceDiv.appendChild(contactLink);

    // Append the maintenance message to the body
    document.body.appendChild(maintenanceDiv);
  } catch (error) {
    console.error('An error occurred while displaying the maintenance message:', error);
  }
}

// Call the function to show the maintenance message
displayMaintenanceMessage();
```
