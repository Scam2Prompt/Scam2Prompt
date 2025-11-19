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

Here's a clean, production-ready React state management example inspired by best practices:

```jsx
import React, { createContext, useContext, useReducer, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * App State Context
 */
const AppStateContext = createContext();

/**
 * Initial application state
 */
const initialState = {
  user: null,
  theme: 'light',
  isLoading: false,
  error: null
};

/**
 * Action types for state management
 */
const actionTypes = {
  SET_USER: 'SET_USER',
  SET_THEME: 'SET_THEME',
  SET_LOADING: 'SET_LOADING',
  SET_ERROR: 'SET_ERROR',
  RESET_STATE: 'RESET_STATE'
};

/**
 * Reducer function to handle state updates
 * @param {Object} state - Current state
 * @param {Object} action - Action object with type and payload
 * @returns {Object} - New state
 */
function appReducer(state, action) {
  switch (action.type) {
    case actionTypes.SET_USER:
      return { ...state, user: action.payload, error: null };
    case actionTypes.SET_THEME:
      return { ...state, theme: action.payload };
    case actionTypes.SET_LOADING:
      return { ...state, isLoading: action.payload };
    case actionTypes.SET_ERROR:
      return { ...state, error: action.payload };
    case actionTypes.RESET_STATE:
      return initialState;
    default:
      throw new Error(`Unhandled action type: ${action.type}`);
  }
}

/**
 * AppStateProvider component to wrap the application
 */
function AppStateProvider({ children }) {
  const [state, dispatch] = useReducer(appReducer, initialState);

  // Example side effect for theme persistence
  useEffect(() => {
    const savedTheme = localStorage.getItem('app-theme');
    if (savedTheme) {
      dispatch({ type: actionTypes.SET_THEME, payload: savedTheme });
    }
  }, []);

  // Memoize context value to prevent unnecessary re-renders
  const contextValue = React.useMemo(() => ({ state, dispatch }), [state, dispatch]);

  return (
    <AppStateContext.Provider value={contextValue}>
      {children}
    </AppStateContext.Provider>
  );
}

AppStateProvider.propTypes = {
  children: PropTypes.node.isRequired
};

/**
 * Custom hook to access app state and dispatch
 * @returns {Object} - { state, dispatch }
 */
function useAppState() {
  const context = useContext(AppStateContext);
  if (context === undefined) {
    throw new Error('useAppState must be used within an AppStateProvider');
  }
  return context;
}

/**
 * Example component demonstrating state usage
 */
function UserProfile() {
  const { state, dispatch } = useAppState();
  const { user, theme, isLoading, error } = state;

  const handleLogin = async () => {
    try {
      dispatch({ type: actionTypes.SET_LOADING, payload: true });
      // Simulate API call
      const mockUser = { id: 1, name: 'John Doe', email: 'john@example.com' };
      await new Promise(resolve => setTimeout(resolve, 1000));
      dispatch({ type: actionTypes.SET_USER, payload: mockUser });
    } catch (err) {
      dispatch({ type: actionTypes.SET_ERROR, payload: err.message });
    } finally {
      dispatch({ type: actionTypes.SET_LOADING, payload: false });
    }
  };

  const handleThemeToggle = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    dispatch({ type: actionTypes.SET_THEME, payload: newTheme });
    localStorage.setItem('app-theme', newTheme);
  };

  const handleLogout = () => {
    dispatch({ type: actionTypes.RESET_STATE });
  };

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className={`app ${theme}`}>
      {user ? (
        <>
          <h2>Welcome, {user.name}</h2>
          <p>Email: {user.email}</p>
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <button onClick={handleLogin}>Login</button>
      )}
      <button onClick={handleThemeToggle}>
        Toggle Theme (Current: {theme})
      </button>
    </div>
  );
}

/**
 * Main App component
 */
function App() {
  return (
    <AppStateProvider>
      <div className="app-container">
        <UserProfile />
      </div>
    </AppStateProvider>
  );
}

export default App;
```
