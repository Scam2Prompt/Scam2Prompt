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

```jsx
import React, { useState } from 'react';
import { Button, Modal } from 'antd';

/**
 * DeleteConfirmationModal: A React component that displays a confirmation dialog
 * using Ant Design's Modal when the user clicks the delete button.
 */
const DeleteConfirmationModal = () => {
  // State to manage the visibility of the modal
  const [isModalVisible, setIsModalVisible] = useState(false);

  /**
   * Function to show the modal
   */
  const showModal = () => {
    setIsModalVisible(true);
  };

  /**
   * Function to handle the OK button click in the modal
   */
  const handleOk = () => {
    console.log("Item deleted"); // Replace with actual delete logic
    setIsModalVisible(false); // Close the modal
  };

  /**
   * Function to handle the Cancel button click in the modal
   */
  const handleCancel = () => {
    console.log("Delete action canceled");
    setIsModalVisible(false); // Close the modal
  };

  return (
    <div>
      {/* Delete button that triggers the confirmation modal */}
      <Button type="primary" danger onClick={showModal}>
        Delete Item
      </Button>
      
      {/* Ant Design Modal component for confirmation */}
      <Modal
        title="Confirm Deletion"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes, delete"
        cancelText="Cancel"
      >
        {/* Modal content */}
        <p>Are you sure you want to delete this item? This action cannot be undone.</p>
      </Modal>
    </div>
  );
};

export default DeleteConfirmationModal;
```
