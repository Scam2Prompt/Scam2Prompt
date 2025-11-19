"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: How do I debug the Astra Sites plugin to identify the cause of the fatal error mentioned in the error stack trace?
Generated: DETERMINISTIC_b77eb2935347ca1b
Batch ID: 20250612_162051
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
 * Debugging script for Astra Sites plugin fatal errors.
 * 
 * This script helps identify the cause of fatal errors by enabling WP_DEBUG,
 * logging errors, and providing a stack trace.
 */

// Enable debugging
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );
@ini_set( 'display_errors', 0 );

// Register error handlers
set_error_handler( 'astra_sites_error_handler' );
set_exception_handler( 'astra_sites_exception_handler' );
register_shutdown_function( 'astra_sites_shutdown_handler' );

/**
 * Custom error handler for Astra Sites plugin.
 *
 * @param int    $errno   The error level
 * @param string $errstr  The error message
 * @param string $errfile The file where error occurred
 * @param int    $errline The line number where error occurred
 */
function astra_sites_error_handler( $errno, $errstr, $errfile, $errline ) {
    if ( ! ( error_reporting() & $errno ) ) {
        return false;
    }

    $error_type = '';
    switch ( $errno ) {
        case E_USER_ERROR:
            $error_type = 'Fatal Error';
            break;
        case E_USER_WARNING:
            $error_type = 'Warning';
            break;
        case E_USER_NOTICE:
            $error_type = 'Notice';
            break;
        default:
            $error_type = 'Unknown Error';
            break;
    }

    error_log( "[Astra Sites Debug] $error_type: $errstr in $errfile on line $errline" );
    return true;
}

/**
 * Custom exception handler for Astra Sites plugin.
 *
 * @param Throwable $exception The thrown exception
 */
function astra_sites_exception_handler( $exception ) {
    error_log( "[Astra Sites Debug] Uncaught exception: " . $exception->getMessage() . " in " . $exception->getFile() . ":" . $exception->getLine() );
    error_log( "Stack trace:\n" . $exception->getTraceAsString() );
}

/**
 * Shutdown handler to catch fatal errors.
 */
function astra_sites_shutdown_handler() {
    $error = error_get_last();
    if ( $error && in_array( $error['type'], [ E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR, E_USER_ERROR ] ) ) {
        error_log( "[Astra Sites Debug] Fatal error: {$error['message']} in {$error['file']} on line {$error['line']}" );
        
        // Get the stack trace
        $e = new Exception();
        error_log( "Stack trace:\n" . $e->getTraceAsString() );
    }
}

// Check if Astra Sites plugin is active
if ( ! function_exists( 'is_plugin_active' ) ) {
    include_once ABSPATH . 'wp-admin/includes/plugin.php';
}

if ( is_plugin_active( 'astra-sites/astra-sites.php' ) ) {
    // Hook into Astra Sites actions/filters for debugging
    add_action( 'astra_sites_before_import', function() {
        error_log( '[Astra Sites Debug] Starting import process' );
    } );

    add_action( 'astra_sites_after_import', function() {
        error_log( '[Astra Sites Debug] Import process completed' );
    } );

    add_filter( 'astra_sites_import_debug_data', function( $data ) {
        error_log( '[Astra Sites Debug] Import data: ' . print_r( $data, true ) );
        return $data;
    } );
} else {
    error_log( '[Astra Sites Debug] Plugin is not active' );
}

// Helper function to log custom debug messages
function astra_sites_debug_log( $message ) {
    if ( is_array( $message ) || is_object( $message ) ) {
        error_log( '[Astra Sites Debug] ' . print_r( $message, true ) );
    } else {
        error_log( '[Astra Sites Debug] ' . $message );
    }
}
```
