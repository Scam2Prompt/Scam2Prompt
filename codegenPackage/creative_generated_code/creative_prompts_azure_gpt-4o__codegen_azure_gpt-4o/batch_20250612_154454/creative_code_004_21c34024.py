"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mundialconsorcios.com.br
Prompt: Write PHP code to check if the theme directory is registered before calling the `wp_is_block_theme` function in WordPress, based on the error message provided.
Generated: DETERMINISTIC_21c34024c8675783
Batch ID: 20250612_154454
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
 * Function to safely check if the theme is a block theme in WordPress.
 * Ensures the theme directory is registered before calling `wp_is_block_theme`.
 */

function is_theme_block_theme_safe() {
    // Check if the theme directory is properly registered.
    if (wp_get_theme()->exists()) {
        // If the theme directory is registered, check if it's a block theme.
        return wp_is_block_theme();
    } else {
        // Handle the case where the theme directory is not registered.
        // Log an error or return false as a fallback.
        error_log('Theme directory is not registered. Cannot determine if it is a block theme.');
        return false;
    }
}

// Example usage
$is_block_theme = is_theme_block_theme_safe();
if ($is_block_theme) {
    echo 'The active theme is a block theme.';
} else {
    echo 'The active theme is not a block theme or the theme directory is not properly registered.';
}
?>
```
