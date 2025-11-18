"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Create a JavaScript function to check if JavaScript is enabled in a browser before rendering a React application, inspired by the behavior of the app at https://wormhole-ntt-ui.vercel.app.
Generated: DETERMINISTIC_6e834ef7792ccb37
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Create a function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a <noscript> element to display a message if JavaScript is disabled
    const noscript = document.createElement('noscript');
    noscript.innerHTML = `<style>body { display: none; }</style>
                          <div style="color: red; text-align: center; margin-top: 20px;">
                          <h1>JavaScript is disabled in your browser</h1>
                          <p>Please enable JavaScript to view this application.</p>
                          </div>`;
    // Append the <noscript> element to the body
    document.body.appendChild(noscript);
}

// Immediately invoke the function to check JavaScript status
isJavaScriptEnabled();

// Import necessary React and ReactDOM modules
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // Your main App component

// Render the React application if JavaScript is enabled
ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);

// Note: Ensure that the <noscript> message will be displayed only if JavaScript is disabled.
// The application will render normally if JavaScript is functional.
```
