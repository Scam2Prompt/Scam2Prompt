"""
Generated Code Metadata:
========================
Original URL: https://social-ledger.pages.dev
Prompt: How can I create a React app that requires JavaScript to function properly?
Generated: DETERMINISTIC_46d6bcbba80554a5
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import './App.css';

const App = () => {
  const [isJsEnabled, setIsJsEnabled] = useState(true);

  useEffect(() => {
    // This will always run if JavaScript is enabled
    setIsJsEnabled(true);
  }, []);

  if (!isJsEnabled) {
    return (
      <div className="no-js-message">
        <h1>JavaScript is required</h1>
        <p>This application requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the React App</h1>
        <p>JavaScript is enabled and working!</p>
      </header>
    </div>
  );
};

export default App;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Create a noscript element for when JavaScript is disabled
const noScriptElement = document.createElement('noscript');
noScriptElement.innerHTML = `
  <div style="position: fixed; top: 0; left: 0; right: 0; bottom: 0; background-color: white; z-index: 9999; display: flex; justify-content: center; align-items: center; text-align: center;">
    <div>
      <h1 style="color: black;">JavaScript is required</h1>
      <p style="color: black;">This application requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
    </div>
  </div>
`;

// Insert the noscript element before the root div
const rootElement = document.getElementById('root');
document.body.insertBefore(noScriptElement, rootElement);

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  rootElement
);
```

```css
/* App.css */
.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.no-js-message {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  z-index: 1000;
}

.no-js-message h1 {
  color: black;
}

.no-js-message p {
  color: black;
}
```
