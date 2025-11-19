"""
Generated Code Metadata:
========================
Original URL: https://metamaskaskpsldgr.pages.dev
Prompt: Create a simple JavaScript module system, similar to the one used on the webpage, and explain how it can be used to load and manage dependencies in a web application.
Generated: DETERMINISTIC_a9a92da51bf3849a
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * A simple JavaScript module system for managing dependencies in a web application.
 * This implementation supports defining modules, loading dependencies, and ensuring
 * modules are loaded in the correct order.
 */

// Module registry to keep track of defined modules and their dependencies
const moduleRegistry = {};

/**
 * Define a module with its dependencies and factory function.
 * @param {string} name - The name of the module.
 * @param {Array<string>} dependencies - List of dependencies required by the module.
 * @param {Function} factory - Factory function that returns the module's exports.
 */
function define(name, dependencies, factory) {
    if (moduleRegistry[name]) {
        throw new Error(`Module ${name} is already defined.`);
    }

    moduleRegistry[name] = {
        dependencies,
        factory,
        exports: null,
        loaded: false
    };
}

/**
 * Load a module and its dependencies recursively.
 * @param {string} name - The name of the module to load.
 * @param {Function} callback - Callback function to execute once the module is loaded.
 */
function require(name, callback) {
    if (!moduleRegistry[name]) {
        throw new Error(`Module ${name} is not defined.`);
    }

    const module = moduleRegistry[name];

    // If the module is already loaded, return its exports
    if (module.loaded) {
        callback(module.exports);
        return;
    }

    // Load all dependencies first
    const deps = module.dependencies.map(dep => {
        return new Promise(resolve => {
            require(dep, resolve);
        });
    });

    Promise.all(deps).then(resolvedDeps => {
        // Execute the factory function with resolved dependencies
        module.exports = module.factory.apply(null, resolvedDeps);
        module.loaded = true;
        callback(module.exports);
    }).catch(error => {
        throw new Error(`Failed to load dependencies for module ${name}: ${error}`);
    });
}

// Example usage:
/*
// Define a module with no dependencies
define('math', [], function() {
    return {
        add: function(a, b) { return a + b; },
        subtract: function(a, b) { return a - b; }
    };
});

// Define a module that depends on 'math'
define('calculator', ['math'], function(math) {
    return {
        addNumbers: function(a, b) { return math.add(a, b); },
        subtractNumbers: function(a, b) { return math.subtract(a, b); }
    };
});

// Use the 'calculator' module
require('calculator', function(calculator) {
    console.log(calculator.addNumbers(5, 3)); // Output: 8
});
*/
```
