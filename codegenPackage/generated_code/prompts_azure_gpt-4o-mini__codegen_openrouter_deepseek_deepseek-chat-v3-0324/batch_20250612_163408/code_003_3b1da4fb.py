"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Explain how to integrate Ant Design's Modal component for user confirmation in a React application with code.
Generated: DETERMINISTIC_3b1da4fba226570f
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation of Ant Design's Modal confirmation in a React application:

```jsx
import React from 'react';
import { Modal, Button } from 'antd';
import { ExclamationCircleFilled } from '@ant-design/icons';

const { confirm } = Modal;

/**
 * Component demonstrating Ant Design confirmation modal usage
 */
const ConfirmationExample = () => {
  /**
   * Shows a confirmation dialog before proceeding with an action
   */
  const showConfirm = () => {
    confirm({
      title: 'Are you sure you want to proceed?',
      icon: <ExclamationCircleFilled />,
      content: 'This action cannot be undone.',
      okText: 'Confirm',
      okType: 'danger',
      cancelText: 'Cancel',
      onOk() {
        return new Promise((resolve, reject) => {
          // Simulate async operation
          setTimeout(() => {
            resolve();
            console.log('Confirmed!');
          }, 1000);
        }).catch(() => console.error('Confirmation failed'));
      },
      onCancel() {
        console.log('Action cancelled');
      },
    });
  };

  /**
   * Shows a delete confirmation with custom styles
   */
  const showDeleteConfirm = () => {
    confirm({
      title: 'Delete this item?',
      icon: <ExclamationCircleFilled />,
      content: 'The item will be permanently deleted from the system.',
      okText: 'Delete',
      okType: 'danger',
      cancelText: 'Cancel',
      centered: true,
      className: 'custom-confirm-modal',
      onOk() {
        return handleDelete();
      },
    });
  };

  /**
   * Handles the actual delete operation
   */
  const handleDelete = async () => {
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1500));
      console.log('Item deleted successfully');
    } catch (error) {
      console.error('Failed to delete item:', error);
      throw error; // Re-throw to keep the modal in loading state
    }
  };

  return (
    <div className="confirmation-example">
      <Button type="primary" onClick={showConfirm}>
        Show Confirmation
      </Button>
      
      <Button
        danger
        onClick={showDeleteConfirm}
        style={{ marginLeft: 16 }}
      >
        Delete Item
      </Button>
    </div>
  );
};

export default ConfirmationExample;
```

And the corresponding CSS for custom styling (optional):

```css
/* Custom modal styles */
.custom-confirm-modal .ant-modal-body {
  padding: 24px;
}

.custom-confirm-modal .ant-modal-confirm-title {
  color: #ff4d4f;
}

.custom-confirm-modal .ant-modal-confirm-content {
  margin-top: 8px;
}
```

This implementation includes:
- Basic confirmation dialog
- Delete confirmation example with async operation
- Promise-based handling for async operations
- Custom styling example
- Proper error handling
- Clean component structure
