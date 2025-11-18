"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Create a React app that displays a message like "You need to enable JavaScript to run this app" when JavaScript is disabled, inspired by the behavior of https://wormhole-ntt-ui.vercel.app.
Generated: DETERMINISTIC_fd687980ca846ccc
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React App</title>
  </head>
  <body>
    <!-- Fallback message for when JavaScript is disabled -->
    <noscript>
      <div style="text-align: center; margin-top: 20%; font-family: Arial, sans-serif">
        <h1>You need to enable JavaScript to run this app</h1>
      </div>
    </noscript>
    <!-- React app root -->
    <div id="root"></div>
    <!-- JavaScript bundle -->
    <script src="./index.js"></script>
  </body>
</html>
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the React app into the root div
ReactDOM.render(<App />, document.getElementById('root'));
```

```jsx
// App.js
import React from 'react';

function App() {
  return (
    <div style={{ textAlign: 'center', marginTop: '20%', fontFamily: 'Arial, sans-serif' }}>
      {/* Main React application */}
      <h1>Welcome to the React App!</h1>
    </div>
  );
}

export default App;
```

```jsx
// package.json
{
  "name": "react-noscript-message",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
``` 

```bash
# Command to set up the project
# Run these in the terminal

# Initialize a new React project
npx create-react-app react-noscript-message

# Navigate into the project directory
cd react-noscript-message

# Replace the contents of public/index.html and src files with the code provided above.

# Start the development server
npm start
```
