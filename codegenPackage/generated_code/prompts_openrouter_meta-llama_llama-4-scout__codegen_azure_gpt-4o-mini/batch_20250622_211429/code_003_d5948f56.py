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
// Import necessary libraries
import React from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css'; // Import Ant Design styles
import { Button, Layout, Typography } from 'antd'; // Import Ant Design components

// Destructure components from Ant Design
const { Header, Content, Footer } = Layout;
const { Title } = Typography;

// Main App component
const App = () => {
  // Function to handle button click
  const handleClick = () => {
    alert('Button clicked!');
  };

  return (
    <Layout>
      <Header style={{ color: 'white', textAlign: 'center' }}>
        <Title level={2} style={{ color: 'white' }}>Ant Design with React</Title>
      </Header>
      <Content style={{ padding: '50px', textAlign: 'center' }}>
        <Button type="primary" onClick={handleClick}>
          Click Me
        </Button>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Ant Design ©2023 Created by Your Name
      </Footer>
    </Layout>
  );
};

// Render the App component into the DOM
ReactDOM.render(<App />, document.getElementById('root'));

// Error handling for rendering
try {
  ReactDOM.render(<App />, document.getElementById('root'));
} catch (error) {
  console.error('Error rendering the application:', error);
}
```

Make sure to include the necessary dependencies in your `package.json`:

```json
{
  "dependencies": {
    "antd": "^4.0.0",
    "react": "^17.0.0",
    "react-dom": "^17.0.0"
  }
}
```

To run the application, ensure you have a React environment set up, and then execute `npm start` or `yarn start`.
