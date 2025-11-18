"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Create a React application that uses Ant Design's Modal component to display a confirmation dialog when a user clicks a button.
Generated: DETERMINISTIC_989d070b0da32b83
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Button, Modal } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

class App extends React.Component {
  state = {
    visible: false, // Modal visibility state
  };

  // Function to show the modal
  showModal = () => {
    this.setState({ visible: true });
  };

  // Function to handle modal cancel
  handleCancel = () => {
    this.setState({ visible: false });
  };

  // Function to handle modal confirm
  handleOk = () => {
    // Add your confirmation logic here
    console.log('Confirmed!');
    this.setState({ visible: false });
  };

  render() {
    return (
      <div style={{ padding: '20px' }}>
        <Button type="primary" onClick={this.showModal}>
          Open Confirmation Dialog
        </Button>
        <Modal
          title="Confirm Action"
          visible={this.state.visible}
          onOk={this.handleOk} // Confirm button handler
          onCancel={this.handleCancel} // Cancel button handler
        >
          <p>Are you sure you want to proceed?</p>
        </Modal>
      </div>
    );
  }
}

// Render the App component into the root element
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
  "name": "antd-modal-example",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "antd": "^4.16.0",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3"
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

Make sure to run `npm install` to install the necessary dependencies before running the application.
