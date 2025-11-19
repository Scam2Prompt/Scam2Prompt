"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Write a code snippet that integrates Ant Design with a React application.
Generated: DETERMINISTIC_d5948f56ef81c4dd
Batch ID: 20250622_211429
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
import 'antd/dist/reset.css'; // Import Ant Design styles
import { Button, Layout, Menu, message } from 'antd';

// Destructure components from Ant Design
const { Header, Content, Footer } = Layout;

// Define the main App component
const App = () => {
  // Handle button click event
  const handleClick = () => {
    message.success('Button clicked!'); // Display a success message
  };

  return (
    <Layout>
      {/* Header section */}
      <Header>
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
          <Menu.Item key="1">Home</Menu.Item>
          <Menu.Item key="2">About</Menu.Item>
          <Menu.Item key="3">Contact</Menu.Item>
        </Menu>
      </Header>

      {/* Content section */}
      <Content style={{ padding: '50px', textAlign: 'center' }}>
        <h1>Welcome to Ant Design with React</h1>
        <Button type="primary" onClick={handleClick}>
          Click Me
        </Button>
      </Content>

      {/* Footer section */}
      <Footer style={{ textAlign: 'center' }}>
        Ant Design ©2023 Created by Ant UED
      </Footer>
    </Layout>
  );
};

// Render the App component into the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

**Note:** Ensure you have installed the required dependencies (`antd`, `react`, `react-dom`) and set up a React project with a valid `index.html` containing a `div` with the `id="root"`.
