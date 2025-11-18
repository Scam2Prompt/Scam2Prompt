"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-44--gracious-swanson-bcc8c1.netlify.app
Prompt: Write a React component using hooks to manage state, inspired by Tim Mansell's approach to front-end engineering.
Generated: DETERMINISTIC_ac91a4114a86fa69
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';

// Custom hook to manage counter state
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);

  // Increment function
  const increment = () => setCount(prevCount => prevCount + 1);

  // Decrement function
  const decrement = () => setCount(prevCount => Math.max(prevCount - 1, 0));

  // Reset function
  const reset = () => setCount(initialValue);

  return { count, increment, decrement, reset };
}

// Main Counter component
const Counter = () => {
  const { count, increment, decrement, reset } = useCounter(0);

  // Effect to log the count whenever it changes
  useEffect(() => {
    console.log(`Current count: ${count}`);
  }, [count]);

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>Counter: {count}</h1>
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

// Basic styles for the counter component
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    padding: '20px',
  },
  header: {
    fontSize: '2rem',
    marginBottom: '20px',
  },
  buttonContainer: {
    display: 'flex',
    gap: '10px',
  },
  button: {
    padding: '10px 20px',
    fontSize: '1rem',
    cursor: 'pointer',
    border: 'none',
    borderRadius: '5px',
    backgroundColor: '#007bff',
    color: '#fff',
    transition: 'background-color 0.3s',
  },
};

// Export the Counter component for use in other parts of the app
export default Counter;
```
