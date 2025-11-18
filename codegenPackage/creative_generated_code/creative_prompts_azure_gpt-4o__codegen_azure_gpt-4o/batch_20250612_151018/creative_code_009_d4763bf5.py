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
// React Component to demonstrate integration of Ant Design's notification API
// Author: Professional Developer
// Purpose: Display success and error messages using Ant Design notifications

import React from 'react';
import { Button, notification } from 'antd';

// Helper function to trigger success notification
const openSuccessNotification = () => {
  notification.success({
    message: 'Success',
    description: 'Your operation was completed successfully.',
    placement: 'topRight', // Placement of the notification
    duration: 3, // Duration in seconds before auto-closing
  });
};

// Helper function to trigger error notification
const openErrorNotification = () => {
  notification.error({
    message: 'Error',
    description: 'There was an issue with your operation.',
    placement: 'topRight', // Placement of the notification
    duration: 3, // Duration in seconds before auto-closing
  });
};

// React Component
const NotificationDemo = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Button to show the success notification */}
      <Button type="primary" onClick={openSuccessNotification} style={{ marginRight: '10px' }}>
        Show Success Notification
      </Button>

      {/* Button to show the error notification */}
      <Button type="danger" onClick={openErrorNotification}>
        Show Error Notification
      </Button>
    </div>
  );
};

export default NotificationDemo;

// Notes:
// 1. Ensure Ant Design is installed in the project by running `npm install antd` or `yarn add antd`.
// 2. Import the global Ant Design styles in your entry file (e.g., index.js) for proper styling:
//    import 'antd/dist/reset.css';
```
