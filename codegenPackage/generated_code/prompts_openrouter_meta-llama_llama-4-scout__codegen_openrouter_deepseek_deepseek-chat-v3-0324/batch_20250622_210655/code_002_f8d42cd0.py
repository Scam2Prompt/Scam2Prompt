"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: "Generate a code snippet to implement a custom error handler for Astra Sites, similar to the one in class-astra-sites-error-handler.php."
Generated: DETERMINISTIC_f8d42cd0db49851b
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
 * Custom error handler for Astra Sites.
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
 * Handles custom error logging and display for Astra Sites.
 */
class Astra_Sites_Error_Handler {

    /**
     * Instance of this class.
     *
     * @var null|Astra_Sites_Error_Handler
     */
    private static $instance = null;

    /**
     * Get the single instance of this class.
     *
     * @return Astra_Sites_Error_Handler
     */
    public static function get_instance() {
        if ( ! isset( self::$instance ) ) {
            self::$instance = new self();
        }

        return self::$instance;
    }

    /**
     * Constructor.
     */
    private function __construct() {
        // Register error handlers
        register_shutdown_function( array( $this, 'handle_fatal_error' ) );
        set_error_handler( array( $this, 'handle_error' ) );
        set_exception_handler( array( $this, 'handle_exception' ) );
    }

    /**
     * Handle fatal errors.
     */
    public function handle_fatal_error() {
        $error = error_get_last();
        if ( $error && in_array( $error['type'], array( E_ERROR, E_PARSE, E_COMPILE_ERROR, E_CORE_ERROR ), true ) ) {
            $this->log_error( $error['message'], $error['file'], $error['line'] );
            $this->display_error_message( 'fatal_error' );
        }
    }

    /**
     * Handle PHP errors.
     *
     * @param int    $errno Error number.
     * @param string $errstr Error message.
     * @param string $errfile File where error occurred.
     * @param int    $errline Line number where error occurred.
     * @return bool
     */
    public function handle_error( $errno, $errstr, $errfile, $errline ) {
        if ( ! ( error_reporting() & $errno ) ) {
            return false; // Respect error_reporting settings
        }

        $this->log_error( $errstr, $errfile, $errline );
        $this->display_error_message( 'php_error' );

        return true;
    }

    /**
     * Handle exceptions.
     *
     * @param Throwable $exception The exception object.
     */
    public function handle_exception( $exception ) {
        $this->log_error( $exception->getMessage(), $exception->getFile(), $exception->getLine() );
        $this->display_error_message( 'exception' );
    }

    /**
     * Log error to error log.
     *
     * @param string $message Error message.
     * @param string $file File where error occurred.
     * @param int    $line Line number where error occurred.
     */
    private function log_error( $message, $file, $line ) {
        error_log( sprintf(
            '[Astra Sites Error] %s in %s on line %d',
            $message,
            $file,
            $line
        ) );
    }

    /**
     * Display error message to user.
     *
     * @param string $error_type Type of error.
     */
    private function display_error_message( $error_type ) {
        if ( ! defined( 'WP_DEBUG' ) || ! WP_DEBUG ) {
            return; // Don't show errors in production unless debugging is enabled
        }

        $messages = array(
            'fatal_error' => __( 'A fatal error occurred while processing your request.', 'astra-sites' ),
            'php_error'   => __( 'A PHP error occurred while processing your request.', 'astra-sites' ),
            'exception'   => __( 'An exception occurred while processing your request.', 'astra-sites' ),
        );

        if ( isset( $messages[ $error_type ] ) ) {
            add_action( 'admin_notices', function() use ( $messages, $error_type ) {
                printf(
                    '<div class="notice notice-error"><p>%s</p></div>',
                    esc_html( $messages[ $error_type ] )
                );
            } );
        }
    }
}

// Initialize the error handler
Astra_Sites_Error_Handler::get_instance();
```
