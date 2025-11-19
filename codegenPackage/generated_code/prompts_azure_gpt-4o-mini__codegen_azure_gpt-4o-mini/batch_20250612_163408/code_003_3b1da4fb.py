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

```javascript
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

/**
 * ConfirmationModal component to handle user confirmation actions.
 * 
 * @param {Object} props - Component properties.
 * @param {boolean} props.visible - Controls the visibility of the modal.
 * @param {function} props.onConfirm - Function to call when the user confirms.
 * @param {function} props.onCancel - Function to call when the user cancels.
 * @param {string} props.title - Title of the modal.
 * @param {string} props.content - Content message of the modal.
 */
const ConfirmationModal = ({ visible, onConfirm, onCancel, title, content }) => {
    return (
        <Modal
            title={title}
            visible={visible}
            onOk={onConfirm}
            onCancel={onCancel}
            okText="Confirm"
            cancelText="Cancel"
        >
            <p>{content}</p>
        </Modal>
    );
};

/**
 * Main App component demonstrating the use of ConfirmationModal.
 */
const App = () => {
    const [isModalVisible, setIsModalVisible] = useState(false);

    // Function to show the modal
    const showModal = () => {
        setIsModalVisible(true);
    };

    // Function to handle confirmation
    const handleConfirm = () => {
        // Perform the action on confirmation
        console.log('User confirmed the action.');
        setIsModalVisible(false);
    };

    // Function to handle cancellation
    const handleCancel = () => {
        console.log('User canceled the action.');
        setIsModalVisible(false);
    };

    return (
        <div>
            <Button type="primary" onClick={showModal}>
                Open Confirmation Modal
            </Button>
            <ConfirmationModal
                visible={isModalVisible}
                onConfirm={handleConfirm}
                onCancel={handleCancel}
                title="Confirm Action"
                content="Are you sure you want to proceed with this action?"
            />
        </div>
    );
};

export default App;
```

### Notes:
- Ensure you have `antd` installed in your project by running `npm install antd`.
- Import the Ant Design CSS in your main entry file (e.g., `index.js` or `App.js`):
  ```javascript
  import 'antd/dist/antd.css';
  ```
