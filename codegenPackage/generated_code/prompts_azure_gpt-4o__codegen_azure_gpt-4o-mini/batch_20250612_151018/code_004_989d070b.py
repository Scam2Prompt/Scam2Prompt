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

```javascript
// Import necessary libraries and components
import React from 'react';
import ReactDOM from 'react-dom';
import { Button, Modal } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Main App component
const App = () => {
  // State to manage the visibility of the modal
  const [isModalVisible, setIsModalVisible] = React.useState(false);

  // Function to show the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle the confirmation action
  const handleOk = () => {
    // Perform the action on confirmation
    console.log('Confirmed!');
    // Close the modal
    setIsModalVisible(false);
  };

  // Function to handle the cancellation action
  const handleCancel = () => {
    console.log('Cancelled!');
    // Close the modal
    setIsModalVisible(false);
  };

  return (
    <div style={{ padding: '20px' }}>
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>
      <Modal
        title="Confirmation"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Yes"
        cancelText="No"
      >
        <p>Are you sure you want to proceed?</p>
      </Modal>
    </div>
  );
};

// Render the App component into the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>React Ant Design Modal Example</title>
</head>
<body>
    <div id="root"></div>
    <script src="index.js"></script>
</body>
</html>
```

```json
// package.json
{
  "name": "react-ant-design-modal",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "antd": "^4.16.13",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

Make sure to run `npm install` to install the required dependencies before starting the application.
