"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to customize the theme of Ant Design using the ConfigProvider component.
Generated: DETERMINISTIC_60874d4fdd857d79
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
import React from 'react';
import ReactDOM from 'react-dom';
import { ConfigProvider, Button } from 'antd';

// Import Ant Design CSS
import 'antd/dist/reset.css';

// Define the custom theme for Ant Design
const customTheme = {
  token: {
    colorPrimary: '#00b96b', // Set primary color to green
    borderRadius: '8px', // Customize border radius
    colorLink: '#1890ff', // Customize link color
    colorTextBase: '#333333', // Base text color
  },
};

// Main App Component
const App = () => {
  return (
    // Wrapping the App with ConfigProvider to apply the custom theme
    <ConfigProvider theme={customTheme}>
      <div style={{ padding: '20px' }}>
        <h1 style={{ color: customTheme.token.colorPrimary }}>
          Welcome to Ant Design Custom Theme
        </h1>
        <Button type="primary">Primary Button</Button>
        <Button type="link">Link Button</Button>
      </div>
    </ConfigProvider>
  );
};

// Render the app to the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

**Note**: Ensure you have installed the necessary dependencies (`antd` and `react-dom`) in your project. You can install them using `npm install antd react-dom` or `yarn add antd react-dom`.
