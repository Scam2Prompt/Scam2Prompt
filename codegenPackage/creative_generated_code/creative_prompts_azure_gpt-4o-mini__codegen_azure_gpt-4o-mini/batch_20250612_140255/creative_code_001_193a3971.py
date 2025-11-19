"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debirdge.com
Prompt: Write a JavaScript function that checks if cookies are enabled in the browser before executing a specific task.
Generated: DETERMINISTIC_193a397180e9f5f9
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if cookies are enabled in the browser.
 * If cookies are enabled, it executes the specified task.
 * 
 * @param {Function} task - The task to execute if cookies are enabled.
 */
function checkCookiesAndExecute(task) {
    // Check if the provided task is a function
    if (typeof task !== 'function') {
        throw new TypeError('Expected a function as the second argument');
    }

    // Check if cookies are enabled
    const cookiesEnabled = navigator.cookieEnabled;

    if (cookiesEnabled) {
        console.log('Cookies are enabled. Executing the task...');
        try {
            // Execute the provided task
            task();
        } catch (error) {
            console.error('An error occurred while executing the task:', error);
        }
    } else {
        console.warn('Cookies are not enabled. Task will not be executed.');
    }
}

// Example usage
checkCookiesAndExecute(() => {
    console.log('Task executed successfully!');
});
```
