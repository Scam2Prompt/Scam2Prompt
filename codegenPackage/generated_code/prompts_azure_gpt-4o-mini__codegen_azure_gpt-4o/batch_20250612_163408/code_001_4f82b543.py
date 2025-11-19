"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: How can I customize Ant Design's theme for a React application? Provide code examples.
Generated: DETERMINISTIC_4f82b5434ea283fb
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules
import React from 'react';
import ReactDOM from 'react-dom';
import { ConfigProvider, Button } from 'antd';
import 'antd/dist/reset.css'; // Import Ant Design's reset styles

// Import Less for theme customization
import './custom-theme.less'; // Custom theme file

// Main App Component
const App = () => {
  return (
    <ConfigProvider>
      <div style={{ padding: '20px' }}>
        <h1>Customized Ant Design Theme</h1>
        <Button type="primary">Primary Button</Button>
        <Button type="default">Default Button</Button>
      </div>
    </ConfigProvider>
  );
};

// Render the App
ReactDOM.render(<App />, document.getElementById('root'));
```

```less
// custom-theme.less
@import '~antd/lib/style/themes/default.less'; // Import default Ant Design theme

// Override Ant Design variables to customize the theme
@primary-color: #1DA57A; // Change primary color
@link-color: #1DA57A; // Change link color
@border-radius-base: 8px; // Change border radius
@font-size-base: 16px; // Change base font size
@heading-color: #333333; // Change heading color
@text-color: #666666; // Change text color

// Additional custom styles (optional)
body {
  background-color: #f0f2f5; // Set a custom background color
}
```

```json
// package.json (Ensure Less loader is configured in your project)
{
  "dependencies": {
    "antd": "^5.x",
    "less": "^4.x",
    "less-loader": "^10.x",
    "react": "^18.x",
    "react-dom": "^18.x"
  }
}
```

```javascript
// webpack.config.js (Example configuration for Less loader)
const path = require('path');

module.exports = {
  module: {
    rules: [
      {
        test: /\.less$/,
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'less-loader',
            options: {
              lessOptions: {
                javascriptEnabled: true, // Enable JavaScript in Less
              },
            },
          },
        ],
        include: path.resolve(__dirname, 'src'),
      },
    ],
  },
};
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ant Design Theme Customization</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
```
