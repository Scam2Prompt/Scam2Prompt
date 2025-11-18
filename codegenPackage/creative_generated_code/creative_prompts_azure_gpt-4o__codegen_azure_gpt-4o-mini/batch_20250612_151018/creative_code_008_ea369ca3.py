"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's notification API to show success and error messages in a React app.
Generated: DETERMINISTIC_ea369ca359a342d8
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
import ReactDOM from 'react-dom';
import { Button, notification } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Function to open a success notification
const openSuccessNotification = () => {
    notification.success({
        message: 'Success',
        description: 'Your operation was completed successfully!',
        placement: 'topRight',
        duration: 3, // Duration in seconds
    });
};

// Function to open an error notification
const openErrorNotification = () => {
    notification.error({
        message: 'Error',
        description: 'There was an issue with your operation.',
        placement: 'topRight',
        duration: 3, // Duration in seconds
    });
};

// Main App component
const App = () => {
    return (
        <div style={{ padding: '50px' }}>
            <h1>Ant Design Notification Example</h1>
            <Button type="primary" onClick={openSuccessNotification}>
                Show Success Notification
            </Button>
            <Button type="danger" onClick={openErrorNotification} style={{ marginLeft: '10px' }}>
                Show Error Notification
            </Button>
        </div>
    );
};

// Render the App component into the DOM
const rootElement = document.getElementById('root');

// Check if rootElement exists before rendering
if (rootElement) {
    ReactDOM.render(<App />, rootElement);
} else {
    console.error('Root element not found. Ensure your HTML has a <div id="root"></div> for React to mount.');
}
```
