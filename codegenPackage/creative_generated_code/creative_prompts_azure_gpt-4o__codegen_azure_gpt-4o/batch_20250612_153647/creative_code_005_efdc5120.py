"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Provide a code example for editing the `pages/index.tsx` file in a Next.js DApp starter project to test hot module replacement (HMR) updates.
Generated: DETERMINISTIC_efdc5120ad41909a
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```tsx
// pages/index.tsx

import { useState } from 'react';

/**
 * This is the main page of the Next.js DApp starter project.
 * It includes a simple counter to test hot module replacement (HMR).
 */
const Home = () => {
  // State to manage the counter value
  const [counter, setCounter] = useState(0);

  // Function to increment the counter value
  const incrementCounter = () => {
    setCounter((prevCounter) => prevCounter + 1);
  };

  // Function to decrement the counter value
  const decrementCounter = () => {
    setCounter((prevCounter) => prevCounter - 1);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      {/* Header */}
      <h1>Welcome to the Next.js DApp Starter</h1>
      <p>
        Modify this page and save to test <strong>Hot Module Replacement (HMR)</strong>.
      </p>

      {/* Counter Section */}
      <div style={{ margin: '20px' }}>
        <h2>Counter Test</h2>
        <p>Current Counter Value: {counter}</p>
        <button onClick={incrementCounter} style={{ marginRight: '10px' }}>
          Increment
        </button>
        <button onClick={decrementCounter}>Decrement</button>
      </div>

      {/* Footer */}
      <footer style={{ marginTop: '50px', fontSize: '14px' }}>
        <p>&copy; {new Date().getFullYear()} Next.js DApp Starter</p>
      </footer>
    </div>
  );
};

export default Home;
```
