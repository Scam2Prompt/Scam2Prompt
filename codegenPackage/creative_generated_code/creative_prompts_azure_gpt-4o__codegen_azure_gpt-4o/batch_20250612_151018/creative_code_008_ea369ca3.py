"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's notification API to show success and error messages in a React app.
Generated: DETERMINISTIC_ea369ca359a342d8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React from 'react';
import { notification, Button } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles (ensure this is included in your project)

// Main React component
const NotificationExample = () => {
  // Function to show a success notification
  const showSuccessNotification = () => {
    notification.success({
      message: 'Success',
      description: 'The operation was completed successfully!',
      placement: 'topRight', // Placement of the notification (optional, defaults to topRight)
      duration: 3, // Time (in seconds) before the notification disappears (optional, defaults to 4.5)
    });
  };

  // Function to show an error notification
  const showErrorNotification = () => {
    notification.error({
      message: 'Error',
      description: 'Something went wrong. Please try again later.',
      placement: 'topRight',
      duration: 3,
    });
  };

  return (
    <div style={{ padding: 20 }}>
      {/* Buttons to trigger success and error notifications */}
      <Button type="primary" onClick={showSuccessNotification}>
        Show Success Notification
      </Button>
      <Button type="danger" onClick={showErrorNotification} style={{ marginLeft: 10 }}>
        Show Error Notification
      </Button>
    </div>
  );
};

// Export the component as default
export default NotificationExample;
```

This code can be included in a React project. Make sure Ant Design is installed (`npm install antd`) before running the code.
