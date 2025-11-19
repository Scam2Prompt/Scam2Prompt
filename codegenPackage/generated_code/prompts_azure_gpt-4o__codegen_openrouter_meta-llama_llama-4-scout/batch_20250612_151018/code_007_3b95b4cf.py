"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Write code to implement a collapsible sidebar navigation menu using Ant Design's Menu and Layout components.
Generated: DETERMINISTIC_3b95b4cf4fdd6c76
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
import { Layout, Menu, Button } from 'antd';
import 'antd/dist/antd.css';

const { Header, Content, Sider } = Layout;

const App = () => {
  const [collapsed, setCollapsed] = useState(false);

  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };

  return (
    <Layout style={{ height: '100vh' }}>
      <Header style={{ background: '#fff', padding: 0, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Button
          type="primary"
          onClick={toggleCollapsed}
          style={{ margin: '0 16px' }}
        >
          {collapsed ? 'Expand' : 'Collapse'}
        </Button>
      </Header>
      <Layout>
        <Sider
          breakpoint="lg"
          collapsedWidth="0"
          onBreakpoint={(broken) => {
            console.log(broken);
          }}
          onCollapse={(collapsed, type) => {
            console.log(collapsed, type);
          }}
          collapsible
          collapsed={collapsed}
          style={{ background: '#fff' }}
        >
          <Menu
            mode="inline"
            defaultSelectedKeys={['1']}
            style={{ border: '0' }}
          >
            <Menu.Item key="1">
              <i className="anticon anticon-home" />
              <span>Home</span>
            </Menu.Item>
            <Menu.Item key="2">
              <i className="anticon anticon-setting" />
              <span>Settings</span>
            </Menu.Item>
            <Menu.Item key="3">
              <i className="anticon anticon-user" />
              <span>Profile</span>
            </Menu.Item>
          </Menu>
        </Sider>
        <Content style={{ padding: '24px', background: '#fff', minHeight: 280 }}>
          Content
        </Content>
      </Layout>
    </Layout>
  );
};

export default App;
```
