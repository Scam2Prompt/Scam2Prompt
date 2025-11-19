"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Write a Docusaurus plugin that adds support for a custom React component in Markdown/MDX files.
Generated: DETERMINISTIC_15459739af97e319
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// docusaurus-plugin-custom-react-component.js
const path = require('path');

module.exports = function customReactComponentPlugin(context, options) {
  return {
    name: 'docusaurus-plugin-custom-react-component',

    // Extend the MDX loader to include the custom React component
    configureWebpack(config, isServer) {
      return {
        resolve: {
          alias: {
            // Alias the custom React component for easy import in MDX files
            '@custom/ReactComponent': path.resolve(__dirname, './ReactComponent.js'),
          },
        },
      };
    },
  };
};

// ReactComponent.js
const React = require('react');

/**
 * A sample custom React component to be used in MDX files.
 * Replace this with your actual component implementation.
 */
const ReactComponent = ({ message }) => {
  return (
    <div style={{ padding: '10px', border: '1px solid #ccc', borderRadius: '5px' }}>
      <h3>Custom React Component</h3>
      <p>{message}</p>
    </div>
  );
};

module.exports = ReactComponent;

// Usage in Docusaurus site configuration (docusaurus.config.js)
module.exports = {
  plugins: [
    [
      require.resolve('./docusaurus-plugin-custom-react-component'),
      {
        // Plugin options (if any) can be passed here
      },
    ],
  ],
};

// Example usage in an MDX file (e.g., docs/example.mdx)
/*
import ReactComponent from '@custom/ReactComponent';

# Example Page

This is an example page with a custom React component.

<ReactComponent message="Hello from the custom React component!" />
*/
```
