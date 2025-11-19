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

```javascript
// App.js
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <noscript>
        <div className="noscript-message">
          You need to enable JavaScript to run this app.
        </div>
      </noscript>
      <div id="root"></div>
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

.noscript-message {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5rem;
  z-index: 1000;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web application"
    />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
```
