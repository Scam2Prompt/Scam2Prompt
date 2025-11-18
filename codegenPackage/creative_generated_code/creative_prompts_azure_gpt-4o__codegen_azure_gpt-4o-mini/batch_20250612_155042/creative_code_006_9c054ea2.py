"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.167079.com
Prompt: Create a WordPress script to automatically email administrators when a critical error is detected on the site.
Generated: DETERMINISTIC_9c054ea2ce1a2e0a
Batch ID: 20250612_155042
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
 * Plugin Name: Critical Error Notifier
 * Description: Automatically emails administrators when a critical error is detected on the site.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Class CriticalErrorNotifier
 * 
 * This class handles the registration of error handlers and notification functionality.
 */
class CriticalErrorNotifier {
    
    /**
     * Constructor to hook WordPress actions and filters.
     */
    public function __construct() {
        // Register the custom error handler
        add_action( 'shutdown', [ $this, 'check_for_fatal_errors' ] );
    }

    /**
     * Checks for fatal errors and sends notification to admins if found.
     */
    public function check_for_fatal_errors() {
        // Check if there are fatal errors in the last request
        $error = error_get_last();
        if ( $error ) {
            // Prepare error details
            $error_message = sprintf(
                "A critical error occurred on your WordPress site:\n\nError Type: %s\nMessage: %s\nFile: %s\nLine: %d\n",
                $error['type'],
                $error['message'],
                $error['file'],
                $error['line']
            );

            // Send email to administrators
            $this->send_error_notification( $error_message );
        }
    }

    /**
     * Sends an error notification email to administrators.
     *
     * @param string $error_message The error message to include in the email.
     */
    private function send_error_notification( $error_message ) {
        // Get all administrators
        $admins = get_users( [ 'role' => 'administrator' ] );
        $admin_emails = wp_list_pluck( $admins, 'user_email' );

        // If there are no administrators, do nothing
        if ( empty( $admin_emails ) ) {
            return;
        }

        // Set email subject and headers
        $subject = 'Critical Error Detected on Your WordPress Site';
        $headers = [ 'Content-Type: text/plain; charset=UTF-8' ];

        // Send email to each administrator
        foreach ( $admin_emails as $email ) {
            wp_mail( $email, $subject, $error_message, $headers );
        }
    }
}

// Instantiate the CriticalErrorNotifier class
new CriticalErrorNotifier();
```
