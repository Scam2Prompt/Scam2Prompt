"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: How do I customize the theme of an Ant Design application in a React project?
Generated: DETERMINISTIC_dcf74099262b2a52
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This is a complete React application showcasing how to customize the theme of an Ant Design application.
// Ant Design supports customization using LESS variables.
// The following code demonstrates how to integrate Ant Design with a custom theme.

// Import necessary libraries
import React from "react";
import ReactDOM from "react-dom/client";
import { ConfigProvider, Button } from "antd";

// Import Ant Design styles with custom theme overrides
import "./custom-theme.less"; // Ensure you create this file with the appropriate theme customizations.

// Custom LESS file (`custom-theme.less`):
// =====================================================
// @primary-color: #1DA57A; // Change primary color
// @link-color: #1890ff;   // Change link color
// @success-color: #52c41a; // Change success state color
// @warning-color: #faad14; // Change warning state color
// @error-color: #f5222d;   // Change error state color
// @font-size-base: 14px;   // Change base font size
// @heading-color: rgba(0, 0, 0, 0.85); // Heading color
// @text-color: rgba(0, 0, 0, 0.65);   // Main text color
// @text-color-secondary: rgba(0, 0, 0, 0.45); // Secondary text color
// @border-radius-base: 4px;  // Border radius
// @box-shadow-base: 0 3px 6px rgba(0, 0, 0, 0.16); // Base box shadow
// =====================================================

// Main App Component
const App = () => {
  return (
    <ConfigProvider>
      {/* Sample UI to test the custom theme */}
      <div style={{ padding: 24 }}>
        <h1>Welcome to the Customized Ant Design Theme</h1>
        <Button type="primary">Primary Button</Button>
        <Button type="default" style={{ margin: "0 8px" }}>
          Default Button
        </Button>
        <Button type="dashed">Dashed Button</Button>
      </div>
    </ConfigProvider>
  );
};

// Render the application
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

// ---------------------------------------------------
// To set up this project:
// 1. Install Ant Design: `npm install antd`
// 2. Install LESS and related loaders: `npm install less less-loader`
// 3. Configure Webpack (or Vite) to support LESS files.
// 4. Create the `custom-theme.less` file in the src folder.
// 5. Import `custom-theme.less` in your main application file.
// ---------------------------------------------------

// Note: Ensure your build tools are properly configured to handle LESS file processing. 
// For example, in a Webpack setup, you may need to adjust `less-loader` options to enable theme customizations.
```
