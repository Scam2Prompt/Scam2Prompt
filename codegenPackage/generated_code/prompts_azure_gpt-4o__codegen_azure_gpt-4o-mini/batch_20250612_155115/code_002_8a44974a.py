"""
Generated Code Metadata:
========================
Original URL: https://usweb09.us
Prompt: Generate PHP code to retrieve and list all available themes, including Twenty Twenty-Five, from a WordPress installation.
Generated: DETERMINISTIC_8a44974a6ae12746
Batch ID: 20250612_155115
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
 * Retrieve and list all available themes in a WordPress installation.
 *
 * This script fetches the themes from the WordPress installation and
 * displays their names and details, including the Twenty Twenty-Five theme.
 */

// Load WordPress environment
require_once('wp-load.php');

// Function to retrieve and list all themes
function list_available_themes() {
    // Get all themes
    $themes = wp_get_themes();

    // Check if themes are available
    if (empty($themes)) {
        echo "No themes found.";
        return;
    }

    // Start outputting the themes
    echo "<h2>Available Themes</h2>";
    echo "<ul>";

    // Loop through each theme and display its details
    foreach ($themes as $theme) {
        // Get theme details
        $theme_name = $theme->get('Name');
        $theme_version = $theme->get('Version');
        $theme_description = $theme->get('Description');
        $theme_author = $theme->get('Author');

        // Output theme information
        echo "<li>";
        echo "<strong>Name:</strong> " . esc_html($theme_name) . "<br>";
        echo "<strong>Version:</strong> " . esc_html($theme_version) . "<br>";
        echo "<strong>Description:</strong> " . esc_html($theme_description) . "<br>";
        echo "<strong>Author:</strong> " . esc_html($theme_author) . "<br>";
        echo "</li>";
    }

    echo "</ul>";
}

// Execute the function to list themes
try {
    list_available_themes();
} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo "An error occurred while retrieving themes: " . esc_html($e->getMessage());
}
?>
```
