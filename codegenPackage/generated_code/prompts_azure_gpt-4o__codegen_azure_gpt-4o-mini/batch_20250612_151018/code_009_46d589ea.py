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

```javascript
import React from 'react';
import { Layout, Menu } from 'antd';
import { HomeOutlined, UserOutlined, SettingOutlined } from '@ant-design/icons';

// Destructure the Layout component from Ant Design
const { Sider, Content } = Layout;

// SidebarNavigation component definition
const SidebarNavigation = () => {
  // State to manage the currently selected menu item
  const [selectedKey, setSelectedKey] = React.useState('1');

  // Handler for menu item selection
  const handleMenuClick = (e) => {
    setSelectedKey(e.key);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* Sidebar (Sider) component */}
      <Sider width={200} className="site-layout-background">
        <Menu
          mode="inline"
          selectedKeys={[selectedKey]}
          onClick={handleMenuClick}
          style={{ height: '100%', borderRight: 0 }}
        >
          <Menu.Item key="1" icon={<HomeOutlined />}>
            Home
          </Menu.Item>
          <Menu.Item key="2" icon={<UserOutlined />}>
            Profile
          </Menu.Item>
          <Menu.Item key="3" icon={<SettingOutlined />}>
            Settings
          </Menu.Item>
        </Menu>
      </Sider>

      {/* Main content area */}
      <Layout style={{ padding: '0 24px 24px' }}>
        <Content
          style={{
            padding: 24,
            margin: 0,
            minHeight: 280,
            background: '#fff',
          }}
        >
          {/* Render content based on selected menu item */}
          {selectedKey === '1' && <h2>Welcome to the Home Page</h2>}
          {selectedKey === '2' && <h2>Your Profile Information</h2>}
          {selectedKey === '3' && <h2>Adjust Your Settings</h2>}
        </Content>
      </Layout>
    </Layout>
  );
};

// Export the SidebarNavigation component for use in other parts of the application
export default SidebarNavigation;
```
