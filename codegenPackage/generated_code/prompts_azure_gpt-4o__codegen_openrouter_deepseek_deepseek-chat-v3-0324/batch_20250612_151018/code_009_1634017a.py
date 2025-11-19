"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Provide a code example to extend Docusaurus functionality by adding a custom React component to the site layout.
Generated: DETERMINISTIC_1634017a24cc41f5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/components/CustomComponent.js
import React from 'react';
import clsx from 'clsx';
import styles from './CustomComponent.module.css';

/**
 * Custom component that can be added to Docusaurus layout
 * @param {Object} props - Component props
 * @param {string} [props.className] - Additional CSS class names
 * @param {React.ReactNode} [props.children] - Child components
 * @returns {JSX.Element} Custom component
 */
function CustomComponent({ className, children }) {
  return (
    <div className={clsx(styles.container, className)}>
      <h2 className={styles.title}>Custom Component</h2>
      <div className={styles.content}>
        {children || 'This is a custom component added to Docusaurus'}
      </div>
    </div>
  );
}

export default CustomComponent;
```

```css
/* src/components/CustomComponent.module.css */
.container {
  padding: 2rem;
  margin: 2rem 0;
  border-radius: 8px;
  background-color: var(--ifm-color-primary-lightest);
  border: 1px solid var(--ifm-color-primary-light);
}

.title {
  color: var(--ifm-color-primary-dark);
  margin-bottom: 1rem;
}

.content {
  color: var(--ifm-font-color-base);
}
```

```javascript
// src/theme/Layout.js
import React from 'react';
import Layout from '@theme/Layout';
import CustomComponent from '../components/CustomComponent';

/**
 * Extended Docusaurus layout with custom component
 * @param {Object} props - Layout props
 * @param {React.ReactNode} props.children - Page content
 * @returns {JSX.Element} Extended layout
 */
export default function CustomLayout({ children }) {
  return (
    <Layout>
      <CustomComponent>
        This content is injected into the custom component
      </CustomComponent>
      {children}
    </Layout>
  );
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... existing config
  themes: ['@docusaurus/theme-classic'],
  plugins: [
    // ... other plugins
    function myPlugin(context, options) {
      return {
        name: 'custom-component-plugin',
        configureWebpack(config, isServer, utils) {
          return {
            resolve: {
              alias: {
                '@theme/Layout': require.resolve('../src/theme/Layout.js'),
              },
            },
          };
        },
      };
    },
  ],
};
```
