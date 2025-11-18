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
 * WordPress Site Speed Optimization Script
 * 
 * This script recommends lightweight themes to optimize WordPress site speed.
 * It identifies installed themes, checks for lightweight options, and suggests alternatives.
 * 
 * Usage:
 * Place this script in your WordPress directory and run it via the command line or browser.
 * 
 * Author: Expert Developer
 */

// Load WordPress environment
define('WP_USE_THEMES', false);
require_once('./wp-load.php');

try {
    // Ensure user has administrative rights
    if (!current_user_can('manage_options')) {
        throw new Exception('Access denied! You must be an administrator to run this script.');
    }

    // Recommended lightweight themes
    $recommendedThemes = [
        'Astra',
        'GeneratePress',
        'Neve',
        'OceanWP',
        'Twenty Twenty-One' // Default lightweight WordPress theme
    ];

    // Get list of installed themes
    $installedThemes = wp_get_themes();
    $installedThemeNames = array_keys($installedThemes);

    // Check if already using a lightweight theme
    $currentTheme = wp_get_theme()->get('Name');
    echo "Current Active Theme: $currentTheme\n";

    if (in_array($currentTheme, $recommendedThemes)) {
        echo "You are already using a lightweight theme. Great job!\n";
    } else {
        echo "Consider switching to a lightweight theme for better performance.\n";
    }

    // Suggest lightweight themes among installed themes
    $suggestedThemes = array_intersect($installedThemeNames, $recommendedThemes);

    if (!empty($suggestedThemes)) {
        echo "Installed lightweight themes that you can activate:\n";
        foreach ($suggestedThemes as $theme) {
            echo "- $theme\n";
        }
    } else {
        echo "No recommended lightweight themes are currently installed.\n";
        echo "Suggested themes to install: " . implode(', ', $recommendedThemes) . "\n";
    }

    // Provide guidance on how to switch themes
    echo "To switch themes, go to Appearance > Themes in your WordPress admin dashboard.\n";

} catch (Exception $e) {
    // Handle errors gracefully
    error_log('Error encountered: ' . $e->getMessage());
    echo "An error occurred: " . htmlspecialchars($e->getMessage()) . "\n";
}
?>
```
