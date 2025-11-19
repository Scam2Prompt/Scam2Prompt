"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: How do I integrate Ant Design's modal component into my React project for user confirmations?
Generated: DETERMINISTIC_9344beebf6e62ac0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

// Create a functional component for the confirmation modal
const ConfirmationModal = () => {
  // State to control the visibility of the modal
  const [isModalVisible, setIsModalVisible] = useState(false);

  // Function to show the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle the "OK" button click
  const handleOk = () => {
    console.log('User confirmed the action'); // Example action on confirmation
    setIsModalVisible(false); // Close the modal
  };

  // Function to handle the "Cancel" button click
  const handleCancel = () => {
    console.log('User canceled the action'); // Example action on cancellation
    setIsModalVisible(false); // Close the modal
  };

  return (
    <div>
      {/* Button to trigger the modal */}
      <Button type="primary" onClick={showModal}>
        Show Confirmation Modal
      </Button>

      {/* Ant Design Modal Component */}
      <Modal
        title="Confirm Your Action" // Title of the modal
        visible={isModalVisible} // Control visibility via state
        onOk={handleOk} // Function to execute on "OK" button click
        onCancel={handleCancel} // Function to execute on "Cancel" button click
        okText="Confirm" // Custom text for the "OK" button
        cancelText="Cancel" // Custom text for the "Cancel" button
      >
        <p>Are you sure you want to perform this action?</p> {/* Modal content */}
      </Modal>
    </div>
  );
};

export default ConfirmationModal; // Export the component for use in the application
```
