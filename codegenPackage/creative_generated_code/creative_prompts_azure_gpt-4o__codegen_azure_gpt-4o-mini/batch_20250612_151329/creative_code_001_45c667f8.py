"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdex-4ld.pages.dev
Prompt: How can I troubleshoot a Webpack-based app that displays an error message about JavaScript being disabled, like the one on https://mdex-4ld.pages.dev?
Generated: DETERMINISTIC_45c667f83c87fbac
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

// Webpack configuration object
module.exports = {
  // Set the mode to development for easier debugging
  mode: 'development',
  
  // Entry point for the application
  entry: './src/index.js',

  // Output configuration
  output: {
    filename: 'bundle.js', // Output bundle filename
    path: path.resolve(__dirname, 'dist'), // Output directory
    publicPath: '/', // Public URL of the output directory
  },

  // Module rules for processing files
  module: {
    rules: [
      {
        // Babel loader for JavaScript transpilation
        test: /\.js$/, // Process .js files
        exclude: /node_modules/, // Exclude node_modules directory
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'], // Use the preset for modern JavaScript
          },
        },
      },
      {
        // CSS loader for stylesheets
        test: /\.css$/, // Process .css files
        use: ['style-loader', 'css-loader'], // Apply loaders
      },
    ],
  },

  // Plugins for additional functionality
  plugins: [
    new CleanWebpackPlugin(), // Cleans up the output directory before each build
    new HtmlWebpackPlugin({
      template: './src/index.html', // Template for the HTML file
      filename: 'index.html', // Output HTML filename
    }),
  ],

  // Development server configuration
  devServer: {
    contentBase: path.join(__dirname, 'dist'), // Serve content from the dist directory
    compress: true, // Enable gzip compression
    port: 9000, // Port for the dev server
    // Display a friendly message if JavaScript is disabled
    before(app) {
      app.get('/js-disabled', (req, res) => {
        res.send(`
          <html>
            <head><title>JavaScript Required</title></head>
            <body>
              <h1>JavaScript is Disabled</h1>
              <p>Please enable JavaScript in your browser settings to use this application.</p>
            </body>
          </html>
        `);
      });
    },
  },

  // Resolve module imports
  resolve: {
    extensions: ['.js'], // Automatically resolve certain extensions
  },

  // Optimization configuration to minimize output for production builds
  optimization: {
    minimize: true, // Minimize output in production mode
  },
};

// Error handling example for Webpack compilation
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection at:', promise, 'reason:', reason);
  // Application specific logging, throwing an error or other logic here
});

// Handle process exit events
process.on('exit', (code) => {
  console.log(`Process exited with code: ${code}`);
});
```
