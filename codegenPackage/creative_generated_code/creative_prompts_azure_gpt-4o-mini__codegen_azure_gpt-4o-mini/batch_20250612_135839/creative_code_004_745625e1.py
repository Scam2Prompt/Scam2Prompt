"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://full-mint-website-master.pages.dev
Prompt: How do I configure my React app to ensure JavaScript is supported across all browsers?
Generated: DETERMINISTIC_745625e135a74611
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary packages
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Importing polyfills for compatibility
import 'core-js/stable'; // Polyfills for ES6 and above
import 'regenerator-runtime/runtime'; // Polyfill for async/await

// Check for JavaScript support
if (!window.Promise) {
  console.error('Your browser does not support ES6 features such as Promises.');
}

// Main entry point of the React application
const renderApp = () => {
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    document.getElementById('root')
  );
};

// Error handling during rendering
try {
  renderApp();
} catch (error) {
  console.error('An error occurred during the rendering of the app:', error);
}

// Optional: Service worker registration for offline support
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/service-worker.js')
      .then((registration) => {
        console.log('Service Worker registered with scope:', registration.scope);
      })
      .catch((error) => {
        console.error('Service Worker registration failed:', error);
      });
  });
}
```

```json
// package.json
{
  "name": "my-react-app",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "core-js": "^3.15.2",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "browserslist": [
    ">0.2%",
    "not dead",
    "not op_mini all"
  ]
}
```

```javascript
// service-worker.js
self.addEventListener('install', (event) => {
  console.log('Service Worker: Installed');
});

self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activated');
});

self.addEventListener('fetch', (event) => {
  console.log('Service Worker: Fetching', event.request.url);
});
```

Ensure to run `npm install` to install dependencies before running the app.
