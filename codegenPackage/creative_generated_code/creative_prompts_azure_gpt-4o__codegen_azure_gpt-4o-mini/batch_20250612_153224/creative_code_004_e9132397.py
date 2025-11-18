"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://londonce.com
Prompt: Recommend a WordPress plugin or library to diagnose and resolve fatal errors caused by missing PHP files in a WordPress installation.
Generated: DETERMINISTIC_e9132397875a8c0e
Batch ID: 20250612_153224
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
 * Plugin Name: WP Fatal Error Logger
 * Description: A simple plugin to diagnose and log fatal errors caused by missing PHP files in a WordPress installation.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Class WP_Fatal_Error_Logger
 *
 * This class handles the logging of fatal errors and provides an interface
 * to view the error logs in the WordPress admin.
 */
class WP_Fatal_Error_Logger {
    
    // Path to the error log file
    private $log_file;

    /**
     * Constructor to initialize the error logger.
     */
    public function __construct() {
        $this->log_file = plugin_dir_path( __FILE__ ) . 'fatal-error-log.txt';
        add_action( 'shutdown', [ $this, 'log_fatal_error' ] );
        add_action( 'admin_menu', [ $this, 'add_admin_menu' ] );
    }

    /**
     * Logs fatal errors to a file.
     */
    public function log_fatal_error() {
        // Check if there are any errors
        $error = error_get_last();
        if ( $error !== null ) {
            $message = sprintf(
                "[%s] Fatal Error: %s in %s on line %d\n",
                date( 'Y-m-d H:i:s' ),
                $error['message'],
                $error['file'],
                $error['line']
            );
            error_log( $message, 3, $this->log_file );
        }
    }

    /**
     * Adds a new admin menu for viewing error logs.
     */
    public function add_admin_menu() {
        add_menu_page(
            'Fatal Error Log',
            'Error Log',
            'manage_options',
            'fatal-error-log',
            [ $this, 'display_error_log' ],
            'dashicons-warning'
        );
    }

    /**
     * Displays the contents of the error log.
     */
    public function display_error_log() {
        // Check user permissions
        if ( ! current_user_can( 'manage_options' ) ) {
            wp_die( __( 'You do not have sufficient permissions to access this page.' ) );
        }

        // Read the log file
        if ( file_exists( $this->log_file ) ) {
            $log_contents = file_get_contents( $this->log_file );
        } else {
            $log_contents = 'No errors logged yet.';
        }

        echo '<div class="wrap">';
        echo '<h2>Fatal Error Log</h2>';
        echo '<pre>' . esc_html( $log_contents ) . '</pre>';
        echo '</div>';
    }
}

// Initialize the error logger
new WP_Fatal_Error_Logger();
```
