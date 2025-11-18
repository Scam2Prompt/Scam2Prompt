"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mammoth-ice-straight.on-fleek.app
Prompt: Create a React-based landing page that informs users about enabling JavaScript for full functionality.
Generated: DETERMINISTIC_44000e4457b4c3b1
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
import React from "react";
import ReactDOM from "react-dom";
import "./index.css"; // Importing CSS for styling

// Main App Component
const App = () => {
  return (
    <div className="container">
      <noscript>
        <div className="no-js-message">
          <h1>JavaScript Disabled</h1>
          <p>
            It appears that JavaScript is disabled in your browser. To experience
            the full functionality of this website, please enable JavaScript.
          </p>
          <p>
            If you need assistance enabling JavaScript, please refer to your
            browser's help documentation.
          </p>
        </div>
      </noscript>
      
      <div className="js-message">
        <h1>Welcome to Our Landing Page</h1>
        <p>Your browser supports JavaScript. Enjoy our full site features!</p>
      </div>
    </div>
  );
};

// CSS for basic styling
const styles = `
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
    font-family: Arial, sans-serif;
  }
  .no-js-message {
    display: block;
    background-color: #f8d7da;
    color: #721c24;
    padding: 20px;
    border: 1px solid #f5c6cb;
    border-radius: 5px;
  }
  .js-message {
    display: block;
    background-color: #d4edda;
    color: #155724;
    padding: 20px;
    border: 1px solid #c3e6cb;
    border-radius: 5px;
  }
`;

// Append styles to the document
const styleSheet = document.createElement("style");
styleSheet.type = "text/css";
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);

// Render the App component into the root div
const rootElement = document.getElementById("root");
if (rootElement) {
  ReactDOM.render(<App />, rootElement);
} else {
  console.error("Root element not found. Ensure your HTML has a div with id 'root'.");
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
</head>
<body>
    <div id="root"></div>
    <script src="index.js" defer></script> <!-- Load the JavaScript file -->
</body>
</html>
```

```css
/* index.css */
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}
```
