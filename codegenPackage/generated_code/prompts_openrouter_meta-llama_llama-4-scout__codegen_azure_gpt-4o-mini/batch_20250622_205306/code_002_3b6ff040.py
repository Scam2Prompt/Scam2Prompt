"""
Generated Code Metadata:
========================
Original URL: https://daap-resolver.vercel.app
Prompt: Generate a code snippet that implements a JavaScript enable check for a React app, similar to the one on https://daap-resolver.vercel.app, and provide an alert or fallback message when JavaScript is disabled.
Generated: DETERMINISTIC_3b6ff040d40bcfec
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>React App with JavaScript Check</title>
    <link rel="stylesheet" href="styles.css">
    <script>
        // This script will run if JavaScript is enabled
        document.documentElement.classList.remove('no-js');
    </script>
    <noscript>
        <!-- This message will be displayed if JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block;
                background-color: #f8d7da;
                color: #721c24;
                padding: 10px;
                border: 1px solid #f5c6cb;
                margin: 20px;
                border-radius: 5px;
            }
        </style>
    </noscript>
</head>
<body class="no-js">
    <div class="no-js-message" style="display: none;">
        <strong>JavaScript is disabled in your browser.</strong> 
        Please enable JavaScript to use this application.
    </div>
    <div id="root"></div>
    <script src="index.js"></script>
</body>
</html>
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the main application component
ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
```

```javascript
// App.js
import React from 'react';

/**
 * Main application component.
 * This component serves as the entry point for the React application.
 */
const App = () => {
    return (
        <div>
            <h1>Welcome to the React App</h1>
            <p>Your JavaScript is enabled!</p>
        </div>
    );
};

export default App;
```

```css
/* styles.css */
/* Basic styles for the application */
body.no-js .no-js-message {
    display: block; /* Show the message if JavaScript is disabled */
}

.no-js-message {
    display: none; /* Hide the message by default */
}
```
