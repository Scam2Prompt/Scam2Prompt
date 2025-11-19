"""
Generated Code Metadata:
========================
Original URL: https://metreniuk.github.io
Prompt: Write a script to analyze the bundle size of a React app created with Create React App, and suggest ways to optimize it for better performance.
Generated: DETERMINISTIC_41e93dd1a922a846
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// analyzeBundleSize.js
// This script analyzes the bundle size of a React app created with Create React App
// and suggests optimization techniques for better performance.

const fs = require('fs');
const path = require('path');
const gzipSize = require('gzip-size');
const chalk = require('chalk');

// Function to analyze the bundle size
async function analyzeBundleSize(buildDir) {
  try {
    console.log(chalk.blue('Analyzing bundle size...'));

    // Ensure the build directory exists
    if (!fs.existsSync(buildDir)) {
      console.error(chalk.red(`Build directory "${buildDir}" does not exist. Please build your app first.`));
      process.exit(1);
    }

    // Read all files in the build directory
    const files = fs.readdirSync(buildDir);

    // Filter for JavaScript and CSS files
    const bundleFiles = files.filter(file => file.endsWith('.js') || file.endsWith('.css'));

    if (bundleFiles.length === 0) {
      console.error(chalk.red('No JavaScript or CSS files found in the build directory.'));
      process.exit(1);
    }

    let totalSize = 0;
    let totalGzipSize = 0;

    console.log(chalk.green('Bundle size details:'));
    console.log(chalk.green('---------------------'));

    for (const file of bundleFiles) {
      const filePath = path.join(buildDir, file);
      const fileSize = fs.statSync(filePath).size;
      const fileGzipSize = await gzipSize.file(filePath);

      totalSize += fileSize;
      totalGzipSize += fileGzipSize;

      console.log(`${chalk.yellow(file)}:`);
      console.log(`  Original size: ${(fileSize / 1024).toFixed(2)} KB`);
      console.log(`  Gzipped size: ${(fileGzipSize / 1024).toFixed(2)} KB`);
    }

    console.log(chalk.green('---------------------'));
    console.log(chalk.green(`Total original size: ${(totalSize / 1024).toFixed(2)} KB`));
    console.log(chalk.green(`Total gzipped size: ${(totalGzipSize / 1024).toFixed(2)} KB`));

    // Suggest optimization techniques
    console.log(chalk.blue('\nOptimization Suggestions:'));
    console.log(chalk.blue('--------------------------'));
    console.log('- Use code splitting to load only the necessary parts of your app.');
    console.log('- Minify your JavaScript and CSS files.');
    console.log('- Remove unused dependencies and code.');
    console.log('- Use tree-shaking to eliminate dead code.');
    console.log('- Optimize images and use lazy loading.');
    console.log('- Consider using a CDN to serve static assets.');
    console.log('- Enable gzip or Brotli compression on your server.');

  } catch (error) {
    console.error(chalk.red('An error occurred while analyzing the bundle size:'), error.message);
    process.exit(1);
  }
}

// Entry point
const buildDir = path.resolve(__dirname, 'build'); // Default build directory
analyzeBundleSize(buildDir);
```

### Instructions:
1. Save this script as `analyzeBundleSize.js` in your project root directory.
2. Run `npm run build` to generate the production build of your React app.
3. Execute the script using `node analyzeBundleSize.js` to analyze the bundle size and get optimization suggestions.

### Dependencies:
Install the required dependencies before running the script:
```bash
npm install gzip-size chalk
```
