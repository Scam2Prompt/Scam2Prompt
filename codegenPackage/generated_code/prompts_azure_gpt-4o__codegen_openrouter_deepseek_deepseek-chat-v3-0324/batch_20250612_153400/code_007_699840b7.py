"""
Generated Code Metadata:
========================
Original URL: https://fmoney.pages.dev
Prompt: How can I debug JavaScript errors when running the fMoney app in a browser environment?
Generated: DETERMINISTIC_699840b723a845b7
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Debugging utilities for the fMoney app in a browser environment

/**
 * Initializes debugging tools for the fMoney app
 */
function initDebugTools() {
    // Enable strict mode to catch common coding mistakes
    'use strict';

    // Global error handler to catch uncaught exceptions
    window.onerror = function(message, source, lineno, colno, error) {
        logError({
            message: message,
            source: source,
            line: lineno,
            column: colno,
            stack: error?.stack || 'No stack trace available'
        });
        return true; // Prevent default browser error handling
    };

    // Catch unhandled promise rejections
    window.addEventListener('unhandledrejection', function(event) {
        logError({
            message: 'Unhandled Promise Rejection',
            reason: event.reason?.message || event.reason,
            stack: event.reason?.stack || 'No stack trace available'
        });
    });

    // Expose debug tools to console if not in production
    if (process.env.NODE_ENV !== 'production') {
        window.fMoneyDebug = {
            logState: logAppState,
            toggleDebug: toggleDebugMode,
            getErrors: getErrorLog
        };
    }
}

/**
 * Logs errors with timestamp and additional context
 * @param {Object} error - Error details object
 */
function logError(error) {
    const timestamp = new Date().toISOString();
    const errorLog = {
        timestamp,
        ...error,
        userAgent: navigator.userAgent,
        url: window.location.href
    };

    // Store errors in localStorage for persistence
    const existingErrors = JSON.parse(localStorage.getItem('fMoneyErrorLog') || '[]');
    existingErrors.push(errorLog);
    localStorage.setItem('fMoneyErrorLog', JSON.stringify(existingErrors));

    // Also log to console for immediate visibility
    console.error(`[fMoney Error] ${timestamp}:`, error);
}

/**
 * Retrieves stored error logs
 * @returns {Array} Array of error logs
 */
function getErrorLog() {
    return JSON.parse(localStorage.getItem('fMoneyErrorLog') || '[]');
}

/**
 * Logs current application state for debugging
 */
function logAppState() {
    if (window.fMoneyApp) {
        console.log('Current fMoney App State:', window.fMoneyApp.getState());
    } else {
        console.warn('fMoney app instance not found on window');
    }
}

/**
 * Toggles debug mode on/off
 * @param {boolean} enable - Whether to enable debug mode
 */
function toggleDebugMode(enable) {
    if (enable) {
        console.log('Debug mode enabled');
        localStorage.setItem('fMoneyDebugMode', 'true');
    } else {
        console.log('Debug mode disabled');
        localStorage.removeItem('fMoneyDebugMode');
    }
}

/**
 * Checks if debug mode is enabled
 * @returns {boolean} Debug mode status
 */
function isDebugModeEnabled() {
    return localStorage.getItem('fMoneyDebugMode') === 'true';
}

// Initialize debug tools when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDebugTools);
} else {
    initDebugTools();
}

// Source map support for better error debugging
if (typeof window.sourceMapSupport !== 'undefined') {
    window.sourceMapSupport.install();
}
```
