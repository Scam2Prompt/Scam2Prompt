"""
Generated Code Metadata:
========================
Original URL: https://coinbase.699539.com
Prompt: Create a WordPress script to automatically restore the site to a previous backup when a critical error occurs.
Generated: DETERMINISTIC_b244e580b1fab648
Batch ID: 20250612_154158
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
 * Plugin Name: Auto Restore on Critical Error
 * Description: Automatically restores the site to a previous backup when a critical error occurs.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Class AutoRestore
 * Handles the automatic restoration of the site on critical errors.
 */
class AutoRestore {

    /**
     * Constructor to initialize the plugin.
     */
    public function __construct() {
        // Hook into the shutdown process to check for fatal errors
        add_action( 'shutdown', array( $this, 'check_for_fatal_error' ) );
    }

    /**
     * Checks for fatal errors and triggers the restore process if found.
     */
    public function check_for_fatal_error() {
        // Check if there are any errors in the error log
        $error = error_get_last();
        if ( $error !== null ) {
            // Log the error for debugging purposes
            error_log( 'Fatal error detected: ' . print_r( $error, true ) );

            // Attempt to restore the site from the latest backup
            $this->restore_from_backup();
        }
    }

    /**
     * Restores the site from the latest backup.
     */
    private function restore_from_backup() {
        // Define the backup directory and the latest backup file
        $backup_dir = WP_CONTENT_DIR . '/backups/';
        $latest_backup = $this->get_latest_backup( $backup_dir );

        if ( $latest_backup ) {
            // Perform the restoration process
            $this->execute_restore( $latest_backup );
        } else {
            error_log( 'No backup found to restore.' );
        }
    }

    /**
     * Retrieves the latest backup file from the backup directory.
     *
     * @param string $backup_dir The directory where backups are stored.
     * @return string|false The path to the latest backup file or false if none found.
     */
    private function get_latest_backup( $backup_dir ) {
        // Check if the backup directory exists
        if ( ! is_dir( $backup_dir ) ) {
            return false;
        }

        // Get all backup files
        $files = glob( $backup_dir . '*.zip' );

        // Sort files by modification time
        usort( $files, function( $a, $b ) {
            return filemtime( $b ) - filemtime( $a );
        });

        // Return the latest backup file or false if none found
        return ! empty( $files ) ? $files[0] : false;
    }

    /**
     * Executes the restoration process from the specified backup file.
     *
     * @param string $backup_file The path to the backup file.
     */
    private function execute_restore( $backup_file ) {
        // Unzip the backup file
        $zip = new ZipArchive;
        if ( $zip->open( $backup_file ) === TRUE ) {
            // Extract the contents to the WordPress root directory
            $zip->extractTo( ABSPATH );
            $zip->close();

            // Log the successful restoration
            error_log( 'Site restored from backup: ' . $backup_file );

            // Optionally, you can redirect to a success page or notify the admin
            // wp_redirect( admin_url() );
            // exit;
        } else {
            error_log( 'Failed to open backup file: ' . $backup_file );
        }
    }
}

// Initialize the AutoRestore class
new AutoRestore();
```

**Note:** Ensure that you have a backup mechanism in place that creates `.zip` files in the `wp-content/backups/` directory for this script to function correctly.
