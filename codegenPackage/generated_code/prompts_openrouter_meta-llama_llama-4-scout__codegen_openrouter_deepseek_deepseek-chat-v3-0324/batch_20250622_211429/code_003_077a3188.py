"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Generate a code snippet using Ant Design's Grid component to create a responsive layout.
Generated: DETERMINISTIC_077a3188e10c12bf
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React from 'react';
import { Row, Col } from 'antd';

/**
 * ResponsiveGridLayout Component
 * 
 * A responsive layout using Ant Design's Grid system.
 * 
 * Features:
 * - Responsive columns that adjust based on screen size
 * - Properly spaced and aligned grid items
 * - Clean and maintainable structure
 */
const ResponsiveGridLayout = () => {
  return (
    <div style={{ padding: '24px' }}>
      {/* 
        Row with responsive columns 
        - xs: 1 column on extra small screens
        - sm: 2 columns on small screens
        - md: 3 columns on medium screens
        - lg: 4 columns on large screens
      */}
      <Row gutter={[16, 16]}>
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{
            background: '#f0f2f5',
            padding: '16px',
            borderRadius: '4px',
            textAlign: 'center',
            height: '100px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}>
            Grid Item 1
          </div>
        </Col>
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{
            background: '#f0f2f5',
            padding: '16px',
            borderRadius: '4px',
            textAlign: 'center',
            height: '100px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}>
            Grid Item 2
          </div>
        </Col>
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{
            background: '#f0f2f5',
            padding: '16px',
            borderRadius: '4px',
            textAlign: 'center',
            height: '100px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}>
            Grid Item 3
          </div>
        </Col>
        <Col xs={24} sm={12} md={8} lg={6}>
          <div style={{
            background: '#f0f2f5',
            padding: '16px',
            borderRadius: '4px',
            textAlign: 'center',
            height: '100px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}>
            Grid Item 4
          </div>
        </Col>
      </Row>
    </div>
  );
};

export default ResponsiveGridLayout;
```
