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
import React, { useState } from 'react';
import { Modal, Button } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

const ConfirmationModal = () => {
  // State to control the visibility of the modal
  const [visible, setVisible] = useState(false);

  // Function to show the modal
  const showModal = () => {
    setVisible(true);
  };

  // Function to handle the "OK" action
  const handleOk = () => {
    // Perform action on confirmation here
    console.log('Confirmed!');
    setVisible(false);
  };

  // Function to handle the "Cancel" action
  const handleCancel = () => {
    console.log('Cancelled!');
    setVisible(false);
  };

  return (
    <>
      {/* Button to trigger the modal */}
      <Button type="primary" onClick={showModal}>
        Open Confirmation Modal
      </Button>
      
      {/* Ant Design Modal component */}
      <Modal
        title="Confirm Action"
        visible={visible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes"
        cancelText="No"
      >
        <p>Are you sure you want to proceed with this action?</p>
      </Modal>
    </>
  );
};

export default ConfirmationModal;
```

### Usage
To use the `ConfirmationModal` component, simply import and include it in your desired component or page:

```javascript
import React from 'react';
import ConfirmationModal from './ConfirmationModal';

const App = () => {
  return (
    <div>
      <h1>User Confirmation Example</h1>
      <ConfirmationModal />
    </div>
  );
};

export default App;
```

### Note
Make sure to install Ant Design in your project by running:
```bash
npm install antd
```
