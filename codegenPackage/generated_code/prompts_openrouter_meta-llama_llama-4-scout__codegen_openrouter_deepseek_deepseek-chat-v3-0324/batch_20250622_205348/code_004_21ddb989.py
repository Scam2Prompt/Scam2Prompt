"""
Generated Code Metadata:
========================
Original URL: https://testsite.104zero.com
Prompt: Create a simple JavaScript library for basic RAM testing and reporting.
Generated: DETERMINISTIC_21ddb989a176d184
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * RAMTest - A simple JavaScript library for basic RAM testing and reporting.
 * @version 1.0.0
 * @license MIT
 */
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.RAMTest = factory();
    }
}(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    /**
     * Default configuration options
     * @type {Object}
     */
    const defaultConfig = {
        testDuration: 5000, // Duration of each test in milliseconds
        maxAllocation: 1024, // Maximum allocation size in MB
        allocationStep: 64, // Allocation step size in MB
        reportInterval: 1000 // Reporting interval in milliseconds
    };

    /**
     * RAMTest constructor
     * @param {Object} config - Configuration options
     * @constructor
     */
    function RAMTest(config) {
        this.config = Object.assign({}, defaultConfig, config);
        this.isRunning = false;
        this.currentTest = null;
        this.listeners = {
            progress: [],
            complete: [],
            error: []
        };
    }

    /**
     * Add event listener
     * @param {string} event - Event name ('progress', 'complete', 'error')
     * @param {function} callback - Callback function
     */
    RAMTest.prototype.on = function (event, callback) {
        if (this.listeners[event]) {
            this.listeners[event].push(callback);
        }
    };

    /**
     * Remove event listener
     * @param {string} event - Event name
     * @param {function} callback - Callback function to remove
     */
    RAMTest.prototype.off = function (event, callback) {
        if (this.listeners[event]) {
            this.listeners[event] = this.listeners[event].filter(
                cb => cb !== callback
            );
        }
    };

    /**
     * Emit event to all listeners
     * @param {string} event - Event name
     * @param {*} data - Data to pass to listeners
     * @private
     */
    RAMTest.prototype._emit = function (event, data) {
        if (this.listeners[event]) {
            this.listeners[event].forEach(callback => {
                try {
                    callback(data);
                } catch (e) {
                    console.error(`Error in ${event} listener:`, e);
                }
            });
        }
    };

    /**
     * Allocate memory block
     * @param {number} sizeMB - Size in MB
     * @returns {ArrayBuffer} Allocated memory block
     * @private
     */
    RAMTest.prototype._allocateMemory = function (sizeMB) {
        try {
            const bytes = sizeMB * 1024 * 1024;
            return new ArrayBuffer(bytes);
        } catch (e) {
            throw new Error(`Failed to allocate ${sizeMB}MB: ${e.message}`);
        }
    };

    /**
     * Run memory test
     * @returns {Promise} Resolves with test results
     */
    RAMTest.prototype.runTest = function () {
        if (this.isRunning) {
            return Promise.reject(new Error('Test already running'));
        }

        this.isRunning = true;
        const startTime = Date.now();
        const endTime = startTime + this.config.testDuration;
        let currentSize = this.config.allocationStep;
        const allocations = [];
        let lastReportTime = startTime;

        return new Promise((resolve, reject) => {
            this.currentTest = setInterval(() => {
                try {
                    const now = Date.now();
                    if (now >= endTime) {
                        this._completeTest(allocations, resolve);
                        return;
                    }

                    // Report progress at intervals
                    if (now - lastReportTime >= this.config.reportInterval) {
                        this._emit('progress', {
                            allocated: allocations.length * this.config.allocationStep,
                            currentSize: currentSize,
                            elapsed: now - startTime
                        });
                        lastReportTime = now;
                    }

                    // Attempt to allocate memory
                    const allocation = this._allocateMemory(currentSize);
                    allocations.push(allocation);
                    currentSize += this.config.allocationStep;

                    // Reset if we hit max allocation
                    if (currentSize > this.config.maxAllocation) {
                        currentSize = this.config.allocationStep;
                    }
                } catch (e) {
                    this._emit('error', e);
                    this._completeTest(allocations, resolve, e);
                }
            }, 100); // Check every 100ms
        });
    };

    /**
     * Complete the current test
     * @param {Array} allocations - Array of allocations
     * @param {function} resolve - Promise resolve function
     * @param {Error} [error] - Optional error
     * @private
     */
    RAMTest.prototype._completeTest = function (allocations, resolve, error) {
        clearInterval(this.currentTest);
        this.isRunning = false;
        this.currentTest = null;

        // Free all allocated memory
        allocations.length = 0;

        const result = {
            success: !error,
            error: error,
            totalAllocated: allocations.length * this.config.allocationStep,
            maxAllocation: this.config.maxAllocation
        };

        this._emit('complete', result);
        if (error) {
            resolve(result); // Still resolve even with error
        } else {
            resolve(result);
        }
    };

    /**
     * Stop current test
     */
    RAMTest.prototype.stopTest = function () {
        if (this.isRunning && this.currentTest) {
            clearInterval(this.currentTest);
            this.isRunning = false;
            this.currentTest = null;
            this._emit('complete', {
                success: false,
                error: new Error('Test stopped by user'),
                totalAllocated: 0,
                maxAllocation: this.config.maxAllocation
            });
        }
    };

    /**
     * Get current configuration
     * @returns {Object} Current configuration
     */
    RAMTest.prototype.getConfig = function () {
        return Object.assign({}, this.config);
    };

    /**
     * Update configuration
     * @param {Object} newConfig - New configuration values
     */
    RAMTest.prototype.updateConfig = function (newConfig) {
        if (this.isRunning) {
            throw new Error('Cannot update config while test is running');
        }
        this.config = Object.assign({}, this.config, newConfig);
    };

    return RAMTest;
}));
```
