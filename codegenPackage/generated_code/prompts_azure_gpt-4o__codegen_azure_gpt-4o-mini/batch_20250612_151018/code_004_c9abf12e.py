"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Create a React-based custom layout for a Docusaurus website, reusing the default header and footer components.
Generated: DETERMINISTIC_c9abf12e5d077349
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
import { Header, Footer } from '@docusaurus/theme-classic';
import { useLocation } from '@docusaurus/router';
import styles from './CustomLayout.module.css';

/**
 * CustomLayout component that wraps the default Docusaurus header and footer.
 * It provides a consistent layout for the pages in the Docusaurus site.
 *
 * @param {Object} props - The component props.
 * @param {React.ReactNode} props.children - The content to be displayed within the layout.
 * @returns {JSX.Element} The rendered layout component.
 */
const CustomLayout = ({ children }) => {
  const location = useLocation();

  // Error handling for missing children
  if (!children) {
    console.error('CustomLayout requires children to be passed.');
    return <div className={styles.error}>Content not available.</div>;
  }

  return (
    <div className={styles.customLayout}>
      <Header location={location} />
      <main className={styles.mainContent}>
        {children}
      </main>
      <Footer />
    </div>
  );
};

// PropTypes for type checking
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default CustomLayout;
```

```css
/* CustomLayout.module.css */
.customLayout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.mainContent {
  flex: 1;
  padding: 20px;
}

.error {
  color: red;
  text-align: center;
  margin: 20px;
}
```

```javascript
// ExamplePage.js
import React from 'react';
import CustomLayout from './CustomLayout';

/**
 * ExamplePage component that demonstrates the usage of CustomLayout.
 * It serves as a sample page within the Docusaurus site.
 *
 * @returns {JSX.Element} The rendered example page.
 */
const ExamplePage = () => {
  return (
    <CustomLayout>
      <h1>Welcome to the Example Page</h1>
      <p>This is a sample page using the custom layout.</p>
    </CustomLayout>
  );
};

export default ExamplePage;
```

```javascript
// docusaurus.config.js
module.exports = {
  // Other Docusaurus configuration options...
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Your docs configuration
        },
        blog: {
          // Your blog configuration
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
```

Make sure to import and use `ExamplePage` in your Docusaurus routing configuration to see the custom layout in action.
