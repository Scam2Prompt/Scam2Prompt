"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devteamtools.com
Prompt: Provide a code snippet to list all available WordPress themes, including Twenty Twenty-Five, using the WordPress Theme API.
Generated: DETERMINISTIC_fd1964c2198892e5
Batch ID: 20250612_145245
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
 * List all available WordPress themes, including Twenty Twenty-Five.
 *
 * This script uses the WordPress Theme API to retrieve and display 
 * all installed themes on the WordPress site.
 *
 * Ensure this code is placed within a WordPress environment.
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

try {
    // Load all available themes using the WordPress Theme API
    $themes = wp_get_themes();

    // Check if themes were retrieved successfully
    if (empty($themes)) {
        throw new Exception('No themes found. Ensure themes are installed in /wp-content/themes/');
    }

    // Iterate through each theme and display its details
    foreach ($themes as $theme_slug => $theme) {
        echo '<strong>Theme Name:</strong> ' . esc_html($theme->get('Name')) . '<br>';
        echo '<strong>Theme Version:</strong> ' . esc_html($theme->get('Version')) . '<br>';
        echo '<strong>Theme Author:</strong> ' . esc_html($theme->get('Author')) . '<br>';
        echo '<strong>Theme Directory Slug:</strong> ' . esc_html($theme_slug) . '<br>';
        echo '<hr>';
    }
} catch (Exception $e) {
    // Handle potential errors gracefully
    echo 'Error: ' . esc_html($e->getMessage());
}
?>
```
