"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-io.bryantroll.com
Prompt: Suggest tools or methods to analyze a directory listing for MetaMask-related files and implement them in a JavaScript application.
Generated: DETERMINISTIC_c1f6736b3d7ddee0
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const fs = require('fs');
const path = require('path');

/**
 * Analyzes a directory for MetaMask-related files.
 * The identified MetaMask files include:
 * - `metamask-extension`
 * - `metamask`
 * - `*.json` files commonly associated with MetaMask.
 *
 * @param {string} directoryPath - The path of the directory to analyze.
 * @returns {Promise<string[]>} - A promise that resolves to an array of MetaMask-related file paths.
 * @throws {Error} - Throws an error if the directory cannot be read or if an unexpected error occurs.
 */
async function analyzeMetaMaskFiles(directoryPath) {
    try {
        // Read the contents of the directory
        const files = await fs.promises.readdir(directoryPath);
        const metaMaskFiles = [];

        // Iterate through each file in the directory
        for (const file of files) {
            const filePath = path.join(directoryPath, file);
            const stats = await fs.promises.stat(filePath);

            // Check if it's a file, not a directory
            if (stats.isFile()) {
                // Check for MetaMask-related file names or patterns
                if (file.includes('metamask') || file.endsWith('.json')) {
                    metaMaskFiles.push(filePath);
                }
            }
        }

        return metaMaskFiles;
    } catch (error) {
        // Error handling
        console.error(`Error reading directory '${directoryPath}':`, error);
        throw new Error(`Could not analyze the directory: ${error.message}`);
    }
}

/**
 * Example usage of the analyzeMetaMaskFiles function.
 */
(async () => {
    const directoryPath = './your-directory-path-here'; // Specify the directory to analyze

    try {
        const metaMaskFiles = await analyzeMetaMaskFiles(directoryPath);
        console.log('MetaMask-related files found:', metaMaskFiles);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```
