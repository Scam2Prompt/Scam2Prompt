"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Provide an example of using the file-loader module to process markdown and HTML files, referencing Fusuma's use case.
Generated: DETERMINISTIC_1d114747e20cf95a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const path = require('path');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const fileLoader = require('file-loader');

// Define constants
const DIST_DIR = path.resolve(__dirname, 'dist');
const SRC_DIR = path.resolve(__dirname, 'src');

// Define Webpack configuration
module.exports = merge(common, {
  // Define module rules
  module: {
    rules: [
      {
        // Use file-loader for markdown and HTML files
        test: /\.(md|html)$/,
        use: [
          {
            loader: fileLoader,
            options: {
              // Output path for processed files
              name: '[name].[ext]',
              // Output directory for processed files
              outputPath: DIST_DIR,
            },
          },
        ],
      },
    ],
  },

  // Define output configuration
  output: {
    // Output path for bundled files
    path: DIST_DIR,
    // Output filename for bundled files
    filename: 'bundle.js',
  },
});

// Define error handling
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
  process.exit(1);
});
```

```javascript
// webpack.common.js
const path = require('path');

module.exports = {
  // Define entry point
  entry: './src/index.js',

  // Define module configuration
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'babel-loader',
        exclude: /node_modules/,
      },
    ],
  },

  // Define resolve configuration
  resolve: {
    extensions: ['.js', '.json'],
  },
};
```

```javascript
// src/index.js
import markdown from './example.md';
import html from './example.html';

console.log(markdown);
console.log(html);
```

```markdown
// src/example.md
# Fusuma Example
This is an example markdown file.
```

```html
<!-- src/example.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>Fusuma Example</title>
  </head>
  <body>
    <h1>This is an example HTML file.</h1>
  </body>
</html>
```

```json
// package.json
{
  "name": "fusuma-example",
  "version": "1.0.0",
  "scripts": {
    "build": "webpack --mode development"
  },
  "dependencies": {
    "file-loader": "^6.2.0",
    "webpack": "^5.72.0",
    "webpack-merge": "^5.8.0"
  },
  "devDependencies": {
    "@babel/core": "^7.12.10",
    "@babel/preset-env": "^7.12.11",
    "babel-loader": "^8.2.3"
  }
}
```
