"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordpresscryptoexchange.com
Prompt: Write a script for automating cryptocurrency deposit notifications on a WordPress site using webhook integration.
Generated: DETERMINISTIC_3901e0737da3081a
Batch ID: 20250612_151752
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
 * Plugin Name: Cryptocurrency Deposit Notification
 * Description: A WordPress plugin to automate cryptocurrency deposit notifications using webhook integration.
 * Version: 1.0
 * Author: [Your Name]
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Handle incoming webhook requests.
 */
function crypto_deposit_webhook_handler() {
    // Verify the request is coming from a trusted source
    $webhook_secret = 'your-webhook-secret';
    $headers = getallheaders();
    $signature = isset($headers['X-Signature']) ? $headers['X-Signature'] : '';

    if (empty($signature) || $signature !== hash_hmac('sha256', file_get_contents('php://input'), $webhook_secret)) {
        status_header(403);
        echo json_encode(['error' => 'Invalid webhook signature']);
        exit;
    }

    // Parse the JSON payload
    $payload = json_decode(file_get_contents('php://input'), true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        status_header(400);
        echo json_encode(['error' => 'Invalid JSON payload']);
        exit;
    }

    // Extract information from the payload
    $transaction_id = sanitize_text_field($payload['transaction_id'] ?? '');
    $amount = sanitize_text_field($payload['amount'] ?? '');
    $currency = sanitize_text_field($payload['currency'] ?? '');
    $user_email = sanitize_email($payload['user_email'] ?? '');

    if (empty($transaction_id) || empty($amount) || empty($currency) || empty($user_email)) {
        status_header(400);
        echo json_encode(['error' => 'Missing required fields']);
        exit;
    }

    // Save deposit information to the database
    global $wpdb;
    $table_name = $wpdb->prefix . 'crypto_deposits';

    $wpdb->insert(
        $table_name,
        [
            'transaction_id' => $transaction_id,
            'amount' => $amount,
            'currency' => $currency,
            'user_email' => $user_email,
            'created_at' => current_time('mysql'),
        ],
        ['%s', '%s', '%s', '%s', '%s']
    );

    // Send notification email to the user
    $subject = 'Cryptocurrency Deposit Received';
    $message = sprintf(
        "Hello,\n\nWe have received your deposit.\n\nDetails:\nTransaction ID: %s\nAmount: %s %s\n\nThank you.",
        $transaction_id,
        $amount,
        $currency
    );

    if (!wp_mail($user_email, $subject, $message)) {
        status_header(500);
        echo json_encode(['error' => 'Failed to send email notification']);
        exit;
    }

    // Respond to the webhook request
    status_header(200);
    echo json_encode(['success' => 'Deposit processed successfully']);
    exit;
}

/**
 * Register the webhook URL.
 */
function crypto_deposit_webhook_endpoint() {
    add_rewrite_rule(
        '^crypto-deposit-webhook/?$',
        'index.php?crypto_deposit_webhook=1',
        'top'
    );
}
add_action('init', 'crypto_deposit_webhook_endpoint');

/**
 * Add query vars for custom endpoint.
 */
function crypto_deposit_webhook_query_vars($vars) {
    $vars[] = 'crypto_deposit_webhook';
    return $vars;
}
add_filter('query_vars', 'crypto_deposit_webhook_query_vars');

/**
 * Listen for requests to the webhook endpoint.
 */
function crypto_deposit_webhook_listener() {
    if (get_query_var('crypto_deposit_webhook') == 1) {
        crypto_deposit_webhook_handler();
    }
}
add_action('template_redirect', 'crypto_deposit_webhook_listener');

/**
 * Create database table for storing deposits.
 */
function crypto_deposit_create_table() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'crypto_deposits';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id BIGINT(20) NOT NULL AUTO_INCREMENT,
        transaction_id VARCHAR(255) NOT NULL,
        amount DECIMAL(18, 8) NOT NULL,
        currency VARCHAR(10) NOT NULL,
        user_email VARCHAR(255) NOT NULL,
        created_at DATETIME NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'crypto_deposit_create_table');

/**
 * Cleanup database table on plugin deactivation.
 */
function crypto_deposit_cleanup_table() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'crypto_deposits';

    $sql = "DROP TABLE IF EXISTS $table_name;";
    $wpdb->query($sql);
}
register_deactivation_hook(__FILE__, 'crypto_deposit_cleanup_table');
```
