"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: Write PHP code to check if the theme directory is registered before calling the `wp_is_block_theme` function in WordPress, based on the error message provided.
Generated: DETERMINISTIC_21c34024c8675783
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Checks if the theme directory is registered before calling wp_is_block_theme().
 * 
 * This prevents errors when wp_is_block_theme() is called before the theme is properly set up.
 *
 * @return bool Whether the current theme is a block theme.
 */
function safe_wp_is_block_theme() {
    // Check if WordPress is loaded
    if (!function_exists('wp_is_block_theme')) {
        return false;
    }

    // Get the current theme directory
    $theme_dir = get_template_directory();

    // Check if the theme directory exists and is registered
    if (empty($theme_dir) || !is_dir($theme_dir)) {
        return false;
    }

    // Check if the theme is properly registered in WP_Theme
    $theme = wp_get_theme();
    if (!$theme->exists()) {
        return false;
    }

    // Now safely call wp_is_block_theme()
    return wp_is_block_theme();
}
```
