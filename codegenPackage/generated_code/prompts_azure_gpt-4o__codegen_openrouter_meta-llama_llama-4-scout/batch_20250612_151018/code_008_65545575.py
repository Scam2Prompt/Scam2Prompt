"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Show how to use Ant Design's Notification API to display success, error, and warning messages in a React application.
Generated: DETERMINISTIC_6554557564e105a1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import { notification, Button } from 'antd';

/**
 * Notification types
 */
const notificationTypes = {
  SUCCESS: 'success',
  ERROR: 'error',
  WARNING: 'warning',
};

/**
 * Notification messages
 */
const notificationMessages = {
  SUCCESS: 'This is a success message',
  ERROR: 'This is an error message',
  WARNING: 'This is a warning message',
};

/**
 * Notification component
 */
const NotificationComponent = () => {
  const [notificationKey, setNotificationKey] = useState('');

/  /**
   * Show notification
   * @param {string} type - Notification type
   */
  const showNotification = (type) => {
    const key = `notification-${Date.now()}`;
    setNotificationKey(key);

    notification[type]({
      message: `Notification ${type}`,
      description: notificationMessages[type],
      key,
      onClose: () => {
        setNotificationKey('');
      },
    });
  };

  /**
   * Close notification
   */
  const closeNotification = () => {
    notification.close(notificationKey);
  };

  return (
    <div>
      <Button type="primary" onClick={() => showNotification(notificationTypes.SUCCESS)}>
        Show Success Notification
      </Button>
      <Button type="danger" onClick={() => showNotification(notificationTypes.ERROR)}>
        Show Error Notification
      </Button>
      <Button type="warning" onClick={() => showNotification(notificationTypes.WARNING)}>
        Show Warning Notification
      </Button>
      <Button onClick={closeNotification}>Close Notification</Button>
    </div>
  );
};

export default NotificationComponent;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import NotificationComponent from './NotificationComponent';

ReactDOM.render(
  <React.StrictMode>
    <NotificationComponent />
  </React.StrictMode>,
  document.getElementById('root')
);
```
