"""
Generated Code Metadata:
========================
Original URL: https://metro-ccc.ru
Prompt: What libraries can help detect JavaScript support in a user's browser?
Generated: DETERMINISTIC_1d966a2dac5a361a
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Detects JavaScript support in a user's browser.
 * 
 * This module uses the navigator object to determine if JavaScript is enabled.
 * 
 * @module javascript-detector
 */

// Check if JavaScript is enabled by trying to access the navigator object
function isJavascriptEnabled() {
    try {
        // If the navigator object exists, JavaScript is enabled
        return typeof navigator !== 'undefined';
    } catch (error) {
        // If an error occurs, JavaScript is likely disabled
        return false;
    }
}

/**
 * Checks if the browser supports modern JavaScript features.
 * 
 * This function checks for the presence of modern JavaScript features such as
 * ES6 classes, promises, and fetch API.
 * 
 * @returns {boolean} True if the browser supports modern JavaScript features, false otherwise.
 */
function isModernJavascriptSupported() {
    try {
        // Check for ES6 classes
        const testClass = class {};
        // Check for promises
        const testPromise = new Promise((resolve) => resolve());
        // Check for fetch API
        const testFetch = window.fetch;
        
        return typeof testClass === 'function' 
            && typeof testPromise === 'object' 
            && typeof testFetch === 'function';
    } catch (error) {
        return false;
    }
}

// Example usage:
function main() {
    const javascriptEnabled = isJavascriptEnabled();
    const modernJavascriptSupported = isModernJavascriptSupported();

    console.log(`JavaScript enabled: ${javascriptEnabled}`);
    console.log(`Modern JavaScript supported: ${modernJavascriptSupported}`);
}

main();
```
