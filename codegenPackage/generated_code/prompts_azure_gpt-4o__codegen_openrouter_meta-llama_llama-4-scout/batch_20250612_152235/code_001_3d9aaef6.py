"""
Generated Code Metadata:
========================
Original URL: https://housing-aj5.pages.dev
Prompt: Create a React application that displays a placeholder message like "You need to enable JavaScript to run this app" when JavaScript is disabled in the browser.
Generated: DETERMINISTIC_3d9aaef6372a6b60
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

```jsx
// App.js
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <noscript>
        <div>
          <h1>You need to enable JavaScript to run this app</h1>
        </div>
      </noscript>
      <div id="js-enabled-message">
        JavaScript is enabled. Your app will render here.
      </div>
    </div>
  );
}

export default App;
```

```css
/* App.css */
.App {
  text-align: center;
}

noscript div {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #f0f0f0;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

#js-enabled-message {
  display: none;
}
```

```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>React App</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
```
