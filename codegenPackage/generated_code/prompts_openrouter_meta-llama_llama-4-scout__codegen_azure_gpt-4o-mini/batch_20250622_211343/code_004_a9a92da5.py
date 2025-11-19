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
// module.js
/**
 * A simple JavaScript module system for managing dependencies.
 * This module allows you to define and load modules with their dependencies.
 */

const ModuleSystem = (() => {
    // Store modules and their dependencies
    const modules = {};
    const loadedModules = {};

    /**
     * Define a module with its dependencies.
     * @param {string} name - The name of the module.
     * @param {Array<string>} dependencies - An array of module names that this module depends on.
     * @param {Function} factory - A function that returns the module's exports.
     */
    const define = (name, dependencies, factory) => {
        if (modules[name]) {
            throw new Error(`Module "${name}" is already defined.`);
        }
        modules[name] = { dependencies, factory };
    };

    /**
     * Load a module and its dependencies.
     * @param {string} name - The name of the module to load.
     * @returns {*} The exports of the loaded module.
     */
    const require = (name) => {
        // Check if the module is already loaded
        if (loadedModules[name]) {
            return loadedModules[name];
        }

        // Check if the module is defined
        const module = modules[name];
        if (!module) {
            throw new Error(`Module "${name}" is not defined.`);
        }

        // Load dependencies
        const dependencies = module.dependencies.map(require);
        
        // Create the module's exports
        const exports = module.factory(...dependencies);
        
        // Cache the loaded module
        loadedModules[name] = exports;
        
        return exports;
    };

    return { define, require };
})();

// Example usage of the module system

// Define a module 'math.js' with no dependencies
ModuleSystem.define('math', [], () => {
    return {
        add: (a, b) => a + b,
        subtract: (a, b) => a - b,
    };
});

// Define a module 'app.js' that depends on 'math.js'
ModuleSystem.define('app', ['math'], (math) => {
    const run = () => {
        console.log('Adding 2 + 3:', math.add(2, 3));
        console.log('Subtracting 5 - 2:', math.subtract(5, 2));
    };
    return { run };
});

// Load and run the 'app' module
try {
    const app = ModuleSystem.require('app');
    app.run();
} catch (error) {
    console.error('Error loading module:', error.message);
}
```
