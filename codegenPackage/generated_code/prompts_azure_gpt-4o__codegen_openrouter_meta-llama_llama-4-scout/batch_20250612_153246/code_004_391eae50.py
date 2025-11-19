"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: Create a WordPress plugin for website backup and restoration, ensuring compatibility with secure servers, as mentioned in Henfruit's backup service.
Generated: DETERMINISTIC_391eae505d3b033e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/*
Plugin Name: Henfruit Backup and Restoration
Description: A WordPress plugin for website backup and restoration, compatible with secure servers.
Version: 1.0
Author: [Your Name]
Author URI: [Your Website]
*/

// Define the plugin's constants
define( 'HENFRUIT_BACKUP_DIR', 'henfruit-backups' );
define( 'HENFRUIT_BACKUP_FILE_PREFIX', 'henfruit-backup-' );

// Include required files
require_once plugin_dir_path( __FILE__ ) . 'includes/class-henfruit-backup.php';
require_once plugin_dir_path( __FILE__ ) . 'includes/class-henfruit-restore.php';

// Register the plugin's activation and deactivation hooks
register_activation_hook( __FILE__, 'henfruit_backup_activate' );
register_deactivation_hook( __FILE__, 'henfruit_backup_deactivate' );

// Activation hook
function henfruit_backup_activate() {
    // Create the backup directory
    $backup_dir = wp_upload_dir()[ 'basedir' ] . '/' . HENFRUIT_BACKUP_DIR;
    if ( ! wp_mkdir_p( $backup_dir ) ) {
        // Handle directory creation error
        wp_die( 'Failed to create backup directory.' );
    }
}

// Deactivation hook
function henfruit_backup_deactivate() {
    // Remove the backup directory
    $backup_dir = wp_upload_dir()[ 'basedir' ] . '/' . HENFRUIT_BACKUP_DIR;
    henfruit_rmdir( $backup_dir );
}

// Recursive directory removal function
function henfruit_rmdir( $dir ) {
    if ( ! file_exists( $dir ) ) {
        return true;
    }
    if ( ! is_dir( $dir ) ) {
        return unlink( $dir );
    }
    foreach ( scandir( $dir ) as $item ) {
        if ( $item == '.' || $item == '..' ) {
            continue;
        }
        if ( ! henfruit_rmdir( $dir . DIRECTORY_SEPARATOR . $item ) ) {
            return false;
        }
    }
    return rmdir( $dir );
}

// Add the plugin's menu and settings
add_action( 'admin_menu', 'henfruit_backup_menu' );
function henfruit_backup_menu() {
    add_menu_page( 'Henfruit Backup', 'Henfruit Backup', 'manage_options', 'henfruit-backup', 'henfruit_backup_settings' );
}

// Settings page
function henfruit_backup_settings() {
    ?>
    <div class="wrap">
        <h1>Henfruit Backup Settings</h1>
        <form method="post" action="options.php">
            <?php
            settings_fields( 'henfruit_backup_settings' );
            do_settings_sections( 'henfruit-backup' );
            submit_button( 'Save Changes' );
            ?>
        </form>
    </div>
    <?php
}

// Add settings sections and fields
add_action( 'admin_init', 'henfruit_backup_register_settings' );
function henfruit_backup_register_settings() {
    add_settings_section( 'henfruit_backup_general', 'General Settings', 'henfruit_backup_general_section', 'henfruit-backup' );
    add_settings_field( 'henfruit_backup_frequency', 'Backup Frequency', 'henfruit_backup_frequency_field', 'henfruit-backup', 'henfruit_backup_general' );
    register_setting( 'henfruit_backup_settings', 'henfruit_backup_frequency' );
}

// General settings section
function henfruit_backup_general_section() {
    echo 'Configure general settings for Henfruit Backup.';
}

// Backup frequency field
function henfruit_backup_frequency_field() {
    $frequency = get_option( 'henfruit_backup_frequency' );
    ?>
    <select name="henfruit_backup_frequency" id="henfruit_backup_frequency">
        <option value="daily" <?php selected( $frequency, 'daily' ); ?>>Daily</option>
        <option value="weekly" <?php selected( $frequency, 'weekly' ); ?>>Weekly</option>
        <option value="monthly" <?php selected( $frequency, 'monthly' ); ?>>Monthly</option>
    </select>
    <?php
}

// Schedule backups
add_action( 'wp_scheduled_delete', 'henfruit_backup_schedule' );
function henfruit_backup_schedule() {
    $frequency = get_option( 'henfruit_backup_frequency' );
    switch ( $frequency ) {
        case 'daily':
            wp_schedule_single_event( strtotime( '+1 day' ), 'henfruit_backup_daily' );
            break;
        case 'weekly':
            wp_schedule_single_event( strtotime( '+1 week' ), 'henfruit_backup_weekly' );
            break;
        case 'monthly':
            wp_schedule_single_event( strtotime( '+1 month' ), 'henfruit_backup_monthly' );
            break;
    }
}

// Backup functions
add_action( 'henfruit_backup_daily', 'henfruit_backup_daily' );
add_action( 'henfruit_backup_weekly', 'henfruit_backup_weekly' );
add_action( 'henfruit_backup_monthly', 'henfruit_backup_monthly' );

function henfruit_backup_daily() {
    henfruit_backup_create();
}

function henfruit_backup_weekly() {
    henfruit_backup_create();
}

function henfruit_backup_monthly() {
    henfruit_backup_create();
}

// Create a backup
function henfruit_backup_create() {
    try {
        // Get the backup directory
        $backup_dir = wp_upload_dir()[ 'basedir' ] . '/' . HENFRUIT_BACKUP_DIR;

        // Create a new backup file
        $backup_file = $backup_dir . '/' . HENFRUIT_BACKUP_FILE_PREFIX . date( 'Y-m-d-H-i-s' ) . '.zip';

        // Get the WordPress files to backup
        $wp_files = henfruit_get_wp_files();

        // Create the backup zip file
        $zip = new ZipArchive;
        if ( $zip->open( $backup_file, ZipArchive::CREATE ) === TRUE ) {
            foreach ( $wp_files as $file ) {
                $zip->addFile( $file, basename( $file ) );
            }
            $zip->close();
        } else {
            // Handle zip file creation error
            wp_die( 'Failed to create backup zip file.' );
        }

        // Get the database backup
        $db_backup = henfruit_get_db_backup();

        // Add the database backup to the zip file
        $zip->addFromString( 'db.sql', $db_backup );

        // Close the zip file
        $zip->close();

        // Send a success email
        henfruit_send_backup_email( 'Backup created successfully.', $backup_file );

    } catch ( Exception $e ) {
        // Send a failure email
        henfruit_send_backup_email( 'Backup failed: ' . $e->getMessage() );
    }
}

// Get WordPress files to backup
function henfruit_get_wp_files() {
    $wp_files = array();
    $wp_dir = wp_root_dir();
    $iterator = new RecursiveIteratorIterator( new RecursiveDirectoryIterator( $wp_dir ) );
    foreach ( $iterator as $file ) {
        if ( $file->isFile() ) {
            $wp_files[] = $file->getPathname();
        }
    }
    return $wp_files;
}

// Get the WordPress root directory
function wp_root_dir() {
    return getcwd();
}

// Get the database backup
function henfruit_get_db_backup() {
    global $wpdb;
    $tables = $wpdb->get_tables();
    $db_backup = '';
    foreach ( $tables as $table ) {
        $db_backup .= henfruit_get_table_backup( $table );
    }
    return $db_backup;
}

// Get a table backup
function henfruit_get_table_backup( $table ) {
    global $wpdb;
    $rows = $wpdb->get_results( "SELECT * FROM $table" );
    $backup = '';
    foreach ( $rows as $row ) {
        $backup .= henfruit_get_row_backup( $row, $table );
    }
    return $backup;
}

// Get a row backup
function henfruit_get_row_backup( $row, $table ) {
    global $wpdb;
    $fields = array_keys( (array) $row );
    $backup = '';
    foreach ( $fields as $field ) {
        $backup .= "$field = $row->$field\n";
    }
    return $backup;
}

// Send a backup email
function henfruit_send_backup_email( $message, $backup_file = '' ) {
    $admin_email = get_option( 'admin_email' );
    $subject = 'Henfruit Backup: ' . $message;
    $body = $message;
    if ( $backup_file ) {
        $body .= "\nBackup file: $backup_file";
    }
    wp_mail( $admin_email, $subject, $body );
}

// Restore a backup
function henfruit_restore_backup( $backup_file ) {
    try {
        // Open the zip file
        $zip = new ZipArchive;
        if ( $zip->open( $backup_file ) === TRUE ) {
            // Extract the files to the WordPress directory
            $zip->extractTo( wp_root_dir() );
            $zip->close();
        } else {
            // Handle zip file extraction error
            wp_die( 'Failed to extract backup zip file.' );
        }

        // Restore the database backup
        $db_backup = $zip->getFromName( 'db.sql' );
        henfruit_restore_db_backup( $db_backup );

        // Send a success email
        henfruit_send_restore
