"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Create a React application using Ant Design's Menu and Layout components to build a sidebar navigation.
Generated: DETERMINISTIC_12a687d82adc2b3e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary dependencies
import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import 'antd/dist/antd.css';

// Define the application component
const App = () => {
  // Define menu items
  const menuItems = [
    {
      key: '1',
      label: 'Home',
      path: '/',
    },
    {
      key: '2',
      label: 'About',
      path: '/about',
    },
    {
      key: '3',
      label: 'Contact',
      path: '/contact',
    },
  ];

  // Initialize state for selected menu item
  const [selectedKeys, setSelectedKeys] = useState(['1']);

  // Handle menu item click
  const handleMenuItemClick = (info) => {
    setSelectedKeys([info.key]);
  };

  // Render the application
  return (
    <Layout style={{ height: '100vh' }}>
      <Layout.Sider>
        <Menu
          mode="inline"
          selectedKeys={selectedKeys}
          onClick={handleMenuItemClick}
          style={{ height: '100%', borderRight: 0 }}
        >
          {menuItems.map((item) => (
            <Menu.Item key={item.key}>
              <a href={item.path}>{item.label}</a>
            </Menu.Item>
          ))}
        </Menu>
      </Layout.Sider>
      <Layout.Content style={{ padding: '24px', minHeight: 280 }}>
        <h1>Content Area</h1>
      </Layout.Content>
    </Layout>
  );
};

// Export the application component
export default App;
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

```css
/* global.css */
body {
  margin: 0;
  padding: 0;
}
```

```json
// package.json
{
  "name": "react-sidebar-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "antd": "^4.24.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": ["react-app", "react-app/jest"]
  }
}
```
