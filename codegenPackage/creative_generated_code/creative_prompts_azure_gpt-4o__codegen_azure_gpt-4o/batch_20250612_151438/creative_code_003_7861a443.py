"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hingehealth.eu
Prompt: Generate code to implement a JavaScript-based notification system that informs users about enabling JavaScript for optimal app functionality, inspired by the Hinge Health EU website.
Generated: DETERMINISTIC_7861a443cde6f1d2
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Notification System to inform users about enabling JavaScript.
 * This script displays a notification bar if JavaScript is detected as disabled.
 * The notification bar provides a message and encourages users to enable JavaScript for optimal functionality.
 */

document.addEventListener("DOMContentLoaded", () => {
  // Function to show the notification
  function showNotification(message) {
    // Create the notification container
    const notificationBar = document.createElement("div");
    notificationBar.setAttribute("id", "js-notification-bar");
    notificationBar.style.position = "fixed";
    notificationBar.style.top = "0";
    notificationBar.style.left = "0";
    notificationBar.style.width = "100%";
    notificationBar.style.backgroundColor = "#ffcc00";
    notificationBar.style.color = "#000";
    notificationBar.style.textAlign = "center";
    notificationBar.style.padding = "15px";
    notificationBar.style.boxShadow = "0px 2px 5px rgba(0, 0, 0, 0.2)";
    notificationBar.style.zIndex = "9999";
    notificationBar.textContent = message;

    // Create a close button
    const closeButton = document.createElement("button");
    closeButton.textContent = "×";
    closeButton.style.marginLeft = "15px";
    closeButton.style.backgroundColor = "transparent";
    closeButton.style.border = "none";
    closeButton.style.fontSize = "1.2rem";
    closeButton.style.cursor = "pointer";

    // Attach event listener to close the notification
    closeButton.addEventListener("click", () => {
      notificationBar.remove();
    });

    // Append the close button to the notification bar
    notificationBar.appendChild(closeButton);

    // Append the notification bar to the body
    document.body.appendChild(notificationBar);
  }

  // Check if JavaScript is enabled (this script runs only if JS is enabled)
  // If JavaScript is not enabled, the user won't see this notification
  // (By design, because the script doesn't execute).
  // However, if you want to ensure this message for non-JS users, it's better
  // to implement a <noscript> tag in your HTML.

  // Display the notification
  showNotification(
    "JavaScript is enabled, but if functionality is not optimal, ensure JavaScript is enabled in your browser settings."
  );
});
```
