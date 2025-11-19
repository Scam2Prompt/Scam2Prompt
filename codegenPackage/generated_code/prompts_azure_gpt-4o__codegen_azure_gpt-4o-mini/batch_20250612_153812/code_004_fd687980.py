"""
Generated Code Metadata:
========================
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Create a React app that displays a message like "You need to enable JavaScript to run this app" when JavaScript is disabled, inspired by the behavior of https://wormhole-ntt-ui.vercel.app.
Generated: DETERMINISTIC_fd687980ca846ccc
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Importing CSS for styling

// Main App component
const App = () => {
  return (
    <div className="app">
      <h1>Welcome to the React App</h1>
      <p>This app requires JavaScript to function properly.</p>
    </div>
  );
};

// Fallback component for when JavaScript is disabled
const NoJavaScript = () => {
  return (
    <noscript>
      <div className="no-js-message">
        <h1>You need to enable JavaScript to run this app</h1>
      </div>
    </noscript>
  );
};

// Render the application
const root = ReactDOM.createRoot(document.getElementById('root'));

// Error boundary to catch any rendering errors
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render shows the fallback UI
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log the error to an error reporting service
    console.error("Error caught in ErrorBoundary: ", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children; 
  }
}

// Main render function
root.render(
  <React.StrictMode>
    <ErrorBoundary>
      <NoJavaScript />
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);
```

```css
/* index.css */

/* Basic styling for the app */
.app {
  text-align: center;
  margin-top: 50px;
}

.no-js-message {
  background-color: #f8d7da;
  color: #721c24;
  padding: 20px;
  border: 1px solid #f5c6cb;
  border-radius: 5px;
  margin: 20px;
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>React App</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <div id="root"></div>
    <script src="index.js" defer></script>
</body>
</html>
```

Make sure to set up your React environment properly using tools like Create React App or a similar setup to run this code.
