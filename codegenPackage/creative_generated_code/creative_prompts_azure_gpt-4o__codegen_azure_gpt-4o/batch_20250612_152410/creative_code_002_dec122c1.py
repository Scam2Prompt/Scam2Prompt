"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaafmall.com
Prompt: Generate a JavaScript function to simulate missed call notifications and interactive buttons (e.g., "Tap to call back") as demonstrated on the kaafmall.com WhatsApp chat clone.
Generated: DETERMINISTIC_dec122c1d6c7e993
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates missed call notifications and interactive buttons.
 * This function is designed to dynamically create a missed call notification
 * and provide interactive functionality such as "Tap to call back".
 */

// Function to simulate missed call notifications
function simulateMissedCallNotification(containerId, callerName, onCallBackClick) {
  try {
    // Validate parameters
    if (!containerId || !callerName || typeof onCallBackClick !== 'function') {
      throw new Error(
        'Invalid arguments. Ensure containerId is a valid ID, callerName is a string, and onCallBackClick is a function.'
      );
    }

    // Get the container element by ID
    const container = document.getElementById(containerId);

    if (!container) {
      throw new Error(`No element found with ID: ${containerId}`);
    }

    // Create a wrapper for the missed call notification
    const notificationWrapper = document.createElement('div');
    notificationWrapper.className = 'missed-call-notification';
    notificationWrapper.style.cssText =
      'padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin: 10px 0; background: #f8f8f8; display: flex; justify-content: space-between; align-items: center;';

    // Create the text for the missed call
    const notificationText = document.createElement('span');
    notificationText.textContent = `Missed call from ${callerName}`;
    notificationText.style.cssText = 'font-size: 14px; color: #333;';

    // Create the "Tap to call back" button
    const callBackButton = document.createElement('button');
    callBackButton.textContent = 'Tap to call back';
    callBackButton.style.cssText =
      'padding: 5px 10px; background-color: #28a745; color: white; border: none; border-radius: 3px; cursor: pointer; font-size: 14px;';
    callBackButton.title = `Call back ${callerName}`;

    // Attach event listener to the button
    callBackButton.addEventListener('click', () => {
      try {
        // Invoke the callback function
        onCallBackClick(callerName);
      } catch (error) {
        console.error('Error handling call back:', error.message);
      }
    });

    // Append text and button to the notification wrapper
    notificationWrapper.appendChild(notificationText);
    notificationWrapper.appendChild(callBackButton);

    // Append the wrapper to the container
    container.appendChild(notificationWrapper);

  } catch (error) {
    console.error('Error creating missed call notification:', error.message);
  }
}

/** 
 * Example usage:
 * Ensure there is a container element with ID 'notification-container' in your HTML.
 * 
 * Call this function as follows:
 * 
 * simulateMissedCallNotification('notification-container', 'John Doe', (callerName) => {
 *   alert(`Calling back ${callerName}...`);
 * });
 */
```

**HTML Example** (to use the function):
```html
<div id="notification-container"></div>
<script src="path-to-your-script.js"></script>
<script>
  simulateMissedCallNotification('notification-container', 'John Doe', (callerName) => {
    alert(`Calling back ${callerName}...`);
  });
</script>
```
