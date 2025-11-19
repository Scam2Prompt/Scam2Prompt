"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Create a code example that demonstrates state management in a React application, inspired by the practices of Tim Mansell.
Generated: DETERMINISTIC_ff8b948ca70196e7
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// StateManagementExample.js
// A simple React application demonstrating state management using functional components and hooks.

import React, { useState } from 'react';

// Counter component to demonstrate state management
const Counter = () => {
  // State declaration using useState hook
  const [count, setCount] = useState(0);

  // Function to handle increment
  const increment = () => {
    setCount((prevCount) => prevCount + 1);
  };

  // Function to handle decrement
  const decrement = () => {
    setCount((prevCount) => Math.max(prevCount - 1, 0)); // Prevent negative count
  };

  // Function to reset the count
  const reset = () => {
    setCount(0);
  };

  return (
    <div style={styles.container}>
      <h1>Counter</h1>
      <p style={styles.count}>Current Count: {count}</p>
      <div style={styles.buttonContainer}>
        <button style={styles.button} onClick={increment}>
          Increment
        </button>
        <button style={styles.button} onClick={decrement}>
          Decrement
        </button>
        <button style={styles.button} onClick={reset}>
          Reset
        </button>
      </div>
    </div>
  );
};

// App component to render the Counter
const App = () => {
  return (
    <div>
      <Counter />
    </div>
  );
};

// Inline styles for the components
const styles = {
  container: {
    textAlign: 'center',
    marginTop: '50px',
  },
  count: {
    fontSize: '24px',
    margin: '20px 0',
  },
  buttonContainer: {
    display: 'flex',
    justifyContent: 'center',
    gap: '10px',
  },
  button: {
    padding: '10px 20px',
    fontSize: '16px',
    cursor: 'pointer',
    border: '1px solid #ccc',
    borderRadius: '5px',
    backgroundColor: '#f0f0f0',
  },
};

export default App;
```
