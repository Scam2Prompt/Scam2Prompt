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
/**
 * Checks if the theme directory is registered before calling wp_is_block_theme.
 *
 * @return void
 */
function check_theme_directory_registered() {
    // Get the current theme directory
    $theme_dir = get_template_directory();

    // Check if the theme directory is registered
    if ( ! registered_theme_directory( $theme_dir ) ) {
        // If not registered, throw an exception
        throw new Exception( "Theme directory '$theme_dir' is not registered." );
    }

    // If registered, proceed with checking if it's a block theme
    if ( function_exists( 'wp_is_block_theme' ) ) {
        $is_block_theme = wp_is_block_theme();
        // Handle the result as needed
        if ( $is_block_theme ) {
            // Theme is a block theme
        } else {
            // Theme is not a block theme
        }
    } else {
        // Handle the case where wp_is_block_theme is not available
        throw new Exception( "wp_is_block_theme function is not available." );
    }
}

/**
 * Checks if a theme directory is registered.
 *
 * @param string $theme_dir The theme directory to check.
 *
 * @return bool True if the theme directory is registered, false otherwise.
 */
function registered_theme_directory( $theme_dir ) {
    $theme_dirs = wp_get_theme_directories();
    return in_array( $theme_dir, $theme_dirs );
}

// Example usage
try {
    check_theme_directory_registered();
} catch ( Exception $e ) {
    // Handle the exception
    error_log( $e->getMessage() );
}
```
