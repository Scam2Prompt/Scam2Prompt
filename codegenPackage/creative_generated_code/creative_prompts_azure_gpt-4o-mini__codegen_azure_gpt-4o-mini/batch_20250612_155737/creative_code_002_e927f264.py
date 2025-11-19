"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter-5g4.pages.dev
Prompt: Can you provide a code snippet for a simple React app that checks if JavaScript is enabled?
Generated: DETERMINISTIC_e927f2647d60d998
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from React
import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';

// Main App component
const App = () => {
  // State to track if JavaScript is enabled
  const [isJsEnabled, setIsJsEnabled] = useState(false);

  // Effect to check if JavaScript is enabled
  useEffect(() => {
    // Set isJsEnabled to true when the component mounts
    setIsJsEnabled(true);
  }, []);

  return (
    <div>
      {!isJsEnabled ? (
        // Message displayed when JavaScript is disabled
        <noscript>
          <div style={{ color: 'red', fontWeight: 'bold' }}>
            JavaScript is disabled in your browser. Please enable it for the best experience.
          </div>
        </noscript>
      ) : (
        // Message displayed when JavaScript is enabled
        <div>
          <h1>JavaScript is enabled!</h1>
          <p>Welcome to the JavaScript-enabled version of the app.</p>
        </div>
      )}
    </div>
  );
};

// Render the App component to the DOM
ReactDOM.render(<App />, document.getElementById('root'));

// Note: Ensure to have a <div id="root"></div> in your HTML file to mount this React app
```

Make sure to include React and ReactDOM in your project by installing them via npm:

```bash
npm install react react-dom
```

Also, ensure your index.html has a `<div id="root"></div>` for mounting the React application.
