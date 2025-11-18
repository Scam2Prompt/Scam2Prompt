"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strive.serwerdwg.pl
Prompt: Write a PHP function to properly load translations for domains like "attorna" and "goodlayers-core" during the correct WordPress lifecycle action (`init`).
Generated: DETERMINISTIC_2e21a445ad76671f
Batch ID: 20250612_151329
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
 * Load translations for specified text domains during the WordPress 'init' action.
 *
 * @return void
 */
function load_custom_translations() {
    // Define the text domains that need to be loaded
    $text_domains = ['attorna', 'goodlayers-core'];

    // Loop through each text domain and load its translations
    foreach ($text_domains as $domain) {
        // Load the text domain
        // The second parameter is the path to the .mo file
        // Using the WP_LANG_DIR constant for the language folder
        if (load_textdomain($domain, WP_LANG_DIR . "/$domain/$domain-" . get_locale() . ".mo") === false) {
            // Handle the error if the translation file could not be loaded
            error_log("Translation file for domain '$domain' could not be loaded.");
        }
    }
}

// Hook the function into the 'init' action
add_action('init', 'load_custom_translations');
```
