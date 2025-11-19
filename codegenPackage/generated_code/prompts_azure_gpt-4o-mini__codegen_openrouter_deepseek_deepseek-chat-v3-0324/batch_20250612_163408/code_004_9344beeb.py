"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: How do I integrate Ant Design's modal component into my React project for user confirmations?
Generated: DETERMINISTIC_9344beebf6e62ac0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation of Ant Design's modal for user confirmations in a React project:

```jsx
import React from 'react';
import { Modal, Button } from 'antd';
import { ExclamationCircleFilled } from '@ant-design/icons';

const { confirm } = Modal;

/**
 * Component demonstrating Ant Design confirmation modal usage
 */
const ConfirmationModal = () => {
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
        }).catch(() => console.log('Oops errors!'));
      },
      onCancel() {
        console.log('Cancelled');
      },
    });
  };

  const showDeleteConfirm = () => {
    confirm({
      title: 'Are you sure you want to delete this item?',
      icon: <ExclamationCircleFilled />,
      content: 'Deleting this item will remove all associated data.',
      okText: 'Yes, delete it',
      okType: 'danger',
      cancelText: 'No, keep it',
      onOk() {
        return handleDelete()
          .then(() => {
            console.log('Item deleted successfully');
          })
          .catch((err) => {
            console.error('Deletion failed:', err);
            throw err; // Keep modal open on error
          });
      },
      onCancel() {
        console.log('Deletion cancelled');
      },
    });
  };

  // Mock delete function
  const handleDelete = () => {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 1500);
    });
  };

  return (
    <div>
      <Button type="primary" onClick={showConfirm}>
        Show Basic Confirm
      </Button>
      <Button
        danger
        onClick={showDeleteConfirm}
        style={{ marginLeft: '16px' }}
      >
        Delete Item
      </Button>
    </div>
  );
};

export default ConfirmationModal;
```

```jsx
// App.js (example usage)
import React from 'react';
import { ConfigProvider } from 'antd';
import ConfirmationModal from './ConfirmationModal';

const App = () => {
  return (
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: '#00b96b',
        },
      }}
    >
      <div style={{ padding: '24px' }}>
        <h1>Ant Design Confirmations</h1>
        <ConfirmationModal />
      </div>
    </ConfigProvider>
  );
};

export default App;
```

```json
// package.json dependencies
{
  "dependencies": {
    "antd": "^5.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@ant-design/icons": "^5.0.0"
  }
}
```
