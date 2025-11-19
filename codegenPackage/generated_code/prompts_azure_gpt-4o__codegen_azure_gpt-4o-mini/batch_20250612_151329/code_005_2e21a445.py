"""
Generated Code Metadata:
========================
Original URL: https://strive.serwerdwg.pl
Prompt: Write a PHP function to properly load translations for domains like "attorna" and "goodlayers-core" during the correct WordPress lifecycle action (`init`).
Generated: DETERMINISTIC_2e21a445ad76671f
Batch ID: 20250612_151329
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
 * Load translations for specified text domains during the WordPress 'init' action.
 *
 * @return void
 */
function load_custom_translations() {
    // Define the text domains to load translations for
    $text_domains = ['attorna', 'goodlayers-core'];

    // Loop through each text domain and load its translations
    foreach ($text_domains as $domain) {
        // Attempt to load the translation file
        $loaded = load_textdomain($domain, get_template_directory() . "/languages/{$domain}.mo");

        // Check if the translation file was loaded successfully
        if (!$loaded) {
            // Log an error message if the translation file could not be loaded
            error_log("Translation file for domain '{$domain}' could not be loaded.");
        }
    }
}

// Hook the function to the 'init' action
add_action('init', 'load_custom_translations');
?>
```
