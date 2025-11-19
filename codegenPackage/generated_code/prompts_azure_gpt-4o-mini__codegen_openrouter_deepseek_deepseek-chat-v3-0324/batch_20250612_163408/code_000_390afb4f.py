"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: How can I implement a responsive layout using Ant Design's grid system in React?
Generated: DETERMINISTIC_390afb4fb9855ba0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean implementation of a responsive layout using Ant Design's grid system in React:

```jsx
import React from 'react';
import { Row, Col } from 'antd';

/**
 * ResponsiveLayout component using Ant Design's grid system
 * Demonstrates responsive behavior across different screen sizes
 */
const ResponsiveLayout = () => {
  return (
    <div style={{ padding: '24px' }}>
      {/* Basic responsive row */}
      <Row gutter={[16, 16]}>
        {/* Column that spans full width on xs, half on sm, and quarter on md and up */}
        <Col xs={24} sm={12} md={6} lg={6} xl={6}>
          <div style={boxStyle}>Box 1</div>
        </Col>
        
        <Col xs={24} sm={12} md={6} lg={6} xl={6}>
          <div style={boxStyle}>Box 2</div>
        </Col>
        
        <Col xs={24} sm={12} md={6} lg={6} xl={6}>
          <div style={boxStyle}>Box 3</div>
        </Col>
        
        <Col xs={24} sm={12} md={6} lg={6} xl={6}>
          <div style={boxStyle}>Box 4</div>
        </Col>
      </Row>

      {/* Row with different responsive behaviors */}
      <Row gutter={[16, 16]} style={{ marginTop: '24px' }}>
        {/* Column that changes order responsively */}
        <Col xs={24} md={12} lg={8} xl={8} order={3}>
          <div style={boxStyle}>First in DOM, last on large screens</div>
        </Col>
        
        <Col xs={24} md={12} lg={8} xl={8} order={1}>
          <div style={boxStyle}>Second in DOM, first on large screens</div>
        </Col>
        
        <Col xs={24} md={24} lg={8} xl={8} order={2}>
          <div style={boxStyle}>Third in DOM, middle on large screens</div>
        </Col>
      </Row>

      {/* Row with offset columns */}
      <Row gutter={[16, 16]} style={{ marginTop: '24px' }}>
        <Col xs={24} sm={12} md={8} lg={6} xl={4}>
          <div style={boxStyle}>Left</div>
        </Col>
        
        <Col xs={24} sm={12} md={8} lg={6} xl={4} offset={2}>
          <div style={boxStyle}>With Offset</div>
        </Col>
      </Row>
    </div>
  );
};

// Common style for the boxes
const boxStyle = {
  background: '#1890ff',
  color: 'white',
  padding: '16px',
  borderRadius: '4px',
  textAlign: 'center',
  height: '100%',
};

export default ResponsiveLayout;
```
