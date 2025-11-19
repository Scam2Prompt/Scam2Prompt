"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metreniuk.github.io
Prompt: How do I analyze the bundle size of my React application created with Create React App?
Generated: DETERMINISTIC_24c6b4569ca79e61
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to analyze the bundle size of a React application created with Create React App.
 *
 * This script uses the `source-map-explorer` package to analyze the bundle size.
 * Make sure to install `source-map-explorer` as a dev dependency:
 * npm install source-map-explorer --save-dev
 *
 * Usage:
 * 1. Build the application: npm run build
 * 2. Run this script: node analyzeBundle.js
 */

const { execSync } = require('child_process');
const path = require('path');

try {
  // Path to the production build folder created by Create React App
  const buildFolder = path.resolve(__dirname, 'build', 'static', 'js');
  
  console.log('Analyzing bundle size...');
  
  // Command to use `source-map-explorer` for analyzing bundle size
  const command = `npx source-map-explorer ${buildFolder}/*.js`;

  // Execute the command and display the analysis output
  const output = execSync(command, { stdio: 'inherit' });
  console.log(output.toString());
  
  console.log('Bundle analysis complete.');
} catch (error) {
  console.error('Error during bundle analysis:', error.message);
  console.error('Make sure you have built the application using `npm run build`.');
}
```
