"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: How can I use Ant Design's Grid system to create a responsive layout for a React application?
Generated: DETERMINISTIC_fa994822ce2513d0
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import { Layout, Row, Col } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

const { Header, Content, Footer } = Layout;

/**
 * App component that demonstrates a responsive layout using Ant Design's Grid system.
 */
const App = () => {
  return (
    <Layout>
      <Header style={{ background: '#001529', color: '#fff', textAlign: 'center' }}>
        <h1>Responsive Layout with Ant Design</h1>
      </Header>
      <Content style={{ padding: '20px' }}>
        <Row gutter={16}>
          {/* First Column */}
          <Col xs={24} sm={12} md={8} lg={6}>
            <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
              <h2>Column 1</h2>
              <p>Content for column 1</p>
            </div>
          </Col>
          {/* Second Column */}
          <Col xs={24} sm={12} md={8} lg={6}>
            <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
              <h2>Column 2</h2>
              <p>Content for column 2</p>
            </div>
          </Col>
          {/* Third Column */}
          <Col xs={24} sm={12} md={8} lg={6}>
            <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
              <h2>Column 3</h2>
              <p>Content for column 3</p>
            </div>
          </Col>
          {/* Fourth Column */}
          <Col xs={24} sm={12} md={8} lg={6}>
            <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
              <h2>Column 4</h2>
              <p>Content for column 4</p>
            </div>
          </Col>
        </Row>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Ant Design Layout Example ©2023 Created by Your Name
      </Footer>
    </Layout>
  );
};

export default App;
```
