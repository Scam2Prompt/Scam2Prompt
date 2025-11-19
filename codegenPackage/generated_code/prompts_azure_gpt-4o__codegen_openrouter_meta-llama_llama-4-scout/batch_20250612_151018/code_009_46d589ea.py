"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to implement a sidebar navigation menu using Ant Design's Menu and Layout components.
Generated: DETERMINISTIC_46d589eacb8c7583
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import 'antd/dist/antd.css';

const { Header, Content, Sider } = Layout;
const { SubMenu } = Menu;

function SidebarNavigation() {
  const [current, setCurrent] = useState('home');

  const handleClick = (e) => {
    setCurrent(e.key);
  };

  return (
    <Layout style={{ height: '100vh' }}>
      <Header style={{ background: '#fff', padding: 0 }} />
      <Layout>
        <Sider width={200} style={{ background: '#fff' }}>
          <Menu
            mode="inline"
            selectedKeys={[current]}
            onClick={handleClick}
            style={{ height: '100%', borderRight: 0 }}
          >
            <Menu.Item key="home">
              <i className="home-icon" />
              Home
            </Menu.Item>
            <SubMenu key="settings" title="Settings">
              <Menu.Item key="profile">Profile</Menu.Item>
              <Menu.Item key="system">System</Menu.Item>
            </SubMenu>
            <Menu.Item key="about">
              <i className="about-icon" />
              About
            </Menu.Item>
          </Menu>
        </Sider>
        <Content style={{ padding: 24, margin: 24, background: '#fff', minHeight: 280 }}>
          <h2>Welcome to the {current} page</h2>
        </Content>
      </Layout>
    </Layout>
  );
}

export default SidebarNavigation;
```
