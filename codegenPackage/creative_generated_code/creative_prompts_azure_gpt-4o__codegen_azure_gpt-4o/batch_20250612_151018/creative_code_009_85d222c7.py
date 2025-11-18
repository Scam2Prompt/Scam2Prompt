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
// Docusaurus plugin to extend the functionality of the default static site generator
const path = require('path');

module.exports = function customPlugin(context, options) {
  return {
    // Specify a unique name for the plugin
    name: 'docusaurus-plugin-custom-static',

    // Extend the content generation phase
    async loadContent() {
      // Custom logic for generating content can be added here
      // Example: Fetch external data or modify existing data
      try {
        const externalData = await fetchExternalData();
        return externalData; // Data to be used in the site generation
      } catch (error) {
        console.error('Error fetching external data:', error);
        return null; // Return null on error
      }
    },

    // Extend the default behavior for managing routes
    async contentLoaded({ content, actions }) {
      const { addRoute } = actions;

      // Example of adding a custom route
      addRoute({
        path: '/custom-page',
        component: path.resolve(__dirname, './customPage.js'),
        exact: true,
      });

      console.log('Custom route added successfully.');
    },

    // Extend the post-build phase
    async postBuild({ outDir }) {
      try {
        // Example: Generate additional static files
        const customFilePath = path.join(outDir, 'custom-data.json');
        const data = { message: 'Hello, world!' };

        require('fs').writeFileSync(customFilePath, JSON.stringify(data, null, 2));
        console.log('Custom file written to:', customFilePath);
      } catch (error) {
        console.error('Error during post-build:', error);
      }
    },
  };
};

// Utility function for external data fetching
async function fetchExternalData() {
  // Simulating external data fetching
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ title: 'External Data Example', content: 'This is fetched externally.' });
    }, 1000);
  });
}
```

Place this file in the `plugins` folder of your Docusaurus project and ensure you add the plugin to your `docusaurus.config.js` file:

```javascript
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  plugins: [
    require.resolve('./plugins/docusaurus-plugin-custom-static'),
  ],
};
```
