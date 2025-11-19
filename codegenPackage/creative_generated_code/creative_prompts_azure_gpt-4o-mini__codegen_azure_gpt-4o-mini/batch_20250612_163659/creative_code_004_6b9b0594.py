"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Implement a JavaScript obfuscation tool that randomizes function and variable names, based on the features outlined on コピーツールラボ.
Generated: DETERMINISTIC_6b9b059420b9bf46
Batch ID: 20250612_163659
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
 * This tool randomizes function and variable names in a given JavaScript code string.
 * Usage:
 * const obfuscatedCode = obfuscate(inputCode);
 */

class Obfuscator {
    constructor() {
        this.variableMap = new Map();
        this.functionMap = new Map();
        this.variableCounter = 0;
        this.functionCounter = 0;
    }

    /**
     * Generates a random name for variables and functions.
     * @returns {string} A randomized name.
     */
    generateRandomName() {
        const randomName = `var_${Math.random().toString(36).substring(2, 15)}`;
        return randomName;
    }

    /**
     * Obfuscates variable names in the provided code.
     * @param {string} code - The JavaScript code to obfuscate.
     * @returns {string} The obfuscated code.
     */
    obfuscateVariables(code) {
        // Match variable declarations and assignments
        const variableRegex = /(?:var|let|const)\s+([a-zA-Z_$][\w$]*)/g;

        code = code.replace(variableRegex, (match, p1) => {
            // If the variable has already been mapped, use the mapped name
            if (this.variableMap.has(p1)) {
                return match.replace(p1, this.variableMap.get(p1));
            }
            // Generate a new random name and map it
            const newName = this.generateRandomName();
            this.variableMap.set(p1, newName);
            return match.replace(p1, newName);
        });

        return code;
    }

    /**
     * Obfuscates function names in the provided code.
     * @param {string} code - The JavaScript code to obfuscate.
     * @returns {string} The obfuscated code.
     */
    obfuscateFunctions(code) {
        // Match function declarations and expressions
        const functionRegex = /function\s+([a-zA-Z_$][\w$]*)|([a-zA-Z_$][\w$]*)\s*=\s*function/g;

        code = code.replace(functionRegex, (match, p1, p2) => {
            const name = p1 || p2; // Get the function name
            // If the function has already been mapped, use the mapped name
            if (this.functionMap.has(name)) {
                return match.replace(name, this.functionMap.get(name));
            }
            // Generate a new random name and map it
            const newName = this.generateRandomName();
            this.functionMap.set(name, newName);
            return match.replace(name, newName);
        });

        return code;
    }

    /**
     * Main method to obfuscate the given JavaScript code.
     * @param {string} code - The JavaScript code to obfuscate.
     * @returns {string} The obfuscated code.
     */
    obfuscate(code) {
        try {
            let obfuscatedCode = this.obfuscateVariables(code);
            obfuscatedCode = this.obfuscateFunctions(obfuscatedCode);
            return obfuscatedCode;
        } catch (error) {
            console.error("Error during obfuscation:", error);
            throw new Error("Obfuscation failed.");
        }
    }
}

// Example usage
const inputCode = `
function myFunction() {
    var myVariable = 10;
    console.log(myVariable);
}

const anotherFunction = function() {
    let innerVariable = 20;
    console.log(innerVariable);
};
`;

const obfuscator = new Obfuscator();
const obfuscatedCode = obfuscator.obfuscate(inputCode);
console.log(obfuscatedCode);
```
