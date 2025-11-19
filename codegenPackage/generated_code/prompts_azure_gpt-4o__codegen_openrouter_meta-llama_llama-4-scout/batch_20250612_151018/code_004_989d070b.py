"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Create a React application that uses Ant Design's Modal component to display a confirmation dialog when a user clicks a button.
Generated: DETERMINISTIC_989d070b0da32b83
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
 * ConfirmationModal component that displays a confirmation dialog when a button is clicked.
 */
function ConfirmationModal() {
  // State to track if the modal is visible
  const [visible, setVisible] = useState(false);

  // Function to show the modal
  const showModal = () => {
    setVisible(true);
  };

  // Function to handle modal ok button click
  const handleOk = () => {
    // Add your logic here for when the user confirms
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
        Open Confirmation Modal
      </Button>
      <Modal
        title="Confirmation"
        visible={visible}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <p>Are you sure you want to proceed?</p>
      </Modal>
    </div>
  );
}

export default ConfirmationModal;
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import ConfirmationModal from './ConfirmationModal';
import 'antd/dist/antd.css'; // Import Ant Design CSS

ReactDOM.render(
  <React.StrictMode>
    <ConfirmationModal />
  </React.StrictMode>,
  document.getElementById('root')
);
```
