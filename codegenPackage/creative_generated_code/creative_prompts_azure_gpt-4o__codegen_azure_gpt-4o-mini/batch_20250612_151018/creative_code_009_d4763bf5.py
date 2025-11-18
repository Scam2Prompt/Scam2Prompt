"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to integrate Ant Design's notification API to display success and error messages in a React application.
Generated: DETERMINISTIC_d4763bf5a15eb357
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { notification, Button } from 'antd';

/**
 * Displays a success notification.
 *
 * @param {string} message - The message to display in the notification.
 * @param {string} description - The description to provide additional context.
 */
const openSuccessNotification = (message, description) => {
    notification.success({
        message: message,
        description: description,
        placement: 'topRight',
        duration: 3,
    });
};

/**
 * Displays an error notification.
 *
 * @param {string} message - The message to display in the notification.
 * @param {string} description - The description to provide additional context.
 */
const openErrorNotification = (message, description) => {
    notification.error({
        message: message,
        description: description,
        placement: 'topRight',
        duration: 3,
    });
};

/**
 * NotificationDemo component that demonstrates how to use Ant Design's notification API.
 */
const NotificationDemo = () => {
    /**
     * Handles the button click to show a success notification.
     */
    const handleSuccessClick = () => {
        try {
            openSuccessNotification('Success!', 'Your operation was successful.');
        } catch (error) {
            console.error('Error displaying success notification:', error);
            openErrorNotification('Notification Error', 'Failed to display success notification.');
        }
    };

    /**
     * Handles the button click to show an error notification.
     */
    const handleErrorClick = () => {
        try {
            openErrorNotification('Error!', 'There was an error with your operation.');
        } catch (error) {
            console.error('Error displaying error notification:', error);
            openErrorNotification('Notification Error', 'Failed to display error notification.');
        }
    };

    return (
        <div>
            <Button type="primary" onClick={handleSuccessClick}>
                Show Success Notification
            </Button>
            <Button type="danger" onClick={handleErrorClick} style={{ marginLeft: 10 }}>
                Show Error Notification
            </Button>
        </div>
    );
};

export default NotificationDemo;
```
