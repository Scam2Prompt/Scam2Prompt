"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Provide examples of using Ant Design's Typography component to style text in a React application.
Generated: DETERMINISTIC_61a327877a66b828
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
import { Typography } from 'antd';

// Destructure the necessary components from Typography
const { Title, Text, Paragraph } = Typography;

/**
 * ExampleComponent demonstrates the usage of Ant Design's Typography components.
 * It showcases different text styles including Title, Text, and Paragraph.
 */
const ExampleComponent = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Title component for main headings */}
      <Title level={1}>Welcome to Ant Design Typography</Title>

      {/* Paragraph component for descriptive text */}
      <Paragraph>
        Ant Design provides a set of high-quality React components out of the box.
        These components are designed to be easy to use and customizable.
      </Paragraph>

      {/* Title component for subheadings */}
      <Title level={2}>Typography Examples</Title>

      {/* Text component for inline text styling */}
      <Text strong>Bold Text</Text> - This text is bold.<br />
      <Text italic>Italic Text</Text> - This text is italic.<br />
      <Text underline>Underlined Text</Text> - This text is underlined.<br />
      <Text type="danger">Danger Text</Text> - This text indicates a danger message.<br />

      {/* Another paragraph for additional information */}
      <Paragraph>
        You can easily customize the typography styles using props. 
        For example, you can change the level of the Title component or the type of Text.
      </Paragraph>
    </div>
  );
};

export default ExampleComponent;
```

Make sure to install Ant Design in your project by running:
```bash
npm install antd
```

And import the Ant Design CSS in your main entry file (e.g., `index.js`):
```javascript
import 'antd/dist/antd.css';
```
