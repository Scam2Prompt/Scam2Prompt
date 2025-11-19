"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: How can I implement a responsive layout using Ant Design's Grid system in a React application?
Generated: DETERMINISTIC_a740de05acad0316
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React from 'react';
import { Row, Col } from 'antd';
import 'antd/dist/reset.css'; // Import Ant Design styles

// Functional component to demonstrate responsive layout using Ant Design's Grid system
const ResponsiveLayout = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Main container row */}
      <Row gutter={[16, 16]} style={{ backgroundColor: '#f5f5f5', padding: '10px' }}>
        {/* First column: Full width on xs, half on sm, third on md or larger */}
        <Col xs={24} sm={12} md={8} lg={8} xl={6}>
          <div style={{ backgroundColor: '#0078d7', color: '#fff', padding: '10px', borderRadius: '4px' }}>
            Column 1
          </div>
        </Col>
        {/* Second column */}
        <Col xs={24} sm={12} md={8} lg={8} xl={6}>
          <div style={{ backgroundColor: '#ff5722', color: '#fff', padding: '10px', borderRadius: '4px' }}>
            Column 2
          </div>
        </Col>
        {/* Third column */}
        <Col xs={24} sm={12} md={8} lg={8} xl={6}>
          <div style={{ backgroundColor: '#8bc34a', color: '#fff', padding: '10px', borderRadius: '4px' }}>
            Column 3
          </div>
        </Col>
        {/* Fourth column */}
        <Col xs={24} sm={24} md={24} lg={8} xl={6}>
          <div style={{ backgroundColor: '#ffc107', color: '#fff', padding: '10px', borderRadius: '4px' }}>
            Column 4
          </div>
        </Col>
      </Row>
    </div>
  );
};

export default ResponsiveLayout;
```
