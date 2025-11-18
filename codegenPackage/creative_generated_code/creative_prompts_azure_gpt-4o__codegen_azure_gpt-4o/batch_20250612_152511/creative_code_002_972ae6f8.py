"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsiteera.com
Prompt: Recommend a WordPress API or library to programmatically disable user registration on a site, as mentioned in the SiteEra content.
Generated: DETERMINISTIC_972ae6f8a9e79ef0
Batch ID: 20250612_152511
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
 * Plugin Name: Disable User Registration
 * Description: A WordPress plugin to programmatically disable user registration on the site.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

/**
 * Hook into the registration filter and disable user registration.
 *
 * @param bool $open Whether registration is open.
 * @return bool False to disable registration.
 */
function disable_user_registration($open) {
    // Return false to disable user registration globally.
    return false;
}
add_filter('register', 'disable_user_registration');

/**
 * Prevent users from accessing the registration page.
 */
function disable_registration_page_redirect() {
    // Check if the current page is the registration page.
    if (isset($_SERVER['REQUEST_URI']) && strpos($_SERVER['REQUEST_URI'], 'wp-login.php?action=register') !== false) {
        // Redirect to the homepage and exit.
        wp_redirect(home_url());
        exit;
    }
}
add_action('init', 'disable_registration_page_redirect');

/**
 * Show an admin notice that user registration is disabled.
 */
function notify_admin_registration_disabled() {
    // Only show the notice to administrators.
    if (current_user_can('manage_options')) {
        echo '<div class="notice notice-warning is-dismissible">';
        echo '<p>User registration is currently disabled on this site.</p>';
        echo '</div>';
    }
}
add_action('admin_notices', 'notify_admin_registration_disabled');
```
