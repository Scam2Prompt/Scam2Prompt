"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to customize the layout while reusing the default header and footer components.
Generated: DETERMINISTIC_a4065d9022817ea3
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Custom Docusaurus plugin to customize the layout
// while reusing the default header and footer components

// Import required modules
const path = require('path');
const { merge } = require('lodash');
const { htmlWebpackPlugin } = require('webpack');

// Define the plugin
module.exports = function customLayoutPlugin(context, options) {
  // Return a function that will be called by Docusaurus
  return {
    name: 'custom-layout-plugin',

    // Extend the Webpack config
    configureWebpack(config, isServer) {
      if (!isServer) {
        // Add a custom HTML plugin to inject a script
        config.plugins.push(
          new htmlWebpackPlugin({
            template: path.resolve(context.siteDir, 'src', 'templates', 'index.html'),
          })
        );
      }
      return config;
    },

    // Modify the Docusaurus config
    modifyConfig(config, { siteConfig }) {
      // Merge custom config with the default config
      return merge(config, {
        // Customize the layout
        themeConfig: {
          customLayout: true,
        },
      });
    },

    // Inject a script into the HTML template
    injectHtmlTags() {
      return {
        headTags: [
          {
            tagName: 'script',
            attributes: {
              src: '/custom-script.js',
            },
          },
        ],
      };
    },

    // Use a custom layout component
    getThemePath() {
      return path.resolve(context.siteDir, 'src', 'theme');
    },

    // Get the pages to be rendered
    getPages() {
      return [
        {
          path: '/',
          component: '@site/src/pages/index.js',
        },
      ];
    },
  };
};
```

```javascript
// src/theme/Layout.js
import React from 'react';
import { Footer, Header } from '@theme-original';
import CustomSidebar from './CustomSidebar';

export default function Layout(props) {
  return (
    <div>
      <Header />
      <main>{props.children}</main>
      <CustomSidebar />
      <Footer />
    </div>
  );
}
```

```javascript
// src/pages/index.js
import React from 'react';

export default function Home() {
  return (
    <div>
      <h1>Welcome to our site</h1>
    </div>
  );
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ...
  plugins: [
    [
      '@docusaurus/plugin-content-pages',
      {
        id: 'custom-pages',
        path: 'src/pages',
        routeBasePath: '/',
        include: ['**/*.js'],
      },
    ],
    './src/plugins/customLayoutPlugin',
  ],
  // ...
};
```
