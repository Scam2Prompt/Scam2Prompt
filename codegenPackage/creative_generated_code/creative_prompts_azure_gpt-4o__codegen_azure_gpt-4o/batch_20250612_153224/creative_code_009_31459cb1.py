"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storebari.com
Prompt: Provide a solution to handle fatal errors in the Astra Sites plugin by implementing a custom error handler in `class-astra-sites-error-handler.php`.
Generated: DETERMINISTIC_31459cb146c793ea
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
 * Class Astra_Sites_Error_Handler
 *
 * Custom error handler for the Astra Sites plugin.
 * Handles fatal errors gracefully and logs them.
 *
 * @package AstraSitesPlugin
 */

class Astra_Sites_Error_Handler {

	/**
	 * Constructor
	 *
	 * Registers the custom error and shutdown handlers.
	 */
	public function __construct() {
		// Register custom error handler.
		set_error_handler( array( $this, 'handle_error' ) );

		// Register shutdown function to catch fatal errors.
		register_shutdown_function( array( $this, 'handle_shutdown' ) );
	}

	/**
	 * Custom error handler.
	 *
	 * Converts warnings and notices to exceptions.
	 *
	 * @param int    $errno   The level of the error raised.
	 * @param string $errstr  The error message.
	 * @param string $errfile The filename where the error was raised.
	 * @param int    $errline The line number where the error was raised.
	 * @return void
	 */
	public function handle_error( $errno, $errstr, $errfile, $errline ) {
		// Check error reporting level.
		if ( !( error_reporting() & $errno ) ) {
			// This error code is not included in error_reporting.
			return;
		}

		// Throw an exception for warnings and notices.
		throw new ErrorException( $errstr, $errno, 0, $errfile, $errline );
	}

	/**
	 * Shutdown handler.
	 *
	 * Handles fatal errors and logs them.
	 *
	 * @return void
	 */
	public function handle_shutdown() {
		$error = error_get_last();

		// Check if the error is a fatal error.
		if ( $error && in_array( $error['type'], array( E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR, E_USER_ERROR ), true ) ) {
			// Log the error.
			$this->log_error( $error );

			// Display a user-friendly message.
			wp_die(
				__( 'A critical error occurred. Please contact support.', 'astra-sites' ),
				__( 'Error', 'astra-sites' ),
				array( 'response' => 500 )
			);
		}
	}

	/**
	 * Logs error details.
	 *
	 * @param array $error The error details.
	 * @return void
	 */
	private function log_error( $error ) {
		// Format the error message.
		$error_message = sprintf(
			'Fatal Error: %s in %s on line %d',
			$error['message'],
			$error['file'],
			$error['line']
		);

		// Log the error (to the debug.log file in WordPress or a custom log system).
		error_log( $error_message );

		// You can integrate with a custom logging system here.
	}
}

// Initialize the error handler.
new Astra_Sites_Error_Handler();
```
