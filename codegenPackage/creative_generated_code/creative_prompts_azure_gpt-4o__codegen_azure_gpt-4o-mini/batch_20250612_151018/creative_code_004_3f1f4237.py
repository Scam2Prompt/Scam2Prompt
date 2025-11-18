"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Create a React component to customize the layout of a Docusaurus site while reusing the default header and footer.
Generated: DETERMINISTIC_3f1f423747ea398e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CustomLayout.js
import React from 'react';
import PropTypes from 'prop-types';
import { Layout } from '@theme/Layout';
import Header from '@theme/Header';
import Footer from '@theme/Footer';

/**
 * CustomLayout component to wrap pages with a custom layout
 * while reusing the default Header and Footer from Docusaurus.
 *
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Content to display within the layout
 * @returns {JSX.Element} Rendered CustomLayout component
 */
const CustomLayout = ({ children }) => {
  return (
    <Layout>
      {/* Render the default Header */}
      <Header />

      <main>
        {/* Main content goes here */}
        {children}
      </main>

      {/* Render the default Footer */}
      <Footer />
    </Layout>
  );
};

// Prop validation for the CustomLayout component
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

// Error boundary to catch rendering errors
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError() {
    // Update state so the next render shows the fallback UI
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log error information for debugging
    console.error("Error caught in ErrorBoundary:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Fallback UI for errors
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}

/**
 * Wrapper to provide error handling to the CustomLayout
 * 
 * @param {Object} props - Component props
 * @returns {JSX.Element} Rendered ErrorBoundary with CustomLayout
 */
const CustomLayoutWithBoundary = (props) => (
  <ErrorBoundary>
    <CustomLayout {...props} />
  </ErrorBoundary>
);

export default CustomLayoutWithBoundary;
```
