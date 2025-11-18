"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-portal-interface-react.pages.dev
Prompt: Create a React app structure for a claim portal interface, including routing and state management features.
Generated: DETERMINISTIC_a14dac9f1123124b
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import { ClaimProvider } from './context/ClaimContext';
import './index.css';

// Wrap the app with routing and context providers
ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <ClaimProvider>
        <App />
      </ClaimProvider>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
```

```javascript
// File: src/App.js
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ClaimDetailsPage from './pages/ClaimDetailsPage';
import NotFoundPage from './pages/NotFoundPage';
import Navbar from './components/Navbar';

const App = () => {
  return (
    <div>
      {/* Navigation Bar */}
      <Navbar />
      {/* Define Routes */}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/claim/:claimId" element={<ClaimDetailsPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </div>
  );
};

export default App;
```

```javascript
// File: src/context/ClaimContext.js
import React, { createContext, useReducer, useContext } from 'react';

// Define initial state
const initialState = {
  claims: [],
};

// Define actions
const CLAIM_ACTIONS = {
  SET_CLAIMS: 'SET_CLAIMS',
  ADD_CLAIM: 'ADD_CLAIM',
};

// Create reducer function
const claimReducer = (state, action) => {
  switch (action.type) {
    case CLAIM_ACTIONS.SET_CLAIMS:
      return { ...state, claims: action.payload };
    case CLAIM_ACTIONS.ADD_CLAIM:
      return { ...state, claims: [...state.claims, action.payload] };
    default:
      throw new Error(`Unhandled action type: ${action.type}`);
  }
};

// Create context
const ClaimContext = createContext();

// Create provider component
export const ClaimProvider = ({ children }) => {
  const [state, dispatch] = useReducer(claimReducer, initialState);

  return (
    <ClaimContext.Provider value={{ state, dispatch }}>
      {children}
    </ClaimContext.Provider>
  );
};

// Custom hook for accessing the claim context
export const useClaimContext = () => {
  const context = useContext(ClaimContext);
  if (!context) {
    throw new Error('useClaimContext must be used within a ClaimProvider');
  }
  return context;
};
```

```javascript
// File: src/components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/claim/sample-id">Sample Claim</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
```

```javascript
// File: src/pages/HomePage.js
import React from 'react';
import { useClaimContext } from '../context/ClaimContext';

const HomePage = () => {
  const { state } = useClaimContext();

  return (
    <div>
      <h1>Claim Portal</h1>
      <ul>
        {state.claims.length > 0 ? (
          state.claims.map((claim) => (
            <li key={claim.id}>
              {claim.title} - {claim.status}
            </li>
          ))
        ) : (
          <li>No claims available.</li>
        )}
      </ul>
    </div>
  );
};

export default HomePage;
```

```javascript
// File: src/pages/ClaimDetailsPage.js
import React from 'react';
import { useParams } from 'react-router-dom';

const ClaimDetailsPage = () => {
  const { claimId } = useParams();

  return (
    <div>
      <h1>Claim Details</h1>
      <p>Details for claim ID: {claimId}</p>
    </div>
  );
};

export default ClaimDetailsPage;
```

```javascript
// File: src/pages/NotFoundPage.js
import React from 'react';

const NotFoundPage = () => {
  return (
    <div>
      <h1>404 Not Found</h1>
      <p>The page you are looking for does not exist.</p>
    </div>
  );
};

export default NotFoundPage;
```

```css
/* File: src/index.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 10px;
}

nav ul li a {
  text-decoration: none;
  color: blue;
}

nav ul li a:hover {
  text-decoration: underline;
}
```
