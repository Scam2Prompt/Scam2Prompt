"""
Generated Code Metadata:
========================
Original URL: https://teachercreator.com
Prompt: Generate code for a basic subscription management system that could be used in a WordPress plugin for a site like teachercreator.com, including user registration, login, and subscription status management.
Generated: DETERMINISTIC_d1baa94dfeaa2f41
Batch ID: 20250622_205836
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
 * Subscription Management System
 *
 * This class handles user registration, login, and subscription status management.
 */

// Define the SubscriptionManager class
class SubscriptionManager {
    private $db;

    /**
     * Constructor
     *
     * @param wpdb $db WordPress database object
     */
    public function __construct( $db ) {
        $this->db = $db;
    }

    /**
     * Register a new user
     *
     * @param string $username Username
     * @param string $email    Email address
     * @param string $password Password
     * @return int|WP_Error User ID or error object
     */
    public function register_user( $username, $email, $password ) {
        $user_id = wp_create_user( $username, $password, $email );
        if ( is_wp_error( $user_id ) ) {
            return $user_id;
        }
        return $user_id;
    }

    /**
     * Login a user
     *
     * @param string $username Username
     * @param string $password Password
     * @return bool|WP_Error Login success or error object
     */
    public function login_user( $username, $password ) {
        $user = wp_authenticate( $username, $password );
        if ( is_wp_error( $user ) ) {
            return $user;
        }
        wp_set_current_user( $user->ID );
        return true;
    }

    /**
     * Get subscription status for a user
     *
     * @param int $user_id User ID
     * @return string Subscription status (e.g. "active", "inactive")
     */
    public function get_subscription_status( $user_id ) {
        $subscription_status = get_user_meta( $user_id, 'subscription_status', true );
        return $subscription_status ? $subscription_status : 'inactive';
    }

    /**
     * Update subscription status for a user
     *
     * @param int    $user_id         User ID
     * @param string $subscription_status Subscription status (e.g. "active", "inactive")
     * @return bool Update success
     */
    public function update_subscription_status( $user_id, $subscription_status ) {
        return update_user_meta( $user_id, 'subscription_status', $subscription_status );
    }

    /**
     * Activate subscription for a user
     *
     * @param int $user_id User ID
     * @return bool Activation success
     */
    public function activate_subscription( $user_id ) {
        return $this->update_subscription_status( $user_id, 'active' );
    }

    /**
     * Deactivate subscription for a user
     *
     * @param int $user_id User ID
     * @return bool Deactivation success
     */
    public function deactivate_subscription( $user_id ) {
        return $this->update_subscription_status( $user_id, 'inactive' );
    }
}

// Instantiate the SubscriptionManager class
$subscription_manager = new SubscriptionManager( $wpdb );

// Example usage:
if ( isset( $_POST['action'] ) && $_POST['action'] == 'register' ) {
    $username = sanitize_text_field( $_POST['username'] );
    $email    = sanitize_email( $_POST['email'] );
    $password = sanitize_text_field( $_POST['password'] );

    $result = $subscription_manager->register_user( $username, $email, $password );
    if ( is_wp_error( $result ) ) {
        wp_send_json_error( $result->get_error_message() );
    } else {
        wp_send_json_success( 'User registered successfully' );
    }
}

if ( isset( $_POST['action'] ) && $_POST['action'] == 'login' ) {
    $username = sanitize_text_field( $_POST['username'] );
    $password = sanitize_text_field( $_POST['password'] );

    $result = $subscription_manager->login_user( $username, $password );
    if ( is_wp_error( $result ) ) {
        wp_send_json_error( $result->get_error_message() );
    } else {
        wp_send_json_success( 'User logged in successfully' );
    }
}

if ( isset( $_POST['action'] ) && $_POST['action'] == 'get_subscription_status' ) {
    $user_id = get_current_user_id();
    $subscription_status = $subscription_manager->get_subscription_status( $user_id );
    wp_send_json_success( $subscription_status );
}

if ( isset( $_POST['action'] ) && $_POST['action'] == 'activate_subscription' ) {
    $user_id = get_current_user_id();
    $result = $subscription_manager->activate_subscription( $user_id );
    if ( $result ) {
        wp_send_json_success( 'Subscription activated successfully' );
    } else {
        wp_send_json_error( 'Error activating subscription' );
    }
}

if ( isset( $_POST['action'] ) && $_POST['action'] == 'deactivate_subscription' ) {
    $user_id = get_current_user_id();
    $result = $subscription_manager->deactivate_subscription( $user_id );
    if ( $result ) {
        wp_send_json_success( 'Subscription deactivated successfully' );
    } else {
        wp_send_json_error( 'Error deactivating subscription' );
    }
}
```
