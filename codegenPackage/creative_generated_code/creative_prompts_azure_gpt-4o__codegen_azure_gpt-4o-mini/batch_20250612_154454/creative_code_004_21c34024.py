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
 * Function to check if the theme directory is registered before calling wp_is_block_theme.
 *
 * @return bool True if the theme is a block theme; otherwise, false.
 */
function is_block_theme_registered() {
    // Check if the theme directory is set and registered
    if ( isset( $GLOBALS['theme'] ) && is_object( $GLOBALS['theme'] ) ) {
        // Check if the theme supports block themes
        if ( function_exists( 'wp_is_block_theme' ) ) {
            return wp_is_block_theme();
        } else {
            // Function does not exist; log an error message
            error_log( 'Error: wp_is_block_theme function does not exist.' );
            return false;
        }
    } else {
        // Log an error message if the theme directory is not registered
        error_log( 'Error: Theme directory is not registered.' );
        return false;
    }
}

// Example usage of the function
if ( is_block_theme_registered() ) {
    // Theme is a block theme
    echo 'This is a block theme.';
} else {
    // Theme is not a block theme or an error occurred
    echo 'This is not a block theme or an error has occurred.';
}
?>
```
