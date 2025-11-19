"""
Generated Code Metadata:
========================
Original URL: https://strive.serwerdwg.pl
Prompt: Write a function in PHP to handle translation loading for a WordPress plugin, addressing the incorrect function call issue mentioned in the website's error messages.
Generated: DETERMINISTIC_30111d485006dcc8
Batch ID: 20250622_204740
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
 * Load translation files for a WordPress plugin.
 *
 * This function checks if the translation files exist for the specified locale
 * and loads them. It handles errors gracefully and ensures that the translations
 * are available for the plugin.
 *
 * @param string $plugin_slug The slug of the plugin.
 * @param string $locale The locale code (e.g., 'en_US').
 * @return void
 */
function load_plugin_translations($plugin_slug, $locale) {
    // Define the path to the languages directory
    $lang_dir = plugin_dir_path(__FILE__) . 'languages/';

    // Construct the translation file path
    $mo_file = $lang_dir . $plugin_slug . '-' . $locale . '.mo';

    // Check if the translation file exists
    if (file_exists($mo_file)) {
        // Load the translation file
        load_textdomain($plugin_slug, $mo_file);
    } else {
        // Log an error message if the translation file is not found
        error_log("Translation file not found: " . $mo_file);
    }
}

// Example usage: Load translations for a plugin with slug 'my-plugin'
add_action('plugins_loaded', function() {
    // Get the current locale
    $locale = get_locale();
    
    // Load translations for the plugin
    load_plugin_translations('my-plugin', $locale);
});
?>
```
