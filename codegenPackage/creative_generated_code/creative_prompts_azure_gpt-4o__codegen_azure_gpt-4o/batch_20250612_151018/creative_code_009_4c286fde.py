"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Write code to use Ant Design's Drawer component to create a collapsible sidebar navigation menu.
Generated: DETERMINISTIC_4c286fdec60d85c1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules and components
import React, { useState } from 'react';
import { Drawer, Button, Menu } from 'antd';
import {
  HomeOutlined,
  UserOutlined,
  SettingOutlined,
  InfoCircleOutlined,
} from '@ant-design/icons';

// Component: SidebarDrawer
const SidebarDrawer = () => {
  // State to manage the visibility of the Drawer
  const [visible, setVisible] = useState(false);

  // Function to handle opening the Drawer
  const showDrawer = () => {
    setVisible(true);
  };

  // Function to handle closing the Drawer
  const closeDrawer = () => {
    setVisible(false);
  };

  return (
    <div>
      {/* Button to open the Drawer */}
      <Button type="primary" onClick={showDrawer}>
        Open Sidebar
      </Button>

      {/* Ant Design Drawer component */}
      <Drawer
        title="Navigation Menu"
        placement="left"
        onClose={closeDrawer}
        visible={visible}
        width={250} // Set width of the Drawer
      >
        {/* Ant Design Menu component inside the Drawer */}
        <Menu mode="inline">
          <Menu.Item key="1" icon={<HomeOutlined />}>
            Home
          </Menu.Item>
          <Menu.Item key="2" icon={<UserOutlined />}>
            Profile
          </Menu.Item>
          <Menu.Item key="3" icon={<SettingOutlined />}>
            Settings
          </Menu.Item>
          <Menu.Item key="4" icon={<InfoCircleOutlined />}>
            About
          </Menu.Item>
        </Menu>
      </Drawer>
    </div>
  );
};

export default SidebarDrawer;
```
