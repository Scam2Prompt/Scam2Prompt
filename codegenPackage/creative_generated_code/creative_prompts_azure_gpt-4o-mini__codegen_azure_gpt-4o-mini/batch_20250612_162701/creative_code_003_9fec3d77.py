"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: What are the best practices for ensuring a React app runs smoothly with JavaScript enabled?
Generated: DETERMINISTIC_9fec3d7745761665
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

/**
 * Function to check if JavaScript is enabled
 * @returns {boolean} - Returns true if JavaScript is enabled, false otherwise
 */
function isJavaScriptEnabled() {
  return true; // If this code runs, JavaScript is enabled
}

/**
 * Function to initialize the application
 */
function initializeApp() {
  // Check if JavaScript is enabled
  if (!isJavaScriptEnabled()) {
    console.error("JavaScript is not enabled. Please enable JavaScript to use this application.");
    return;
  }

  // Render the main App component into the DOM
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    document.getElementById('root')
  );
}

// Execute the initialization function
initializeApp();

// Service Worker registration for production builds
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js')
      .then(registration => {
        console.log('Service Worker registered with scope:', registration.scope);
      })
      .catch(error => {
        console.error('Service Worker registration failed:', error);
      });
  });
}
```
