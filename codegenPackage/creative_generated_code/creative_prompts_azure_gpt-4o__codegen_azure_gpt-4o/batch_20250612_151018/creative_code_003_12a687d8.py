"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Create a React application using Ant Design's Menu and Layout components to build a sidebar navigation.
Generated: DETERMINISTIC_12a687d82adc2b3e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// File: src/App.js

// Import necessary libraries
import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import {
  UserOutlined,
  LaptopOutlined,
  NotificationOutlined,
} from '@ant-design/icons';
import './App.css';

// Destructure Ant Design Layout components
const { Header, Sider, Content } = Layout;

const App = () => {
  // State to handle collapsed state of the sidebar
  const [collapsed, setCollapsed] = useState(false);

  // Function to handle sidebar toggle
  const handleCollapse = (collapsedState) => {
    setCollapsed(collapsedState);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* Header section */}
      <Header className="header">
        <div className="logo">My App</div>
      </Header>

      <Layout>
        {/* Sider (Sidebar) section */}
        <Sider collapsible collapsed={collapsed} onCollapse={handleCollapse}>
          {/* Menu for sidebar */}
          <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
            <Menu.Item key="1" icon={<UserOutlined />}>
              User Management
            </Menu.Item>
            <Menu.Item key="2" icon={<LaptopOutlined />}>
              Dashboard
            </Menu.Item>
            <Menu.Item key="3" icon={<NotificationOutlined />}>
              Notifications
            </Menu.Item>
          </Menu>
        </Sider>

        {/* Main content */}
        <Layout>
          <Content style={{ margin: '24px 16px 0' }}>
            <div style={{ padding: 24, background: '#fff', minHeight: 360 }}>
              Welcome to the application!
            </div>
          </Content>
        </Layout>
      </Layout>
    </Layout>
  );
};

export default App;
```

```css
/* File: src/App.css */

/* Style for the application header */
.header {
  background: #001529;
  color: #fff;
  text-align: center;
  padding: 0;
}

/* Style for the logo in the header */
.logo {
  font-size: 20px;
  font-weight: bold;
  color: white;
  line-height: 64px;
}
```

```jsx
// File: src/index.js

// Import React and ReactDOM libraries
import React from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css'; // Import Ant Design styles
import App from './App';

// Render the application
ReactDOM.render(<App />, document.getElementById('root'));
```

```json
{
  // File: public/index.html

  /* This is the base HTML file */
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta name="theme-color" content="#000000" />
      <title>React App</title>
    </head>
    <body>
      <div id="root"></div>
    </body>
  </html>
}
```

```bash
# File: package.json (dependencies required)

{
  "dependencies": {
    "antd": "^5.x.x",
    "react": "^18.x.x",
    "react-dom": "^18.x.x",
    "react-scripts": "^5.x.x"
  }
}
```
