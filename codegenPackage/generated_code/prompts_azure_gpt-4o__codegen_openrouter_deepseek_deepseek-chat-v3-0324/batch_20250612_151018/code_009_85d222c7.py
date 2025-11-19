"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Write a Docusaurus plugin to extend the functionality of the default static site generator.
Generated: DETERMINISTIC_85d222c774c6df8c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Docusaurus plugin to extend the default static site generator functionality
// This plugin adds custom functionality to the build process

const fs = require('fs-extra');
const path = require('path');

/**
 * Docusaurus plugin to extend static site generation.
 * @param {import('@docusaurus/types').LoadContext} context
 * @param {Object} options
 * @param {string} [options.customDir] - Custom directory to process
 * @param {boolean} [options.verbose=false] - Enable verbose logging
 */
function docusaurusStaticSiteGeneratorPlugin(context, options) {
  const { siteDir, generatedFilesDir } = context;
  const { customDir = 'custom', verbose = false } = options || {};

  return {
    name: 'docusaurus-static-site-generator-plugin',

    async loadContent() {
      if (verbose) {
        console.log('Loading custom content...');
      }

      try {
        const customContentPath = path.join(siteDir, customDir);
        if (!(await fs.pathExists(customContentPath))) {
          if (verbose) {
            console.warn(`Custom directory ${customDir} not found`);
          }
          return null;
        }

        const files = await fs.readdir(customContentPath);
        return { files, customContentPath };
      } catch (error) {
        console.error('Error loading custom content:', error);
        throw error;
      }
    },

    async contentLoaded({ content, actions }) {
      if (!content) return;

      if (verbose) {
        console.log('Processing custom content...');
      }

      const { createData, addRoute } = actions;
      const { files, customContentPath } = content;

      try {
        for (const file of files) {
          const filePath = path.join(customContentPath, file);
          const fileContent = await fs.readFile(filePath, 'utf-8');

          // Create data file for each custom content
          const dataPath = await createData(
            `custom-${path.parse(file).name}.json`,
            JSON.stringify({
              content: fileContent,
              metadata: {
                filename: file,
                lastModified: (await fs.stat(filePath)).mtime,
              },
            })
          );

          // Add route for each custom content
          addRoute({
            path: `/custom/${path.parse(file).name}`,
            component: '@site/src/components/CustomContent.js',
            modules: {
              content: dataPath,
            },
            exact: true,
          });
        }
      } catch (error) {
        console.error('Error processing custom content:', error);
        throw error;
      }
    },

    async postBuild({ outDir }) {
      if (verbose) {
        console.log('Running post-build operations...');
      }

      try {
        // Example post-build operation: Copy custom assets to build directory
        const customAssetsPath = path.join(siteDir, 'src', 'custom-assets');
        const buildAssetsPath = path.join(outDir, 'custom-assets');

        if (await fs.pathExists(customAssetsPath)) {
          await fs.copy(customAssetsPath, buildAssetsPath);
          if (verbose) {
            console.log('Custom assets copied to build directory');
          }
        }
      } catch (error) {
        console.error('Error in post-build operations:', error);
        throw error;
      }
    },

    configureWebpack(config, isServer) {
      if (verbose) {
        console.log('Configuring webpack...');
      }

      return {
        // Add custom webpack configuration if needed
        resolve: {
          alias: {
            '@custom': path.resolve(siteDir, 'src/custom'),
          },
        },
      };
    },
  };
}

module.exports = docusaurusStaticSiteGeneratorPlugin;
```
