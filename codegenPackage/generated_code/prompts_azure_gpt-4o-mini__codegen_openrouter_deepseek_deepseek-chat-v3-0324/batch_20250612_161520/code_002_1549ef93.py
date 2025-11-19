"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: Create a JavaScript function that displays a notification for homeowners to schedule a free roof inspection after a storm, inspired by the services of JaraEs Construction LLC.
Generated: DETERMINISTIC_1549ef93217fd3b5
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a notification for homeowners to schedule a free roof inspection after a storm.
 * @param {Object} options - Configuration options for the notification
 * @param {string} options.companyName - Name of the construction company
 * @param {string} options.phoneNumber - Contact phone number
 * @param {string} options.notificationText - Custom notification text
 * @param {number} options.displayDuration - Duration in milliseconds to show the notification (default: 10000)
 * @param {string} options.notificationType - Type of notification ('banner' or 'modal', default: 'banner')
 */
function showRoofInspectionNotification(options = {}) {
    // Default options
    const defaults = {
        companyName: 'JaraEs Construction LLC',
        phoneNumber: '(555) 123-4567',
        notificationText: 'After the recent storm, schedule your FREE roof inspection today!',
        displayDuration: 10000,
        notificationType: 'banner'
    };

    // Merge defaults with provided options
    const config = { ...defaults, ...options };

    try {
        // Validate required parameters
        if (!config.companyName || !config.phoneNumber || !config.notificationText) {
            throw new Error('Missing required configuration parameters');
        }

        // Create notification element based on type
        let notification;
        if (config.notificationType === 'modal') {
            notification = createModalNotification(config);
        } else {
            notification = createBannerNotification(config);
        }

        // Add notification to the DOM
        document.body.appendChild(notification);

        // Set timeout to remove notification
        setTimeout(() => {
            notification.classList.add('fade-out');
            setTimeout(() => {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
            }, 500);
        }, config.displayDuration);

    } catch (error) {
        console.error('Error displaying roof inspection notification:', error.message);
    }
}

/**
 * Creates a banner-style notification element
 * @param {Object} config - Configuration object
 * @returns {HTMLElement} The created banner element
 */
function createBannerNotification(config) {
    const banner = document.createElement('div');
    banner.className = 'roof-inspection-banner';
    banner.style.cssText = `
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #2c3e50;
        color: white;
        padding: 15px;
        text-align: center;
        z-index: 1000;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.2);
        transition: opacity 0.5s ease;
    `;

    const content = document.createElement('div');
    content.style.cssText = `
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
    `;

    const text = document.createElement('p');
    text.textContent = config.notificationText;
    text.style.margin = '0';

    const ctaButton = document.createElement('button');
    ctaButton.textContent = `Call ${config.companyName} at ${config.phoneNumber}`;
    ctaButton.style.cssText = `
        background-color: #e74c3c;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
        margin-left: 20px;
    `;
    ctaButton.addEventListener('click', () => {
        window.location.href = `tel:${config.phoneNumber.replace(/[^\d+]/g, '')}`;
    });

    const closeButton = document.createElement('button');
    closeButton.innerHTML = '&times;';
    closeButton.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
        margin-left: 15px;
    `;
    closeButton.addEventListener('click', () => {
        banner.classList.add('fade-out');
        setTimeout(() => {
            if (document.body.contains(banner)) {
                document.body.removeChild(banner);
            }
        }, 500);
    });

    content.appendChild(text);
    content.appendChild(ctaButton);
    content.appendChild(closeButton);
    banner.appendChild(content);

    return banner;
}

/**
 * Creates a modal-style notification element
 * @param {Object} config - Configuration object
 * @returns {HTMLElement} The created modal element
 */
function createModalNotification(config) {
    const modal = document.createElement('div');
    modal.className = 'roof-inspection-modal';
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0,0,0,0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        transition: opacity 0.5s ease;
    `;

    const modalContent = document.createElement('div');
    modalContent.style.cssText = `
        background-color: white;
        padding: 30px;
        border-radius: 8px;
        max-width: 500px;
        width: 90%;
        text-align: center;
        position: relative;
    `;

    const closeButton = document.createElement('button');
    closeButton.innerHTML = '&times;';
    closeButton.style.cssText = `
        position: absolute;
        top: 10px;
        right: 10px;
        background: none;
        border: none;
        font-size: 20px;
        cursor: pointer;
    `;
    closeButton.addEventListener('click', () => {
        modal.classList.add('fade-out');
        setTimeout(() => {
            if (document.body.contains(modal)) {
                document.body.removeChild(modal);
            }
        }, 500);
    });

    const title = document.createElement('h2');
    title.textContent = 'Free Roof Inspection';
    title.style.color = '#2c3e50';
    title.style.marginTop = '0';

    const text = document.createElement('p');
    text.textContent = config.notificationText;
    text.style.marginBottom = '20px';

    const ctaButton = document.createElement('button');
    ctaButton.textContent = `Schedule Now: ${config.phoneNumber}`;
    ctaButton.style.cssText = `
        background-color: #e74c3c;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 10px;
        display: block;
        width: 100%;
    `;
    ctaButton.addEventListener('click', () => {
        window.location.href = `tel:${config.phoneNumber.replace(/[^\d+]/g, '')}`;
    });

    const companyInfo = document.createElement('p');
    companyInfo.textContent = `Provided by ${config.companyName}`;
    companyInfo.style.color = '#7f8c8d';
    companyInfo.style.fontSize = '14px';
    companyInfo.style.marginBottom = '0';

    modalContent.appendChild(closeButton);
    modalContent.appendChild(title);
    modalContent.appendChild(text);
    modalContent.appendChild(ctaButton);
    modalContent.appendChild(companyInfo);
    modal.appendChild(modalContent);

    return modal;
}

// Add CSS for fade-out animation
const style = document.createElement('style');
style.textContent = `
    .fade-out {
        opacity: 0 !important;
    }
`;
document.head.appendChild(style);

// Example usage:
// showRoofInspectionNotification();
// showRoofInspectionNotification({
//     notificationType: 'modal',
//     displayDuration: 15000
// });
```
