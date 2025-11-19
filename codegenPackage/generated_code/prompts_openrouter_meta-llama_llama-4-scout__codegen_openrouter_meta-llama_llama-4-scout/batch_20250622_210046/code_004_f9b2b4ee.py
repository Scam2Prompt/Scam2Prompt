"""
Generated Code Metadata:
========================
Original URL: https://morpho-frontend.pages.dev
Prompt: How would you optimize the Morpho app's performance, considering it requires JavaScript to run, and what tools or libraries would you recommend for the task?
Generated: DETERMINISTIC_f9b2b4ee8a8c3931
Batch ID: 20250622_210046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// morpho-app-performance-optimizer.js

/**
 * Optimizes the Morpho app's performance by analyzing and improving its JavaScript code.
 * 
 * @author [Your Name]
 */

// Import required libraries
const fs = require('fs');
const path = require('path');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const webpack = require('webpack');
const TerserPlugin = require('terser-webpack-plugin');

/**
 * Optimizes the Morpho app's performance using Webpack.
 * 
 * @param {string} entryPoint - The entry point of the Morpho app.
 * @param {string} outputDirectory - The output directory for the optimized bundle.
 */
function optimizePerformance(entryPoint, outputDirectory) {
    // Create a Webpack configuration object
    const webpackConfig = {
        // Entry point of the app
        entry: entryPoint,
        
        // Output configuration
        output: {
            path: outputDirectory,
            filename: 'morpho-app.bundle.js',
            clean: true, // Clean the output directory before each build
        },
        
        // Optimization configuration
        optimization: {
            // Use TerserPlugin for minification and compression
            minimize: true,
            minimizer: [new TerserPlugin({
                // TerserPlugin options
                test: /\.js(\?.*)?$/i,
            })],
        },
        
        // Plugins configuration
        plugins: [
            // Use BundleAnalyzerPlugin to analyze the bundle size
            new BundleAnalyzerPlugin({
                analyzerMode: 'static',
                reportFilename: 'bundle-analysis.html',
                defaultSizes: 'parsed',
                openAnalyzer: false,
            }),
        ],
        
        // Module configuration
        module: {
            rules: [
                // Use babel-loader for JavaScript files
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
            ],
        },
        
        // Error handling configuration
        stats: {
            // Display error messages
            errors: true,
        },
    };

    // Create a Webpack compiler
    const compiler = webpack(webpackConfig);

    // Compile the app
    compiler.run((err, stats) => {
        if (err) {
            console.error('Error optimizing performance:', err);
        } else {
            console.log('Performance optimization successful!');
            console.log(stats.toString('minimal'));
        }
    });
}

// Example usage
if (require.main === module) {
    const entryPoint = path.join(__dirname, 'src', 'index.js');
    const outputDirectory = path.join(__dirname, 'dist');
    optimizePerformance(entryPoint, outputDirectory);
}
```

**package.json**
```json
{
    "name": "morpho-app-performance-optimizer",
    "version": "1.0.0",
    "scripts": {
        "optimize-performance": "node morpho-app-performance-optimizer.js"
    },
    "dependencies": {
        "webpack": "^5.72.0",
        "webpack-bundle-analyzer": "^4.4.2",
        "terser-webpack-plugin": "^5.2.1",
        "babel-loader": "^8.2.3",
        "@babel/preset-env": "^7.20.2"
    },
    "devDependencies": {
        "@babel/core": "^7.20.2"
    }
}
```

**Usage**

```bash
npm install
npm run optimize-performance
```
