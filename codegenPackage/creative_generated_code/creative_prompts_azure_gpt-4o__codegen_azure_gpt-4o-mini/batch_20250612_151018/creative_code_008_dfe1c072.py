"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-52--gracious-swanson-bcc8c1.netlify.app
Prompt: Generate a React code snippet for a front-end application that aligns with Tim Mansell's JavaScript development practices.
Generated: DETERMINISTIC_dfe1c072cd297a05
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
import PropTypes from 'prop-types';
import './App.css'; // Assuming you have a CSS file for styling

/**
 * A simple counter component that increments or decrements a value.
 */
const Counter = ({ initialCount }) => {
  const [count, setCount] = useState(initialCount);

  // Handle incrementing the counter
  const increment = () => {
    setCount(prevCount => prevCount + 1);
  };

  // Handle decrementing the counter
  const decrement = () => {
    setCount(prevCount => Math.max(0, prevCount - 1)); // Prevent negative count
  };

  // Effect to log the count to the console
  useEffect(() => {
    console.log(`Current count: ${count}`);
  }, [count]); // Dependency array to run effect when count changes

  return (
    <div className="counter">
      <h1>Counter: {count}</h1>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};

// PropTypes for type checking
Counter.propTypes = {
  initialCount: PropTypes.number.isRequired,
};

// Default props
Counter.defaultProps = {
  initialCount: 0,
};

/**
 * Main App component that renders the Counter component.
 */
const App = () => {
  return (
    <div className="App">
      <h1>Welcome to the Counter App</h1>
      <Counter initialCount={0} />
    </div>
  );
};

export default App;
```
