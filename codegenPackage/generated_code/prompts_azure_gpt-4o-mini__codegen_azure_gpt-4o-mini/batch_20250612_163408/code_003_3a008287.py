"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for customizing themes in Ant Design for a React project?
Generated: DETERMINISTIC_3a0082871777cddb
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React from 'react';
import { ConfigProvider } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Define a custom theme configuration
const customTheme = {
  // Customize primary color
  primaryColor: '#1DA57A',
  // Customize link color
  linkColor: '#1DA57A',
  // Customize success color
  successColor: '#52c41a',
  // Customize warning color
  warningColor: '#faad14',
  // Customize error color
  errorColor: '#f5222d',
  // Customize font size
  fontSizeBase: '14px',
  // Customize border radius
  borderRadiusBase: '4px',
};

// Main App component
const App = () => {
  return (
    // Wrap the application with ConfigProvider to apply custom theme
    <ConfigProvider theme={customTheme}>
      <div style={{ padding: '20px' }}>
        <h1>Custom Ant Design Theme Example</h1>
        {/* Example Ant Design Button */}
        <button type="button" style={{ backgroundColor: customTheme.primaryColor, color: '#fff', border: 'none', padding: '10px 20px', borderRadius: customTheme.borderRadiusBase }}>
          Custom Themed Button
        </button>
      </div>
    </ConfigProvider>
  );
};

// Error boundary component for error handling
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render shows the fallback UI
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log the error to an error reporting service
    console.error("Error caught in ErrorBoundary: ", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Fallback UI in case of error
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children; 
  }
}

// Render the App component wrapped in ErrorBoundary
const Root = () => (
  <ErrorBoundary>
    <App />
  </ErrorBoundary>
);

export default Root;
```
