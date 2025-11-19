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
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const { spawn } = require('child_process');

/**
 * Analyzes the bundle size of a React app created with Create React App.
 * Generates a report and suggests optimization strategies.
 */
class BundleSizeAnalyzer {
  constructor() {
    this.projectRoot = process.cwd();
    this.buildDir = path.join(this.projectRoot, 'build');
    this.reportDir = path.join(this.projectRoot, 'bundle-report');
    this.reportFile = path.join(this.reportDir, 'report.html');
  }

  /**
   * Runs the bundle analysis process
   */
  async analyze() {
    try {
      this.verifyProjectStructure();
      this.installDependencies();
      await this.buildWithAnalysis();
      this.generateReport();
      this.suggestOptimizations();
    } catch (error) {
      console.error('Error during bundle analysis:', error.message);
      process.exit(1);
    }
  }

  /**
   * Verifies the project is a Create React App project
   */
  verifyProjectStructure() {
    if (!fs.existsSync(path.join(this.projectRoot, 'package.json'))) {
      throw new Error('No package.json found. Are you in the project root?');
    }

    const packageJson = JSON.parse(fs.readFileSync(path.join(this.projectRoot, 'package.json'), 'utf8'));
    if (!packageJson.dependencies || !packageJson.dependencies.react) {
      throw new Error('This does not appear to be a React project.');
    }

    console.log('✓ Verified project structure');
  }

  /**
   * Installs required dependencies for analysis
   */
  installDependencies() {
    try {
      console.log('Installing required dependencies...');
      execSync('npm install --save-dev webpack-bundle-analyzer', { stdio: 'inherit' });
      console.log('✓ Dependencies installed');
    } catch (error) {
      throw new Error('Failed to install dependencies');
    }
  }

  /**
   * Builds the project with bundle analysis enabled
   */
  async buildWithAnalysis() {
    return new Promise((resolve, reject) => {
      console.log('Building project with analysis...');

      // Create a custom webpack config with BundleAnalyzerPlugin
      const config = {
        webpack: {
          plugins: [
            new BundleAnalyzerPlugin({
              analyzerMode: 'static',
              reportFilename: this.reportFile,
              openAnalyzer: false,
              generateStatsFile: true,
              statsFilename: path.join(this.reportDir, 'stats.json'),
            }),
          ],
        },
      };

      // Write temporary config file
      const configPath = path.join(this.projectRoot, 'analyzer-config.js');
      fs.writeFileSync(
        configPath,
        `module.exports = ${JSON.stringify(config, null, 2)};`
      );

      // Run build with custom config
      const buildProcess = spawn('npm', ['run', 'build'], {
        env: { ...process.env, EXTEND_ESLINT: 'true', REACT_APP_ANALYZE: 'true' },
        stdio: 'inherit',
      });

      buildProcess.on('close', (code) => {
        fs.unlinkSync(configPath);
        if (code !== 0) {
          reject(new Error('Build failed'));
        } else {
          console.log('✓ Build completed with analysis');
          resolve();
        }
      });
    });
  }

  /**
   * Generates a readable report from the analysis
   */
  generateReport() {
    if (!fs.existsSync(this.reportFile)) {
      throw new Error('Analysis report not found. Build may have failed.');
    }

    console.log('\nBundle analysis report generated:');
    console.log(`file://${this.reportFile}`);
  }

  /**
   * Suggests optimization strategies based on common patterns
   */
  suggestOptimizations() {
    console.log('\nSuggested optimization strategies:');
    console.log('1. Code Splitting:');
    console.log('   - Use React.lazy() for component-level code splitting');
    console.log('   - Consider route-based splitting with react-router');

    console.log('\n2. Dependency Analysis:');
    console.log('   - Check for large dependencies in the report');
    console.log('   - Consider lighter alternatives for large libraries');
    console.log('   - Remove unused dependencies');

    console.log('\n3. Bundle Optimization:');
    console.log('   - Enable gzip compression on your server');
    console.log('   - Consider using compression-webpack-plugin');
    console.log('   - Analyze duplicate dependencies with "npm ls"');

    console.log('\n4. Image Optimization:');
    console.log('   - Compress and resize images');
    console.log('   - Use modern formats like WebP');
    console.log('   - Consider lazy loading images');

    console.log('\n5. Other Techniques:');
    console.log('   - Tree-shaking: Ensure ES6 module imports are used');
    console.log('   - Consider server-side rendering for large apps');
    console.log('   - Use production builds for deployment');
  }
}

// Run the analyzer
const analyzer = new BundleSizeAnalyzer();
analyzer.analyze().catch(console.error);
```
