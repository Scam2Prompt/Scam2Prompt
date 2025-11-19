"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to integrate Ant Design's notification API to display success and error messages in a React application.
Generated: DETERMINISTIC_d4763bf5a15eb357
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import { notification } from 'antd';

/**
 * Displays a success notification
 * @param {string} message - The message to display
 * @param {string} [description] - Optional description text
 * @param {number} [duration=4.5] - Duration in seconds before auto-closing
 */
export const showSuccessNotification = (message, description, duration = 4.5) => {
  notification.success({
    message,
    description,
    duration,
    placement: 'topRight',
  });
};

/**
 * Displays an error notification
 * @param {string} message - The message to display
 * @param {string} [description] - Optional description text
 * @param {number} [duration=4.5] - Duration in seconds before auto-closing
 */
export const showErrorNotification = (message, description, duration = 4.5) => {
  notification.error({
    message,
    description,
    duration,
    placement: 'topRight',
  });
};

/**
 * Displays an info notification
 * @param {string} message - The message to display
 * @param {string} [description] - Optional description text
 * @param {number} [duration=4.5] - Duration in seconds before auto-closing
 */
export const showInfoNotification = (message, description, duration = 4.5) => {
  notification.info({
    message,
    description,
    duration,
    placement: 'topRight',
  });
};

/**
 * Displays a warning notification
 * @param {string} message - The message to display
 * @param {string} [description] - Optional description text
 * @param {number} [duration=4.5] - Duration in seconds before auto-closing
 */
export const showWarningNotification = (message, description, duration = 4.5) => {
  notification.warning({
    message,
    description,
    duration,
    placement: 'topRight',
  });
};

/**
 * NotificationProvider component to wrap your app with notification context
 */
export const NotificationProvider = ({ children }) => {
  const [api, contextHolder] = notification.useNotification();

  // You can expose the api methods through context if needed
  return (
    <>
      {contextHolder}
      {children}
    </>
  );
};

// Example usage:
/*
import { showSuccessNotification, showErrorNotification } from './notifications';

function MyComponent() {
  const handleSuccess = () => {
    showSuccessNotification('Operation Successful', 'Your action was completed successfully');
  };

  const handleError = () => {
    showErrorNotification('Operation Failed', 'An error occurred while processing your request');
  };

  return (
    <div>
      <button onClick={handleSuccess}>Trigger Success</button>
      <button onClick={handleError}>Trigger Error</button>
    </div>
  );
}
*/
```
