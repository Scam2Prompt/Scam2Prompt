"""
Generated Code Metadata:
========================
Original URL: https://nerzo.app
Prompt: What are the best practices for using `document.write()` in a JavaScript application, considering performance and user experience?
Generated: DETERMINISTIC_4ae69f54ce292532
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a JavaScript code snippet demonstrating best practices for using `document.write()` with performance and user experience considerations:

```javascript
/**
 * Safe wrapper for document.write() with performance and UX considerations
 * @param {string} content - The content to be written
 * @param {string} targetElementId - (Optional) ID of element to write content into
 * @param {boolean} async - Whether to execute asynchronously
 */
function safeDocumentWrite(content, targetElementId = null, async = false) {
    // Check if document is still loading
    if (document.readyState === 'loading') {
        if (async) {
            // Defer execution until DOM is fully loaded
            document.addEventListener('DOMContentLoaded', () => {
                executeWrite(content, targetElementId);
            });
        } else {
            // Execute immediately during loading phase
            executeWrite(content, targetElementId);
        }
    } else {
        // DOM is already loaded - use DOM manipulation methods instead
        console.warn('DOM already loaded. Consider using DOM manipulation methods instead of document.write()');
        if (targetElementId) {
            const element = document.getElementById(targetElementId);
            if (element) {
                element.insertAdjacentHTML('beforeend', content);
            } else {
                console.error(`Target element with ID ${targetElementId} not found`);
            }
        } else {
            document.body.insertAdjacentHTML('beforeend', content);
        }
    }
}

/**
 * Internal function to handle the actual writing
 * @param {string} content - The content to write
 * @param {string|null} targetElementId - Target element ID or null
 */
function executeWrite(content, targetElementId) {
    try {
        if (targetElementId) {
            const element = document.getElementById(targetElementId);
            if (element) {
                document.write = (function(write) {
                    return function(string) {
                        element.insertAdjacentHTML('beforeend', string);
                    };
                })(document.write);
            }
        }
        document.write(content);
    } catch (error) {
        console.error('Error in document.write operation:', error);
        // Fallback to DOM manipulation
        if (targetElementId) {
            const element = document.getElementById(targetElementId);
            if (element) {
                element.insertAdjacentHTML('beforeend', content);
            }
        } else {
            document.body.insertAdjacentHTML('beforeend', content);
        }
    } finally {
        // Restore original document.write if modified
        if (targetElementId && document.write.__original) {
            document.write = document.write.__original;
        }
    }
}

// Example usage:
// During loading phase (sync)
// safeDocumentWrite('<p>Hello World</p>');

// During loading phase (async)
// safeDocumentWrite('<p>Hello World</p>', null, true);

// After loading phase (with target element)
// safeDocumentWrite('<p>Hello World</p>', 'content-container');
```
