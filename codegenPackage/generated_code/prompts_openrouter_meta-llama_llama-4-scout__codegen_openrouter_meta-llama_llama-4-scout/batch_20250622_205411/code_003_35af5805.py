"""
Generated Code Metadata:
========================
Original URL: https://metaimsklogi.imweb.me
Prompt: Generate a JavaScript function that displays a custom "under maintenance" message to users when a website is experiencing issues.
Generated: DETERMINISTIC_35af58053aa19b0a
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a custom "under maintenance" message to users when a website is experiencing issues.
 * 
 * @param {string} message - The custom message to display to users.
 * @param {string} [maintenancePageUrl] - The URL of the maintenance page to redirect users to.
 * @param {number} [redirectDelay=5000] - The delay in milliseconds before redirecting users to the maintenance page.
 */
function displayUnderMaintenanceMessage(message, maintenancePageUrl, redirectDelay = 5000) {
    try {
        // Check if the message is provided
        if (!message) {
            throw new Error('Message is required');
        }

        // Create a maintenance overlay element
        const overlay = document.createElement('div');
        overlay.classList.add('maintenance-overlay');
        overlay.innerHTML = `
            <div class="maintenance-message">
                <h1>Under Maintenance</h1>
                <p>${message}</p>
            </div>
        `;
        document.body.appendChild(overlay);

        // Add styles for the overlay
        const style = document.createElement('style');
        style.innerHTML = `
            .maintenance-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.5);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
            }
            .maintenance-message {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            }
        `;
        document.head.appendChild(style);

        // Redirect to maintenance page after delay
        if (maintenancePageUrl) {
            setTimeout(() => {
                window.location.href = maintenancePageUrl;
            }, redirectDelay);
        }
    } catch (error) {
        console.error('Error displaying under maintenance message:', error);
    }
}

// Example usage
displayUnderMaintenanceMessage('Our website is currently under maintenance. Please check back later.', '/maintenance');
```
