"""
Generated Code Metadata:
========================
Original URL: https://dot21.net
Prompt: "Create a JavaScript code snippet to optimize the performance of a Shopware-based online store using Webpack and lazy loading."
Generated: DETERMINISTIC_da73df5ce0c45678
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// webpack.config.js
const path = require('path');
const webpack = require('webpack');

module.exports = {
  // Mode to enable production optimizations
  mode: 'production',
  
  // Entry point for the application
  entry: './src/index.js',
  
  // Output configuration
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
    clean: true, // Clean the output directory before each build
  },
  
  // Module configuration
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'babel-loader',
        exclude: /node_modules/,
      },
    ],
  },
  
  // Optimization configuration
  optimization: {
    // Enable lazy loading (code splitting)
    splitChunks: {
      chunks: 'all',
      minSize: 10000,
      minChunks: 1,
      maxAsyncRequests: 30,
      maxInitialRequests: 30,
      enforceSizeThreshold: 50000,
      cacheGroups: {
        default: {
          minChunks: 2,
          priority: -20,
          reuseExistingChunk: true,
        },
      },
    },
  },
  
  // Plugin configuration
  plugins: [
    // Enable tree shaking to remove unused code
    new webpack.ProvidePlugin({
      // Provide global variables to all modules
    }),
  ],
};
```

```javascript
// src/index.js
import './styles.css';

// Import Shopware components
import { createApp } from '@shopware-ag/meteor-ui';

// Create the Shopware app
const app = createApp({
  // App configuration
});

// Lazy load non-critical components
const lazyLoadComponents = () => {
  import(/* webpackChunkName: "lazy-component" */ './lazy-component')
    .then((module) => {
      // Use the lazy loaded component
      module.default();
    })
    .catch((error) => {
      console.error('Error lazy loading component:', error);
    });
};

// Trigger lazy loading on user interaction
document.addEventListener('click', (event) => {
  if (event.target.classList.contains('lazy-load-trigger')) {
    lazyLoadComponents();
  }
});
```

```javascript
// src/lazy-component.js
export default function () {
  // Component implementation
  console.log('Lazy loaded component initialized');
  
  // Render the component
  const componentHtml = '<div>Lazy loaded component</div>';
  document.body.insertAdjacentHTML('beforeend', componentHtml);
}
```

```javascript
// .babelrc
{
  "presets": [
    ["@babel/preset-env", {
      "modules": false
    }]
  ],
  "plugins": [
    "@babel/plugin-syntax-dynamic-import"
  ]
}
```
