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
// Import required libraries
const solidityCoverage = require('solidity-coverage');
const fs = require('fs');
const path = require('path');

/**
 * Judge AI Code Linter
 * 
 * This tool analyzes smart contracts using Solidity-coverage.
 */

// Define the linter class
class CodeLinter {
  /**
   * Initialize the linter with the contract path and config.
   * 
   * @param {string} contractPath - Path to the smart contract.
   * @param {object} config - Configuration for the linter.
   */
  constructor(contractPath, config) {
    this.contractPath = contractPath;
    this.config = config;
  }

  /**
   * Run the linter and generate a report.
   * 
   * @returns {Promise<object>} A promise resolving to the report.
   */
  async lint() {
    try {
      // Check if the contract path exists
      if (!fs.existsSync(this.contractPath)) {
        throw new Error(`Contract path does not exist: ${this.contractPath}`);
      }

      // Run solidity-coverage
      const report = await solidityCoverage(this.contractPath, this.config);

      // Return the report
      return report;
    } catch (error) {
      // Handle any errors that occur during linting
      console.error(`Error linting contract: ${error.message}`);
      throw error;
    }
  }

  /**
   * Generate a markdown report from the linting results.
   * 
   * @param {object} report - The report from the linting process.
   * @returns {string} A markdown string representing the report.
   */
  generateMarkdownReport(report) {
    // Create a markdown string
    let markdown = '# Judge AI Code Linter Report\n\n';

    // Add a summary section
    markdown += '## Summary\n\n';
    markdown += `* Total files: ${report.files.length}\n`;
    markdown += `* Total lines: ${report.lines.length}\n`;
    markdown += `* Uncovered lines: ${report.uncoveredLines.length}\n\n`;

    // Add a files section
    markdown += '## Files\n\n';
    report.files.forEach((file) => {
      markdown += `* ${file.file} - ${file.lines.length} lines, ${file.uncoveredLines.length} uncovered\n`;
    });

    // Return the markdown string
    return markdown;
  }
}

// Define the main function
async function main() {
  // Define the contract path and config
  const contractPath = path.join(__dirname, 'contracts', 'ExampleContract.sol');
  const config = {
    // Add your config options here
  };

  // Create a new linter
  const linter = new CodeLinter(contractPath, config);

  // Run the linter
  const report = await linter.lint();

  // Generate a markdown report
  const markdownReport = linter.generateMarkdownReport(report);

  // Save the markdown report to a file
  fs.writeFileSync('lint-report.md', markdownReport);

  // Print a success message
  console.log('Linting complete. Report saved to lint-report.md');
}

// Run the main function
main().catch((error) => {
  console.error(`Error: ${error.message}`);
  process.exit(1);
});
```
