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
import { Grid } from 'antd';

/**
 * Responsive Grid Layout using Ant Design's Grid component.
 */
const ResponsiveGrid = () => {
  return (
    <Grid.Container>
      <Grid.Item span={24} md={{ span: 12 }} lg={{ span: 8 }} xl={{ span: 6 }}>
        <div style={{ background: '#f0f2f5', padding: '16px', margin: '16px', border: '1px solid #d9d9d9' }}>
          <h3>Column 1</h3>
        </div>
      </Grid.Item>
      <Grid.Item span={24} md={{ span: 12 }} lg={{ span: 8 }} xl={{ span: 6 }}>
        <div style={{ background: '#f0f2f5', padding: '16px', margin: '16px', border: '1px solid #d9d9d9' }}>
          <h3>Column 2</h3>
        </div>
      </Grid.Item>
      <Grid.Item span={24} md={{ span: 12 }} lg={{ span: 8 }} xl={{ span: 6 }}>
        <div style={{ background: '#f0f2f5', padding: '16px', margin: '16px', border: '1px solid #d9d9d9' }}>
          <h3>Column 3</h3>
        </div>
      </Grid.Item>
      <Grid.Item span={24} md={{ span: 12 }} lg={{ span: 8 }} xl={{ span: 6 }}>
        <div style={{ background: '#f0f2f5', padding: '16px', margin: '16px', border: '1px solid #d9d9d9' }}>
          <h3>Column 4</h3>
        </div>
      </Grid.Item>
    </Grid.Container>
  );
};

export default ResponsiveGrid;
```

```css
/* For demonstration purposes only */
.ant-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.ant-grid > .ant-grid-item {
  margin: 16px;
}

.ant-grid > .ant-grid-item > div {
  text-align: center;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import ResponsiveGrid from './ResponsiveGrid';

ReactDOM.render(
  <React.StrictMode>
    <ResponsiveGrid />
  </React.StrictMode>,
  document.getElementById('root')
);
```
