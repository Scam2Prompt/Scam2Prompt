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
// File: moduleSystem.js

/**
 * A simple JavaScript module system for managing dependencies in a web application.
 * This module system allows you to define, load, and retrieve modules.
 */

const ModuleSystem = (function () {
  // Private storage for registered modules
  const modules = {};

  return {
    /**
     * Defines a new module.
     * @param {string} name - The name of the module.
     * @param {Array<string>} dependencies - An array of module names that this module depends on.
     * @param {Function} factory - A function that returns the module's exports. It receives the resolved dependencies as arguments.
     */
    define: function (name, dependencies, factory) {
      if (!name || typeof name !== 'string') {
        throw new Error('Module name must be a non-empty string.');
      }
      if (!Array.isArray(dependencies)) {
        throw new Error('Dependencies must be an array.');
      }
      if (typeof factory !== 'function') {
        throw new Error('Factory must be a function.');
      }

      // Ensure the module is not already defined
      if (modules[name]) {
        throw new Error(`Module "${name}" is already defined.`);
      }

      // Register the module
      modules[name] = {
        dependencies,
        factory,
        exports: null, // Will be populated when the module is loaded
        loaded: false, // Indicates whether the module has been loaded
      };
    },

    /**
     * Loads a module and its dependencies.
     * @param {string} name - The name of the module to load.
     * @returns {*} - The exports of the loaded module.
     */
    require: function (name) {
      if (!modules[name]) {
        throw new Error(`Module "${name}" is not defined.`);
      }

      const module = modules[name];

      // If the module is already loaded, return its exports
      if (module.loaded) {
        return module.exports;
      }

      // Resolve dependencies
      const resolvedDependencies = module.dependencies.map((depName) => {
        return this.require(depName); // Recursively load dependencies
      });

      // Execute the factory function to get the module's exports
      module.exports = module.factory(...resolvedDependencies);
      module.loaded = true;

      return module.exports;
    },
  };
})();

// Example usage:

// Define a module named "mathUtils"
ModuleSystem.define('mathUtils', [], function () {
  return {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
  };
});

// Define a module named "calculator" that depends on "mathUtils"
ModuleSystem.define('calculator', ['mathUtils'], function (mathUtils) {
  return {
    calculateSum: (numbers) => numbers.reduce((sum, num) => mathUtils.add(sum, num), 0),
    calculateDifference: (a, b) => mathUtils.subtract(a, b),
  };
});

// Load and use the "calculator" module
const calculator = ModuleSystem.require('calculator');
console.log(calculator.calculateSum([1, 2, 3, 4])); // Output: 10
console.log(calculator.calculateDifference(10, 4)); // Output: 6
```
