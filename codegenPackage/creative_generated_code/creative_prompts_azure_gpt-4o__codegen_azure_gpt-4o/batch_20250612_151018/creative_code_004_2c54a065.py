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

```jsx
// Import required modules and components from React and Ant Design
import React from "react";
import { Row, Col } from "antd";

// Functional Component to demonstrate Ant Design's Grid System
const ResponsiveGrid = () => {
  return (
    <div style={{ padding: "20px" }}>
      {/* Grid System with Ant Design */}
      <Row gutter={[16, 16]}>
        {/* First Column */}
        <Col xs={24} sm={12} md={8}>
          <div style={{ backgroundColor: "#f0f0f0", padding: "20px", textAlign: "center" }}>
            Column 1
          </div>
        </Col>
        
        {/* Second Column */}
        <Col xs={24} sm={12} md={8}>
          <div style={{ backgroundColor: "#d9d9d9", padding: "20px", textAlign: "center" }}>
            Column 2
          </div>
        </Col>
        
        {/* Third Column */}
        <Col xs={24} sm={24} md={8}>
          <div style={{ backgroundColor: "#bfbfbf", padding: "20px", textAlign: "center" }}>
            Column 3
          </div>
        </Col>
      </Row>
    </div>
  );
};

// Export the component as default
export default ResponsiveGrid;
```
