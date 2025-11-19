"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Write a code snippet to implement a responsive layout using Ant Design's Grid system in a React app.
Generated: DETERMINISTIC_e364a58bed63b50a
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { Row, Col } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

const ResponsiveLayout = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Row to contain the grid columns */}
      <Row gutter={16}>
        {/* First Column: spans 24 on extra small, 12 on small, 8 on medium, and 6 on large screens */}
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 1
          </div>
        </Col>
        {/* Second Column: spans 24 on extra small, 12 on small, 8 on medium, and 6 on large screens */}
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 2
          </div>
        </Col>
        {/* Third Column: spans 24 on extra small, 12 on small, 8 on medium, and 6 on large screens */}
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 3
          </div>
        </Col>
        {/* Fourth Column: spans 24 on extra small, 12 on small, 8 on medium, and 6 on large screens */}
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 4
          </div>
        </Col>
      </Row>
    </div>
  );
};

// Export the component for use in other parts of the application
export default ResponsiveLayout;
```
