"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to use Ant Design's Modal component for displaying a confirmation dialog in a React app.
Generated: DETERMINISTIC_aaef73274a6cf268
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

/**
 * ConfirmationDialog component that uses Ant Design's Modal
 * to display a confirmation dialog.
 */
const ConfirmationDialog = () => {
  // State to control the visibility of the modal
  const [isVisible, setIsVisible] = useState(false);

  /**
   * Function to show the modal
   */
  const showModal = () => {
    setIsVisible(true);
  };

  /**
   * Function to handle the confirmation action
   */
  const handleOk = () => {
    // Perform the action on confirmation
    console.log('Confirmed!');
    // Close the modal
    setIsVisible(false);
  };

  /**
   * Function to handle the cancellation action
   */
  const handleCancel = () => {
    // Close the modal without performing any action
    console.log('Cancelled');
    setIsVisible(false);
  };

  return (
    <div>
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>
      <Modal
        title="Confirm Action"
        visible={isVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes"
        cancelText="No"
      >
        <p>Are you sure you want to proceed with this action?</p>
      </Modal>
    </div>
  );
};

export default ConfirmationDialog;
```

Make sure to install Ant Design in your project by running:
```bash
npm install antd
```

And import the Ant Design CSS in your main entry file (e.g., `index.js` or `App.js`):
```javascript
import 'antd/dist/antd.css';
```
