"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for customizing Ant Design's theme and styles in a React project?
Generated: DETERMINISTIC_07ed09e0e164b757
Batch ID: 20250622_211429
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
import './custom-theme.less'; // Import custom theme styles

// Error boundary for handling unexpected errors
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Error caught in ErrorBoundary:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}

// Main App component
const App = () => {
  return (
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: '#1DA57A', // Customize primary color
          borderRadius: '4px', // Customize border radius
        },
      }}
    >
      <div style={{ padding: '20px' }}>
        <h1>Customized Ant Design Theme</h1>
        <Button type="primary">Primary Button</Button>
        <Button type="default">Default Button</Button>
      </div>
    </ConfigProvider>
  );
};

// Render the application
ReactDOM.render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>,
  document.getElementById('root')
);
```

```less
// custom-theme.less
@import '~antd/dist/antd.less'; // Import Ant Design's default styles

// Override Ant Design variables
@primary-color: #1DA57A; // Customize primary color
@border-radius-base: 4px; // Customize border radius

// Add custom styles
body {
  font-family: 'Arial, sans-serif';
}
```

```json
// package.json dependencies (ensure these are installed)
{
  "dependencies": {
    "antd": "^5.0.0", // Ensure you have the latest version of Ant Design
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "less": "^4.0.0",
    "less-loader": "^10.0.0"
  }
}
```

```javascript
// webpack.config.js (if using Webpack for bundling)
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
      },
    ],
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'), // Optional alias for cleaner imports
    },
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
  <title>Ant Design Custom Theme</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
```
