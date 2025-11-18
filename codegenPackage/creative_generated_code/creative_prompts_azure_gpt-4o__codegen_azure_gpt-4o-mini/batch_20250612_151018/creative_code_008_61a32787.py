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
// Import necessary libraries
import React from 'react';
import { Typography } from 'antd'; // Importing Typography from Ant Design

// Destructure the components needed from Typography
const { Title, Text, Paragraph } = Typography;

// Main App component
const App = () => {
  return (
    <div style={{ padding: '20px' }}>
      {/* Main Title */}
      <Title level={1} style={{ color: '#1890ff' }}>
        Welcome to Ant Design Typography
      </Title>

      {/* Sub Title */}
      <Title level={2} style={{ color: '#52c41a' }}>
        Styling Text with Ant Design
      </Title>

      {/* Paragraph with Text styling */}
      <Paragraph>
        This is an example of a paragraph using the Ant Design Typography component. 
        You can easily style text by using the <Text strong>Text</Text> component.
      </Paragraph>

      {/* Emphasized Text */}
      <Text type="secondary" style={{ fontSize: '16px' }}>
        This is secondary text, typically used for less important information.
      </Text>

      {/* Warning Text */}
      <Text type="danger" style={{ fontWeight: 'bold' }}>
        This is a danger text, used to convey an alert or warning!
      </Text>

      {/* Success Text */}
      <Text type="success">
        This indicates success and positive outcomes.
      </Text>
    </div>
  );
};

// Error Boundary for handling potential rendering errors
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state to indicate an error occurred
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log the error to an error reporting service
    console.error("Error caught in ErrorBoundary:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Fallback UI in case of error
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children; 
  }
}

// Exporting App wrapped in ErrorBoundary for production readiness
export default () => (
  <ErrorBoundary>
    <App />
  </ErrorBoundary>
);
```
