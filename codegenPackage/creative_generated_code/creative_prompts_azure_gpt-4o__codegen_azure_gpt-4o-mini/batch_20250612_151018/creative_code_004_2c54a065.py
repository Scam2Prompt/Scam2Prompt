"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Grid system to create a responsive layout with three columns.
Generated: DETERMINISTIC_2c54a065b5cd9d34
Batch ID: 20250612_151018
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

const ResponsiveGrid = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Define a responsive Row */}
      <Row gutter={[16, 16]}>
        {/* Column 1 */}
        <Col xs={24} sm={12} md={8}>
          <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 1
          </div>
        </Col>
        {/* Column 2 */}
        <Col xs={24} sm={12} md={8}>
          <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 2
          </div>
        </Col>
        {/* Column 3 */}
        <Col xs={24} sm={12} md={8}>
          <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
            Column 3
          </div>
        </Col>
      </Row>
    </div>
  );
};

export default ResponsiveGrid;
```
