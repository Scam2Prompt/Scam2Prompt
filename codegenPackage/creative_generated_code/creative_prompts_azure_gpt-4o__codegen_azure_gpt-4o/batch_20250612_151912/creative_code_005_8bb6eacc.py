"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: Write code to create a pop-up notification system that triggers based on user actions, such as scrolling or exiting the page, as mentioned on SafeSteth.com.
Generated: DETERMINISTIC_8bb6eacc7501de5f
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Pop-up Notification System
 * This script shows a notification pop-up based on user actions 
 * such as scrolling or attempting to exit the page.
 * 
 * Author: [Your Name]
 * Date: [Insert Date]
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize the pop-up system when the page is fully loaded

    // Create the notification HTML structure
    const notification = document.createElement('div');
    notification.id = 'popupNotification';
    notification.style.display = 'none'; // Initially hidden
    notification.style.position = 'fixed';
    notification.style.zIndex = '1000';
    notification.style.top = '50%';
    notification.style.left = '50%';
    notification.style.transform = 'translate(-50%, -50%)';
    notification.style.width = '300px';
    notification.style.padding = '20px';
    notification.style.backgroundColor = '#fff';
    notification.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    notification.style.borderRadius = '8px';
    notification.style.fontFamily = 'Arial, sans-serif';
    notification.innerHTML = `
        <h2>Important Notification</h2>
        <p>Don't miss out on our updates and offers!</p>
        <button id="closePopup">Close</button>
    `;
    document.body.appendChild(notification);

    const closeButton = document.getElementById('closePopup');
    closeButton.style.marginTop = '10px';
    closeButton.style.padding = '10px 20px';
    closeButton.style.border = 'none';
    closeButton.style.cursor = 'pointer';
    closeButton.style.borderRadius = '5px';
    closeButton.style.backgroundColor = '#007BFF';
    closeButton.style.color = '#fff';

    // Show the pop-up notification
    const showNotification = () => {
        notification.style.display = 'block';
    };

    // Hide the pop-up notification
    const hideNotification = () => {
        notification.style.display = 'none';
    };

    // Add event listener to the close button to hide the pop-up
    closeButton.addEventListener('click', hideNotification);

    // Trigger the notification on scroll
    let hasScrolled = false;
    window.addEventListener('scroll', () => {
        if (!hasScrolled) {
            showNotification();
            hasScrolled = true; // Ensures pop-up triggers only once
        }
    });

    // Trigger the notification on page exit
    const handleExitIntent = (event) => {
        if (event.clientY < 0) {
            showNotification();
            window.removeEventListener('mousemove', handleExitIntent); // Prevent multiple triggers
        }
    };

    window.addEventListener('mousemove', handleExitIntent);

    // Error handling (basic example)
    try {
        if (!notification || !closeButton) {
            throw new Error('Pop-up notification system failed to initialize.');
        }
    } catch (error) {
        console.error(error.message);
    }
});
```
