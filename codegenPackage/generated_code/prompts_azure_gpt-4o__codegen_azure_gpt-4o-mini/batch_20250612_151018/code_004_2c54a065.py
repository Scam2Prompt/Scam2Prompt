"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Grid system to create a responsive layout with three columns.
Generated: DETERMINISTIC_2c54a065b5cd9d34
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React from 'react';
import { Layout, Row, Col } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

const { Header, Content, Footer } = Layout;

const ResponsiveGridExample = () => {
  return (
    <Layout>
      <Header style={{ color: 'white', textAlign: 'center' }}>
        <h1>Responsive Grid Example</h1>
      </Header>
      <Content style={{ padding: '20px' }}>
        <Row gutter={16}>
          {/* First Column */}
          <Col xs={24} sm={12} md={8}>
            <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
              <h2>Column 1</h2>
              <p>This is the first column.</p>
            </div>
          </Col>
          {/* Second Column */}
          <Col xs={24} sm={12} md={8}>
            <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
              <h2>Column 2</h2>
              <p>This is the second column.</p>
            </div>
          </Col>
          {/* Third Column */}
          <Col xs={24} sm={12} md={8}>
            <div style={{ background: '#f0f2f5', padding: '20px', textAlign: 'center' }}>
              <h2>Column 3</h2>
              <p>This is the third column.</p>
            </div>
          </Col>
        </Row>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Ant Design Grid Example ©2023
      </Footer>
    </Layout>
  );
};

// Error boundary to catch any rendering errors
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render shows the fallback UI
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log the error to an error reporting service
    console.error("Error caught in ErrorBoundary: ", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Fallback UI
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children; 
  }
}

// Main application rendering
const App = () => (
  <ErrorBoundary>
    <ResponsiveGridExample />
  </ErrorBoundary>
);

export default App;
```
