"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Use Ant Design's Modal component to create a confirmation dialog in React that triggers on a button click.
Generated: DETERMINISTIC_26373222f5015b8d
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
import { Button, Modal } from 'antd';

/**
 * ConfirmationDialog component that renders a button
 * which triggers a confirmation dialog when clicked.
 */
const ConfirmationDialog = () => {
  // State to control the visibility of the modal
  const [isModalVisible, setIsModalVisible] = useState(false);

  /**
   * Function to show the modal
   */
  const showModal = () => {
    setIsModalVisible(true);
  };

  /**
   * Function to handle the confirmation action
   */
  const handleOk = () => {
    // Perform the confirmation action here
    console.log("Confirmed!");
    // Close the modal
    setIsModalVisible(false);
  };

  /**
   * Function to handle the cancellation action
   */
  const handleCancel = () => {
    console.log("Cancelled!");
    // Close the modal
    setIsModalVisible(false);
  };

  return (
    <>
      {/* Button to trigger the modal */}
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>

      {/* Ant Design Modal */}
      <Modal
        title="Confirm Action"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes"
        cancelText="No"
      >
        <p>Are you sure you want to proceed?</p>
      </Modal>
    </>
  );
};

export default ConfirmationDialog;
```

**Usage:**
To use the `ConfirmationDialog` component, simply import it and include it in your JSX like so:

```javascript
import React from 'react';
import ConfirmationDialog from './ConfirmationDialog';

const App = () => (
  <div>
    <h1>My App</h1>
    <ConfirmationDialog />
  </div>
);

export default App;
```

**Dependencies:**
Make sure to install `antd` if you haven't already:

```bash
npm install antd
```
