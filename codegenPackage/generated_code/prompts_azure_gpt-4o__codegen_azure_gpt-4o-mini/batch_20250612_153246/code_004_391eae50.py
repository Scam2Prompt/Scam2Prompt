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
/**
 * Plugin Name: Secure Backup and Restore
 * Description: A WordPress plugin for backing up and restoring website data, ensuring compatibility with secure servers.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class SecureBackup
 * Handles the backup and restoration of WordPress site data.
 */
class SecureBackup {

    // Directory to store backups
    private $backup_dir;

    public function __construct() {
        // Set the backup directory
        $this->backup_dir = WP_CONTENT_DIR . '/backups/';

        // Create backup directory if it doesn't exist
        if ( ! file_exists( $this->backup_dir ) ) {
            wp_mkdir_p( $this->backup_dir );
        }

        // Register admin menu
        add_action( 'admin_menu', array( $this, 'add_admin_menu' ) );
    }

    /**
     * Add admin menu for the plugin
     */
    public function add_admin_menu() {
        add_menu_page(
            'Secure Backup',
            'Secure Backup',
            'manage_options',
            'secure-backup',
            array( $this, 'backup_page' ),
            'dashicons-backup',
            100
        );
    }

    /**
     * Display the backup page
     */
    public function backup_page() {
        if ( isset( $_POST['backup'] ) ) {
            $this->create_backup();
        }

        if ( isset( $_POST['restore'] ) ) {
            $this->restore_backup();
        }

        ?>
        <div class="wrap">
            <h1>Secure Backup and Restore</h1>
            <form method="post">
                <input type="submit" name="backup" class="button button-primary" value="Create Backup">
                <input type="submit" name="restore" class="button button-secondary" value="Restore Backup">
            </form>
        </div>
        <?php
    }

    /**
     * Create a backup of the WordPress site
     */
    private function create_backup() {
        // Backup database
        global $wpdb;
        $tables = $wpdb->get_results( 'SHOW TABLES', ARRAY_N );
        $backup_file = $this->backup_dir . 'backup-' . date( 'Y-m-d_H-i-s' ) . '.sql';

        $sql = '';
        foreach ( $tables as $table ) {
            $table_name = $table[0];
            $create_table = $wpdb->get_row( "SHOW CREATE TABLE $table_name", ARRAY_N );
            $sql .= $create_table[1] . ";\n\n";

            $rows = $wpdb->get_results( "SELECT * FROM $table_name", ARRAY_A );
            foreach ( $rows as $row ) {
                $sql .= "INSERT INTO $table_name (" . implode( ', ', array_keys( $row ) ) . ") VALUES ('" . implode( "', '", array_map( 'esc_sql', array_values( $row ) ) ) . "');\n";
            }
            $sql .= "\n\n";
        }

        // Write to backup file
        if ( file_put_contents( $backup_file, $sql ) === false ) {
            wp_die( 'Error creating backup file.' );
        }

        echo '<div class="updated"><p>Backup created successfully: ' . esc_html( basename( $backup_file ) ) . '</p></div>';
    }

    /**
     * Restore the latest backup
     */
    private function restore_backup() {
        $files = glob( $this->backup_dir . '*.sql' );
        if ( empty( $files ) ) {
            wp_die( 'No backup files found.' );
        }

        // Sort files by date
        usort( $files, function( $a, $b ) {
            return filemtime( $b ) - filemtime( $a );
        });

        $latest_backup = $files[0];

        // Restore database from backup
        $sql = file_get_contents( $latest_backup );
        if ( $sql === false ) {
            wp_die( 'Error reading backup file.' );
        }

        // Execute SQL queries
        require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );
        dbDelta( $sql );

        echo '<div class="updated"><p>Database restored successfully from: ' . esc_html( basename( $latest_backup ) ) . '</p></div>';
    }
}

// Initialize the plugin
new SecureBackup();
```
