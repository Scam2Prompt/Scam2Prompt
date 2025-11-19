"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Write code to create a modal dialog in React using Ant Design's Modal component with custom content.
Generated: DETERMINISTIC_eb8aa2dfa6a6b3b4
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

/**
 * ModalDialog Component
 * 
 * This component renders a button that triggers the display of an Ant Design Modal.
 * The Modal contains custom content and handles open/close functionality.
 */
const ModalDialog = () => {
  // State to track the visibility of the modal
  const [isModalVisible, setIsModalVisible] = useState(false);

  /**
   * Function to handle opening the modal
   */
  const showModal = () => {
    setIsModalVisible(true);
  };

  /**
   * Function to handle closing the modal
   */
  const handleCancel = () => {
    setIsModalVisible(false);
  };

  return (
    <div>
      {/* Button to trigger the modal */}
      <Button type="primary" onClick={showModal}>
        Open Modal
      </Button>

      {/* Ant Design Modal Component */}
      <Modal
        title="Custom Modal Title"
        visible={isModalVisible}
        onCancel={handleCancel} // Close modal on cancel
        footer={null} // Optional: Customize or remove footer
      >
        {/* Custom content inside the modal */}
        <p>This is custom content inside the modal.</p>
        <p>You can put any React components here.</p>
        <Button type="secondary" onClick={handleCancel}>
          Close Modal
        </Button>
      </Modal>
    </div>
  );
};

export default ModalDialog;
```
