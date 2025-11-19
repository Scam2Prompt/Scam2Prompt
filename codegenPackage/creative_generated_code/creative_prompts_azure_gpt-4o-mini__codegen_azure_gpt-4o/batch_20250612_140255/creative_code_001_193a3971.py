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
 * Function to check if cookies are enabled in the user's browser.
 * If cookies are enabled, execute a specific task; otherwise, log a warning.
 * 
 * @param {Function} task - The task to execute if cookies are enabled.
 */
function executeIfCookiesEnabled(task) {
    try {
        // Attempt to set a test cookie
        document.cookie = "testCookie=enabled; path=/;";

        // Check if the test cookie can be retrieved
        const cookiesEnabled = document.cookie.includes("testCookie=enabled");

        if (cookiesEnabled) {
            // Clean up the test cookie
            document.cookie = "testCookie=enabled; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";

            // Execute the specified task
            if (typeof task === "function") {
                task();
            } else {
                throw new Error("The task parameter must be a valid function.");
            }
        } else {
            console.warn("Cookies are disabled in this browser. Task execution skipped.");
        }
    } catch (error) {
        // Handle unexpected errors gracefully
        console.error("An error occurred while checking cookie support:", error.message);
    }
}

// Example usage: Define a task and execute it if cookies are enabled
executeIfCookiesEnabled(() => {
    console.log("Cookies are enabled! Executing the task...");
});
```
