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
#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

/**
 * Analyze the bundle size of a React app created with Create React App.
 * @param {string} projectPath - Path to the React app project.
 */
function analyzeBundleSize(projectPath) {
  try {
    // Navigate to the project directory
    process.chdir(projectPath);

    // Run the build command to generate the production build
    console.log('Running production build...');
    execSync('npm run build', { stdio: 'inherit' });

    // Get the bundle size
    const bundlePath = path.join(projectPath, 'build', 'static', 'js', 'main.*.js');
    const bundleSize = getFileSize(bundlePath);

    console.log(`Bundle size: ${formatFileSize(bundleSize)}`);

    // Analyze the bundle size and provide suggestions
    const suggestions = analyzeBundle(bundlePath);
    console.log('Suggestions:');
    suggestions.forEach(suggestion => console.log(`- ${suggestion}`));
  } catch (error) {
    console.error('Error analyzing bundle size:', error);
    process.exit(1);
  }
}

/**
 * Get the file size in bytes.
 * @param {string} filePath - Path to the file.
 * @returns {number} File size in bytes.
 */
function getFileSize(filePath) {
  try {
    return fs.statSync(filePath).size;
  } catch (error) {
    console.error(`Error getting file size: ${error}`);
    return 0;
  }
}

/**
 * Format file size in bytes to a human-readable format.
 * @param {number} fileSize - File size in bytes.
 * @returns {string} Formatted file size.
 */
function formatFileSize(fileSize) {
  if (fileSize < 1024) {
    return `${fileSize} B`;
  } else if (fileSize < 1024 * 1024) {
    return `${(fileSize / 1024).toFixed(2)} KB`;
  } else {
    return `${(fileSize / (1024 * 1024)).toFixed(2)} MB`;
  }
}

/**
 * Analyze the bundle and provide suggestions for optimization.
 * @param {string} bundlePath - Path to the bundle file.
 * @returns {string[]} Suggestions for optimization.
 */
function analyzeBundle(bundlePath) {
  // Use a simple regex to detect large libraries
  const largeLibraryRegex = /[a-zA-Z0-9]+\.min\.js/g;
  const largeLibraries = [];
  let match;
  const bundleContent = fs.readFileSync(bundlePath, 'utf8');
  while ((match = largeLibraryRegex.exec(bundleContent)) !== null) {
    largeLibraries.push(match[0]);
  }

  const suggestions = [];
  if (largeLibraries.length > 0) {
    suggestions.push('Consider code splitting or lazy loading for large libraries:');
    largeLibraries.forEach(library => suggestions.push(`- ${library}`));
  }

  // Check for duplicate dependencies
  const dependencies = getDependencies(bundlePath);
  const duplicateDependencies = getDuplicateDependencies(dependencies);
  if (duplicateDependencies.length > 0) {
    suggestions.push('Consider removing duplicate dependencies:');
    duplicateDependencies.forEach(dependency => suggestions.push(`- ${dependency}`));
  }

  return suggestions;
}

/**
 * Get dependencies from the bundle.
 * @param {string} bundlePath - Path to the bundle file.
 * @returns {string[]} Dependencies.
 */
function getDependencies(bundlePath) {
  // Simple regex to detect dependencies
  const dependencyRegex = /import\s+.*?\s+from\s+['"](.*?)['"]/g;
  const dependencies = [];
  let match;
  const bundleContent = fs.readFileSync(bundlePath, 'utf8');
  while ((match = dependencyRegex.exec(bundleContent)) !== null) {
    dependencies.push(match[1]);
  }
  return dependencies;
}

/**
 * Get duplicate dependencies.
 * @param {string[]} dependencies - Dependencies.
 * @returns {string[]} Duplicate dependencies.
 */
function getDuplicateDependencies(dependencies) {
  const dependencyCount = {};
  dependencies.forEach(dependency => {
    if (dependencyCount[dependency]) {
      dependencyCount[dependency]++;
    } else {
      dependencyCount[dependency] = 1;
    }
  });
  return Object.keys(dependencyCount).filter(dependency => dependencyCount[dependency] > 1);
}

// Run the script
if (require.main === module) {
  if (process.argv.length !== 3) {
    console.error('Usage: node bundle-analyzer.js <project-path>');
    process.exit(1);
  }
  analyzeBundleSize(process.argv[2]);
}
```
