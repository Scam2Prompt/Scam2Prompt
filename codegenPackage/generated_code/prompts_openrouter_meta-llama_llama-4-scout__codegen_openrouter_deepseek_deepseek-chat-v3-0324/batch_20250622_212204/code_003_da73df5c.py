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
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = (env, argv) => {
  const isProduction = argv.mode === 'production';

  return {
    entry: {
      main: './src/main.js',
      // Split vendor bundles
      vendor: ['lodash', 'axios'],
    },
    output: {
      filename: isProduction ? '[name].[contenthash].js' : '[name].js',
      path: path.resolve(__dirname, 'public/dist'),
      publicPath: '/dist/',
    },
    optimization: {
      splitChunks: {
        chunks: 'all',
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name: 'vendors',
            chunks: 'all',
          },
        },
      },
      runtimeChunk: 'single',
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env'],
            },
          },
        },
        {
          test: /\.css$/,
          use: [
            isProduction ? MiniCssExtractPlugin.loader : 'style-loader',
            'css-loader',
            'postcss-loader',
          ],
        },
      ],
    },
    plugins: [
      new CleanWebpackPlugin(),
      new MiniCssExtractPlugin({
        filename: isProduction ? '[name].[contenthash].css' : '[name].css',
      }),
      ...(isProduction ? [new BundleAnalyzerPlugin({ analyzerMode: 'static' })] : []),
    ],
    devtool: isProduction ? 'source-map' : 'eval-cheap-module-source-map',
  };
};

// src/main.js
import('./lazy-module').then((module) => {
  module.init();
}).catch((error) => {
  console.error('Error loading lazy module:', error);
});

// Shopware lazy loading for product listings
document.addEventListener('DOMContentLoaded', () => {
  const productListingObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        import('./product-listing').then((module) => {
          module.initProductListing(entry.target);
        }).catch((error) => {
          console.error('Error loading product listing:', error);
        });
        productListingObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.product-listing-container').forEach((container) => {
    productListingObserver.observe(container);
  });
});

// src/product-listing.js
export function initProductListing(container) {
  // Initialize product listing functionality
  console.log('Product listing initialized for:', container);
}

// src/lazy-module.js
export function init() {
  console.log('Lazy module initialized');
}
```
