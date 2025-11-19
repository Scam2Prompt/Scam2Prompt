"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Use Ant Design's Modal component to create a confirmation dialog in React that triggers on a button click.
Generated: DETERMINISTIC_26373222f5015b8d
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
import { ExclamationCircleOutlined } from '@ant-design/icons';

const ConfirmationDialog = () => {
  const [isModalVisible, setIsModalVisible] = useState(false);

  const showModal = () => {
    setIsModalVisible(true);
  };

  const handleOk = () => {
    // Perform action on confirmation
    console.log('Action confirmed');
    setIsModalVisible(false);
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>
      <Modal
        title={
          <>
            <ExclamationCircleOutlined style={{ color: '#faad14', marginRight: 8 }} />
            Confirm Action
          </>
        }
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Confirm"
        cancelText="Cancel"
      >
        <p>Are you sure you want to perform this action?</p>
      </Modal>
    </>
  );
};

export default ConfirmationDialog;
```
