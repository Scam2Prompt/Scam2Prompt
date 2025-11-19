"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-portal-interface-react.pages.dev
Prompt: How do I set up a state management solution for a claim portal in React, inspired by SuperFarm's Claim Portal?
Generated: DETERMINISTIC_89fb192ae8e55c7c
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { createContext, useContext, useReducer } from 'react';

// Define the initial state for the claim portal
const initialState = {
  claims: [],
  loading: false,
  error: null,
};

// Action types for reducer
const ACTIONS = {
  FETCH_CLAIMS_REQUEST: 'FETCH_CLAIMS_REQUEST',
  FETCH_CLAIMS_SUCCESS: 'FETCH_CLAIMS_SUCCESS',
  FETCH_CLAIMS_FAILURE: 'FETCH_CLAIMS_FAILURE',
  ADD_CLAIM: 'ADD_CLAIM',
  REMOVE_CLAIM: 'REMOVE_CLAIM',
};

// Create a context for the claim portal
const ClaimContext = createContext();

// Reducer function to manage state transitions
const claimReducer = (state, action) => {
  switch (action.type) {
    case ACTIONS.FETCH_CLAIMS_REQUEST:
      return { ...state, loading: true, error: null };
    case ACTIONS.FETCH_CLAIMS_SUCCESS:
      return { ...state, loading: false, claims: action.payload };
    case ACTIONS.FETCH_CLAIMS_FAILURE:
      return { ...state, loading: false, error: action.payload };
    case ACTIONS.ADD_CLAIM:
      return { ...state, claims: [...state.claims, action.payload] };
    case ACTIONS.REMOVE_CLAIM:
      return { ...state, claims: state.claims.filter(claim => claim.id !== action.payload) };
    default:
      return state;
  }
};

// Provider component to wrap around the application
export const ClaimProvider = ({ children }) => {
  const [state, dispatch] = useReducer(claimReducer, initialState);

  // Fetch claims from an API
  const fetchClaims = async () => {
    dispatch({ type: ACTIONS.FETCH_CLAIMS_REQUEST });
    try {
      const response = await fetch('/api/claims'); // Replace with the actual API endpoint
      if (!response.ok) throw new Error('Failed to fetch claims');
      const data = await response.json();
      dispatch({ type: ACTIONS.FETCH_CLAIMS_SUCCESS, payload: data });
    } catch (error) {
      dispatch({ type: ACTIONS.FETCH_CLAIMS_FAILURE, payload: error.message });
    }
  };

  // Add a new claim
  const addClaim = (claim) => {
    dispatch({ type: ACTIONS.ADD_CLAIM, payload: claim });
  };

  // Remove a claim by ID
  const removeClaim = (id) => {
    dispatch({ type: ACTIONS.REMOVE_CLAIM, payload: id });
  };

  return (
    <ClaimContext.Provider value={{ state, fetchClaims, addClaim, removeClaim }}>
      {children}
    </ClaimContext.Provider>
  );
};

// Custom hook to use claim context
export const useClaimContext = () => {
  const context = useContext(ClaimContext);
  if (!context) {
    throw new Error('useClaimContext must be used within a ClaimProvider');
  }
  return context;
};

// Example component to display claims
const ClaimList = () => {
  const { state, fetchClaims } = useClaimContext();

  // Fetch claims on component mount
  React.useEffect(() => {
    fetchClaims();
  }, [fetchClaims]);

  if (state.loading) return <div>Loading...</div>;
  if (state.error) return <div>Error: {state.error}</div>;

  return (
    <ul>
      {state.claims.map(claim => (
        <li key={claim.id}>{claim.description}</li>
      ))}
    </ul>
  );
};

// Example usage of the ClaimProvider and ClaimList components
const App = () => {
  return (
    <ClaimProvider>
      <h1>Claim Portal</h1>
      <ClaimList />
    </ClaimProvider>
  );
};

export default App;
```
