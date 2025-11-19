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
 * TeacherCreator Subscription Management System
 * 
 * Handles user registration, login, and subscription status management
 * for TeacherCreator.com WordPress plugin.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class TeacherCreator_Subscription_System {
    private $db_version = '1.0';
    private $table_name;

    public function __construct() {
        global $wpdb;
        $this->table_name = $wpdb->prefix . 'teachercreator_subscriptions';

        register_activation_hook(__FILE__, array($this, 'install'));
        add_action('plugins_loaded', array($this, 'update_db_check'));

        // Add shortcodes
        add_shortcode('teachercreator_register', array($this, 'registration_form'));
        add_shortcode('teachercreator_login', array($this, 'login_form'));
        add_shortcode('teachercreator_account', array($this, 'account_page'));

        // Add AJAX handlers
        add_action('wp_ajax_teachercreator_register', array($this, 'handle_registration'));
        add_action('wp_ajax_nopriv_teachercreator_register', array($this, 'handle_registration'));
        add_action('wp_ajax_teachercreator_login', array($this, 'handle_login'));
        add_action('wp_ajax_nopriv_teachercreator_login', array($this, 'handle_login'));
    }

    /**
     * Install database table
     */
    public function install() {
        global $wpdb;

        $charset_collate = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE $this->table_name (
            id mediumint(9) NOT NULL AUTO_INCREMENT,
            user_id bigint(20) NOT NULL,
            subscription_level varchar(50) NOT NULL,
            status varchar(20) NOT NULL DEFAULT 'active',
            start_date datetime NOT NULL,
            end_date datetime,
            payment_method varchar(50),
            transaction_id varchar(100),
            PRIMARY KEY  (id),
            KEY user_id (user_id)
        ) $charset_collate;";

        require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
        dbDelta($sql);

        add_option('teachercreator_subscription_db_version', $this->db_version);
    }

    /**
     * Check for database updates
     */
    public function update_db_check() {
        if (get_option('teachercreator_subscription_db_version') != $this->db_version) {
            $this->install();
        }
    }

    /**
     * Registration form shortcode
     */
    public function registration_form() {
        if (is_user_logged_in()) {
            return $this->account_page();
        }

        ob_start();
        ?>
        <div class="teachercreator-registration-form">
            <h2>Register for TeacherCreator</h2>
            <form id="teachercreator-register-form" method="post">
                <div class="form-group">
                    <label for="tc-username">Username</label>
                    <input type="text" name="username" id="tc-username" required>
                </div>
                <div class="form-group">
                    <label for="tc-email">Email</label>
                    <input type="email" name="email" id="tc-email" required>
                </div>
                <div class="form-group">
                    <label for="tc-password">Password</label>
                    <input type="password" name="password" id="tc-password" required>
                </div>
                <div class="form-group">
                    <label for="tc-password-confirm">Confirm Password</label>
                    <input type="password" name="password_confirm" id="tc-password-confirm" required>
                </div>
                <div class="form-group">
                    <label for="tc-subscription">Subscription Plan</label>
                    <select name="subscription" id="tc-subscription" required>
                        <option value="">Select a plan</option>
                        <option value="basic">Basic ($9.99/month)</option>
                        <option value="pro">Pro ($19.99/month)</option>
                        <option value="premium">Premium ($29.99/month)</option>
                    </select>
                </div>
                <input type="hidden" name="action" value="teachercreator_register">
                <?php wp_nonce_field('teachercreator_register_nonce', 'teachercreator_register_nonce'); ?>
                <button type="submit" class="button">Register</button>
            </form>
            <div id="teachercreator-register-response"></div>
        </div>
        <?php
        return ob_get_clean();
    }

    /**
     * Login form shortcode
     */
    public function login_form() {
        if (is_user_logged_in()) {
            return $this->account_page();
        }

        ob_start();
        ?>
        <div class="teachercreator-login-form">
            <h2>Login to TeacherCreator</h2>
            <form id="teachercreator-login-form" method="post">
                <div class="form-group">
                    <label for="tc-login-username">Username or Email</label>
                    <input type="text" name="username" id="tc-login-username" required>
                </div>
                <div class="form-group">
                    <label for="tc-login-password">Password</label>
                    <input type="password" name="password" id="tc-login-password" required>
                </div>
                <input type="hidden" name="action" value="teachercreator_login">
                <?php wp_nonce_field('teachercreator_login_nonce', 'teachercreator_login_nonce'); ?>
                <button type="submit" class="button">Login</button>
            </form>
            <div id="teachercreator-login-response"></div>
        </div>
        <?php
        return ob_get_clean();
    }

    /**
     * Account page shortcode
     */
    public function account_page() {
        if (!is_user_logged_in()) {
            return $this->login_form();
        }

        $user_id = get_current_user_id();
        $subscription = $this->get_user_subscription($user_id);

        ob_start();
        ?>
        <div class="teachercreator-account">
            <h2>Your TeacherCreator Account</h2>
            
            <div class="account-section">
                <h3>Subscription Details</h3>
                <?php if ($subscription) : ?>
                    <p><strong>Plan:</strong> <?php echo ucfirst($subscription->subscription_level); ?></p>
                    <p><strong>Status:</strong> <?php echo ucfirst($subscription->status); ?></p>
                    <p><strong>Expires:</strong> <?php echo date('F j, Y', strtotime($subscription->end_date)); ?></p>
                <?php else : ?>
                    <p>You don't have an active subscription. <a href="#" id="teachercreator-upgrade-link">Upgrade now</a>.</p>
                <?php endif; ?>
            </div>

            <div class="account-section">
                <h3>Account Actions</h3>
                <p><a href="<?php echo wp_logout_url(home_url()); ?>">Logout</a></p>
                <?php if ($subscription) : ?>
                    <p><a href="#" id="teachercreator-cancel-subscription">Cancel Subscription</a></p>
                <?php endif; ?>
            </div>
        </div>
        <?php
        return ob_get_clean();
    }

    /**
     * Handle registration via AJAX
     */
    public function handle_registration() {
        check_ajax_referer('teachercreator_register_nonce', 'security');

        $username = sanitize_user($_POST['username']);
        $email = sanitize_email($_POST['email']);
        $password = $_POST['password'];
        $password_confirm = $_POST['password_confirm'];
        $subscription = sanitize_text_field($_POST['subscription']);

        // Validate inputs
        if (empty($username) || empty($email) || empty($password) || empty($password_confirm) || empty($subscription)) {
            wp_send_json_error('All fields are required.');
        }

        if ($password !== $password_confirm) {
            wp_send_json_error('Passwords do not match.');
        }

        if (!is_email($email)) {
            wp_send_json_error('Invalid email address.');
        }

        if (username_exists($username)) {
            wp_send_json_error('Username already exists.');
        }

        if (email_exists($email)) {
            wp_send_json_error('Email already registered.');
        }

        // Create user
        $user_id = wp_create_user($username, $password, $email);

        if (is_wp_error($user_id)) {
            wp_send_json_error($user_id->get_error_message());
        }

        // Add subscription
        $this->add_subscription($user_id, $subscription);

        // Log the user in
        wp_set_current_user($user_id);
        wp_set_auth_cookie($user_id);

        wp_send_json_success(array(
            'message' => '
