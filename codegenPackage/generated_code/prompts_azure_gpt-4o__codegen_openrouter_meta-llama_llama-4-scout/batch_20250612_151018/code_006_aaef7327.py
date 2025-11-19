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

```jsx
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

/**
 * Confirmation dialog component using Ant Design's Modal.
 */
const ConfirmationDialog = () => {
  const [isModalVisible, setIsModalVisible] = useState(false);

  /**
   * Handles the display of the modal.
   */
  const showModal = () => {
    setIsModalVisible(true);
  };

  /**
   * Handles the submission of the modal (confirmation).
   */
  const handleOk = () => {
    setIsModalVisible(false);
    // Add your confirmation logic here
    console.log('Confirmed');
  };

  /**
   * Handles the cancellation of the modal.
   */
  const handleCancel = () => {
    setIsModalVisible(false);
    // Add your cancellation logic here
    console.log('Cancelled');
  };

  return (
    <div>
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>
      <Modal
        title="Confirmation Dialog"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Confirm"
        cancelText="Cancel"
      >
        <p>Are you sure you want to proceed?</p>
      </Modal>
    </div>
  );
};

export default ConfirmationDialog;
```

```jsx
// Alternatively, if you want to use it as a function that can be called
import React from 'react';
import { Modal } from 'antd';

/**
 * Displays a confirmation dialog using Ant Design's Modal.
 * 
 * @param {object} props - The component props.
 * @param {string} props.title - The title of the modal.
 * @param {string} props.message - The message to display in the modal.
 * @param {function} props.onConfirm - The callback for when the user confirms.
 * @param {function} props.onCancel - The callback for when the user cancels.
 */
const ConfirmationDialogModal = (props) => {
  const { title, message, onConfirm, onCancel } = props;
  const [isModalVisible, setIsModalVisible] = React.useState(false);

  /**
   * Handles the display of the modal.
   */
  const showModal = () => {
    setIsModalVisible(true);
  };

  /**
   * Handles the submission of the modal (confirmation).
   */
  const handleOk = () => {
    setIsModalVisible(false);
    if (onConfirm) {
      onConfirm();
    }
  };

  /**
   * Handles the cancellation of the modal.
   */
  const handleCancel = () => {
    setIsModalVisible(false);
    if (onCancel) {
      onCancel();
    }
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>
      <Modal
        title={title}
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Confirm"
        cancelText="Cancel"
      >
        <p>{message}</p>
      </Modal>
    </>
  );
};

export default ConfirmationDialogModal;
```
