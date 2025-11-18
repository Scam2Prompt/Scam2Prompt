"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mammoth-ice-straight.on-fleek.app
Prompt: Provide code to integrate a third-party library in a React app that checks for JavaScript support and displays a custom message.
Generated: DETERMINISTIC_a7505fce6795c55c
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';

// Third-party library for feature detection
import Modernizr from 'modernizr';

// Custom hook to check for JavaScript support
const useJavaScriptSupport = () => {
    const [isJavaScriptSupported, setIsJavaScriptSupported] = useState(true);

    useEffect(() => {
        // Check if JavaScript is supported using Modernizr
        if (!Modernizr.canvas) {
            setIsJavaScriptSupported(false);
        }
    }, []);

    return isJavaScriptSupported;
};

// Main App component
const App = () => {
    const isJavaScriptSupported = useJavaScriptSupport();

    return (
        <div>
            {isJavaScriptSupported ? (
                <h1>Welcome to the React App!</h1>
            ) : (
                <h1>JavaScript is not supported in your browser. Please enable it to enjoy the full experience.</h1>
            )}
        </div>
    );
};

// Render the App component
const rootElement = document.getElementById('root');
if (rootElement) {
    ReactDOM.render(<App />, rootElement);
} else {
    console.error('Root element not found. Please check your HTML file.');
}
```

### Additional notes:
- Ensure that you have `modernizr` installed in your project. You can add it via npm:
  ```bash
  npm install modernizr
  ```
- The code checks for the support of the `<canvas>` element as a proxy for general JavaScript support using Modernizr. You can customize this check based on your specific needs.
- Make sure to include a div with the ID `root` in your HTML file for the React app to mount correctly.
