"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Write code to use Ant Design's Drawer component to create a collapsible sidebar navigation menu.
Generated: DETERMINISTIC_4c286fdec60d85c1
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
import { Drawer, Button, Menu } from 'antd';
import { MenuOutlined } from '@ant-design/icons';
import 'antd/dist/antd.css'; // Import Ant Design styles

const SidebarDrawer = () => {
  // State to control the visibility of the Drawer
  const [visible, setVisible] = useState(false);

  // Function to show the Drawer
  const showDrawer = () => {
    setVisible(true);
  };

  // Function to close the Drawer
  const onClose = () => {
    setVisible(false);
  };

  return (
    <>
      {/* Button to trigger the Drawer */}
      <Button 
        type="primary" 
        icon={<MenuOutlined />} 
        onClick={showDrawer}
        style={{ marginBottom: 16 }}
      >
        Open Menu
      </Button>

      {/* Drawer component for the sidebar */}
      <Drawer
        title="Navigation Menu"
        placement="left"
        closable={true}
        onClose={onClose}
        visible={visible}
        width={300} // Set the width of the Drawer
      >
        {/* Menu component for navigation items */}
        <Menu
          mode="inline"
          defaultSelectedKeys={['1']}
          style={{ height: '100%', borderRight: 0 }}
        >
          <Menu.Item key="1">Home</Menu.Item>
          <Menu.Item key="2">About</Menu.Item>
          <Menu.Item key="3">Services</Menu.Item>
          <Menu.Item key="4">Contact</Menu.Item>
        </Menu>
      </Drawer>
    </>
  );
};

export default SidebarDrawer;
```

Make sure to install Ant Design in your project by running:
```bash
npm install antd @ant-design/icons
```

This code creates a collapsible sidebar navigation menu using Ant Design's Drawer component.
