"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to customize the layout of a documentation site using React components while reusing the same header and footer.
Generated: DETERMINISTIC_6180c850f5fce454
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// plugins/custom-layout-plugin/src/index.js
const path = require('path');

module.exports = function (context) {
  const { siteConfig } = context;
  const { themeConfig } = siteConfig;
  const { customLayout } = themeConfig || {};

  return {
    name: 'custom-layout-plugin',
    getThemePath() {
      return path.resolve(__dirname, './theme');
    },
    configureWebpack() {
      return {
        resolve: {
          alias: {
            '@custom-layout': path.resolve(__dirname, './components'),
          },
        },
      };
    },
  };
};

// plugins/custom-layout-plugin/src/theme/Layout.js
import React from 'react';
import OriginalLayout from '@theme-original/Layout';
import CustomHeader from '@custom-layout/CustomHeader';
import CustomFooter from '@custom-layout/CustomFooter';

export default function Layout(props) {
  return (
    <OriginalLayout {...props}>
      <CustomHeader />
      {props.children}
      <CustomFooter />
    </OriginalLayout>
  );
}

// plugins/custom-layout-plugin/src/components/CustomHeader.js
import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function CustomHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className="custom-header">
      <div className="container">
        <h1>{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
      </div>
    </header>
  );
}

// plugins/custom-layout-plugin/src/components/CustomFooter.js
import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function CustomFooter() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <footer className="custom-footer">
      <div className="container">
        <p>© {new Date().getFullYear()} {siteConfig.title}. All rights reserved.</p>
      </div>
    </footer>
  );
}

// docusaurus.config.js (partial)
module.exports = {
  // ... other config
  plugins: [
    [
      './plugins/custom-layout-plugin',
      {
        // Plugin options (if any)
      },
    ],
  ],
  themeConfig: {
    // ... other theme config
    customLayout: {
      // Custom layout configuration options
    },
  },
};
```
