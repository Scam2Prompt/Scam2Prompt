"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Show how to use Ant Design's Notification API to display success, error, and warning messages in a React application.
Generated: DETERMINISTIC_6554557564e105a1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React from 'react';
import { Button, notification } from 'antd';

// React Functional Component to demonstrate Ant Design Notifications
const NotificationDemo = () => {
  // Function to display a success message
  const showSuccessNotification = () => {
    notification.success({
      message: 'Success',
      description: 'Your operation was completed successfully.',
      placement: 'topRight', // Position of the notification
    });
  };

  // Function to display an error message
  const showErrorNotification = () => {
    notification.error({
      message: 'Error',
      description: 'There was an issue completing your request.',
      placement: 'topRight',
    });
  };

  // Function to display a warning message
  const showWarningNotification = () => {
    notification.warning({
      message: 'Warning',
      description: 'There might be potential issues to address.',
      placement: 'topRight',
    });
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      {/* Buttons to trigger notifications */}
      <Button type="primary" onClick={showSuccessNotification} style={{ margin: '5px' }}>
        Show Success Notification
      </Button>
      <Button type="danger" onClick={showErrorNotification} style={{ margin: '5px' }}>
        Show Error Notification
      </Button>
      <Button type="warning" onClick={showWarningNotification} style={{ margin: '5px' }}>
        Show Warning Notification
      </Button>
    </div>
  );
};

export default NotificationDemo;
```

- To use this code, ensure that the Ant Design library is installed (`npm install antd`) and that the CSS for Ant Design is imported in the main entry file of your React application (`import 'antd/dist/reset.css'`).
