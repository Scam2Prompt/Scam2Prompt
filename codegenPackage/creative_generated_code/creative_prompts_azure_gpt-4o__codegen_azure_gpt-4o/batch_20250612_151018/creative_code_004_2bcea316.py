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

```javascript
// Import necessary dependencies
import React from 'react';
import { Modal, Button } from 'antd';

// Functional component to showcase Ant Design's Modal for confirmation dialog
const ConfirmationModalExample = () => {
  // Function to handle the confirmation dialog
  const showConfirmation = () => {
    Modal.confirm({
      title: 'Are you sure?',
      content: 'Do you really want to perform this action?',
      okText: 'Yes',
      cancelText: 'No',
      onOk: () => {
        // Handle the action when "Yes" is clicked
        console.log('Confirmed: Action performed.');
      },
      onCancel: () => {
        // Handle the action when "No" is clicked
        console.log('Cancelled: Action aborted.');
      },
    });
  };

  return (
    <div>
      {/* Button to trigger the confirmation modal */}
      <Button type="primary" onClick={showConfirmation}>
        Show Confirmation Dialog
      </Button>
    </div>
  );
};

export default ConfirmationModalExample;
```
