"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: How can I use Ant Design's Modal component to display a confirmation dialog? Write example code.
Generated: DETERMINISTIC_a7ed1d1d17c81f2f
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { Modal, Button } from 'antd';

/**
 * ConfirmationDialog component to display a confirmation dialog using Ant Design's Modal.
 * 
 * @param {Object} props - The properties object.
 * @param {boolean} props.visible - Determines if the modal is visible.
 * @param {Function} props.onConfirm - Function to execute when the user confirms the action.
 * @param {Function} props.onCancel - Function to execute when the user cancels the action.
 */
const ConfirmationDialog = ({ visible, onConfirm, onCancel }) => {
    // Function to handle confirm button click
    const handleConfirm = () => {
        try {
            onConfirm();
        } catch (error) {
            console.error("Error during confirmation:", error);
            // You may want to handle the error further, e.g., show a notification
        }
    };

    return (
        <Modal
            title="Confirm Action"
            visible={visible}
            onOk={handleConfirm}
            onCancel={onCancel}
            okText="Yes"
            cancelText="No"
            maskClosable={false} // Prevent closing by clicking outside
        >
            <p>Are you sure you want to proceed with this action?</p>
        </Modal>
    );
};

/**
 * Example usage of ConfirmationDialog component.
 */
const App = () => {
    const [isModalVisible, setIsModalVisible] = React.useState(false);

    const showModal = () => {
        setIsModalVisible(true);
    };

    const handleConfirm = () => {
        // Handle confirmation logic here
        console.log("Action confirmed!");
        setIsModalVisible(false);
    };

    const handleCancel = () => {
        // Handle cancellation logic here
        console.log("Action cancelled.");
        setIsModalVisible(false);
    };

    return (
        <div>
            <Button type="primary" onClick={showModal}>
                Show Confirmation Dialog
            </Button>
            <ConfirmationDialog 
                visible={isModalVisible} 
                onConfirm={handleConfirm} 
                onCancel={handleCancel} 
            />
        </div>
    );
};

export default App;
```

Make sure to install Ant Design by running:
```bash
npm install antd
```

And import Ant Design's CSS in your main entry file (e.g., `index.js`):
```javascript
import 'antd/dist/antd.css';
```
