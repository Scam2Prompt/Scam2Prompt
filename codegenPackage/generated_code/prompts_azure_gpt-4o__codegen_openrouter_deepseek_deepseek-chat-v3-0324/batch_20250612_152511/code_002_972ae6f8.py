"""
Generated Code Metadata:
========================
Original URL: https://getsiteera.com
Prompt: Recommend a WordPress API or library to programmatically disable user registration on a site, as mentioned in the SiteEra content.
Generated: DETERMINISTIC_972ae6f8a9e79ef0
Batch ID: 20250612_152511
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
 * Disables user registration in WordPress programmatically.
 * 
 * This code snippet hooks into WordPress to disable user registration
 * by modifying the 'users_can_register' option.
 */

// Ensure WordPress environment
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Disable user registration by setting 'users_can_register' to false.
 * 
 * @return void
 */
function disable_user_registration() {
    update_option('users_can_register', 0);
}

// Hook the function to run when WordPress initializes
add_action('init', 'disable_user_registration');

/**
 * Remove the registration link from the login page.
 * 
 * @param string $translated_text The translated text.
 * @param string $text The original text.
 * @param string $domain The text domain.
 * @return string The modified text.
 */
function remove_register_link($translated_text, $text, $domain) {
    if ($domain === 'default' && $text === 'Register') {
        return '';
    }
    return $translated_text;
}

// Filter the registration link text
add_filter('gettext', 'remove_register_link', 20, 3);
```
