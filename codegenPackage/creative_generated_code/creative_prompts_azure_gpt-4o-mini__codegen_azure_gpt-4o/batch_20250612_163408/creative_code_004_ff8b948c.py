"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Create a code example that demonstrates state management in a React application, inspired by the practices of Tim Mansell.
Generated: DETERMINISTIC_ff8b948ca70196e7
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.js
import React, { useState } from 'react'; // Import React and the useState hook
import Counter from './Counter'; // Import the Counter component

const App = () => {
  // State management in the App component
  const [count, setCount] = useState(0); // State to hold the count value

  // Function to handle increment action
  const increment = () => {
    setCount((prevCount) => prevCount + 1); // Update state with the incremented value
  };

  // Function to handle decrement action
  const decrement = () => {
    setCount((prevCount) => Math.max(0, prevCount - 1)); // Ensure count doesn't go below 0
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>State Management Example</h1>
      {/* Pass state and state management utilities as props */}
      <Counter count={count} increment={increment} decrement={decrement} />
    </div>
  );
};

export default App;

// Counter.js
import React from 'react';
import PropTypes from 'prop-types'; // Import PropTypes for type-checking

const Counter = ({ count, increment, decrement }) => {
  return (
    <div>
      <h2>Current Count: {count}</h2>
      {/* Buttons to interact with state */}
      <button onClick={increment} style={{ margin: '10px', padding: '10px' }}>
        Increment
      </button>
      <button onClick={decrement} style={{ margin: '10px', padding: '10px' }}>
        Decrement
      </button>
    </div>
  );
};

// Prop type validation for the component props
Counter.propTypes = {
  count: PropTypes.number.isRequired, // count must be a number
  increment: PropTypes.func.isRequired, // increment must be a function
  decrement: PropTypes.func.isRequired, // decrement must be a function
};

export default Counter;

// index.js
import React from 'react';
import ReactDOM from 'react-dom/client'; // ReactDOM with createRoot API
import App from './App'; // Import the main App component

// Render the application to the DOM
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```

**Note**: This code assumes that you have a standard React project set up (e.g., created using `create-react-app`) and that all dependencies (React, ReactDOM, PropTypes) are installed.
