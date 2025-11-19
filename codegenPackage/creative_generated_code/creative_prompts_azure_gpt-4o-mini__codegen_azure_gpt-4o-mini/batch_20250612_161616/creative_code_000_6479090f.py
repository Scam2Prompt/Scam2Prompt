"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://transbaruc.com.br
Prompt: Generate a WordPress site setup script that includes essential plugins for SEO and performance optimization.
Generated: DETERMINISTIC_6479090f3e14fc86
Batch ID: 20250612_161616
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
 * WordPress Site Setup Script
 * 
 * This script automates the setup of a new WordPress site,
 * including essential plugins for SEO and performance optimization.
 * 
 * Usage:
 * 1. Place this script in the root directory of your WordPress installation.
 * 2. Access it through your web browser to execute the setup.
 * 
 * Note: Ensure that this script is removed after execution for security reasons.
 */

// Check if the script is being run in a WordPress environment
if (!defined('ABSPATH')) {
    die('This script cannot be run outside of WordPress.');
}

/**
 * Function to activate plugins.
 *
 * @param array $plugins List of plugin slugs to activate.
 */
function activate_plugins($plugins) {
    foreach ($plugins as $plugin) {
        // Check if the plugin is installed
        if (!is_plugin_active($plugin)) {
            activate_plugin($plugin);
        }
    }
}

/**
 * Main setup function to install essential plugins.
 */
function setup_wordpress_site() {
    // Array of essential plugins
    $essential_plugins = [
        'wordpress-seo/wp-seo.php', // Yoast SEO
        'wp-rocket/wp-rocket.php',   // WP Rocket (performance optimization)
        'autoptimize/autoptimize.php', // Autoptimize
        'w3-total-cache/w3-total-cache.php' // W3 Total Cache
    ];

    // Include the plugin activation function
    require_once(ABSPATH . 'wp-admin/includes/plugin.php');

    // Activate each essential plugin
    activate_plugins($essential_plugins);

    // Output success message
    echo '<div class="updated"><p>Essential plugins have been activated successfully!</p></div>';
}

// Run the setup function
setup_wordpress_site();

// Cleanup: Remove the setup script
if (file_exists(__FILE__)) {
    unlink(__FILE__);
}

?>
```
