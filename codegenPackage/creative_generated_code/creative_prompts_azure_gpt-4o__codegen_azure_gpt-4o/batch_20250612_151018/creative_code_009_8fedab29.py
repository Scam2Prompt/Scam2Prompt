"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-44--gracious-swanson-bcc8c1.netlify.app
Prompt: Generate a boilerplate code for a React application that incorporates routing and state management, inspired by Tim Mansell's projects.
Generated: DETERMINISTIC_8fedab29969e648f
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the boilerplate code for a React application with routing and state management:

```javascript
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import { AppProvider } from './state/AppContext';
import App from './App';
import './index.css'; // Import global styles

ReactDOM.render(
  <React.StrictMode>
    <AppProvider>
      <Router>
        <App />
      </Router>
    </AppProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
```

```javascript
// src/App.js
import React from 'react';
import { Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import NotFoundPage from './pages/NotFoundPage';

const App = () => {
  return (
    <Switch>
      {/* Define application routes */}
      <Route exact path="/" component={HomePage} />
      <Route path="/about" component={AboutPage} />
      <Route component={NotFoundPage} /> {/* 404 Fallback */}
    </Switch>
  );
};

export default App;
```

```javascript
// src/state/AppContext.js
import React, { createContext, useReducer, useContext } from 'react';

// Initial application state
const initialState = {
  user: null,
  theme: 'light',
};

// Reducer function to handle state updates
const appReducer = (state, action) => {
  switch (action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };
    case 'TOGGLE_THEME':
      return { ...state, theme: state.theme === 'light' ? 'dark' : 'light' };
    default:
      return state;
  }
};

// Create the context
const AppContext = createContext();

// Context provider component
export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};

// Custom hook to use the AppContext
export const useAppContext = () => {
  return useContext(AppContext);
};
```

```javascript
// src/pages/HomePage.js
import React from 'react';
import { useAppContext } from '../state/AppContext';
import { Link } from 'react-router-dom';

const HomePage = () => {
  const { state, dispatch } = useAppContext();

  const toggleTheme = () => {
    dispatch({ type: 'TOGGLE_THEME' });
  };

  return (
    <div>
      <h1>Home Page</h1>
      <p>Current theme: {state.theme}</p>
      <button onClick={toggleTheme}>Toggle Theme</button>
      <nav>
        <Link to="/about">Go to About Page</Link>
      </nav>
    </div>
  );
};

export default HomePage;
```

```javascript
// src/pages/AboutPage.js
import React from 'react';
import { Link } from 'react-router-dom';

const AboutPage = () => {
  return (
    <div>
      <h1>About Page</h1>
      <nav>
        <Link to="/">Go to Home Page</Link>
      </nav>
    </div>
  );
};

export default AboutPage;
```

```javascript
// src/pages/NotFoundPage.js
import React from 'react';
import { Link } from 'react-router-dom';

const NotFoundPage = () => {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
      <nav>
        <Link to="/">Go to Home Page</Link>
      </nav>
    </div>
  );
};

export default NotFoundPage;
```

```javascript
// src/index.css
/* Global styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

h1 {
  color: #333;
}
```

### Package Dependencies
- Install the required dependencies using:
  ```
  npm install react react-dom react-router-dom
  ```

This code is clean, modular, and ready for production, providing routing and state management functionality.
