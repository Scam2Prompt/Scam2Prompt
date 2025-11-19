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

```javascript
// Import necessary dependencies
import React, { useReducer, createContext, useContext } from 'react';

// Define initial state
const initialState = {
  count: 0,
};

// Create a context for state management
const CounterContext = createContext();

// Define a reducer function to handle state updates
const counterReducer = (state, action) => {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return initialState;
    default:
      throw new Error(`Unhandled action type: ${action.type}`);
  }
};

// Create a provider component to encapsulate state and dispatch logic
const CounterProvider = ({ children }) => {
  const [state, dispatch] = useReducer(counterReducer, initialState);

  return (
    <CounterContext.Provider value={{ state, dispatch }}>
      {children}
    </CounterContext.Provider>
  );
};

// Custom hook to use the Counter context
const useCounter = () => {
  const context = useContext(CounterContext);
  if (context === undefined) {
    throw new Error('useCounter must be used within a CounterProvider');
  }
  return context;
};

// Main Counter component
const Counter = () => {
  const { state, dispatch } = useCounter();

  return (
    <div>
      <h1>Count: {state.count}</h1>
      <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>Decrement</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
    </div>
  );
};

// App component that uses CounterProvider to manage state
const App = () => {
  return (
    <CounterProvider>
      <Counter />
    </CounterProvider>
  );
};

// Export the main App component for rendering
export default App;
```
