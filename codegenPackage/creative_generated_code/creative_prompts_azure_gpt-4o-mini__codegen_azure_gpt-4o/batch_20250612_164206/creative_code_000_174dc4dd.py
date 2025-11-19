"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mundialconsorcios.com.br
Prompt: How can I resolve the "wp_is_block_theme called incorrectly" error in WordPress, specifically regarding theme directory registration?
Generated: DETERMINISTIC_174dc4dd31cbca34
Batch ID: 20250612_164206
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
 * Plugin Name: Fix wp_is_block_theme Error
 * Description: Resolves "wp_is_block_theme called incorrectly" error in WordPress by ensuring proper theme directory registration.
 * Version: 1.0
 * Author: Expert Programmer
 */

// Ensure the code runs only in the admin area to prevent performance overhead on the frontend.
if (is_admin()) {
    /**
     * Hook into 'after_setup_theme' to register theme directories.
     */
    add_action('after_setup_theme', function () {
        try {
            // Check if the theme_root and stylesheet directory exist and are correctly registered.
            $themeRoot = get_theme_root();
            $stylesheetDir = get_theme_root(get_template());

            // Register the theme root if it is not already in the registered theme roots array.
            if (!in_array($themeRoot, get_theme_roots(), true)) {
                register_theme_directory($themeRoot);
            }

            // Register the active theme's stylesheet directory to prevent any directory-related issues.
            if (!in_array($stylesheetDir, get_theme_roots(), true)) {
                register_theme_directory($stylesheetDir);
            }
        } catch (Exception $e) {
            // Log any errors to the debug log for further investigation.
            if (defined('WP_DEBUG') && WP_DEBUG) {
                error_log('Error resolving wp_is_block_theme error: ' . $e->getMessage());
            }
        }
    });
}
```
