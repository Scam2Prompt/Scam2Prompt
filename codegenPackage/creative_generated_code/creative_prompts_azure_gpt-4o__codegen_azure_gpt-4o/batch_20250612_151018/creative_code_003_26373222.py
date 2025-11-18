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
// Import necessary libraries and components
import React, { useState } from 'react';
import { Button, Modal } from 'antd';

// Functional component for the confirmation dialog
const ConfirmationDialog = () => {
  // State to manage the visibility of the modal
  const [isModalVisible, setIsModalVisible] = useState(false);

  // Function to show the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle OK button click (user confirms)
  const handleOk = () => {
    console.log("User confirmed the action.");
    setIsModalVisible(false); // Close the modal
  };

  // Function to handle Cancel button click
  const handleCancel = () => {
    console.log("User canceled the action.");
    setIsModalVisible(false); // Close the modal
  };

  return (
    <>
      {/* Button to trigger the modal */}
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>

      {/* Ant Design Modal component */}
      <Modal
        title="Confirmation"
        visible={isModalVisible}
        onOk={handleOk} // Callback for OK button
        onCancel={handleCancel} // Callback for Cancel button
        okText="Confirm" // Custom text for OK button
        cancelText="Cancel" // Custom text for Cancel button
      >
        {/* Modal content */}
        <p>Are you sure you want to proceed?</p>
      </Modal>
    </>
  );
};

// Export the component for use in other parts of the application
export default ConfirmationDialog;
```
