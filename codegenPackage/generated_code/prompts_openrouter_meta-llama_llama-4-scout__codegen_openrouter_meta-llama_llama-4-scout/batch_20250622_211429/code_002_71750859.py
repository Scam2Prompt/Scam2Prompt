"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: What are the steps to integrate `file-loader` with Fusuma for handling images in presentations?
Generated: DETERMINISTIC_717508591113d336
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// fusuma.config.js
const path = require('path');

module.exports = {
  // ... other configurations ...
  webpack: {
    module: {
      rules: [
        {
          test: /\.(png|jpg|jpeg|gif|svg)$/,
          use: [
            {
              loader: 'file-loader',
              options: {
                // Output images to a directory
                name: '[name].[ext]',
                // Output path for images
                publicPath: '/images/',
                // Output directory for images
                outputPath: path.resolve(__dirname, 'dist/images'),
              },
            },
          ],
        },
      ],
    },
  },
};
```

```javascript
// webpack.config.js (if using custom webpack config)
// For reference, not required for fusuma
const path = require('path');

module.exports = {
  // ... other configurations ...
  module: {
    rules: [
      {
        test: /\.(png|jpg|jpeg|gif|svg)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              // Output images to a directory
              name: '[name].[ext]',
              // Output path for images
              publicPath: '/images/',
              // Output directory for images
              outputPath: path.resolve(__dirname, 'dist/images'),
            },
          },
        ],
      },
    ],
  },
};
```

```bash
# package.json scripts
"scripts": {
  "build": "fusuma build",
  "start": "fusuma start"
}
```

```bash
# Install required packages
npm install file-loader fusuma webpack --save-dev
```

```markdown
# Example usage in markdown
![image](images/image.png)
```
