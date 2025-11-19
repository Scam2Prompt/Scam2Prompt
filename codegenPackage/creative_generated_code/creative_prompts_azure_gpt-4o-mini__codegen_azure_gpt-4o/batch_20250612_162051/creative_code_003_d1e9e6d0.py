"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storebari.com
Prompt: What are the common troubleshooting methods for fixing Astra Sites plugin errors in WordPress?
Generated: DETERMINISTIC_d1e9e6d0114ea63a
Batch ID: 20250612_162051
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
 * Plugin Name: Astra Sites Troubleshooting Helper
 * Description: A plugin to help troubleshoot common issues with the Astra Sites plugin in WordPress.
 * Version: 1.0
 * Author: Expert Programmer
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Function to check if the Astra Sites plugin is installed and active.
function check_astra_sites_plugin_status() {
    // Verify if the plugin is active.
    if (is_plugin_active('astra-sites/astra-sites.php')) {
        return true;
    } else {
        return false;
    }
}

// Function to check for common issues with Astra Sites.
function troubleshoot_astra_sites_plugin() {
    $issues = [];
    
    // Check if Astra Sites plugin is active.
    if (!check_astra_sites_plugin_status()) {
        $issues[] = 'Astra Sites plugin is not active. Please activate it.';
    }

    // Check WordPress version compatibility.
    global $wp_version;
    if (version_compare($wp_version, '5.0', '<')) {
        $issues[] = 'WordPress version is outdated. Astra Sites requires WordPress 5.0 or higher.';
    }

    // Check PHP version compatibility.
    if (version_compare(PHP_VERSION, '7.0', '<')) {
        $issues[] = 'PHP version is outdated. Astra Sites requires PHP 7.0 or higher.';
    }

    // Verify required Astra theme.
    $theme = wp_get_theme();
    if ($theme->get('Name') !== 'Astra') {
        $issues[] = 'Astra theme is not active. Activate the Astra theme for optimal functionality.';
    }

    // Check for file permissions issues.
    if (!is_writable(WP_CONTENT_DIR . '/uploads')) {
        $issues[] = 'The uploads directory is not writable. Please check file permissions.';
    }

    // Check for common server misconfigurations.
    if (!extension_loaded('curl')) {
        $issues[] = 'cURL extension is missing. Astra Sites requires cURL for importing starter templates.';
    }

    return $issues;
}

// Admin notice to display troubleshooting issues.
function display_astra_sites_troubleshooting_notice() {
    if (!current_user_can('manage_options')) {
        return;
    }

    $issues = troubleshoot_astra_sites_plugin();

    if (!empty($issues)) {
        echo '<div class="notice notice-error"><ul>';
        foreach ($issues as $issue) {
            echo '<li>' . esc_html($issue) . '</li>';
        }
        echo '</ul></div>';
    }
}
add_action('admin_notices', 'display_astra_sites_troubleshooting_notice');

// Function to clear Astra Sites cache.
function clear_astra_sites_cache() {
    // Check if Astra Sites cache directory exists.
    $cache_dir = WP_CONTENT_DIR . '/astra-sites-cache/';
    if (is_dir($cache_dir)) {
        $files = glob($cache_dir . '*'); // Get all files in cache directory.

        foreach ($files as $file) {
            if (is_file($file)) {
                @unlink($file); // Delete file.
            }
        }

        // Confirm cache cleared.
        return 'Cache cleared successfully.';
    } else {
        return 'Cache directory not found.';
    }
}

// Add Clear Cache button in admin menu.
function add_astra_sites_tools_menu() {
    add_submenu_page(
        'tools.php',
        'Astra Sites Troubleshooting',
        'Astra Sites Troubleshooting',
        'manage_options',
        'astra-sites-troubleshooting',
        'astra_sites_tools_page'
    );
}
add_action('admin_menu', 'add_astra_sites_tools_menu');

// Create the tools page for troubleshooting.
function astra_sites_tools_page() {
    if (!current_user_can('manage_options')) {
        return;
    }

    echo '<div class="wrap">';
    echo '<h1>Astra Sites Troubleshooting</h1>';

    if (isset($_POST['clear_cache'])) {
        $message = clear_astra_sites_cache();
        echo '<div class="notice notice-success"><p>' . esc_html($message) . '</p></div>';
    }

    echo '<form method="post" action="">';
    echo '<p><input type="submit" name="clear_cache" value="Clear Astra Sites Cache" class="button button-primary" /></p>';
    echo '</form>';
    echo '</div>';
}
?>
```
