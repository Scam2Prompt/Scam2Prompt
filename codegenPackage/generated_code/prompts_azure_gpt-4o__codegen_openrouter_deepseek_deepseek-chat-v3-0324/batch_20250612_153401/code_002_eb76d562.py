"""
Generated Code Metadata:
========================
Original URL: https://meta-drago.vercel.app
Prompt: Generate code for a React-based application that dynamically enables JavaScript functionality when hosted on Vercel.
Generated: DETERMINISTIC_eb76d56232c944af
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready React application with dynamic JavaScript functionality for Vercel:

```jsx
// src/App.js
import React, { useState, useEffect } from 'react';

/**
 * Main application component that dynamically enables JavaScript functionality
 * when hosted on Vercel environment.
 */
function App() {
  const [isVercel, setIsVercel] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const checkEnvironment = async () => {
      try {
        // Check if running on Vercel by looking for environment variables
        const isVercelEnv = process.env.NEXT_PUBLIC_VERCEL_ENV || 
                           process.env.REACT_APP_VERCEL_ENV || 
                           window.location.hostname.includes('vercel.app');
        
        setIsVercel(!!isVercelEnv);
      } catch (err) {
        setError('Failed to detect environment');
        console.error('Environment detection error:', err);
      } finally {
        setIsLoading(false);
      }
    };

    checkEnvironment();
  }, []);

  if (isLoading) {
    return <div className="loading">Loading application...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>React Vercel App</h1>
        <p>
          {isVercel 
            ? 'Running on Vercel with full JavaScript functionality enabled!'
            : 'Not running on Vercel - some features may be limited.'}
        </p>
      </header>

      <main className="app-content">
        {isVercel && (
          <div className="dynamic-content">
            <button 
              onClick={() => alert('Vercel-powered functionality!')}
              className="cta-button"
            >
              Click for Vercel Feature
            </button>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
```

```jsx
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```css
/* src/index.css */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.app {
  text-align: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background-color: #282c34;
  padding: 2rem;
  color: white;
}

.app-content {
  flex: 1;
  padding: 2rem;
}

.loading, .error {
  padding: 2rem;
  font-size: 1.2rem;
}

.error {
  color: #ff6b6b;
}

.cta-button {
  padding: 0.8rem 1.5rem;
  background: #0070f3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.2s ease;
}

.cta-button:hover {
  background: #0366d6;
}
```

```json
// package.json
{
  "name": "react-vercel-app",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

```js
// vercel.json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ],
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```
