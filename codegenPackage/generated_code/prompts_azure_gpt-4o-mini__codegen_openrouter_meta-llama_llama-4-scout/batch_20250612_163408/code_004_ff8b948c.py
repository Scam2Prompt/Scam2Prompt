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
// UserContext.js
import { createContext, useState, useEffect } from 'react';

/**
 * User context for state management.
 */
const UserContext = createContext();

/**
 * User context provider.
 * 
 * @param {Object} props - Component props.
 * @param {ReactNode} props.children - Child components.
 * @returns {JSX.Element} User context provider element.
 */
export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    const storedUser = localStorage.getItem('user');
    return storedUser ? JSON.parse(storedUser) : null;
  });

  useEffect(() => {
    localStorage.setItem('user', JSON.stringify(user));
  }, [user]);

  const login = (newUser) => {
    setUser(newUser);
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <UserContext.Provider value={{ user, login, logout }}>
      {children}
    </UserContext.Provider>
  );
};

export default UserContext;
```

```jsx
// App.js
import React from 'react';
import { UserProvider } from './UserContext';
import Navbar from './Navbar';
import Home from './Home';

/**
 * Main application component.
 * 
 * @returns {JSX.Element} Application element.
 */
function App() {
  return (
    <UserProvider>
      <Navbar />
      <Home />
    </UserProvider>
  );
}

export default App;
```

```jsx
// Navbar.js
import React, { useContext } from 'react';
import UserContext from './UserContext';

/**
 * Navigation bar component.
 * 
 * @returns {JSX.Element} Navigation bar element.
 */
function Navbar() {
  const { user, logout } = useContext(UserContext);

  return (
    <nav>
      {user ? (
        <div>
          <span>Welcome, {user.name}!</span>
          <button onClick={logout}>Logout</button>
        </div>
      ) : (
        <span>Please login</span>
      )}
    </nav>
  );
}

export default Navbar;
```

```jsx
// Home.js
import React, { useContext } from 'react';
import UserContext from './UserContext';

/**
 * Home page component.
 * 
 * @returns {JSX.Element} Home page element.
 */
function Home() {
  const { user, login } = useContext(UserContext);

  const handleLogin = () => {
    const newUser = { name: 'John Doe', email: 'john@example.com' };
    login(newUser);
  };

  return (
    <div>
      {user ? (
        <span>Welcome to the home page, {user.name}!</span>
      ) : (
        <button onClick={handleLogin}>Login</button>
      )}
    </div>
  );
}

export default Home;
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

/**
 * Renders the application to the DOM.
 */
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```
