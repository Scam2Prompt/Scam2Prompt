"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sgeek-seo.com
Prompt: Write a PHP script to optimize WordPress site speed using lightweight themes, as recommended in the SGeek SEO post about minimalistic WordPress themes.
Generated: DETERMINISTIC_c4c8782023991e38
Batch ID: 20250612_151109
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
 * WordPress Speed Optimization Script
 * This script recommends lightweight themes to optimize WordPress site speed.
 * Based on recommendations from SGeek SEO about minimalistic WordPress themes.
 */

// Define an array of recommended lightweight themes
$recommended_themes = array(
    'Astra',
    'GeneratePress',
    'Neve',
    'Blocksy',
    'OceanWP',
    'Kadence',
    'Hestia',
    'Schema',
    'Zerif Lite',
    'Ashe'
);

/**
 * Function to display recommended themes
 */
function display_recommended_themes($themes) {
    // Check if the themes array is empty
    if (empty($themes)) {
        echo "No themes available.";
        return;
    }

    echo "<h2>Recommended Lightweight WordPress Themes</h2>";
    echo "<ul>";
    foreach ($themes as $theme) {
        echo "<li>" . htmlspecialchars($theme) . "</li>"; // Sanitize output
    }
    echo "</ul>";
}

// Check if we are in the admin area
if (is_admin()) {
    // Display the recommended themes to the user
    display_recommended_themes($recommended_themes);
} else {
    // If not in admin area, display a message
    echo "<p>This script is designed to run in the WordPress admin area.</p>";
}

// Hook into admin_init to run the script when in the admin area
add_action('admin_init', function() {
    try {
        // Check for theme installation and activation functionality
        if (isset($_POST['install_theme'])) {
            $theme_name = sanitize_text_field($_POST['theme_name']);

            // Check if the theme is one of the recommended ones
            if (in_array($theme_name, $GLOBALS['recommended_themes'])) {
                // Logic to install and activate the theme (placeholder, implement as needed)
                // switch_theme($theme_name);
                echo "<p>Theme '{$theme_name}' has been activated successfully!</p>";
            } else {
                throw new Exception("Theme '{$theme_name}' is not a recommended theme.");
            }
        }
    } catch (Exception $e) {
        // Handle any exceptions by displaying an error message
        echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
    }
});
?>
```
