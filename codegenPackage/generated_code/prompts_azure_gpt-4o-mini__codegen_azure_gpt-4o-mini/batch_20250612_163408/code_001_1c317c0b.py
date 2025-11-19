"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: What are the key components of the Ant Design library for building modern web applications?
Generated: DETERMINISTIC_1c317c0bef81333c
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React from 'react';
import { Button, Layout, Menu, Breadcrumb } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Destructure components from Ant Design
const { Header, Content, Footer } = Layout;

// Main App component
const App = () => {
  return (
    <Layout className="layout">
      <Header>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
          <Menu.Item key="1">Home</Menu.Item>
          <Menu.Item key="2">About</Menu.Item>
          <Menu.Item key="3">Contact</Menu.Item>
        </Menu>
      </Header>
      <Content style={{ padding: '0 50px' }}>
        <Breadcrumb style={{ margin: '16px 0' }}>
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>List</Breadcrumb.Item>
        </Breadcrumb>
        <div className="site-layout-content">
          <h1>Welcome to Ant Design</h1>
          <Button type="primary">Primary Button</Button>
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Ant Design ©2023 Created by Your Name
      </Footer>
    </Layout>
  );
};

// Error boundary component for error handling
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render shows the fallback UI
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log the error to an error reporting service
    console.error("Error caught in ErrorBoundary: ", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Fallback UI
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children; 
  }
}

// Render the App component wrapped in ErrorBoundary
const Root = () => (
  <ErrorBoundary>
    <App />
  </ErrorBoundary>
);

export default Root;
```
