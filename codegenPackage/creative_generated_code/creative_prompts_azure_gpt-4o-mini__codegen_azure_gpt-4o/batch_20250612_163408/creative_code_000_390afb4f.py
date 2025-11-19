"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: How can I implement a responsive layout using Ant Design's grid system in React?
Generated: DETERMINISTIC_390afb4fb9855ba0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries and components
import React from 'react';
import { Row, Col } from 'antd'; // Ant Design grid components
import 'antd/dist/antd.css'; // Ant Design CSS for styling

// ResponsiveLayout Component
const ResponsiveLayout = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Using Ant Design's Row and Col for the grid system */}
      <Row gutter={[16, 16]} /* gutter adds spacing between columns */>
        {/* First Column: Full width on small screens, 8/24 (1/3) on medium, 6/24 (1/4) on large */}
        <Col xs={24} sm={24} md={8} lg={6}>
          <div style={{ backgroundColor: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 1
          </div>
        </Col>

        {/* Second Column: Full width on small screens, 8/24 (1/3) on medium, 6/24 (1/4) on large */}
        <Col xs={24} sm={24} md={8} lg={6}>
          <div style={{ backgroundColor: '#ffffff', padding: '20px', textAlign: 'center' }}>
            Column 2
          </div>
        </Col>

        {/* Third Column: Full width on small screens, 8/24 (1/3) on medium, 6/24 (1/4) on large */}
        <Col xs={24} sm={24} md={8} lg={6}>
          <div style={{ backgroundColor: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 3
          </div>
        </Col>

        {/* Fourth Column: Full width on small screens, 24/24 on medium, 6/24 (1/4) on large */}
        <Col xs={24} sm={24} md={24} lg={6}>
          <div style={{ backgroundColor: '#ffffff', padding: '20px', textAlign: 'center' }}>
            Column 4
          </div>
        </Col>
      </Row>
    </div>
  );
};

// Export the component to be used elsewhere
export default ResponsiveLayout;
```
