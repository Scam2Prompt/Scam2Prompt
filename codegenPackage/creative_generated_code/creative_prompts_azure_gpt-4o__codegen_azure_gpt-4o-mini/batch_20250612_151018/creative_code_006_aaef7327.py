"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to use Ant Design's Modal component for displaying a confirmation dialog in a React app.
Generated: DETERMINISTIC_aaef73274a6cf268
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

/**
 * ConfirmationDialog component is used to display a confirmation dialog
 * when the user attempts to perform a critical action.
 */
const ConfirmationDialog = () => {
  // State to control the visibility of the modal
  const [isModalVisible, setIsModalVisible] = useState(false);

  /**
   * Show the modal dialog
   */
  const showModal = () => {
    setIsModalVisible(true);
  };

  /**
   * Handle the confirmation action
   */
  const handleOk = () => {
    // Perform the action that requires confirmation here
    console.log('Confirmed action');
    setIsModalVisible(false);
  };

  /**
   * Handle the cancellation of the action
   */
  const handleCancel = () => {
    console.log('Action cancelled');
    setIsModalVisible(false);
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>
      <Modal
        title="Confirm Action"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes"
        cancelText="No"
      >
        <p>Are you sure you want to proceed with this action?</p>
      </Modal>
    </>
  );
};

export default ConfirmationDialog;
```

Make sure to install Ant Design in your project using:

```bash
npm install antd
```

And include the Ant Design CSS in your `index.js` or `App.js`:

```javascript
import 'antd/dist/antd.css';
```
