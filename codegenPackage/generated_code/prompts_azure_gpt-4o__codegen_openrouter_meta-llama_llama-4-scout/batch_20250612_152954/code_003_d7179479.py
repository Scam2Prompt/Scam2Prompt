"""
Generated Code Metadata:
========================
Original URL: https://sonic-explorer.skavel.cz
Prompt: Write code to troubleshoot JavaScript compatibility issues when using Sonic Explorer for audio exploration.
Generated: DETERMINISTIC_d717947936c819f7
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// sonic-explorer-troubleshooter.js

/**
 * Troubleshoots JavaScript compatibility issues with Sonic Explorer.
 * @author [Your Name]
 */

// Define the SonicExplorerTroubleshooter class
class SonicExplorerTroubleshooter {
  /**
   * Initializes the troubleshooter.
   * @param {Object} sonicExplorer - The Sonic Explorer instance.
   */
  constructor(sonicExplorer) {
    this.sonicExplorer = sonicExplorer;
  }

  /**
   * Checks if the browser supports the required features.
   * @returns {Boolean} True if the browser is compatible, false otherwise.
   */
  checkBrowserCompatibility() {
    try {
      // Check if the browser supports Web Audio API
      if (!window.AudioContext) {
        throw new Error('Web Audio API is not supported');
      }

      // Check if the browser supports Web Workers
      if (!window.Worker) {
        throw new Error('Web Workers are not supported');
      }

      // Check if the browser supports ES6 modules
      if (!window.Promise) {
        throw new Error('ES6 modules are not supported');
      }

      return true;
    } catch (error) {
      console.error('Browser compatibility check failed:', error.message);
      return false;
    }
  }

  /**
   * Troubleshoots common issues with Sonic Explorer.
   * @returns {Object} An object containing issue descriptions and solutions.
   */
  troubleshootCommonIssues() {
    const issues = {};

    // Check for audio context issues
    if (!this.sonicExplorer.audioContext) {
      issues.audioContext = {
        description: 'Audio context is not initialized',
        solution: 'Recreate the audio context or reload the page',
      };
    }

    // Check for worker issues
    if (!this.sonicExplorer.worker) {
      issues.worker = {
        description: 'Web worker is not initialized',
        solution: 'Recreate the web worker or reload the page',
      };
    }

    // Check for module loading issues
    if (!this.sonicExplorer.modulesLoaded) {
      issues.modulesLoaded = {
        description: 'ES6 modules are not loaded',
        solution: 'Reload the page or check module imports',
      };
    }

    return issues;
  }

  /**
   * Logs information about the Sonic Explorer instance.
   */
  logSonicExplorerInfo() {
    console.log('Sonic Explorer instance:', this.sonicExplorer);
    console.log('Audio context:', this.sonicExplorer.audioContext);
    console.log('Web worker:', this.sonicExplorer.worker);
    console.log('Modules loaded:', this.sonicExplorer.modulesLoaded);
  }
}

// Example usage:
try {
  const sonicExplorer = new SonicExplorer(); // Assume SonicExplorer is defined elsewhere
  const troubleshooter = new SonicExplorerTroubleshooter(sonicExplorer);

  if (!troubleshooter.checkBrowserCompatibility()) {
    console.error('Browser is not compatible with Sonic Explorer');
  }

  const issues = troubleshooter.troubleshootCommonIssues();
  if (Object.keys(issues).length > 0) {
    console.log('Common issues detected:');
    Object.keys(issues).forEach((issue) => {
      console.log(`  - ${issues[issue].description}`);
      console.log(`    Solution: ${issues[issue].solution}`);
    });
  }

  troubleshooter.logSonicExplorerInfo();
} catch (error) {
  console.error('Error troubleshooting Sonic Explorer:', error.message);
}
```
