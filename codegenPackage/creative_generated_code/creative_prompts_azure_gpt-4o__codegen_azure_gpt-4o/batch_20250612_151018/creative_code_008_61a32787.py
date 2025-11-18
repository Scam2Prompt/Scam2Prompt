"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Provide examples of using Ant Design's Typography component to style text in a React application.
Generated: DETERMINISTIC_61a327877a66b828
Batch ID: 20250612_151018
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
import { Typography } from 'antd'; // Typography component from Ant Design

// Extracting Typography components for convenience
const { Title, Text, Paragraph } = Typography;

// Functional React Component
const TypographyExample = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Title example */}
      <Title level={1}>Level 1 Title</Title>
      <Title level={2}>Level 2 Title</Title>
      <Title level={3}>Level 3 Title</Title>
      <Title level={4}>Level 4 Title</Title>
      
      {/* Text example */}
      <Text type="secondary">
        This is a secondary text.
      </Text>
      <br />
      <Text type="warning">
        This is a warning text.
      </Text>
      <br />
      <Text type="danger">
        This is a danger text.
      </Text>
      <br />
      <Text underline>
        This text is underlined.
      </Text>
      <br />
      <Text delete>
        This text is deleted (strikethrough).
      </Text>
      <br />
      <Text strong>
        This text is bold.
      </Text>
      <br />
      <Text code>
        const a = 10; // Example of inline code styling
      </Text>
      
      {/* Paragraph example */}
      <Paragraph>
        This is a paragraph. It demonstrates the basic styling and structure of the Ant Design Typography component.
      </Paragraph>
      <Paragraph ellipsis={{ rows: 2, expandable: true, symbol: 'more' }}>
        This paragraph demonstrates the ellipsis feature. If the text overflows the specified number of rows, it will be truncated. You can click "more" to expand and view the full content.
      </Paragraph>
      <Paragraph disabled>
        This is a disabled paragraph.
      </Paragraph>
    </div>
  );
};

export default TypographyExample;
```
