"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: How can I customize Ant Design's theme for a React application? Provide code examples.
Generated: DETERMINISTIC_4f82b5434ea283fb
Batch ID: 20250612_163408
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
import 'antd/dist/reset.css'; // Ensure the reset styles are imported

// Import Less to enable theme customization
// Note: You must install `less` and `less-loader` for this to work
// npm install less less-loader

// In your webpack or Vite configuration, configure `less-loader`
// Example for webpack:
// {
//   test: /\.less$/,
//   use: [
//     'style-loader',
//     'css-loader',
//     {
//       loader: 'less-loader',
//       options: {
//         lessOptions: {
//           modifyVars: {
//             '@primary-color': '#1DA57A', // Example: Change the primary color
//             '@link-color': '#1890ff', // Example: Change link color
//             '@font-size-base': '16px', // Example: Base font size
//           },
//           javascriptEnabled: true,
//         },
//       },
//     },
//   ],
// }

// Customized theme injected into Ant Design globally
const App = () => {
  return (
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: '#1DA57A', // Custom primary color
          colorLink: '#1890ff', // Custom link color
          borderRadius: '8px', // Custom border radius
        },
      }}
    >
      <div style={{ padding: '20px' }}>
        {/* Example usage of Ant Design components */}
        <h1>Hello, Ant Design!</h1>
        <Button type="primary">Primary Button</Button>
        <Button type="link">Link Button</Button>
      </div>
    </ConfigProvider>
  );
};

// Render the React app
ReactDOM.render(<App />, document.getElementById('root'));

// Instructions:
// - Ensure `less-loader` is correctly configured in your build tool.
// - Modify the Less variables as per your theme requirements.
// - Use `ConfigProvider` to globally apply your customized theme in the application.
```
