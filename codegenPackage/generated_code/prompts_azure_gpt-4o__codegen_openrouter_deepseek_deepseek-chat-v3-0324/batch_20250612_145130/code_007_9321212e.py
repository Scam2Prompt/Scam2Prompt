"""
Generated Code Metadata:
========================
Original URL: https://demo3.cloudwp.dev
Prompt: Write a PHP script to notify users when their WordPress Playground environment becomes inactive, using InMotion Central's features.
Generated: DETERMINISTIC_9321212e90725120
Batch ID: 20250612_145130
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
 * WordPress Playground Inactivity Notifier
 * 
 * This script monitors WordPress Playground environments and sends notifications
 * to users when their environment becomes inactive.
 * 
 * Requirements:
 * - WordPress Playground with InMotion Central integration
 * - PHP 7.4 or higher
 * - Properly configured mail server or SMTP for email notifications
 */

// Prevent direct access
defined('ABSPATH') || exit;

class WP_Playground_Inactivity_Notifier {
    /**
     * @var int Inactivity threshold in minutes
     */
    private $inactivity_threshold = 30;

    /**
     * @var string Notification email subject
     */
    private $email_subject = 'Your WordPress Playground Environment is Inactive';

    /**
     * Initialize the notifier
     */
    public function __construct() {
        add_action('init', [$this, 'setup_schedule']);
        add_action('wp_playground_check_inactivity', [$this, 'check_inactive_environments']);
    }

    /**
     * Setup the cron schedule for checking inactivity
     */
    public function setup_schedule() {
        if (!wp_next_scheduled('wp_playground_check_inactivity')) {
            wp_schedule_event(time(), 'hourly', 'wp_playground_check_inactivity');
        }
    }

    /**
     * Check for inactive environments and send notifications
     */
    public function check_inactive_environments() {
        $environments = $this->get_active_environments();
        
        foreach ($environments as $environment) {
            if ($this->is_environment_inactive($environment)) {
                $this->send_inactivity_notification($environment);
                $this->mark_environment_notified($environment);
            }
        }
    }

    /**
     * Get all active WordPress Playground environments
     * 
     * @return array List of active environments
     */
    private function get_active_environments() {
        global $wpdb;
        
        $query = "SELECT * FROM {$wpdb->prefix}playground_environments 
                 WHERE status = 'active' AND notified = 0";
        
        return $wpdb->get_results($query, ARRAY_A);
    }

    /**
     * Check if an environment is inactive
     * 
     * @param array $environment Environment data
     * @return bool True if inactive, false otherwise
     */
    private function is_environment_inactive($environment) {
        $last_activity = strtotime($environment['last_activity']);
        $current_time = current_time('timestamp');
        $inactive_seconds = $this->inactivity_threshold * 60;
        
        return ($current_time - $last_activity) > $inactive_seconds;
    }

    /**
     * Send inactivity notification to user
     * 
     * @param array $environment Environment data
     * @return bool True if email was sent successfully
     */
    private function send_inactivity_notification($environment) {
        $user = get_user_by('id', $environment['user_id']);
        if (!$user) {
            return false;
        }

        $to = $user->user_email;
        $subject = $this->email_subject;
        $message = $this->get_notification_message($environment, $user);
        $headers = ['Content-Type: text/html; charset=UTF-8'];

        return wp_mail($to, $subject, $message, $headers);
    }

    /**
     * Generate notification message
     * 
     * @param array $environment Environment data
     * @param WP_User $user User object
     * @return string HTML email message
     */
    private function get_notification_message($environment, $user) {
        $site_name = get_bloginfo('name');
        $login_url = wp_login_url();
        $environment_url = $environment['url'];
        
        ob_start();
        ?>
        <html>
        <body>
            <p>Hello <?php echo esc_html($user->display_name); ?>,</p>
            
            <p>Your WordPress Playground environment at <a href="<?php echo esc_url($environment_url); ?>">
            <?php echo esc_html($environment_url); ?></a> has been inactive for more than 
            <?php echo $this->inactivity_threshold; ?> minutes.</p>
            
            <p>To keep your environment active, please log in and use it within the next 24 hours.</p>
            
            <p><a href="<?php echo esc_url($login_url); ?>">Click here to log in</a></p>
            
            <p>If you no longer need this environment, you can safely ignore this message.</p>
            
            <p>Best regards,<br>
            The <?php echo esc_html($site_name); ?> Team</p>
        </body>
        </html>
        <?php
        return ob_get_clean();
    }

    /**
     * Mark environment as notified in database
     * 
     * @param array $environment Environment data
     */
    private function mark_environment_notified($environment) {
        global $wpdb;
        
        $wpdb->update(
            "{$wpdb->prefix}playground_environments",
            ['notified' => 1],
            ['id' => $environment['id']]
        );
    }

    /**
     * Clean up on deactivation
     */
    public static function deactivate() {
        wp_clear_scheduled_hook('wp_playground_check_inactivity');
    }
}

// Initialize the notifier
if (defined('INMOTION_CENTRAL') && INMOTION_CENTRAL) {
    $notifier = new WP_Playground_Inactivity_Notifier();
    
    // Register deactivation hook
    register_deactivation_hook(__FILE__, ['WP_Playground_Inactivity_Notifier', 'deactivate']);
}
```
