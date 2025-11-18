"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: How can I use Ant Design's Grid system to create a responsive layout? Provide example code.
Generated: DETERMINISTIC_6f8dadc481664ccd
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';
import { Layout, Row, Col } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Define the main layout component
const ResponsiveGridLayout = () => {
  return (
    <Layout style={{ padding: '20px' }}>
      <Row gutter={[16, 16]} justify="center">
        {/* Define the first row with 2 columns */}
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{ backgroundColor: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 1
          </div>
        </Col>
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{ backgroundColor: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 2
          </div>
        </Col>
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{ backgroundColor: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 3
          </div>
        </Col>
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{ backgroundColor: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 4
          </div>
        </Col>
      </Row>
    </Layout>
  );
};

// Export the component for use in other parts of the application
export default ResponsiveGridLayout;
```
