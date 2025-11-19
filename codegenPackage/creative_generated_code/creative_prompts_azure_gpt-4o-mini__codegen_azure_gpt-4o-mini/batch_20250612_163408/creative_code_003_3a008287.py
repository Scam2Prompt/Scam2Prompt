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
// src/theme.js

import { createTheme } from '@ant-design/cssinjs';

// Define a function to create a custom theme for Ant Design
export const getCustomTheme = (primaryColor = '#1890ff') => {
    return createTheme({
        token: {
            colorPrimary: primaryColor,
            // Add more custom tokens as needed
        },
        // Additional theme options can go here
    });
};
```

```javascript
// src/App.js

import React from 'react';
import { ConfigProvider } from 'antd';
import { getCustomTheme } from './theme';
import MyComponent from './MyComponent';

const App = () => {
    // Set the primary color for the theme
    const theme = getCustomTheme('#ff4d4f'); // Customize primary color here

    return (
        // Wrap your application in the ConfigProvider with the custom theme
        <ConfigProvider theme={theme}>
            <MyComponent />
        </ConfigProvider>
    );
};

export default App;
```

```javascript
// src/MyComponent.js

import React from 'react';
import { Button } from 'antd';

// Create a sample component to demonstrate the theme
const MyComponent = () => {
    return (
        <div style={{ padding: '20px' }}>
            <h1>Welcome to My Themed App</h1>
            <Button type="primary">Primary Button</Button>
        </div>
    );
};

export default MyComponent;
```

```javascript
// src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Entry point of the application
ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
```

```json
// package.json

{
  "name": "antd-theme-customization",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "antd": "^4.16.13",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "@ant-design/cssinjs": "^1.0.0" // Ensure to install necessary packages
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

```bash
# Installation command
npm install antd @ant-design/cssinjs react react-dom
```

```css
/* src/index.css - Add any global styles here */

body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
}
```
