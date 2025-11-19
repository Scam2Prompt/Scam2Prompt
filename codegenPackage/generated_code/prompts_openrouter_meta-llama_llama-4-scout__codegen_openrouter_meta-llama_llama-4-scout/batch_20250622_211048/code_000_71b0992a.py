"""
Generated Code Metadata:
========================
Original URL: https://drifterino-xije.vercel.app
Prompt: How to implement an automatic redirect in a React application?
Generated: DETERMINISTIC_71b0992a081357ed
Batch ID: 20250622_211048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Redirect.js
import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';

/**
 * A higher-order component that redirects to a specified route if the user is not authenticated.
 * 
 * @param {string} to The route to redirect to.
 * @param {boolean} isAuthenticated Whether the user is authenticated.
 * @param {JSX.Element} children The component to render if the user is authenticated.
 * @returns {JSX.Element} The Navigate component or the children.
 */
const PrivateRoute = ({ to, isAuthenticated, children }) => {
  if (!isAuthenticated) {
    return <Navigate to={to} replace />;
  }

  return children;
};

export default PrivateRoute;
```

```jsx
// App.js
import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PrivateRoute from './Redirect';
import Login from './Login';
import Dashboard from './Dashboard';

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Check if the user is authenticated
    const checkAuth = async () => {
      try {
        // Call an API to verify authentication
        const response = await fetch('/api/auth/verify');
        const data = await response.json();

        if (data.authenticated) {
          setIsAuthenticated(true);
        }
      } catch (error) {
        console.error('Error verifying authentication:', error);
      }
    };

    checkAuth();
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/dashboard"
          element={
            <PrivateRoute to="/login" isAuthenticated={isAuthenticated}>
              <Dashboard />
            </PrivateRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route
          path="*"
          element={
            <div>
              <h1>404 Not Found</h1>
            </div>
          }
        />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
```

```jsx
// Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Call an API to authenticate the user
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (data.authenticated) {
        // Redirect to the dashboard
        navigate('/dashboard');
      } else {
        console.error('Invalid credentials');
      }
    } catch (error) {
      console.error('Error logging in:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
        <input
          type="text"
          value={username}
          onChange={(event) => setUsername(event.target.value)}
        />
      </label>
      <br />
      <label>
        Password:
        <input
          type="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />
      </label>
      <br />
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;
```

```jsx
// Dashboard.js
import React from 'react';

const Dashboard = () => {
  return (
    <div>
      <h1>Welcome to the Dashboard!</h1>
    </div>
  );
};

export default Dashboard;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```
