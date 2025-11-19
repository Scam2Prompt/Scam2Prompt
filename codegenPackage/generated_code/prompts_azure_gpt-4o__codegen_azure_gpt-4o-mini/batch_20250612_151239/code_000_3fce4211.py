"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Write JavaScript code that uses a browser-based tool to obfuscate function and variable names, as described in the "JavaScript難読化ツール" section of コピーツールラボ.
Generated: DETERMINISTIC_3fce4211de663580
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * JavaScript Obfuscator
 * This tool obfuscates function and variable names in a given JavaScript code string.
 * It uses a simple mapping to replace original names with obfuscated names.
 */

class JavaScriptObfuscator {
    constructor() {
        this.nameMap = new Map(); // Map to store original names and their obfuscated counterparts
        this.counter = 0; // Counter to generate unique obfuscated names
    }

    /**
     * Obfuscates the provided JavaScript code.
     * @param {string} code - The JavaScript code to obfuscate.
     * @returns {string} - The obfuscated JavaScript code.
     */
    obfuscate(code) {
        // Regular expression to match variable and function names
        const namePattern = /\b([a-zA-Z_$][0-9a-zA-Z_$]*)\b/g;

        // Replace names in the code using the mapping
        return code.replace(namePattern, (match) => {
            // If the name is already obfuscated, return it
            if (this.nameMap.has(match)) {
                return this.nameMap.get(match);
            }

            // Generate a new obfuscated name
            const obfuscatedName = `obf${this.counter++}`;
            this.nameMap.set(match, obfuscatedName); // Store the mapping
            return obfuscatedName; // Return the obfuscated name
        });
    }

    /**
     * Displays the original and obfuscated names for reference.
     */
    displayNameMapping() {
        console.log("Original Name -> Obfuscated Name:");
        this.nameMap.forEach((value, key) => {
            console.log(`${key} -> ${value}`);
        });
    }
}

// Example usage
try {
    const obfuscator = new JavaScriptObfuscator();
    const originalCode = `
        function myFunction() {
            var myVariable = 10;
            console.log(myVariable);
        }
        myFunction();
    `;

    const obfuscatedCode = obfuscator.obfuscate(originalCode);
    console.log("Obfuscated Code:\n", obfuscatedCode);
    obfuscator.displayNameMapping();
} catch (error) {
    console.error("An error occurred during obfuscation:", error);
}
```
