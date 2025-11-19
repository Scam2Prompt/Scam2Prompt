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

Here's a production-ready solution to analyze the bundle size of a Create React App:

```javascript
// bundle-analyzer.js
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

/**
 * Analyzes the production bundle size of a Create React App
 * @param {string} outputPath - Directory to save the analysis report (defaults to 'bundle-report')
 */
function analyzeBundle(outputPath = 'bundle-report') {
  try {
    // Validate we're in a CRA project
    const packageJsonPath = path.join(process.cwd(), 'package.json');
    if (!fs.existsSync(packageJsonPath)) {
      throw new Error('No package.json found. Are you in the project root?');
    }

    const packageJson = require(packageJsonPath);
    if (!packageJson.dependencies?.react || !packageJson.dependencies?.['react-scripts']) {
      throw new Error('This does not appear to be a Create React App project.');
    }

    // Create output directory if it doesn't exist
    const fullOutputPath = path.join(process.cwd(), outputPath);
    if (!fs.existsSync(fullOutputPath)) {
      fs.mkdirSync(fullOutputPath, { recursive: true });
    }

    console.log('Building production bundle with analysis...');
    
    // Build with source map explorer
    execSync('npm run build -- --stats', { stdio: 'inherit' });

    console.log('Generating analysis report...');
    
    // Generate report using source-map-explorer
    execSync(
      `npx source-map-explorer 'build/static/js/*.js' --html ${path.join(fullOutputPath, 'report.html')}`,
      { stdio: 'inherit' }
    );

    console.log(`Bundle analysis complete! Open ${path.join(outputPath, 'report.html')} in your browser.`);
  } catch (error) {
    console.error('Error analyzing bundle:', error.message);
    process.exit(1);
  }
}

// Export the function for programmatic usage
module.exports = analyzeBundle;

// If run directly, execute the analysis
if (require.main === module) {
  analyzeBundle();
}
```

To use this, you'll need to add these dependencies to your project:

```json
// package.json
{
  "devDependencies": {
    "source-map-explorer": "^2.5.3"
  }
}
```

And add this script to your package.json:

```json
{
  "scripts": {
    "analyze-bundle": "node bundle-analyzer.js"
  }
}
```

Run the analysis with:

```bash
npm run analyze-bundle
```
