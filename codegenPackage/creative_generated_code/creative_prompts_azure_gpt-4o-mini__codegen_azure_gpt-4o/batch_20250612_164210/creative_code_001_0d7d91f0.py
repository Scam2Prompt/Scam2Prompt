"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stroyalentertainnmentrc.com
Prompt: Write a PHP function that handles HTTP response codes, specifically for 404 errors, based on the techniques from stroyalentertainnmentrc.com.
Generated: DETERMINISTIC_0d7d91f012ef3692
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Handles HTTP response codes, specifically for 404 errors.
 * This function sends the appropriate HTTP header and renders a custom 404 error page.
 * 
 * @param string $customErrorPage Path to the custom 404 error page (optional).
 * @return void
 */
function handleHttp404Error($customErrorPage = null)
{
    try {
        // Send the 404 HTTP header
        http_response_code(404);

        // Check if a custom error page is provided
        if ($customErrorPage && file_exists($customErrorPage)) {
            // Safely include the custom error page
            include $customErrorPage;
        } else {
            // Default fallback message if no custom error page exists
            echo "<h1>404 Not Found</h1>";
            echo "<p>The page you are looking for could not be found.</p>";
        }
    } catch (Exception $e) {
        // Log the error for debugging purposes
        error_log("Error handling 404 HTTP response: " . $e->getMessage());
        
        // Display a generic error message
        echo "<h1>An unexpected error occurred.</h1>";
        echo "<p>We are currently unable to process your request.</p>";
    }
}

// Example usage
// handleHttp404Error('/path/to/custom-404.html');
?>
```
