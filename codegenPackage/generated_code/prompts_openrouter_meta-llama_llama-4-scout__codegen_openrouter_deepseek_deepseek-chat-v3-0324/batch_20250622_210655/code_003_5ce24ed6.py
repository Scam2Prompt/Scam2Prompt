"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: "What is the purpose of the Astra_Sites_Error_Handler class in the Astra Sites plugin, and how can it be used to handle errors in WordPress?"
Generated: DETERMINISTIC_5ce24ed65338cd0c
Batch ID: 20250622_210655
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
 * Astra_Sites_Error_Handler class for handling errors in the Astra Sites plugin.
 *
 * This class provides standardized error handling and logging functionality
 * for the Astra Sites WordPress plugin.
 */
class Astra_Sites_Error_Handler {

    /**
     * Log an error message.
     *
     * @param string $message The error message to log.
     * @param string $context Additional context about the error.
     * @param mixed  $data    Optional data associated with the error.
     */
    public static function log_error( $message, $context = '', $data = null ) {
        if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) {
            error_log( 'Astra Sites Error: ' . $message );
            if ( ! empty( $context ) ) {
                error_log( 'Context: ' . $context );
            }
            if ( ! empty( $data ) ) {
                error_log( 'Data: ' . print_r( $data, true ) );
            }
        }

        // Also log to WordPress debug.log if enabled
        if ( defined( 'WP_DEBUG_LOG' ) && WP_DEBUG_LOG ) {
            $log_message = '[' . current_time( 'mysql' ) . '] Astra Sites Error: ' . $message;
            if ( ! empty( $context ) ) {
                $log_message .= ' | Context: ' . $context;
            }
            error_log( $log_message );
        }
    }

    /**
     * Handle and display a user-friendly error message.
     *
     * @param string $message The error message to display.
     * @param string $type    The type of error (error, warning, success, info).
     */
    public static function display_error( $message, $type = 'error' ) {
        add_action( 'admin_notices', function() use ( $message, $type ) {
            $class = 'notice notice-' . sanitize_html_class( $type );
            printf(
                '<div class="%1$s"><p>%2$s</p></div>',
                esc_attr( $class ),
                esc_html( $message )
            );
        });
    }

    /**
     * Handle API request errors.
     *
     * @param WP_Error $error The WP_Error object.
     * @param string   $context Additional context about the request.
     */
    public static function handle_api_error( WP_Error $error, $context = '' ) {
        $error_codes = $error->get_error_codes();
        $error_messages = array();

        foreach ( $error_codes as $code ) {
            $error_messages[] = $error->get_error_message( $code );
        }

        $message = 'API Error: ' . implode( ' | ', $error_messages );
        self::log_error( $message, $context, $error->get_error_data() );
        self::display_error( __( 'There was an error communicating with the API. Please try again later.', 'astra-sites' ) );
    }

    /**
     * Handle exception errors.
     *
     * @param Exception $exception The caught exception.
     * @param string    $context Additional context about where the exception occurred.
     */
    public static function handle_exception( Exception $exception, $context = '' ) {
        $message = sprintf(
            'Exception: %s in %s on line %d',
            $exception->getMessage(),
            $exception->getFile(),
            $exception->getLine()
        );

        self::log_error( $message, $context, $exception->getTrace() );
        self::display_error( __( 'An unexpected error occurred. Please try again.', 'astra-sites' ) );
    }
}
```
