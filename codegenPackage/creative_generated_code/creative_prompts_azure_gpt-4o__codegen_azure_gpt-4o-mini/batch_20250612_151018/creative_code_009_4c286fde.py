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

```javascript
import React, { useState } from 'react';
import { Drawer, Button, Menu } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

const SidebarDrawer = () => {
  // State to manage the visibility of the Drawer
  const [visible, setVisible] = useState(false);

  // Function to show the Drawer
  const showDrawer = () => {
    setVisible(true);
  };

  // Function to hide the Drawer
  const onClose = () => {
    setVisible(false);
  };

  return (
    <div>
      {/* Button to trigger the Drawer */}
      <Button type="primary" onClick={showDrawer}>
        Open Navigation Menu
      </Button>
      
      {/* Drawer component for sidebar navigation */}
      <Drawer
        title="Navigation Menu"
        placement="left"
        closable={true}
        onClose={onClose}
        visible={visible}
        // You can set width of drawer here, default is 256px
        width={300}
      >
        {/* Menu items for navigation */}
        <Menu
          // Default selected key
          defaultSelectedKeys={['1']}
          mode="inline"
        >
          <Menu.Item key="1">Home</Menu.Item>
          <Menu.Item key="2">About</Menu.Item>
          <Menu.Item key="3">Services</Menu.Item>
          <Menu.Item key="4">Contact</Menu.Item>
        </Menu>
      </Drawer>
    </div>
  );
};

export default SidebarDrawer;
```
