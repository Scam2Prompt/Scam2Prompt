"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Write a React function that uses Ant Design's Modal component to display a confirmation dialog when a user clicks a delete button.
Generated: DETERMINISTIC_8503f8b0d1dc3a8c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { Modal, Button } from 'antd';

const ConfirmationDialog = ({ onConfirm, onCancel }) => {
  // State to control the visibility of the modal
  const [visible, setVisible] = React.useState(false);

  // Function to show the modal
  const showModal = () => {
    setVisible(true);
  };

  // Function to handle the confirmation action
  const handleOk = () => {
    try {
      onConfirm(); // Call the confirmation callback
      setVisible(false); // Close the modal
    } catch (error) {
      console.error('Error during confirmation:', error);
      // You may handle the error further, e.g., show a notification
    }
  };

  // Function to handle the cancellation action
  const handleCancel = () => {
    setVisible(false); // Close the modal
    if (onCancel) {
      onCancel(); // Call the cancel callback if provided
    }
  };

  return (
    <>
      <Button type="primary" danger onClick={showModal}>
        Delete
      </Button>
      <Modal
        title="Confirm Deletion"
        visible={visible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes, delete it"
        cancelText="No, cancel"
      >
        <p>Are you sure you want to delete this item?</p>
      </Modal>
    </>
  );
};

export default ConfirmationDialog;
```
