"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for theming in Ant Design when building a React application?
Generated: DETERMINISTIC_cf837e7469f0cf01
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
import 'antd/dist/reset.css'; // Use the reset.css for consistent styling across browsers
import './index.css'; // Custom global styles

// Ant Design provides a way to customize themes using less variables.
// However, for runtime theming, we can use ConfigProvider and CSS variables.

// Define a custom theme object
const customTheme = {
  token: {
    colorPrimary: '#1890ff', // Primary color
    colorSuccess: '#52c41a', // Success color
    colorWarning: '#faad14', // Warning color
    colorError: '#f5222d', // Error color
    borderRadius: 4, // Border radius for components
    fontSize: 14, // Base font size
  },
};

// App component
const App = () => {
  return (
    // Wrap the application with ConfigProvider to apply the theme
    <ConfigProvider theme={customTheme}>
      <div style={{ padding: '20px' }}>
        <h1 style={{ color: 'var(--ant-primary-color)' }}>Welcome to Themed Ant Design</h1>
        <Button type="primary">Primary Button</Button>
        <Button type="default" style={{ marginLeft: '10px' }}>
          Default Button
        </Button>
        <Button type="dashed" style={{ marginLeft: '10px' }}>
          Dashed Button
        </Button>
      </div>
    </ConfigProvider>
  );
};

// Error handling for rendering the application
try {
  ReactDOM.render(<App />, document.getElementById('root'));
} catch (error) {
  console.error('Error rendering the application:', error);
}
```

```css
/* index.css */
/* Custom global styles */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background-color: #f0f2f5; /* Light background color */
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}
```

**Note:** This code demonstrates runtime theming using `ConfigProvider` in Ant Design. For advanced theming, you can use Less variables during the build process or CSS-in-JS solutions.
