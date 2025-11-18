"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Modal component to display a confirmation dialog when a user clicks a button.
Generated: DETERMINISTIC_2bcea316522cbf2d
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';
import { Modal, Button } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

const ConfirmationModal = () => {
  // State to control the visibility of the modal
  const [isModalVisible, setIsModalVisible] = React.useState(false);

  // Function to show the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle the confirmation action
  const handleOk = () => {
    // Perform the action upon confirmation
    console.log('Confirmed!');
    // Close the modal
    setIsModalVisible(false);
  };

  // Function to handle the cancellation action
  const handleCancel = () => {
    console.log('Cancelled');
    // Close the modal
    setIsModalVisible(false);
  };

  return (
    <div>
      {/* Button to trigger the modal */}
      <Button type="primary" onClick={showModal}>
        Open Confirmation Modal
      </Button>
      
      {/* Ant Design Modal component */}
      <Modal
        title="Confirm Action"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes"
        cancelText="No"
      >
        <p>Are you sure you want to proceed with this action?</p>
      </Modal>
    </div>
  );
};

export default ConfirmationModal;
```
