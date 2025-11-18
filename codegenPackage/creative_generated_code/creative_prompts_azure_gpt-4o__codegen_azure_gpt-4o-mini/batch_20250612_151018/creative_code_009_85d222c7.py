"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Write a Docusaurus plugin to extend the functionality of the default static site generator.
Generated: DETERMINISTIC_85d222c774c6df8c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// docusaurus-plugin-example.js
const { Plugin } = require('@docusaurus/core');

/**
 * A Docusaurus plugin to extend the functionality of the default static site generator.
 *
 * @param {Object} options - Plugin options
 * @param {string} options.customOption - An example of a custom option to configure plugin behavior
 * @returns {Plugin} The Docusaurus plugin
 */
function createDocusaurusPlugin(options) {
  // Validate options to ensure required parameters are present
  if (!options || typeof options.customOption !== 'string') {
    throw new Error('Invalid options: customOption is required and must be a string.');
  }

  return {
    name: 'docusaurus-plugin-example',

    // The plugin's lifecycle methods
    async onInit({ actions }) {
      // Log plugin initialization
      console.log('Docusaurus Plugin Example initialized with option:', options.customOption);
    },

    async contentLoaded({ content, actions }) {
      const { addRoute } = actions;

      // Example of adding a custom route
      addRoute({
        path: '/custom',
        component: require.resolve('./src/components/CustomComponent'),
        exact: true,
      });

      // Log the loaded content (for debugging purposes)
      console.log('Content loaded:', content);
    },

    // Additional lifecycle methods can be added here
  };
}

module.exports = createDocusaurusPlugin;
```

```javascript
// src/components/CustomComponent.js
import React from 'react';

/**
 * CustomComponent is a simple React component for displaying custom content.
 *
 * @returns {JSX.Element} The rendered component
 */
const CustomComponent = () => {
  return (
    <div>
      <h1>Custom Page</h1>
      <p>This is a custom page added by the Docusaurus plugin!</p>
    </div>
  );
};

export default CustomComponent;
```

```json
// package.json
{
  "name": "docusaurus-plugin-example",
  "version": "1.0.0",
  "main": "docusaurus-plugin-example.js",
  "dependencies": {
    "@docusaurus/core": "^2.0.0"
  }
}
```

Make sure to install the necessary dependencies by running:
```bash
npm install
```

To use the plugin, add it to your Docusaurus configuration file (`docusaurus.config.js`):
```javascript
module.exports = {
  plugins: [
    require('./path/to/docusaurus-plugin-example')({
      customOption: 'Your custom option value',
    }),
  ],
};
```
