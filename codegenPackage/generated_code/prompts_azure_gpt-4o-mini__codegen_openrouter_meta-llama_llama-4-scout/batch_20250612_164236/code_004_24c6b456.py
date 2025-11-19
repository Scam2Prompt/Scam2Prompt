"""
Generated Code Metadata:
========================
Original URL: https://metreniuk.github.io
Prompt: How do I analyze the bundle size of my React application created with Create React App?
Generated: DETERMINISTIC_24c6b4569ca79e61
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// bundle-analyzer.js
const fs = require('fs');
const path = require('path');
const { BundleAnalyzer } = require('webpack-bundle-analyzer');

/**
 * Analyzes the bundle size of a React application created with Create React App.
 * 
 * @param {string} buildPath - The path to the build directory of the React application.
 */
function analyzeBundleSize(buildPath) {
    try {
        // Check if build path exists
        if (!fs.existsSync(buildPath)) {
            throw new Error(`Build path '${buildPath}' does not exist.`);
        }

        // Get the stats file path
        const statsFilePath = path.join(buildPath, 'stats.json');

        // Check if stats file exists
        if (!fs.existsSync(statsFilePath)) {
            throw new Error(`Stats file '${statsFilePath}' does not exist. Run 'npm run build' to generate it.`);
        }

        // Read the stats file
        const statsFileContent = fs.readFileSync(statsFilePath, 'utf8');
        const stats = JSON.parse(statsFileContent);

        // Create a bundle analyzer
        const analyzer = new BundleAnalyzer(stats, {
            analyzer: {
                // Open the report in the default browser
                openAnalyzer: true,
            },
        });

        // Start the analysis
        analyzer.startAnalysis();
    } catch (error) {
        console.error('Error analyzing bundle size:', error.message);
        process.exit(1);
    }
}

// Example usage
if (require.main === module) {
    analyzeBundleSize(path.join(__dirname, 'build'));
}
```

```bash
# package.json
"scripts": {
    "analyze:bundle": "node bundle-analyzer.js"
}
```

```javascript
// webpack.config.js (if using a custom webpack config)
// or
// react-app.config.js (if using react-app-rewired)
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = {
    // ... other configurations ...
    plugins: [
        // ... other plugins ...
        new BundleAnalyzerPlugin({
            analyzerMode: 'static',
            reportFilename: 'bundle-analysis.html',
            defaultSizes: 'parsed',
            openAnalyzer: false,
        }),
    ],
};
```

```bash
# Run the analysis
npm run analyze:bundle
```
