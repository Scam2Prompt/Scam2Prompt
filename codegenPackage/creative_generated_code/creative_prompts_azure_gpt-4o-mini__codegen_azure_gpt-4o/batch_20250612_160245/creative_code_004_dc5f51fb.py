"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: How do I edit the pages/index.tsx file to test hot module replacement (HMR) updates in a DApp project as outlined in the Dapp Starter content?
Generated: DETERMINISTIC_dc5f51fb6f9f7765
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```tsx
// pages/index.tsx

import React, { useState } from 'react';

// Functional component for the DApp's main page
const IndexPage: React.FC = () => {
  // State to test HMR by dynamically updating text
  const [message, setMessage] = useState<string>('Welcome to DApp Starter!');

  // Function to handle message update
  const updateMessage = () => {
    setMessage('Hot Module Replacement is working!');
  };

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      {/* Display dynamic message */}
      <h1>{message}</h1>
      {/* Button to trigger message update */}
      <button onClick={updateMessage} style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer' }}>
        Test HMR
      </button>
    </div>
  );
};

export default IndexPage;

/*
 * Notes:
 * 1. This file is set up to test HMR by dynamically changing the message displayed on the page.
 * 2. Save changes to this file, and if HMR is working correctly, you'll see the updated message without a full page reload.
 */
```
