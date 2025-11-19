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
import React, { useState } from 'react';
import { Layout, Menu, theme } from 'antd';
import {
  DesktopOutlined,
  FileOutlined,
  PieChartOutlined,
  TeamOutlined,
  UserOutlined,
} from '@ant-design/icons';

const { Sider } = Layout;

function getItem(label, key, icon, children) {
  return {
    key,
    icon,
    children,
    label,
  };
}

const items = [
  getItem('Dashboard', '1', <PieChartOutlined />),
  getItem('Users', 'sub1', <UserOutlined />, [
    getItem('All Users', '2'),
    getItem('Admins', '3'),
    getItem('Customers', '4'),
  ]),
  getItem('Team', 'sub2', <TeamOutlined />, [
    getItem('Team 1', '5'), 
    getItem('Team 2', '6')
  ]),
  getItem('Files', '9', <FileOutlined />),
  getItem('Settings', '10', <DesktopOutlined />),
];

const SidebarMenu = () => {
  const [collapsed, setCollapsed] = useState(false);
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  return (
    <Sider
      collapsible
      collapsed={collapsed}
      onCollapse={(value) => setCollapsed(value)}
      style={{
        background: colorBgContainer,
      }}
      width={250}
    >
      <div className="demo-logo-vertical" />
      <Menu
        theme="light"
        defaultSelectedKeys={['1']}
        mode="inline"
        items={items}
        style={{
          height: '100%',
          borderRight: 0,
        }}
      />
    </Sider>
  );
};

export default SidebarMenu;
```
