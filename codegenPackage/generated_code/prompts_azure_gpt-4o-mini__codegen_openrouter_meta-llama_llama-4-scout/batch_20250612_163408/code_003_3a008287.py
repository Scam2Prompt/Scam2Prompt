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

```jsx
// Import necessary dependencies
import React from 'react';
import { ConfigProvider } from 'antd';
import enUS from 'antd/lib/locale/en_US';

// Define a custom theme using CSS variables
const customTheme = {
  token: {
    colorPrimary: '#1890ff',
    colorInfo: '#1890ff',
    colorSuccess: '#52c41a',
    colorWarning: '#faad14',
    colorError: '#ff4d4f',
  },
};

// Define a function to customize Ant Design theme
function CustomizedThemeProvider({ children }) {
  return (
    <ConfigProvider
      theme={customTheme}
      locale={enUS} // Use a specific locale for internationalization
    >
      {children}
    </ConfigProvider>
  );
}

// Example usage
function App() {
  try {
    return (
      <CustomizedThemeProvider>
        <div>
          <h1>Customized Theme Example</h1>
          <button style={{ backgroundColor: 'var(--ant-color-primary)' }}>
            Primary Button
          </button>
        </div>
      </CustomizedThemeProvider>
    );
  } catch (error) {
    console.error('Error rendering customized theme:', error);
    return <div>Error: {error.message}</div>;
  }
}

// Export the App component
export default App;
```
