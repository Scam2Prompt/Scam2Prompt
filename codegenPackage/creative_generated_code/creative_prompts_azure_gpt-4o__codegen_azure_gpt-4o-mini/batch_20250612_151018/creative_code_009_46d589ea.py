"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to implement a sidebar navigation menu using Ant Design's Menu and Layout components.
Generated: DETERMINISTIC_46d589eacb8c7583
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';
import { Layout, Menu } from 'antd';
import { HomeOutlined, UserOutlined, SettingOutlined } from '@ant-design/icons';

// Destructuring the Layout component
const { Header, Content, Sider } = Layout;

// SidebarNavigation component definition
const SidebarNavigation = () => {
  // State to hold the currently selected menu item
  const [selectedKey, setSelectedKey] = React.useState('home');

  // Function to handle menu item selection
  const handleMenuClick = (e) => {
    setSelectedKey(e.key); // Update the selected menu item state
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* Sidebar (Sider) containing the navigation menu */}
      <Sider width={200} className="site-layout-background">
        <Menu
          mode="inline"
          selectedKeys={[selectedKey]} // Set the selected key from state
          onClick={handleMenuClick} // Attach click handler
          style={{ height: '100%', borderRight: 0 }}
        >
          <Menu.Item key="home" icon={<HomeOutlined />}>
            Home
          </Menu.Item>
          <Menu.Item key="profile" icon={<UserOutlined />}>
            Profile
          </Menu.Item>
          <Menu.Item key="settings" icon={<SettingOutlined />}>
            Settings
          </Menu.Item>
        </Menu>
      </Sider>

      <Layout>
        <Header className="site-layout-background" style={{ padding: 0 }}>
          <h2>My Application</h2>
        </Header>
        <Content style={{ margin: '0 16px' }}>
          <div
            style={{
              padding: 24,
              minHeight: 360,
              background: '#fff',
            }}
          >
            {/* Display content based on the selected menu item */}
            {selectedKey === 'home' && <h3>Welcome to the Home Page!</h3>}
            {selectedKey === 'profile' && <h3>User Profile Information</h3>}
            {selectedKey === 'settings' && <h3>Settings Configuration</h3>}
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default SidebarNavigation;
```

Make sure to install the necessary dependencies before running the code:

```bash
npm install antd @ant-design/icons
```
