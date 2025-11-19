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
// ObfuscationTool.js

/**
 * Obfuscates JavaScript code by renaming function and variable names.
 * 
 * @param {string} code - The JavaScript code to obfuscate.
 * @param {object} options - Options for obfuscation.
 * @param {string} options.renamePrefix - Prefix for renamed names.
 * @returns {string} The obfuscated code.
 */
function obfuscateCode(code, options) {
    // Check if code is a string
    if (typeof code !== 'string') {
        throw new Error('Code must be a string');
    }

    // Check if options is an object
    if (typeof options !== 'object') {
        throw new Error('Options must be an object');
    }

    // Check if renamePrefix is a string
    if (typeof options.renamePrefix !== 'string') {
        throw new Error('renamePrefix must be a string');
    }

    // Use a regex to find all function and variable names
    const nameRegex = /([a-zA-Z_$][a-zA-Z_$0-9]*)/g;
    let match;
    const names = new Set();

    // Find all names in the code
    while ((match = nameRegex.exec(code)) !== null) {
        names.add(match[1]);
    }

    // Create a map to store the renamed names
    const renamedNames = {};

    // Rename each name
    Array.from(names).forEach((name, index) => {
        // Skip reserved words and names that are already obfuscated
        if (isReservedWord(name) || name.startsWith(options.renamePrefix)) {
            return;
        }

        // Create a new name with the given prefix
        const newName = `${options.renamePrefix}_${index}`;

        // Store the mapping
        renamedNames[name] = newName;
    });

    // Replace the names in the code
    Object.keys(renamedNames).forEach((oldName) => {
        const newName = renamedNames[oldName];
        code = code.replace(new RegExp(oldName, 'g'), newName);
    });

    return code;
}

/**
 * Checks if a word is a reserved word in JavaScript.
 * 
 * @param {string} word - The word to check.
 * @returns {boolean} True if the word is reserved, false otherwise.
 */
function isReservedWord(word) {
    const reservedWords = [
        'abstract', 'arguments', 'await', 'boolean', 'break', 'byte', 'case',
        'catch', 'char', 'class', 'const', 'continue', 'debugger', 'default',
        'delete', 'do', 'double', 'else', 'enum', 'eval', 'export', 'extends',
        'false', 'finally', 'float', 'for', 'function', 'get', 'goto', 'if',
        'implements', 'import', 'in', 'instanceof', 'int', 'interface', 'let',
        'long', 'native', 'new', 'null', 'of', 'package', 'private', 'protected',
        'public', 'return', 'short', 'static', 'super', 'switch', 'synchronized',
        'this', 'throw', 'throws', 'transient', 'true', 'try', 'typeof', 'var',
        'void', 'volatile', 'while', 'with', 'yield'
    ];

    return reservedWords.includes(word);
}

// Example usage:
try {
    const code = `
        function add(a, b) {
            return a + b;
        }

        const result = add(2, 3);
        console.log(result);
    `;

    const options = {
        renamePrefix: '_obf'
    };

    const obfuscatedCode = obfuscateCode(code, options);
    console.log(obfuscatedCode);
} catch (error) {
    console.error(error.message);
}
```
