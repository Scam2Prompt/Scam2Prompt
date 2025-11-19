"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for customizing themes in Ant Design for a React project?
Generated: DETERMINISTIC_3a0082871777cddb
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: themeConfig.js

/**
 * This file contains the theme customization for an Ant Design-based React project.
 * It uses Less for overriding default Ant Design variables.
 * Ensure that `react-app-rewired` and `less-loader` are installed and configured.
 */

// Import required modules
const { override, addLessLoader } = require('customize-cra');

// Export the overridden configuration
module.exports = override(
  // Configure Less loader to customize Ant Design themes
  addLessLoader({
    lessOptions: {
      javascriptEnabled: true, // Enable JS in Less
      modifyVars: {
        // Custom themes: Override Ant Design variables here
        '@primary-color': '#1890ff', // Primary color
        '@link-color': '#1DA57A', // Link color
        '@success-color': '#52c41a', // Success state color
        '@warning-color': '#faad14', // Warning state color
        '@error-color': '#f5222d', // Error state color
        '@font-size-base': '14px', // Base font size
        '@heading-color': 'rgba(0, 0, 0, 0.85)', // Heading color
        '@text-color': 'rgba(0, 0, 0, 0.65)', // Text color
        '@text-color-secondary': 'rgba(0, 0, 0, 0.45)', // Secondary text color
        '@border-radius-base': '4px', // Default border radius
      },
    },
  })
);

// File: App.less

/**
 * This file contains custom styling using Less.
 * It can directly define global styles or override component-specific styles.
 */

@import '~antd/dist/antd.less'; // Import Ant Design's default styles

// Example: Custom global styles
body {
  font-family: 'Arial, sans-serif';
  background-color: #f0f2f5;
}

// Example: Override Ant Design component styles
.ant-btn {
  border-radius: @border-radius-base;
  transition: all 0.3s ease-in-out;
}

.ant-btn-primary {
  background-color: @primary-color;
  border-color: @primary-color;

  &:hover {
    background-color: lighten(@primary-color, 10%);
    border-color: lighten(@primary-color, 10%);
  }
}

// File: index.js

/**
 * Entry file for the React application.
 * Ensure that the `themeConfig.js` is properly configured before running the application.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.less'; // Import customized Ant Design styles
import './App.less'; // Import additional custom styles
import App from './App';

// Render the main App component
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// File: App.js

/**
 * Main App component for the React application.
 * Demonstrates usage of Ant Design components with customized styling.
 */

import React from 'react';
import { Button, Alert } from 'antd';

const App = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Example: Custom-styled Ant Design button */}
      <Button type="primary">Click Me!</Button>

      {/* Example: Ant Design alert component */}
      <Alert
        message="Success!"
        description="This is a success alert with customized theme."
        type="success"
        showIcon
        style={{ marginTop: '20px' }}
      />
    </div>
  );
};

export default App;
```
