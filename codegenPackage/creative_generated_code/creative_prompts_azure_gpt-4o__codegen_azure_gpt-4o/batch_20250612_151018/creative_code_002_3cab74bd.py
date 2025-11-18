"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Generate React code to implement a collapsible sidebar navigation menu using Ant Design's Menu and Layout components.
Generated: DETERMINISTIC_3cab74bd73169a86
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
import React, { useState } from "react";
import { Layout, Menu } from "antd";
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
} from "@ant-design/icons";
import "antd/dist/reset.css"; // Ensure Ant Design styles are imported

// Destructure components from Ant Design
const { Header, Sider, Content } = Layout;

// Main App Component
const App = () => {
  // State to manage the collapsed state of the sidebar
  const [collapsed, setCollapsed] = useState(false);

  // Toggle the collapsed state
  const toggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  return (
    <Layout style={{ minHeight: "100vh" }}>
      {/* Sidebar */}
      <Sider collapsible collapsed={collapsed} trigger={null}>
        <div className="logo" style={{ height: "32px", margin: "16px", background: "rgba(255,255,255,0.2)" }} />
        <Menu theme="dark" mode="inline" defaultSelectedKeys={["1"]}>
          {/* Menu Items */}
          <Menu.Item key="1" icon={<UserOutlined />}>
            Home
          </Menu.Item>
          <Menu.Item key="2" icon={<VideoCameraOutlined />}>
            About
          </Menu.Item>
          <Menu.Item key="3" icon={<UploadOutlined />}>
            Contact
          </Menu.Item>
        </Menu>
      </Sider>

      {/* Main Layout */}
      <Layout>
        {/* Header */}
        <Header style={{ padding: "0 16px", background: "#fff" }}>
          {/* Collapse/Expand Button */}
          {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
            className: "trigger",
            onClick: toggleCollapse,
          })}
        </Header>

        {/* Content Section */}
        <Content style={{ margin: "24px 16px", padding: 24, background: "#fff" }}>
          <h1>Welcome to the Collapsible Sidebar Demo!</h1>
          <p>Click the icon in the header to collapse or expand the sidebar.</p>
        </Content>
      </Layout>
    </Layout>
  );
};

export default App;
```
