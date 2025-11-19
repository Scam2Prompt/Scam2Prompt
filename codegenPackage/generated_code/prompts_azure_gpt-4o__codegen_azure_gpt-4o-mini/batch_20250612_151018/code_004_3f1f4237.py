"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Create a React component to customize the layout of a Docusaurus site while reusing the default header and footer.
Generated: DETERMINISTIC_3f1f423747ea398e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CustomLayout.js
import React from 'react';
import PropTypes from 'prop-types';
import { Layout as DocusaurusLayout } from '@docusaurus/theme-classic';
import Header from '@theme/Header';
import Footer from '@theme/Footer';
import { useLocation } from '@docusaurus/router';

/**
 * CustomLayout component to customize the layout of a Docusaurus site.
 * It reuses the default header and footer while allowing for custom content.
 *
 * @param {Object} props - The component props.
 * @param {React.ReactNode} props.children - The content to be displayed within the layout.
 * @returns {JSX.Element} The rendered layout component.
 */
const CustomLayout = ({ children }) => {
  const location = useLocation();

  // Error handling for missing children
  if (!children) {
    console.error('CustomLayout: No children provided.');
    return <div>Error: No content available.</div>;
  }

  return (
    <DocusaurusLayout>
      <Header location={location} />
      <main>{children}</main>
      <Footer />
    </DocusaurusLayout>
  );
};

// PropTypes for type checking
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default CustomLayout;
```

```javascript
// UsageExample.js
import React from 'react';
import CustomLayout from './CustomLayout';

/**
 * Example usage of the CustomLayout component.
 *
 * @returns {JSX.Element} The rendered example page.
 */
const UsageExample = () => {
  return (
    <CustomLayout>
      <h1>Welcome to My Custom Docusaurus Page</h1>
      <p>This is a custom layout example using Docusaurus.</p>
    </CustomLayout>
  );
};

export default UsageExample;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import UsageExample from './UsageExample';

/**
 * Main entry point for the application.
 */
const App = () => {
  return <UsageExample />;
};

// Render the application
ReactDOM.render(<App />, document.getElementById('root'));
```
