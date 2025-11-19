"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Explain how to integrate Ant Design's Modal component for user confirmation in a React application with code.
Generated: DETERMINISTIC_3b1da4fba226570f
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React from 'react';
import { Modal, Button } from 'antd'; // Ant Design components
import 'antd/dist/antd.css'; // Ant Design styles

// Define the ConfirmModal component
const ConfirmModal = () => {
  // State to manage modal visibility
  const [isModalVisible, setIsModalVisible] = React.useState(false);

  // Function to show the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle confirmation (OK button)
  const handleOk = () => {
    console.log('User confirmed action.');
    setIsModalVisible(false); // Close the modal
  };

  // Function to handle cancellation (Cancel button)
  const handleCancel = () => {
    console.log('User canceled action.');
    setIsModalVisible(false); // Close the modal
  };

  return (
    <div>
      {/* Button to trigger modal */}
      <Button type="primary" onClick={showModal}>
        Show Confirmation Modal
      </Button>

      {/* Modal component */}
      <Modal
        title="Confirm Action"
        visible={isModalVisible} // Control visibility 
        onOk={handleOk} // Handle OK action
        onCancel={handleCancel} // Handle Cancel action
        okText="Confirm" // Customize OK button text
        cancelText="Cancel" // Customize Cancel button text
      >
        <p>Are you sure you want to proceed?</p>
      </Modal>
    </div>
  );
};

// Export the ConfirmModal component
export default ConfirmModal;
```

### Notes:
- Install `antd` if not already installed: `npm install antd`.
- Ant Design CSS is imported for proper styling.
- Error handling is handled through logging user actions (`handleOk` and `handleCancel`).
