"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Write code to customize the layout of a Docusaurus site by reusing React components for the header and footer.
Generated: DETERMINISTIC_8658984340fd75c6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// src/theme/Layout/index.js

import React from 'react';
import PropTypes from 'prop-types'; // For type-checking props
import clsx from 'clsx'; // Utility for conditional class handling
import { useBaseUrlUtils } from '@docusaurus/useBaseUrl'; // Hook for managing base URL
import { useScrollTop } from '@docusaurus/theme-common'; // Hook for scrolling behavior
import Header from '@theme/Header'; // Reusing default Header
import Footer from '@theme/Footer'; // Reusing default Footer
import styles from './styles.module.css'; // Custom styles for Layout

// Main Layout component
const Layout = ({ children, wrapperClassName }) => {
  // Automatically scrolls to the top when the layout is rendered
  useScrollTop();

  return (
    <div className={clsx(styles.layoutWrapper, wrapperClassName)}>
      {/* Header component */}
      <Header />

      {/* Main content wrapper */}
      <main className={clsx(styles.contentWrapper)}>
        {children}
      </main>

      {/* Footer component */}
      <Footer />
    </div>
  );
};

// Define prop types for Layout component
Layout.propTypes = {
  children: PropTypes.node.isRequired, // Ensures children are passed
  wrapperClassName: PropTypes.string, // Optional custom wrapper class
};

// Default export of the Layout component
export default Layout;

// styles.module.css

/* Custom styles for Layout */
.layoutWrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.contentWrapper {
  flex: 1;
  padding: 20px; /* Add some padding */
}
```
