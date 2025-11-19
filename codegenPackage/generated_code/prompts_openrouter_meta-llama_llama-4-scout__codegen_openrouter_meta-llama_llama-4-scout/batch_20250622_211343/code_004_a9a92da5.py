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
// module-system.js

/**
 * A simple JavaScript module system.
 * 
 * This module system allows you to define and load dependencies in a web application.
 * It uses a registry to store and manage modules.
 */

// Module registry
const registry = {};

/**
 * Registers a new module in the registry.
 * 
 * @param {string} name - The name of the module.
 * @param {function} factory - The factory function that returns the module.
 */
function registerModule(name, factory) {
    if (registry[name]) {
        throw new Error(`Module ${name} already registered.`);
    }
    registry[name] = factory;
}

/**
 * Loads a module from the registry.
 * 
 * @param {string} name - The name of the module to load.
 * @returns {*} The loaded module.
 */
function loadModule(name) {
    if (!registry[name]) {
        throw new Error(`Module ${name} not found.`);
    }
    return registry[name]();
}

/**
 * Defines a new module using the provided factory function.
 * 
 * @param {string} name - The name of the module.
 * @param {function} dependencies - An array of dependency names.
 * @param {function} factory - The factory function that returns the module.
 */
function defineModule(name, dependencies, factory) {
    registerModule(name, () => {
        const deps = dependencies.map(loadModule);
        return factory(...deps);
    });
}

// Example usage:

/**
 * A sample module that depends on another module.
 */
defineModule('moduleA', [], () => {
    return {
        sayHello: () => console.log('Hello from module A!')
    };
});

defineModule('moduleB', ['moduleA'], (moduleA) => {
    return {
        sayGoodbye: () => {
            moduleA.sayHello();
            console.log('Goodbye from module B!');
        }
    };
});

// Load and use the modules
try {
    const moduleA = loadModule('moduleA');
    const moduleB = loadModule('moduleB');
    moduleA.sayHello();
    moduleB.sayGoodbye();
} catch (error) {
    console.error(error.message);
}
```
