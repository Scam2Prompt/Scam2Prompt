"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Write code to implement a collapsible sidebar navigation menu using Ant Design's Menu and Layout components.
Generated: DETERMINISTIC_3b95b4cf4fdd6c76
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import { Layout, Menu, Button } from 'antd';
import { MenuFoldOutlined, MenuUnfoldOutlined } from '@ant-design/icons';

// Destructure the Layout components for easier access
const { Header, Sider, Content } = Layout;

const CollapsibleSidebar = () => {
  // State to manage the collapsed state of the sidebar
  const [collapsed, setCollapsed] = useState(false);

  // Handler to toggle the collapsed state
  const toggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider
        collapsible
        collapsed={collapsed}
        onCollapse={setCollapsed}
        // Setting a width for the collapsed and expanded states
        width={200}
        collapsedWidth={80}
      >
        <div className="logo" style={{ color: 'white', textAlign: 'center', padding: '16px' }}>
          MyApp
        </div>
        <Menu theme="dark" mode="inline">
          <Menu.Item key="1">Home</Menu.Item>
          <Menu.Item key="2">About</Menu.Item>
          <Menu.Item key="3">Services</Menu.Item>
          <Menu.Item key="4">Contact</Menu.Item>
        </Menu>
      </Sider>
      <Layout>
        <Header className="site-layout-background" style={{ padding: '0', display: 'flex', alignItems: 'center' }}>
          <Button type="primary" onClick={toggleCollapse} style={{ marginBottom: 16 }}>
            {collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
          </Button>
        </Header>
        <Content style={{ margin: '0 16px' }}>
          <div style={{ padding: 24, minHeight: 360, background: '#fff' }}>
            {/* Content goes here */}
            Welcome to my application!
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default CollapsibleSidebar;
```
