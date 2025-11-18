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

```jsx
// Import necessary modules
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

// ConfirmationDialog component
const ConfirmationDialog = () => {
  // State to control the visibility of the modal
  const [isModalVisible, setIsModalVisible] = useState(false);

  // Function to show the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle 'OK' button click
  const handleOk = () => {
    console.log('User confirmed action');
    setIsModalVisible(false); // Close the modal
  };

  // Function to handle 'Cancel' button click
  const handleCancel = () => {
    console.log('User canceled action');
    setIsModalVisible(false); // Close the modal
  };

  return (
    <div>
      {/* Button to trigger the modal */}
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>

      {/* Ant Design Modal component */}
      <Modal
        title="Confirmation"
        visible={isModalVisible}
        onOk={handleOk} // Handler for OK button
        onCancel={handleCancel} // Handler for Cancel button
        okText="Yes" // Custom text for OK button
        cancelText="No" // Custom text for Cancel button
      >
        <p>Are you sure you want to proceed?</p>
      </Modal>
    </div>
  );
};

export default ConfirmationDialog;
```
