"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Provide a step-by-step guide for editing the `pages/index.tsx` file in the Dapp Starter template to test hot module replacement (HMR) updates.
Generated: DETERMINISTIC_fdf696393ebc64ba
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```tsx
// File: pages/index.tsx

import { useState } from 'react';

// This is the main component for the index page of the Dapp Starter template.
const Home = () => {
  // Step 1: Define a state variable to test HMR updates.
  const [counter, setCounter] = useState(0);

  // Step 2: Add a function to handle counter increment.
  const incrementCounter = () => {
    setCounter((prevCounter) => prevCounter + 1);
  };

  // Step 3: Add a function to handle counter reset.
  const resetCounter = () => {
    setCounter(0);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      {/* Page Heading */}
      <h1>Welcome to the Dapp Starter Template</h1>

      {/* Step 4: Display the counter value */}
      <p style={{ fontSize: '20px', fontWeight: 'bold' }}>
        Current Counter Value: {counter}
      </p>

      {/* Step 5: Add buttons to interact with the counter */}
      <div>
        <button
          style={{
            padding: '10px 20px',
            fontSize: '16px',
            marginRight: '10px',
          }}
          onClick={incrementCounter}
        >
          Increment Counter
        </button>
        <button
          style={{
            padding: '10px 20px',
            fontSize: '16px',
          }}
          onClick={resetCounter}
        >
          Reset Counter
        </button>
      </div>

      {/* Step 6: Add a sample message to test HMR */}
      <p style={{ marginTop: '20px', fontSize: '16px', color: 'gray' }}>
        Try editing this message to test Hot Module Replacement (HMR):{' '}
        <span style={{ color: 'blue' }}>
          This is a sample message for HMR testing!
        </span>
      </p>
    </div>
  );
};

export default Home;

/*
  Notes:
  - This file demonstrates how to test HMR by making edits to the counter 
    functionality or the sample message.
  - When HMR works correctly, changes will reflect on the page without 
    requiring a full page reload.
  - To test HMR updates:
    1. Modify the text inside <span> or any other part of the component.
    2. Save the file and observe the changes in the browser.
*/
```
