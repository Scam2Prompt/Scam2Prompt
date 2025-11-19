"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Write a React function that uses Ant Design's Modal component to display a confirmation dialog when a user clicks a delete button.
Generated: DETERMINISTIC_8503f8b0d1dc3a8c
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
import { ExclamationCircleFilled } from '@ant-design/icons';

const DeleteConfirmationModal = ({ itemName, onConfirm }) => {
  const [open, setOpen] = useState(false);
  const [confirmLoading, setConfirmLoading] = useState(false);

  const showModal = () => {
    setOpen(true);
  };

  const handleOk = async () => {
    setConfirmLoading(true);
    try {
      await onConfirm();
      setOpen(false);
    } catch (error) {
      console.error('Error during deletion:', error);
    } finally {
      setConfirmLoading(false);
    }
  };

  const handleCancel = () => {
    setOpen(false);
  };

  return (
    <>
      <Button danger onClick={showModal}>
        Delete
      </Button>
      <Modal
        title={
          <>
            <ExclamationCircleFilled style={{ color: '#faad14', marginRight: 8 }} />
            Confirm Deletion
          </>
        }
        open={open}
        onOk={handleOk}
        confirmLoading={confirmLoading}
        onCancel={handleCancel}
        okText="Delete"
        okButtonProps={{ danger: true }}
        cancelButtonProps={{ type: 'text' }}
      >
        <p>Are you sure you want to delete {itemName}? This action cannot be undone.</p>
      </Modal>
    </>
  );
};

export default DeleteConfirmationModal;
```
