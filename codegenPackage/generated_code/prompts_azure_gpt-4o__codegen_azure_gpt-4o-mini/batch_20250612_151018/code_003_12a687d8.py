"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Create a React application using Ant Design's Menu and Layout components to build a sidebar navigation.
Generated: DETERMINISTIC_12a687d82adc2b3e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React from 'react';
import ReactDOM from 'react-dom';
import { Layout, Menu } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Destructure Layout components for easier access
const { Header, Content, Sider } = Layout;

// Main App component
const App = () => {
  // State to manage the currently selected menu item
  const [selectedKey, setSelectedKey] = React.useState('1');

  // Handle menu item click
  const handleMenuClick = (e) => {
    setSelectedKey(e.key);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider width={200} className="site-layout-background">
        <Menu
          mode="inline"
          selectedKeys={[selectedKey]}
          onClick={handleMenuClick}
          style={{ height: '100%', borderRight: 0 }}
        >
          <Menu.Item key="1">Home</Menu.Item>
          <Menu.Item key="2">About</Menu.Item>
          <Menu.Item key="3">Services</Menu.Item>
          <Menu.Item key="4">Contact</Menu.Item>
        </Menu>
      </Sider>
      <Layout>
        <Header className="site-layout-background" style={{ padding: 0 }}>
          <h1 style={{ color: 'white', textAlign: 'center' }}>My Application</h1>
        </Header>
        <Content style={{ margin: '16px' }}>
          <div style={{ padding: 24, minHeight: 360, background: '#fff' }}>
            {/* Render content based on selected menu item */}
            {selectedKey === '1' && <h2>Welcome to the Home Page</h2>}
            {selectedKey === '2' && <h2>About Us</h2>}
            {selectedKey === '3' && <h2>Our Services</h2>}
            {selectedKey === '4' && <h2>Contact Us</h2>}
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

// Render the App component into the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

Make sure to include the following in your `index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>React Ant Design Sidebar</title>
</head>
<body>
    <div id="root"></div>
</body>
</html>
```

And ensure you have the necessary dependencies installed:

```bash
npm install antd react react-dom
```
