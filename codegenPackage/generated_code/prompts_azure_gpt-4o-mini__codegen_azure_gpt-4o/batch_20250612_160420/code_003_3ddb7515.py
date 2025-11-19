"""
Generated Code Metadata:
========================
Original URL: https://www.zkasino.it
Prompt: Create a JavaScript code to display a maintenance alert on a webpage, similar to the one found on zkasino.it.
Generated: DETERMINISTIC_3ddb7515ec72144f
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Maintenance Alert Script
// This script displays a maintenance alert banner on a webpage.
// The alert is customizable and can be toggled on/off easily.

// Function to create and display the maintenance alert
function displayMaintenanceAlert(message, isActive) {
  // Check if the alert is active
  if (!isActive) {
    console.log("Maintenance alert is not active.");
    return;
  }

  // Create the alert container
  const alertContainer = document.createElement("div");
  alertContainer.id = "maintenance-alert";
  alertContainer.style.position = "fixed";
  alertContainer.style.top = "0";
  alertContainer.style.left = "0";
  alertContainer.style.width = "100%";
  alertContainer.style.backgroundColor = "#ffcc00";
  alertContainer.style.color = "#000";
  alertContainer.style.textAlign = "center";
  alertContainer.style.padding = "10px";
  alertContainer.style.zIndex = "1000";
  alertContainer.style.boxShadow = "0px 4px 6px rgba(0, 0, 0, 0.1)";
  alertContainer.style.fontFamily = "Arial, sans-serif";
  alertContainer.style.fontSize = "16px";

  // Add the message to the alert container
  alertContainer.textContent = message;

  // Create a close button for the alert
  const closeButton = document.createElement("button");
  closeButton.textContent = "X";
  closeButton.style.marginLeft = "10px";
  closeButton.style.backgroundColor = "#000";
  closeButton.style.color = "#fff";
  closeButton.style.border = "none";
  closeButton.style.padding = "5px 10px";
  closeButton.style.cursor = "pointer";
  closeButton.style.borderRadius = "3px";

  // Add click event to close the alert
  closeButton.addEventListener("click", () => {
    document.body.removeChild(alertContainer);
  });

  // Append the close button to the alert container
  alertContainer.appendChild(closeButton);

  // Append the alert container to the body
  document.body.appendChild(alertContainer);
}

// Example usage
// Customize the message and toggle the alert on/off
const maintenanceMessage = "Our website is currently undergoing maintenance. We apologize for any inconvenience.";
const isAlertActive = true;

// Display the maintenance alert
displayMaintenanceAlert(maintenanceMessage, isAlertActive);
```
