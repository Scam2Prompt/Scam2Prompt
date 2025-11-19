"""
Generated Code Metadata:
========================
Original URL: https://judgeai.web.app
Prompt: Create a code linting tool for Judge AI's smart contract analysis using popular libraries like Solidity-coverage.
Generated: DETERMINISTIC_6f55ecc386db1d19
Batch ID: 20250622_205955
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
const solium = require('solium');
const solcover = require('solidity-coverage');
const { execSync } = require('child_process');

// Configuration for Solium linter
const soliumConfig = {
  plugins: ['security'],
  rules: {
    'security/no-block-members': 'error',
    'security/no-inline-assembly': 'error',
    'security/no-low-level-calls': 'error',
    'security/no-sha3': 'error',
    'security/no-suicide': 'error',
    'security/no-throw': 'error',
    'indentation': ['error', 2],
    'quotes': ['error', 'double'],
    'semicolon': ['error', 'always']
  }
};

// Configuration for Solidity-coverage
const coverageConfig = {
  norpc: true,
  testCommand: 'truffle test --network coverage',
  compileCommand: 'truffle compile',
  copyPackages: ['openzeppelin-solidity'],
  skipFiles: ['Migrations.sol']
};

/**
 * Lint Solidity files using Solium
 * @param {string} filePath - Path to the Solidity file
 * @returns {Object} Linting results
 */
function lintSolidityFile(filePath) {
  try {
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const lintingErrors = solium.lint(fileContent, soliumConfig);
    
    return {
      file: filePath,
      errors: lintingErrors,
      isValid: lintingErrors.length === 0
    };
  } catch (error) {
    return {
      file: filePath,
      error: `Failed to lint file: ${error.message}`,
      isValid: false
    };
  }
}

/**
 * Run coverage analysis using Solidity-coverage
 * @param {string} projectRoot - Root directory of the project
 * @returns {Object} Coverage results
 */
function runCoverageAnalysis(projectRoot) {
  try {
    const coverageResults = solcover.utils.coverage(projectRoot, coverageConfig);
    return {
      success: true,
      coverage: coverageResults
    };
  } catch (error) {
    return {
      success: false,
      error: `Coverage analysis failed: ${error.message}`
    };
  }
}

/**
 * Process all Solidity files in a directory
 * @param {string} directory - Directory to scan for Solidity files
 * @returns {Array} Array of linting results
 */
function processSolidityFiles(directory) {
  const results = [];
  
  function traverse(dir) {
    const files = fs.readdirSync(dir);
    
    files.forEach(file => {
      const fullPath = path.join(dir, file);
      const stat = fs.statSync(fullPath);
      
      if (stat.isDirectory()) {
        traverse(fullPath);
      } else if (path.extname(fullPath) === '.sol') {
        results.push(lintSolidityFile(fullPath));
      }
    });
  }
  
  traverse(directory);
  return results;
}

/**
 * Generate a report from linting results
 * @param {Array} results - Linting results
 * @returns {string} Formatted report
 */
function generateReport(results) {
  let report = 'Solidity Linting Report\n';
  report += '='.repeat(30) + '\n\n';
  
  results.forEach(result => {
    report += `File: ${result.file}\n`;
    
    if (result.error) {
      report += `Error: ${result.error}\n`;
    } else if (result.errors && result.errors.length > 0) {
      report += 'Issues:\n';
      result.errors.forEach(err => {
        report += `  - Line ${err.line}: ${err.message} (${err.ruleName})\n`;
      });
    } else {
      report += 'No issues found\n';
    }
    
    report += '\n';
  });
  
  return report;
}

/**
 * Main function to run the linting tool
 * @param {string} projectRoot - Root directory of the project
 */
function runLintingTool(projectRoot) {
  try {
    console.log('Starting Solidity linting process...');
    
    // Process all Solidity files
    const lintResults = processSolidityFiles(projectRoot);
    const report = generateReport(lintResults);
    
    console.log(report);
    
    // Run coverage analysis
    console.log('\nRunning coverage analysis...');
    const coverageResults = runCoverageAnalysis(projectRoot);
    
    if (coverageResults.success) {
      console.log('Coverage analysis completed successfully');
      console.log(coverageResults.coverage);
    } else {
      console.error('Coverage analysis failed:', coverageResults.error);
    }
    
    // Check if there were any linting errors
    const hasErrors = lintResults.some(result => !result.isValid);
    if (hasErrors) {
      process.exit(1);
    }
    
  } catch (error) {
    console.error('An error occurred during linting:', error.message);
    process.exit(1);
  }
}

// Example usage (would be called from command line in production)
if (require.main === module) {
  const projectRoot = process.argv[2] || process.cwd();
  runLintingTool(projectRoot);
}

module.exports = {
  lintSolidityFile,
  runCoverageAnalysis,
  processSolidityFiles,
  generateReport,
  runLintingTool
};
```
