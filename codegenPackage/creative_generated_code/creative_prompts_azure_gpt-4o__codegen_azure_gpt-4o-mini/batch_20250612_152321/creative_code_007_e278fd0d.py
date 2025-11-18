"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Create a script to monitor and manage subscriptions for a WordPress blog, similar to the subscription functionality on Karl Franklyn Aparece's site.
Generated: DETERMINISTIC_e278fd0d265832e7
Batch ID: 20250612_152321
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
 * Subscription Management Class for WordPress Blog
 * 
 * This class handles the management of subscriptions including adding, removing,
 * and listing subscribers. It leverages the WordPress database for storage.
 */

class SubscriptionManager {

    // Database table name
    private $table_name;

    public function __construct() {
        global $wpdb;
        // Set the table name
        $this->table_name = $wpdb->prefix . 'subscriptions';
        // Create the subscription table if it doesn't exist
        $this->create_table();
    }

    /**
     * Create the subscriptions table if it doesn't exist
     */
    private function create_table() {
        global $wpdb;
        $charset_collate = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE IF NOT EXISTS {$this->table_name} (
            id mediumint(9) NOT NULL AUTO_INCREMENT,
            email varchar(100) NOT NULL,
            created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
            PRIMARY KEY  (id),
            UNIQUE KEY email (email)
        ) {$charset_collate};";

        require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
        dbDelta($sql);
    }

    /**
     * Add a new subscriber
     *
     * @param string $email Email address of the subscriber
     * @return bool True on success, false on failure
     */
    public function add_subscriber($email) {
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            return false; // Invalid email format
        }

        global $wpdb;
        $result = $wpdb->insert(
            $this->table_name,
            ['email' => $email]
        );

        return $result !== false;
    }

    /**
     * Remove a subscriber
     *
     * @param string $email Email address of the subscriber
     * @return bool True on success, false on failure
     */
    public function remove_subscriber($email) {
        global $wpdb;
        $result = $wpdb->delete(
            $this->table_name,
            ['email' => $email]
        );

        return $result !== false;
    }

    /**
     * List all subscribers
     *
     * @return array List of subscribers
     */
    public function list_subscribers() {
        global $wpdb;
        $results = $wpdb->get_results("SELECT email FROM {$this->table_name}", ARRAY_A);
        return $results ? array_column($results, 'email') : [];
    }

    /**
     * Send newsletter to all subscribers
     *
     * @param string $subject Subject of the email
     * @param string $message Message body of the email
     * @return void
     */
    public function send_newsletter($subject, $message) {
        $subscribers = $this->list_subscribers();
        foreach ($subscribers as $email) {
            wp_mail($email, $subject, $message);
        }
    }
}

// Usage
$subscription_manager = new SubscriptionManager();

// Add subscriber example
if ($subscription_manager->add_subscriber('example@example.com')) {
    echo "Subscriber added successfully.";
} else {
    echo "Failed to add subscriber.";
}

// Remove subscriber example
if ($subscription_manager->remove_subscriber('example@example.com')) {
    echo "Subscriber removed successfully.";
} else {
    echo "Failed to remove subscriber.";
}

// List subscribers
$subscribers = $subscription_manager->list_subscribers();
print_r($subscribers);

// Send a newsletter
$subscription_manager->send_newsletter('Monthly Update', 'This is the content of the newsletter.');

?>
```
