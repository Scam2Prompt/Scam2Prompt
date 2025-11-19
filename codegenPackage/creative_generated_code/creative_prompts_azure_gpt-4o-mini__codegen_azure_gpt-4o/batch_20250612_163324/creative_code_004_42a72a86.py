"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krushinews18.com
Prompt: Create a PHP function to handle 404 errors in a WordPress blog, similar to the "Nothing Found" message on krushinews18.com.
Generated: DETERMINISTIC_42a72a865d54eea8
Batch ID: 20250612_163324
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
 * Custom 404 Error Handler for WordPress
 * 
 * This function displays a custom "Nothing Found" message
 * on 404 error pages in a WordPress blog.
 * 
 * Usage:
 * Add this function to your theme's `functions.php` file.
 * WordPress will automatically call the custom template for 404 errors.
 */

function custom_404_error_handler() {
    // Start Output Buffering
    ob_start();

    // Set HTTP Response Code to 404
    http_response_code(404);

    // Display Custom Message for "Nothing Found"
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>404 - Page Not Found</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.5em;
                margin-bottom: 30px;
            }
            a {
                display: inline-block;
                text-decoration: none;
                color: #0073aa;
                font-weight: bold;
                font-size: 1.2em;
                padding: 10px 20px;
                border: 1px solid #0073aa;
                border-radius: 5px;
                background-color: #fff;
            }
            a:hover {
                background-color: #0073aa;
                color: #fff;
            }
        </style>
    </head>
    <body>
        <h1>Oops! Nothing Found</h1>
        <p>We couldn't find the page you're looking for. It might have been moved or deleted.</p>
        <p><a href="<?php echo esc_url(home_url('/')); ?>">Go to Homepage</a></p>
    </body>
    </html>
    <?php

    // End Output Buffering and Send the Output
    ob_end_flush();

    // Exit to prevent any further processing
    exit;
}

// Hook into WordPress' template_redirect to intercept 404 errors
function override_404_template() {
    if (is_404()) {
        custom_404_error_handler();
    }
}
add_action('template_redirect', 'override_404_template');
?>
```
