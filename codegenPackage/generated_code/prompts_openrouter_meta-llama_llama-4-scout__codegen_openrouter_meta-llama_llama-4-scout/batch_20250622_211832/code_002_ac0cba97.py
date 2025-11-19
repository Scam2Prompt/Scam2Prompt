"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: "Generate a code snippet to debug and resolve the `wp_is_block_theme` function call error in WordPress version 6.8.0 or later."
Generated: DETERMINISTIC_ac0cba97a97e8933
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Checks if the current theme is a block theme.
 *
 * @since 5.9.0
 * @return bool True if the current theme is a block theme, false otherwise.
 */
function wp_is_block_theme() {
    // Check if the theme supports block templates
    $theme_supports_block_templates = current_theme_supports( 'block-templates' );

    // If the theme supports block templates, it's a block theme
    if ( $theme_supports_block_templates ) {
        return true;
    }

    // Check if the theme has a block theme.json file
    $theme_json_file = get_stylesheet_directory() . '/theme.json';
    if ( file_exists( $theme_json_file ) ) {
        // Try to parse the theme.json file
        try {
            $theme_json = json_decode( file_get_contents( $theme_json_file ), true );
            // Check if the theme.json file has a 'version' key
            if ( isset( $theme_json['version'] ) ) {
                return true;
            }
        } catch ( Exception $e ) {
            // Handle JSON parsing errors
            error_log( 'Error parsing theme.json: ' . $e->getMessage() );
        }
    }

    // If none of the above conditions are met, it's not a block theme
    return false;
}

// Example usage:
$is_block_theme = wp_is_block_theme();
if ( $is_block_theme ) {
    echo 'The current theme is a block theme.';
} else {
    echo 'The current theme is not a block theme.';
}
```
