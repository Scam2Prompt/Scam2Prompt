"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nerzo.app
Prompt: What are the best practices for using `document.write()` in a JavaScript application, considering performance and user experience?
Generated: DETERMINISTIC_4ae69f54ce292532
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A utility function to safely use document.write()
 * in a way that minimizes performance impacts and improves user experience.
 * 
 * Note: document.write() can overwrite the entire document if called after the page has finished loading,
 * so it should be used with caution.
 *
 * @param {string} content - The HTML content to write to the document.
 * @throws Will throw an error if the content is not a string.
 */
function safeDocumentWrite(content) {
    // Check if the input is a string
    if (typeof content !== 'string') {
        throw new Error('Content must be a string');
    }

    // Ensure document.write is called only during the document loading phase
    if (document.readyState === 'loading') {
        document.write(content);
    } else {
        console.warn('document.write() was called after the document has finished loading. Use this method before the page is fully loaded.');
    }
}

// Usage example:
try {
    // This should only be called before the DOM is fully loaded
    safeDocumentWrite('<h1>Hello, world!</h1>');
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
