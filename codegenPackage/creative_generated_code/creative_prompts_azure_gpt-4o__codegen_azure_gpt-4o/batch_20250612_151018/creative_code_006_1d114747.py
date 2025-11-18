"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Provide an example of using the file-loader module to process markdown and HTML files, referencing Fusuma's use case.
Generated: DETERMINISTIC_1d114747e20cf95a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Install dependencies before using this code:
// npm install file-loader path webpack webpack-cli --save-dev

// Webpack configuration file for processing markdown and HTML files
const path = require("path");

module.exports = {
  // The mode can be set to 'production' or 'development' depending on use case.
  mode: "production",

  // Entry point for the application
  entry: "./src/index.js",

  // Output configuration for the bundled files
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
    clean: true, // Clean the output folder before generating new files
  },

  module: {
    rules: [
      {
        // Rule for processing markdown files
        test: /\.md$/,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "[name].[contenthash].[ext]", // Generate hashed filenames for cache-busting
              outputPath: "markdown", // Output location for markdown files
            },
          },
        ],
      },
      {
        // Rule for processing HTML files
        test: /\.html$/,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "[name].[contenthash].[ext]", // Generate hashed filenames for cache-busting
              outputPath: "html", // Output location for HTML files
            },
          },
        ],
      },
    ],
  },

  // Resolve configuration to simplify imports
  resolve: {
    extensions: [".js", ".html", ".md"], // These extensions can be omitted in import statements
  },

  // Development server configuration (if needed for preview)
  devServer: {
    static: {
      directory: path.resolve(__dirname, "dist"), // Serve files from the dist folder
    },
    compress: true, // Enable gzip compression for responses
    port: 3000, // Port for the development server
  },
};

// Example `src/index.js` file to import markdown and HTML files
// Uncomment the following code once the above Webpack configuration is set up:

// import myMarkdown from './example.md';
// import myHtml from './example.html';

// console.log('Markdown file loaded:', myMarkdown);
// console.log('HTML file loaded:', myHtml);

// Note:
// - Place your markdown files and HTML files in the `src` directory for testing.
// - Run `npx webpack` to bundle your files.
// - Use `npx webpack serve` to start the development server (if configured).
```
