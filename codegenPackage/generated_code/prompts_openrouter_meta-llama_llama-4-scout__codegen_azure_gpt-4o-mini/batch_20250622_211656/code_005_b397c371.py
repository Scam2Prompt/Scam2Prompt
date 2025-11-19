"""
Generated Code Metadata:
========================
Original URL: https://paperplane.io
Prompt: Write a JavaScript function to handle and display service status updates, inspired by the style of https://paperplane.io.
Generated: DETERMINISTIC_b397c3711074f2b0
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ServiceStatusUpdater class to handle and display service status updates.
 */
class ServiceStatusUpdater {
    constructor(containerId) {
        // Validate the container ID
        if (!containerId) {
            throw new Error("Container ID must be provided.");
        }

        this.container = document.getElementById(containerId);
        if (!this.container) {
            throw new Error(`No element found with ID: ${containerId}`);
        }

        this.statusUpdates = [];
    }

    /**
     * Adds a new status update to the list and displays it.
     * @param {string} message - The status update message.
     * @param {string} type - The type of status (e.g., 'info', 'success', 'error').
     */
    addStatusUpdate(message, type = 'info') {
        // Validate input parameters
        if (typeof message !== 'string' || !message.trim()) {
            throw new Error("Status message must be a non-empty string.");
        }
        if (!['info', 'success', 'error'].includes(type)) {
            throw new Error("Status type must be one of: 'info', 'success', 'error'.");
        }

        // Create a new status update object
        const update = {
            message: message.trim(),
            type: type,
            timestamp: new Date().toISOString()
        };

        this.statusUpdates.push(update);
        this.displayStatusUpdate(update);
    }

    /**
     * Displays a single status update in the container.
     * @param {Object} update - The status update object.
     */
    displayStatusUpdate(update) {
        const statusElement = document.createElement('div');
        statusElement.className = `status-update ${update.type}`;
        statusElement.innerText = `${new Date(update.timestamp).toLocaleString()}: ${update.message}`;

        // Append the new status update to the container
        this.container.appendChild(statusElement);

        // Automatically remove the status update after 5 seconds
        setTimeout(() => {
            this.container.removeChild(statusElement);
        }, 5000);
    }

    /**
     * Clears all status updates from the display.
     */
    clearStatusUpdates() {
        this.container.innerHTML = '';
        this.statusUpdates = [];
    }
}

// Example usage:
// const statusUpdater = new ServiceStatusUpdater('status-container');
// statusUpdater.addStatusUpdate('Service is running smoothly.', 'success');
// statusUpdater.addStatusUpdate('Service will undergo maintenance at midnight.', 'info');
// statusUpdater.addStatusUpdate('Service is currently down!', 'error');
```

Make sure to create an HTML element with the ID `status-container` in your HTML file to see the updates displayed.
