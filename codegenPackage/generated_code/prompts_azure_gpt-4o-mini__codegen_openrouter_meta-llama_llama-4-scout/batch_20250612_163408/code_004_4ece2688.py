"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Explain how to customize Ant Design themes in a React project for better branding.
Generated: DETERMINISTIC_4ece268867143874
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary dependencies
import React from 'react';
import ReactDOM from 'react-dom';
import { ConfigProvider } from 'antd';
import enUS from 'antd/lib/locale/en_US';
import App from './App';
import 'antd/dist/antd.css'; // Import Ant Design CSS

// Define a custom theme
const customTheme = {
  primaryColor: '#3f51b5', // Primary color
  infoColor: '#03A9F4', // Info color
  successColor: '#4CAF50', // Success color
  warningColor: '#FF9800', // Warning color
  errorColor: '#f44336', // Error color
};

// Create a custom theme config
const themeConfig = {
  token: {
    colorPrimary: customTheme.primaryColor,
    colorInfo: customTheme.infoColor,
    colorSuccess: customTheme.successColor,
    colorWarning: customTheme.warningColor,
    colorError: customTheme.errorColor,
  },
};

// Configure Ant Design with custom theme and locale
const config = {
  theme: themeConfig,
  locale: enUS,
};

// Main application component
function Main() {
  return (
    <ConfigProvider config={config}>
      <App />
    </ConfigProvider>
  );
}

// Render the application
ReactDOM.render(
  <React.StrictMode>
    <Main />
  </React.StrictMode>,
  document.getElementById('root')
);

// Handle rendering error
try {
  // Render the application
} catch (error) {
  console.error('Error rendering application:', error);
}
```

```css
/* ant-overrides.css */
:root {
  --primary-color: #3f51b5;
  --info-color: #03A9F4;
  --success-color: #4CAF50;
  --warning-color: #FF9800;
  --error-color: #f44336;
}
```

```javascript
// webpack.config.js
module.exports = {
  // Other configurations...
  lessLoaderOptions: {
    lessOptions: {
      modifyVars: {
        '@primary-color': '#3f51b5',
        '@info-color': '#03A9F4',
        '@success-color': '#4CAF50',
        '@warning-color': '#FF9800',
        '@error-color': '#f44336',
      },
    },
  },
};
```
