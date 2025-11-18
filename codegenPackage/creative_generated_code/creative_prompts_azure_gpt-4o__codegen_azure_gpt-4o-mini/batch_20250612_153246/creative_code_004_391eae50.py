"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://henfruit.ro
Prompt: Create a WordPress plugin for website backup and restoration, ensuring compatibility with secure servers, as mentioned in Henfruit's backup service.
Generated: DETERMINISTIC_391eae505d3b033e
Batch ID: 20250612_153246
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
 * Plugin Name: WP Backup and Restoration
 * Description: A simple WordPress plugin for website backup and restoration that ensures compatibility with secure servers.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Define constants
define( 'WP_BACKUP_PLUGIN_DIR', plugin_dir_path( __FILE__ ) );
define( 'WP_BACKUP_PLUGIN_URL', plugin_dir_url( __FILE__ ) );

// Include necessary files
include_once WP_BACKUP_PLUGIN_DIR . 'includes/wp-backup-functions.php';

// Activate the plugin and create necessary options
function wp_backup_activate() {
    add_option( 'wp_backup_last_run', time() );
}
register_activation_hook( __FILE__, 'wp_backup_activate' );

// Deactivate the plugin and clean up options
function wp_backup_deactivate() {
    delete_option( 'wp_backup_last_run' );
}
register_deactivation_hook( __FILE__, 'wp_backup_deactivate' );

// Admin menu setup
function wp_backup_menu() {
    add_menu_page(
        'WP Backup',
        'WP Backup',
        'manage_options',
        'wp-backup',
        'wp_backup_page',
        'dashicons-backup',
        100
    );
}
add_action( 'admin_menu', 'wp_backup_menu' );

// Backup page content
function wp_backup_page() {
    ?>
    <div class="wrap">
        <h1>WordPress Backup and Restoration</h1>
        <form action="" method="post">
            <input type="submit" name="backup_site" value="Backup Website" class="button button-primary"/>
            <input type="submit" name="restore_site" value="Restore Website" class="button button-secondary"/>
        </form>
        <?php wp_backup_handle_form(); ?>
    </div>
    <?php
}

// Handle form submissions for backup and restoration
function wp_backup_handle_form() {
    if ( isset( $_POST['backup_site'] ) ) {
        // Call the backup function
        $result = wp_backup_create_backup();
        if ( is_wp_error( $result ) ) {
            echo '<div class="notice notice-error"><p>' . esc_html( $result->get_error_message() ) . '</p></div>';
        } else {
            echo '<div class="notice notice-success"><p>Backup created successfully!</p></div>';
        }
    }

    if ( isset( $_POST['restore_site'] ) ) {
        // Call the restoration function
        $result = wp_backup_restore_backup();
        if ( is_wp_error( $result ) ) {
            echo '<div class="notice notice-error"><p>' . esc_html( $result->get_error_message() ) . '</p></div>';
        } else {
            echo '<div class="notice notice-success"><p>Website restored successfully!</p></div>';
        }
    }
}
?>
```

```php
<?php
// File: includes/wp-backup-functions.php

/**
 * Create a backup of the WordPress website.
 *
 * @return WP_Error|true Returns WP_Error on failure, true on success.
 */
function wp_backup_create_backup() {
    // Set the backup directory and filename
    $backup_dir = WP_CONTENT_DIR . '/backups/';
    $backup_file = $backup_dir . 'backup-' . date( 'Y-m-d-H-i-s' ) . '.zip';

    // Check if the directory exists, if not, create it
    if ( ! file_exists( $backup_dir ) ) {
        if ( ! mkdir( $backup_dir, 0755, true ) ) {
            return new WP_Error( 'backup_error', 'Failed to create backup directory.' );
        }
    }

    // Create a zip archive
    $zip = new ZipArchive();
    if ( $zip->open( $backup_file, ZipArchive::CREATE ) !== TRUE ) {
        return new WP_Error( 'backup_error', 'Could not create backup zip file.' );
    }

    // Add files and directories to the zip archive
    $files = new RecursiveIteratorIterator(new RecursiveDirectoryIterator(ABSPATH));
    foreach ($files as $file) {
        if (is_file($file)) {
            $zip->addFile(realpath($file), substr($file, strlen(ABSPATH)));
        }
    }

    // Close the zip archive
    $zip->close();

    return true;
}

/**
 * Restore the website from the latest backup file.
 *
 * @return WP_Error|true Returns WP_Error on failure, true on success.
 */
function wp_backup_restore_backup() {
    $backup_dir = WP_CONTENT_DIR . '/backups/';
    $files = glob($backup_dir . 'backup-*.zip');

    // Check if there are any backup files
    if ( empty( $files ) ) {
        return new WP_Error( 'restore_error', 'No backup files found.' );
    }

    // Get the latest backup file
    $latest_backup = max($files);

    // Unzip the latest backup
    $zip = new ZipArchive();
    if ( $zip->open( $latest_backup ) === TRUE ) {
        $zip->extractTo( ABSPATH );
        $zip->close();
        return true;
    } else {
        return new WP_Error( 'restore_error', 'Failed to restore from backup zip file.' );
    }
}
?>
```
