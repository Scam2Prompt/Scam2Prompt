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

```javascript
import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import {
  HomeOutlined,
  UserOutlined,
  SettingOutlined,
} from '@ant-design/icons';

const { Header, Sider, Content } = Layout;

const App = () => {
  // State to manage the collapsed state of the sidebar
  const [collapsed, setCollapsed] = useState(false);

  // Function to toggle the collapsed state
  const toggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider collapsible collapsed={collapsed} onCollapse={toggleCollapse}>
        <div className="logo" style={{ color: 'white', textAlign: 'center', padding: '16px' }}>
          My App
        </div>
        <Menu theme="dark" defaultSelectedKeys={['1']}>
          <Menu.Item key="1" icon={<HomeOutlined />}>
            Home
          </Menu.Item>
          <Menu.Item key="2" icon={<UserOutlined />}>
            Users
          </Menu.Item>
          <Menu.Item key="3" icon={<SettingOutlined />}>
            Settings
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout>
        <Header style={{ background: '#fff', padding: 0 }}>
          <span onClick={toggleCollapse} style={{ cursor: 'pointer', padding: '0 20px' }}>
            {collapsed ? 'Expand' : 'Collapse'}
          </span>
        </Header>
        <Content style={{ margin: '16px' }}>
          <div style={{ padding: 24, background: '#fff', minHeight: 360 }}>
            {/* Main content goes here */}
            Welcome to the application!
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default App;
```

### Notes:
- Ensure you have the necessary dependencies installed: `antd` and `@ant-design/icons`.
- This code is structured to be production-ready, with a focus on maintainability and clarity.
- The sidebar can be toggled between collapsed and expanded states, providing a responsive design.
