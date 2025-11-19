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
 * Displays a maintenance message on a webpage.
 * The message is styled and centered on the page with a semi-transparent background.
 * 
 * @param {string} message - The maintenance message to display
 * @param {Object} [options] - Optional configuration
 * @param {string} [options.backgroundColor='rgba(0, 0, 0, 0.8)'] - Background color
 * @param {string} [options.textColor='#ffffff'] - Text color
 * @param {string} [options.fontSize='24px'] - Font size
 * @param {string} [options.fontFamily='Arial, sans-serif'] - Font family
 * @param {boolean} [options.fullScreen=true] - Whether to cover the full screen
 */
function showMaintenanceMessage(message, options = {}) {
    // Default options
    const defaultOptions = {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        textColor: '#ffffff',
        fontSize: '24px',
        fontFamily: 'Arial, sans-serif',
        fullScreen: true
    };

    // Merge user options with defaults
    const config = { ...defaultOptions, ...options };

    try {
        // Create the maintenance message container
        const maintenanceDiv = document.createElement('div');
        maintenanceDiv.id = 'maintenance-message';
        
        // Apply styles
        maintenanceDiv.style.position = config.fullScreen ? 'fixed' : 'absolute';
        maintenanceDiv.style.top = '0';
        maintenanceDiv.style.left = '0';
        maintenanceDiv.style.width = '100%';
        maintenanceDiv.style.height = config.fullScreen ? '100vh' : '100%';
        maintenanceDiv.style.backgroundColor = config.backgroundColor;
        maintenanceDiv.style.color = config.textColor;
        maintenanceDiv.style.display = 'flex';
        maintenanceDiv.style.justifyContent = 'center';
        maintenanceDiv.style.alignItems = 'center';
        maintenanceDiv.style.zIndex = '9999';
        maintenanceDiv.style.fontFamily = config.fontFamily;
        maintenanceDiv.style.fontSize = config.fontSize;
        maintenanceDiv.style.textAlign = 'center';
        maintenanceDiv.style.padding = '20px';
        maintenanceDiv.style.boxSizing = 'border-box';

        // Create the message content
        const messageContent = document.createElement('div');
        messageContent.textContent = message;
        maintenanceDiv.appendChild(messageContent);

        // Add to the document
        document.body.appendChild(maintenanceDiv);
        document.body.style.overflow = 'hidden';

        // Handle potential removal
        return {
            remove: function() {
                if (document.body.contains(maintenanceDiv)) {
                    document.body.removeChild(maintenanceDiv);
                    document.body.style.overflow = '';
                }
            }
        };
    } catch (error) {
        console.error('Failed to display maintenance message:', error);
        return {
            remove: function() {}
        };
    }
}

// Example usage:
// showMaintenanceMessage("We're currently undergoing maintenance. Please check back soon.", {
//     backgroundColor: 'rgba(50, 50, 50, 0.9)',
//     textColor: '#f8f8f8',
//     fontSize: '28px'
// });
```
