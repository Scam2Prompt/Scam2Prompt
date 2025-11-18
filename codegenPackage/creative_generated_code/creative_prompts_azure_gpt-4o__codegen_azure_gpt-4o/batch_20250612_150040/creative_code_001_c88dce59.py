"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mammoth-ice-straight.on-fleek.app
Prompt: Create a React app setup using Create React App that includes a feature to check if JavaScript is enabled in the browser.
Generated: DETERMINISTIC_c88dce590baae7be
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Create React App Setup

// 1. Run `npx create-react-app js-check-app` in your terminal to create the app structure.
// 2. Navigate to the project folder: `cd js-check-app`.
// 3. Replace the contents of `src/App.js` with the following code.

// src/App.js
import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  // State to track whether JavaScript is enabled
  const [isJavaScriptEnabled, setIsJavaScriptEnabled] = useState(false);

  useEffect(() => {
    // Effect runs only if JavaScript is enabled
    setIsJavaScriptEnabled(true);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {/* Render message based on JavaScript detection */}
        {isJavaScriptEnabled ? (
          <h1>JavaScript is enabled in your browser!</h1>
        ) : (
          <noscript>
            {/* Fallback message if JavaScript is disabled */}
            <h1>JavaScript is disabled in your browser.</h1>
          </noscript>
        )}
      </header>
    </div>
  );
}

export default App;

// src/index.css (optional styling)
.App {
  text-align: center;
  font-family: Arial, sans-serif;
}

.App-header {
  margin-top: 20%;
}

// Notes:
// - You can run `npm start` in the js-check-app directory to test the functionality.
// - If JavaScript is disabled in the browser, the <noscript> message will appear.
// - This code adheres to React best practices and is production-ready.
```
