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
// Required imports
import React, { useState } from "react";
import ReactDOM from "react-dom";
import { Modal, Button } from "antd";
import "antd/dist/reset.css"; // Ant Design CSS reset file

// Main App Component
const App = () => {
  const [isModalVisible, setIsModalVisible] = useState(false);

  // Function to handle showing the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle "OK" button action
  const handleOk = () => {
    console.log("User confirmed action");
    setIsModalVisible(false);
  };

  // Function to handle "Cancel" button action
  const handleCancel = () => {
    console.log("User canceled action");
    setIsModalVisible(false);
  };

  return (
    <div style={{ padding: "20px" }}>
      {/* Button to trigger the modal */}
      <Button type="primary" onClick={showModal}>
        Open Confirmation Dialog
      </Button>

      {/* Ant Design Modal Component */}
      <Modal
        title="Confirmation"
        visible={isModalVisible}
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

// Rendering the App component into the DOM
ReactDOM.render(<App />, document.getElementById("root"));
```

**Note:** Ensure you have installed the required dependencies (`react`, `react-dom`, `antd`) and set up a standard React project. Use a tool like `create-react-app` or configure the project manually with a bundler like Webpack.
