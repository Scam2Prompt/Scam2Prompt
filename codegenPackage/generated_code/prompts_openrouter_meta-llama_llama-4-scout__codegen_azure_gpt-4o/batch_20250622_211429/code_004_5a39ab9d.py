"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for customizing Ant Design themes and layouts in a React project?
Generated: DETERMINISTIC_5a39ab9d3d288faa
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules and components
import React from 'react';
import ReactDOM from 'react-dom';
import { ConfigProvider, Layout, Menu } from 'antd';
import { createTheme } from '@ant-design/cssinjs';
import './index.css'; // Custom CSS for overriding styles

// Ant Design components
const { Header, Content, Footer, Sider } = Layout;

// Custom theme configuration using Ant Design's CSS-in-JS approach
const theme = createTheme({
  token: {
    colorPrimary: '#1890ff', // Primary color
    borderRadius: '4px', // Border radius for buttons and inputs
    fontSizeBase: '16px', // Base font size
  },
});

// Main App component
const App = () => {
  return (
    // ConfigProvider allows customization of Ant Design themes
    <ConfigProvider theme={theme}>
      <Layout style={{ minHeight: '100vh' }}>
        {/* Sider for navigation */}
        <Sider collapsible>
          <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
            <Menu.Item key="1">Home</Menu.Item>
            <Menu.Item key="2">About</Menu.Item>
            <Menu.Item key="3">Contact</Menu.Item>
          </Menu>
        </Sider>

        {/* Main layout */}
        <Layout>
          <Header style={{ background: '#fff', padding: 0 }}>
            <h1 style={{ marginLeft: '16px' }}>My Ant Design App</h1>
          </Header>
          <Content style={{ margin: '16px' }}>
            <div style={{ padding: '24px', background: '#fff', minHeight: '360px' }}>
              Welcome to the customized Ant Design layout!
            </div>
          </Content>
          <Footer style={{ textAlign: 'center' }}>
            Ant Design ©2023 Created by Ant UED
          </Footer>
        </Layout>
      </Layout>
    </ConfigProvider>
  );
};

// Error handling for rendering the app
try {
  ReactDOM.render(<App />, document.getElementById('root'));
} catch (error) {
  console.error('Error rendering the application:', error);
}
```

```css
/* index.css */
/* Custom CSS overrides for Ant Design components */
.ant-layout-header {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15); /* Add shadow to header */
}

.ant-menu-item-selected {
  background-color: #40a9ff !important; /* Change selected menu item color */
}

.ant-layout-footer {
  background-color: #f0f2f5; /* Footer background color */
}
```

**Note:** Ensure you have installed the required dependencies (`antd`, `@ant-design/cssinjs`, `react`, `react-dom`) in your project before running this code.
