"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mammoth-ice-straight.on-fleek.app
Prompt: Write code to dynamically render a React component only if JavaScript is enabled in the user's browser environment.
Generated: DETERMINISTIC_4c30c1d3269e9b7e
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

// Define a component to be rendered if JavaScript is enabled
const JavaScriptEnabledComponent = () => {
  return (
    <div>
      <h1>JavaScript is enabled!</h1>
      <p>This content is rendered dynamically using React.</p>
    </div>
  );
};

// Define a fallback static HTML for browsers without JavaScript
const NoJavaScriptFallback = () => {
  return (
    <noscript>
      <style>{`
        .no-js-message { 
          font-family: Arial, sans-serif; 
          color: red; 
          text-align: center; 
          margin: 20px; 
        }
      `}</style>
      <div className="no-js-message">
        <h1>JavaScript is not enabled</h1>
        <p>For full functionality, please enable JavaScript.</p>
      </div>
    </noscript>
  );
};

// Render the fallback message for non-JS environments
ReactDOM.render(
  <NoJavaScriptFallback />,
  document.getElementById('no-js-fallback')
);

// Render the main React component dynamically if JavaScript is enabled
ReactDOM.render(
  <JavaScriptEnabledComponent />,
  document.getElementById('js-enabled-root')
);

// HTML Structure (ensure this is part of your HTML file)
/*
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic React Rendering</title>
  </head>
  <body>
    <div id="no-js-fallback"></div>
    <div id="js-enabled-root"></div>
    <script src="path/to/your/bundle.js"></script>
  </body>
</html>
*/
```
