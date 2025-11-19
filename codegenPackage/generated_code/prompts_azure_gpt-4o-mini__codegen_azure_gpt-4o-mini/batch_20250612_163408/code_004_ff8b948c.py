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

```javascript
// Import necessary libraries
import React, { useReducer, createContext, useContext } from 'react';

// Define the initial state of the application
const initialState = {
    count: 0,
};

// Create a context for the state
const StateContext = createContext();

// Define action types
const ACTIONS = {
    INCREMENT: 'increment',
    DECREMENT: 'decrement',
    RESET: 'reset',
};

// Create a reducer function to manage state transitions
const reducer = (state, action) => {
    switch (action.type) {
        case ACTIONS.INCREMENT:
            return { ...state, count: state.count + 1 };
        case ACTIONS.DECREMENT:
            return { ...state, count: state.count - 1 };
        case ACTIONS.RESET:
            return initialState;
        default:
            throw new Error(`Unhandled action type: ${action.type}`);
    }
};

// Create a provider component to wrap the application
const StateProvider = ({ children }) => {
    const [state, dispatch] = useReducer(reducer, initialState);

    return (
        <StateContext.Provider value={{ state, dispatch }}>
            {children}
        </StateContext.Provider>
    );
};

// Custom hook to use the state context
const useStateContext = () => {
    const context = useContext(StateContext);
    if (!context) {
        throw new Error('useStateContext must be used within a StateProvider');
    }
    return context;
};

// Create a Counter component to display and manipulate the count
const Counter = () => {
    const { state, dispatch } = useStateContext();

    return (
        <div>
            <h1>Count: {state.count}</h1>
            <button onClick={() => dispatch({ type: ACTIONS.INCREMENT })}>Increment</button>
            <button onClick={() => dispatch({ type: ACTIONS.DECREMENT })}>Decrement</button>
            <button onClick={() => dispatch({ type: ACTIONS.RESET })}>Reset</button>
        </div>
    );
};

// Main App component
const App = () => {
    return (
        <StateProvider>
            <Counter />
        </StateProvider>
    );
};

// Export the App component as the default export
export default App;
```
