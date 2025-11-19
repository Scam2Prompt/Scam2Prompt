"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to customize the layout by reusing React components while maintaining the default header and footer.
Generated: DETERMINISTIC_373e689617660767
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/extend-docusaurus.js
const path = require('path');
const React = require('react');
const { 
  HtmlWebpackPlugin 
} = require('webpack');

// Import default Docusaurus components
const DefaultNavbar = require('@theme/Navbar');
const DefaultFooter = require('@theme/Footer');

// Custom layout component
const CustomLayout = (props) => {
  return (
    <div>
      {/* Reuse default header */}
      <DefaultNavbar />
      {/* Custom main content */}
      {props.children}
      {/* Reuse default footer */}
      <DefaultFooter />
    </div>
  );
};

// Docusaurus plugin to customize layout
module.exports = function (context, options) {
  return {
    name: 'custom-layout-plugin',
    async contentLoaded({ content, actions }) {
      const { createData, addRoute } = actions;
      // Create data for custom layout
      const customLayoutData = await createData(
        'custom-layout',
        JSON.stringify({
          // Add custom metadata if needed
        })
      );

      // Add custom route for layout
      addRoute({
        path: '/',
        component: '@site/src/pages/index.js',
        exact: true,
      });

      // Extend default theme with custom layout
      context.themeConfig = {
        ...context.themeConfig,
        customLayout: CustomLayout,
      };
    },
    configureWebpack(config, { isServer, utils }) {
      // Add custom webpack configuration if needed
      return config;
    },
    getThemePath() {
      // Return path to custom theme
      return path.join(context.siteDir, 'src', 'theme');
    },
  };
};
```

```javascript
// src/theme/index.js
const path = require('path');
module.exports = {
  // Export custom layout component
  Layout: require(path.join(__dirname, 'Layout')).default,
};
```

```javascript
// src/theme/Layout.js
import React from 'react';
import { 
  useLocation 
} from '@docusaurus/router';
import CustomLayout from '@site/src/extend-docusaurus';

const Layout = (props) => {
  const location = useLocation();

  // Use custom layout for specific routes
  if (location.pathname === '/') {
    return <CustomLayout {...props} />;
  }

  // Fallback to default layout
  return <>{props.children}</>;
};

export default Layout;
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  plugins: [
    [
      '@site/src/extend-docusaurus',
      {
        // Add custom options if needed
      },
    ],
  ],
};
```
