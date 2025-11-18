"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usweb09.us
Prompt: Generate PHP code to retrieve and list all available themes, including Twenty Twenty-Five, from a WordPress installation.
Generated: DETERMINISTIC_8a44974a6ae12746
Batch ID: 20250612_155115
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
 * Retrieve and list all available themes in a WordPress installation.
 *
 * This script fetches the list of themes, including the Twenty Twenty-Five theme,
 * and displays them in an HTML unordered list format.
 */

// Include WordPress functionality
require_once('wp-load.php');

// Function to retrieve and list all available themes
function list_available_themes() {
    // Get all themes
    $themes = wp_get_themes();

    // Check if any themes are available
    if (empty($themes)) {
        echo '<p>No themes found.</p>';
        return;
    }

    // Start output
    echo '<h2>Available Themes</h2>';
    echo '<ul>';

    // Iterate through each theme
    foreach ($themes as $theme_slug => $theme) {
        // Get theme details
        $theme_name = $theme->get('Name');
        $is_active = $theme_slug === get_option('stylesheet'); // Check if the theme is currently active

        // Output theme name and status
        echo '<li>' . esc_html($theme_name) . ($is_active ? ' (Active)' : '') . '</li>';
    }

    echo '</ul>';
}

// Execute the function to list themes
try {
    list_available_themes();
} catch (Exception $e) {
    // Handle any errors gracefully
    echo '<p>Error retrieving themes: ' . esc_html($e->getMessage()) . '</p>';
}

?>
```
