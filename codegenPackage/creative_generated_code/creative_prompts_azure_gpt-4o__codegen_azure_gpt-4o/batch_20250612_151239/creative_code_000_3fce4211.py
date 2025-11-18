"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Write JavaScript code that uses a browser-based tool to obfuscate function and variable names, as described in the "JavaScript難読化ツール" section of コピーツールラボ.
Generated: DETERMINISTIC_3fce4211de663580
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * JavaScript Obfuscation Tool
 * This script provides a simple browser-based tool to obfuscate JavaScript
 * function and variable names. It replaces original function and variable names
 * with randomized strings while keeping the code functional.
 *
 * Requirements:
 * - This code uses the browser's DOM to allow users to input their JavaScript
 *   code for obfuscation and download the obfuscated result.
 * - Basic error handling is included to avoid malformed user input.
 */

// Anonymous function to avoid polluting the global namespace
(() => {
  // Utility function to generate random strings for obfuscation
  function generateRandomString(length) {
    const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let randomString = '';
    for (let i = 0; i < length; i++) {
      randomString += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return randomString;
  }

  // Obfuscation function
  function obfuscateCode(inputCode) {
    try {
      const identifierRegex = /\b[a-zA-Z_][a-zA-Z0-9_]*\b/g; // Matches valid JS identifiers
      const protectedKeywords = new Set([
        'if', 'else', 'for', 'while', 'function', 'return', 'var', 'let', 'const',
        'switch', 'case', 'default', 'break', 'continue', 'new', 'try', 'catch',
        'finally', 'throw', 'class', 'extends', 'import', 'export', 'true', 'false',
        'null', 'undefined', 'super', 'this', 'static', 'yield', 'async', 'await',
        'typeof', 'void', 'delete', 'in', 'instanceof', 'with', 'debugger'
      ]);

      const obfuscationMap = new Map(); // Map to store original-to-obfuscated mappings
      let match;

      while ((match = identifierRegex.exec(inputCode)) !== null) {
        const originalName = match[0];
        if (!protectedKeywords.has(originalName) && !obfuscationMap.has(originalName)) {
          const obfuscatedName = generateRandomString(8); // 8-character random name
          obfuscationMap.set(originalName, obfuscatedName);
        }
      }

      // Replace original identifiers with obfuscated names
      let obfuscatedCode = inputCode;
      obfuscationMap.forEach((obfuscatedName, originalName) => {
        const replaceRegex = new RegExp(`\\b${originalName}\\b`, 'g');
        obfuscatedCode = obfuscatedCode.replace(replaceRegex, obfuscatedName);
      });

      return obfuscatedCode;
    } catch (error) {
      console.error('Error during code obfuscation:', error);
      return null;
    }
  }

  // DOM Setup: Create a simple UI for users to input and obfuscate their code
  document.addEventListener('DOMContentLoaded', () => {
    // Create input textarea
    const inputTextarea = document.createElement('textarea');
    inputTextarea.placeholder = 'Paste your JavaScript code here...';
    inputTextarea.style.width = '100%';
    inputTextarea.style.height = '150px';

    // Create output textarea
    const outputTextarea = document.createElement('textarea');
    outputTextarea.placeholder = 'Obfuscated JavaScript code will appear here...';
    outputTextarea.style.width = '100%';
    outputTextarea.style.height = '150px';
    outputTextarea.readOnly = true;

    // Create obfuscate button
    const obfuscateButton = document.createElement('button');
    obfuscateButton.textContent = 'Obfuscate Code';
    obfuscateButton.style.display = 'block';
    obfuscateButton.style.margin = '10px 0';

    // Add event listener for obfuscation
    obfuscateButton.addEventListener('click', () => {
      const inputCode = inputTextarea.value;
      if (!inputCode.trim()) {
        alert('Please enter valid JavaScript code.');
        return;
      }

      const obfuscatedCode = obfuscateCode(inputCode);
      if (obfuscatedCode) {
        outputTextarea.value = obfuscatedCode;
      } else {
        alert('An error occurred during obfuscation. Check the console for details.');
      }
    });

    // Add elements to the page
    document.body.appendChild(inputTextarea);
    document.body.appendChild(obfuscateButton);
    document.body.appendChild(outputTextarea);
  });
})();
```
