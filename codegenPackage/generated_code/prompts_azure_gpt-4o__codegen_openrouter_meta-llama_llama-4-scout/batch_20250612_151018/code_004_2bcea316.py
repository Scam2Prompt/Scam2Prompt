"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Modal component to display a confirmation dialog when a user clicks a button.
Generated: DETERMINISTIC_2bcea316522cbf2d
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
 * Confirmation Dialog Example
 * 
 * This component demonstrates how to use Ant Design's Modal component to display a confirmation dialog when a user clicks a button.
 */
const ConfirmationDialog = () => {
  // State to track whether the modal is visible
  const [visible, setVisible] = useState(false);

  // Function to show the modal
  const showModal = () => {
    setVisible(true);
  };

  // Function to handle modal ok button click
  const handleOk = () => {
    // Add your confirmation logic here
    console.log('Confirmed');
    setVisible(false);
  };

  // Function to handle modal cancel button click
  const handleCancel = () => {
    console.log('Cancelled');
    setVisible(false);
  };

  return (
    <div>
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>
      <Modal
        title="Confirmation Dialog"
        visible={visible}
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

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import ConfirmationDialog from './ConfirmationDialog';

ReactDOM.render(
  <React.StrictMode>
    <ConfirmationDialog />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```css
/* styles.css */
@import '~antd/dist/antd.css';

#root {
  text-align: center;
  margin-top: 20px;
}
```
