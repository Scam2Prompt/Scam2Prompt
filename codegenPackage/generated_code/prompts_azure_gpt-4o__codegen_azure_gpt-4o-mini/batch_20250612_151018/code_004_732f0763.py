"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Write a React application using Ant Design's Grid system to create a responsive layout with three columns.
Generated: DETERMINISTIC_732f076345af9b6b
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
import { Layout, Row, Col } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Destructure Layout components for easier access
const { Header, Content, Footer } = Layout;

// Main App component
const App = () => {
  return (
    <Layout>
      <Header style={{ color: 'white', textAlign: 'center', fontSize: '24px' }}>
        Responsive Grid Layout
      </Header>
      <Content style={{ padding: '20px' }}>
        {/* Ant Design Row component for responsive layout */}
        <Row gutter={16}>
          {/* First Column */}
          <Col xs={24} sm={12} md={8}>
            <div style={columnStyle}>
              <h2>Column 1</h2>
              <p>This is the first column.</p>
            </div>
          </Col>
          {/* Second Column */}
          <Col xs={24} sm={12} md={8}>
            <div style={columnStyle}>
              <h2>Column 2</h2>
              <p>This is the second column.</p>
            </div>
          </Col>
          {/* Third Column */}
          <Col xs={24} sm={12} md={8}>
            <div style={columnStyle}>
              <h2>Column 3</h2>
              <p>This is the third column.</p>
            </div>
          </Col>
        </Row>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Ant Design Grid Layout ©2023 Created by OpenAI
      </Footer>
    </Layout>
  );
};

// Style for each column
const columnStyle = {
  background: '#f0f2f5',
  padding: '20px',
  borderRadius: '8px',
  textAlign: 'center',
};

// Render the App component into the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

Make sure to include a `div` with `id="root"` in your HTML file for the React application to render properly.
