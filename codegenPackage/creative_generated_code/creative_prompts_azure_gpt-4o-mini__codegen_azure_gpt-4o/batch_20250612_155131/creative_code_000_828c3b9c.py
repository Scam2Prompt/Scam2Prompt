"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayacosmetics.com
Prompt: Generate a code snippet for a WordPress theme that displays a custom welcome message on the homepage, similar to "Hello world!".
Generated: DETERMINISTIC_828c3b9c8d1b11f7
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready code snippet for a WordPress theme that displays a custom welcome message on the homepage:

```php
<?php
/**
 * Theme Functions File
 *
 * This file contains the code to add a custom welcome message
 * on the homepage of the WordPress theme.
 *
 * @package WordPressTheme
 */

// Hook into 'wp_head' to display the custom welcome message.
add_action('wp_head', 'display_custom_welcome_message');

/**
 * Outputs a custom welcome message on the homepage.
 *
 * This function checks if the current page is the homepage and
 * displays a custom welcome message using inline HTML and CSS.
 */
function display_custom_welcome_message() {
    // Ensure this is only executed on the homepage.
    if (is_front_page()) {
        ?>
        <style>
            /* Inline CSS for styling the welcome message */
            .custom-welcome-message {
                font-size: 24px;
                font-weight: bold;
                color: #333;
                text-align: center;
                margin-top: 20px;
            }
        </style>
        <div class="custom-welcome-message">
            <?php echo esc_html__('Hello world! Welcome to our website.', 'your-theme-textdomain'); ?>
        </div>
        <?php
    }
}
```

To use this code snippet:
1. Place this code in the `functions.php` file of your WordPress theme.
2. Replace `'your-theme-textdomain'` with your theme's correct text domain for proper translation support.

This code follows WordPress best practices, includes error handling via `esc_html__` for sanitization, and is production-ready.
