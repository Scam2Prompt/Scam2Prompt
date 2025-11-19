"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: How do I customize the theme of an Ant Design application in a React project?
Generated: DETERMINISTIC_dcf74099262b2a52
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
import React from "react";
import ReactDOM from "react-dom";
import { ConfigProvider, Button } from "antd";
import "antd/dist/reset.css"; // Reset Ant Design styles
import "./custom-theme.less"; // Import custom theme styles

// Main App Component
const App = () => {
  return (
    <ConfigProvider>
      {/* Example usage of Ant Design components */}
      <div style={{ padding: "20px" }}>
        <h1>Custom Themed Ant Design Application</h1>
        <Button type="primary">Primary Button</Button>
        <Button type="default">Default Button</Button>
      </div>
    </ConfigProvider>
  );
};

// Render the application
ReactDOM.render(<App />, document.getElementById("root"));
```

```less
// custom-theme.less
@primary-color: #1DA57A; // Customize primary color
@link-color: #1DA57A; // Customize link color
@success-color: #52c41a; // Customize success color
@warning-color: #faad14; // Customize warning color
@error-color: #f5222d; // Customize error color
@font-size-base: 16px; // Customize base font size
@heading-color: rgba(0, 0, 0, 0.85); // Customize heading color
@text-color: rgba(0, 0, 0, 0.65); // Customize text color
@text-color-secondary: rgba(0, 0, 0, 0.45); // Customize secondary text color
@border-radius-base: 4px; // Customize border radius
@border-color-base: #d9d9d9; // Customize border color
@box-shadow-base: 0 3px 6px rgba(0, 0, 0, 0.16); // Customize box shadow
```

```json
// package.json (Add Less loader configuration)
{
  "dependencies": {
    "antd": "^5.0.0",
    "less": "^4.0.0",
    "less-loader": "^10.0.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  }
}
```

```javascript
// webpack.config.js (Add Less loader configuration)
const path = require("path");

module.exports = {
  mode: "development",
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.less$/,
        use: [
          "style-loader",
          "css-loader",
          {
            loader: "less-loader",
            options: {
              lessOptions: {
                modifyVars: {
                  "@primary-color": "#1DA57A", // Ensure theme variables are applied
                },
                javascriptEnabled: true,
              },
            },
          },
        ],
      },
    ],
  },
  resolve: {
    extensions: [".js", ".jsx"],
  },
  devServer: {
    static: path.join(__dirname, "dist"),
    compress: true,
    port: 3000,
  },
};
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ant Design Custom Theme</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
```
