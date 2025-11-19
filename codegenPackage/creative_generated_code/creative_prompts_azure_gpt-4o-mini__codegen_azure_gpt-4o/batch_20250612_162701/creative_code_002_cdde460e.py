"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Can you provide code examples for setting up a React app that displays a message when JavaScript is disabled?
Generated: DETERMINISTIC_cdde460e0af26efc
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules from React
import React from 'react';
import ReactDOM from 'react-dom';

// Root component of the application
function App() {
  return (
    <div>
      {/* This content will only appear if JavaScript is enabled */}
      <h1>Welcome to My React App</h1>
      <p>If you are seeing this, JavaScript is enabled!</p>
    </div>
  );
}

// Render the App component to the root div
ReactDOM.render(<App />, document.getElementById('root'));

/* 
  The following <noscript> tag is part of the HTML file, not JavaScript. 
  It ensures that users are shown a message if JavaScript is disabled. 
*/

// Example HTML file: index.html
/*
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>React App</title>
</head>
<body>
  <!-- This message is shown when JavaScript is disabled -->
  <noscript>
    <div style="color: red; font-weight: bold;">
      JavaScript is disabled in your browser. Please enable it to view the application.
    </div>
  </noscript>
  
  <!-- React app will be mounted here -->
  <div id="root"></div>
  
  <!-- Include the React app script -->
  <script src="./path/to/your/bundle.js"></script>
</body>
</html>
*/
```
