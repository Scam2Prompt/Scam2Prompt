"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: How can I use Ant Design's Modal component to display a confirmation dialog? Write example code.
Generated: DETERMINISTIC_a7ed1d1d17c81f2f
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from React and Ant Design
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

// Define the functional component
const ConfirmationDialogExample = () => {
  const [isModalVisible, setIsModalVisible] = useState(false);

  // Function to show the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle "OK" action
  const handleOk = () => {
    console.log('User confirmed.');
    setIsModalVisible(false);
  };

  // Function to handle "Cancel" action
  const handleCancel = () => {
    console.log('User canceled.');
    setIsModalVisible(false);
  };

  return (
    <div>
      {/* Button to trigger the confirmation dialog */}
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>

      {/* Ant Design Modal component */}
      <Modal
        title="Confirmation"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes"
        cancelText="No"
      >
        <p>Are you sure you want to proceed?</p>
      </Modal>
    </div>
  );
};

// Export the component
export default ConfirmationDialogExample;
```
