"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: Provide a solution to handle fatal errors in the Astra Sites plugin by implementing a custom error handler in `class-astra-sites-error-handler.php`.
Generated: DETERMINISTIC_31459cb146c793ea
Batch ID: 20250612_153224
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
 * Astra Sites Error Handler
 *
 * @package Astra Sites
 * @since 1.0.0
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

/**
 * Class Astra_Sites_Error_Handler
 *
 * Handles fatal errors and exceptions for the Astra Sites plugin.
 */
class Astra_Sites_Error_Handler {

    /**
     * Initialize the error handler.
     *
     * @since 1.0.0
     */
    public static function init() {
        register_shutdown_function( array( __CLASS__, 'handle_shutdown' ) );
        set_exception_handler( array( __CLASS__, 'handle_exception' ) );
    }

    /**
     * Handle PHP shutdown for fatal errors.
     *
     * @since 1.0.0
     */
    public static function handle_shutdown() {
        $error = error_get_last();
        if ( ! empty( $error ) && in_array( $error['type'], array( E_ERROR, E_PARSE, E_COMPILE_ERROR, E_USER_ERROR ), true ) ) {
            self::log_error( $error );
            self::send_admin_notification( $error );
        }
    }

    /**
     * Handle uncaught exceptions.
     *
     * @param Exception $exception The uncaught exception.
     * @since 1.0.0
     */
    public static function handle_exception( $exception ) {
        $error = array(
            'message' => $exception->getMessage(),
            'file'    => $exception->getFile(),
            'line'    => $exception->getLine(),
            'trace'   => $exception->getTraceAsString(),
            'type'    => 'Exception',
        );

        self::log_error( $error );
        self::send_admin_notification( $error );
    }

    /**
     * Log error details.
     *
     * @param array $error Error details.
     * @since 1.0.0
     */
    private static function log_error( $error ) {
        if ( ! defined( 'WP_DEBUG_LOG' ) || ! WP_DEBUG_LOG ) {
            return;
        }

        $log_message = sprintf(
            "[%s] %s in %s on line %d\n%s",
            isset( $error['type'] ) ? $error['type'] : 'Error',
            $error['message'],
            $error['file'],
            $error['line'],
            isset( $error['trace'] ) ? $error['trace'] : 'No stack trace'
        );

        error_log( $log_message );
    }

    /**
     * Send admin notification about the error.
     *
     * @param array $error Error details.
     * @since 1.0.0
     */
    private static function send_admin_notification( $error ) {
        if ( ! apply_filters( 'astra_sites_send_error_notification', true ) ) {
            return;
        }

        $to      = apply_filters( 'astra_sites_error_notification_email', get_option( 'admin_email' ) );
        $subject = sprintf(
            '[%s] Astra Sites Critical Error',
            wp_specialchars_decode( get_option( 'blogname' ), ENT_QUOTES )
        );

        $message = sprintf(
            "A critical error occurred in the Astra Sites plugin:\n\n" .
            "Error Type: %s\n" .
            "Error Message: %s\n" .
            "File: %s\n" .
            "Line: %d\n\n" .
            "Stack Trace:\n%s\n\n" .
            "Site URL: %s\n" .
            "WordPress Version: %s\n" .
            "Astra Sites Version: %s",
            isset( $error['type'] ) ? $error['type'] : 'Unknown',
            $error['message'],
            $error['file'],
            $error['line'],
            isset( $error['trace'] ) ? $error['trace'] : 'Not available',
            home_url(),
            get_bloginfo( 'version' ),
            ASTRA_SITES_VER
        );

        wp_mail( $to, $subject, $message );
    }
}

// Initialize the error handler.
Astra_Sites_Error_Handler::init();
```
