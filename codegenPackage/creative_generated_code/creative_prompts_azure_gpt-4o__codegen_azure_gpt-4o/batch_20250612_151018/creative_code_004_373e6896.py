"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to customize the layout by reusing React components while maintaining the default header and footer.
Generated: DETERMINISTIC_373e689617660767
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Docusaurus Plugin: Customize Layout by Reusing React Components
// File: docusaurus-plugin-custom-layout.js

const path = require('path');

module.exports = function customLayoutPlugin(context, options) {
  return {
    // Define the plugin name
    name: 'docusaurus-plugin-custom-layout',
    
    // Specify additional React component files to be used in the layout
    getPathsToWatch() {
      return [path.resolve(__dirname, './components')];
    },
    
    // Extend Docusaurus configuration to include custom React components
    configureWebpack(config, isServer, utils) {
      return {
        resolve: {
          alias: {
            '@custom/components': path.resolve(__dirname, './components'),
          },
        },
      };
    },
    
    // Inject a custom layout file into the Docusaurus build
    async contentLoaded({ actions }) {
      const { addRoute } = actions;

      addRoute({
        path: '*',
        component: '@custom/components/CustomLayout',
        exact: false,
      });
    },
  };
};

// File: components/CustomLayout.js
// Description: Custom layout component reusing Docusaurus header and footer

import React from 'react';
import Layout from '@theme/Layout'; // Default Docusaurus layout
import CustomContent from './CustomContent'; // Custom React content component

const CustomLayout = (props) => {
  return (
    <Layout>
      <CustomContent {...props} />
    </Layout>
  );
};

export default CustomLayout;

// File: components/CustomContent.js
// Description: Example of reusable custom React content component

import React from 'react';

const CustomContent = (props) => {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Welcome to the Customized Layout!</h1>
      <p>This is an example of custom content.</p>
      {/* Render default page content */}
      {props.children}
    </div>
  );
};

export default CustomContent;

// File: index.js
// Description: Entry point for this plugin

module.exports = require('./docusaurus-plugin-custom-layout');
```
