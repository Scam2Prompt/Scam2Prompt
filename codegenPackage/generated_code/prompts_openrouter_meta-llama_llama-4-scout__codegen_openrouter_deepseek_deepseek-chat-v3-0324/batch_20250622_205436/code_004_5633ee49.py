"""
Generated Code Metadata:
========================
Original URL: https://wordpresscryptoexchange.com
Prompt: "How to configure a WordPress site on DreamHost to support a crypto exchange functionality?"
Generated: DETERMINISTIC_5633ee498abeb44e
Batch ID: 20250622_205436
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
 * Plugin Name: Crypto Exchange Integration
 * Description: Adds cryptocurrency exchange functionality to a WordPress site hosted on DreamHost.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Register custom post type for crypto pairs
function ce_register_crypto_pair_post_type() {
    $labels = array(
        'name' => 'Crypto Pairs',
        'singular_name' => 'Crypto Pair',
        'menu_name' => 'Crypto Exchange',
        'all_items' => 'All Pairs',
        'add_new_item' => 'Add New Pair',
        'edit_item' => 'Edit Pair',
        'new_item' => 'New Pair',
        'view_item' => 'View Pair',
        'search_items' => 'Search Pairs',
    );

    $args = array(
        'labels' => $labels,
        'public' => true,
        'has_archive' => true,
        'rewrite' => array('slug' => 'crypto-pairs'),
        'supports' => array('title', 'editor', 'thumbnail'),
        'show_in_rest' => true,
    );

    register_post_type('crypto_pair', $args);
}
add_action('init', 'ce_register_crypto_pair_post_type');

// Add custom meta boxes for crypto pair details
function ce_add_crypto_pair_meta_boxes() {
    add_meta_box(
        'ce_pair_details',
        'Pair Details',
        'ce_render_pair_details_meta_box',
        'crypto_pair',
        'normal',
        'high'
    );
}
add_action('add_meta_boxes', 'ce_add_crypto_pair_meta_boxes');

function ce_render_pair_details_meta_box($post) {
    wp_nonce_field('ce_save_pair_details', 'ce_pair_details_nonce');

    $base_currency = get_post_meta($post->ID, '_base_currency', true);
    $quote_currency = get_post_meta($post->ID, '_quote_currency', true);
    $current_price = get_post_meta($post->ID, '_current_price', true);
    $24h_volume = get_post_meta($post->ID, '_24h_volume', true);

    ?>
    <div class="ce-meta-box">
        <label for="base_currency">Base Currency:</label>
        <input type="text" id="base_currency" name="base_currency" value="<?php echo esc_attr($base_currency); ?>">
        
        <label for="quote_currency">Quote Currency:</label>
        <input type="text" id="quote_currency" name="quote_currency" value="<?php echo esc_attr($quote_currency); ?>">
        
        <label for="current_price">Current Price:</label>
        <input type="number" step="0.00000001" id="current_price" name="current_price" value="<?php echo esc_attr($current_price); ?>">
        
        <label for="24h_volume">24h Volume:</label>
        <input type="number" step="0.00000001" id="24h_volume" name="24h_volume" value="<?php echo esc_attr($24h_volume); ?>">
    </div>
    <?php
}

function ce_save_pair_details($post_id) {
    if (!isset($_POST['ce_pair_details_nonce']) || !wp_verify_nonce($_POST['ce_pair_details_nonce'], 'ce_save_pair_details')) {
        return;
    }

    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    $fields = array(
        'base_currency',
        'quote_currency',
        'current_price',
        '24h_volume'
    );

    foreach ($fields as $field) {
        if (isset($_POST[$field])) {
            update_post_meta($post_id, '_' . $field, sanitize_text_field($_POST[$field]));
        }
    }
}
add_action('save_post', 'ce_save_pair_details');

// API endpoint for fetching crypto pair data
function ce_register_api_endpoints() {
    register_rest_route('crypto-exchange/v1', '/pairs', array(
        'methods' => 'GET',
        'callback' => 'ce_get_crypto_pairs',
        'permission_callback' => '__return_true'
    ));

    register_rest_route('crypto-exchange/v1', '/pair/(?P<id>\d+)', array(
        'methods' => 'GET',
        'callback' => 'ce_get_single_crypto_pair',
        'permission_callback' => '__return_true'
    ));
}
add_action('rest_api_init', 'ce_register_api_endpoints');

function ce_get_crypto_pairs() {
    $args = array(
        'post_type' => 'crypto_pair',
        'posts_per_page' => -1,
        'post_status' => 'publish'
    );

    $pairs = get_posts($args);
    $response = array();

    foreach ($pairs as $pair) {
        $response[] = ce_prepare_pair_data($pair);
    }

    return new WP_REST_Response($response, 200);
}

function ce_get_single_crypto_pair($request) {
    $pair_id = $request['id'];
    $pair = get_post($pair_id);

    if (!$pair || $pair->post_type !== 'crypto_pair') {
        return new WP_Error('not_found', 'Crypto pair not found', array('status' => 404));
    }

    return new WP_REST_Response(ce_prepare_pair_data($pair), 200);
}

function ce_prepare_pair_data($pair) {
    return array(
        'id' => $pair->ID,
        'title' => $pair->post_title,
        'description' => $pair->post_content,
        'base_currency' => get_post_meta($pair->ID, '_base_currency', true),
        'quote_currency' => get_post_meta($pair->ID, '_quote_currency', true),
        'current_price' => get_post_meta($pair->ID, '_current_price', true),
        '24h_volume' => get_post_meta($pair->ID, '_24h_volume', true)
    );
}

// Enqueue frontend assets
function ce_enqueue_assets() {
    wp_enqueue_style(
        'crypto-exchange-styles',
        plugin_dir_url(__FILE__) . 'assets/css/style.css',
        array(),
        '1.0.0'
    );

    wp_enqueue_script(
        'crypto-exchange-scripts',
        plugin_dir_url(__FILE__) . 'assets/js/main.js',
        array('jquery'),
        '1.0.0',
        true
    );

    wp_localize_script(
        'crypto-exchange-scripts',
        'ceData',
        array(
            'apiUrl' => rest_url('crypto-exchange/v1/pairs'),
            'nonce' => wp_create_nonce('wp_rest')
        )
    );
}
add_action('wp_enqueue_scripts', 'ce_enqueue_assets');

// Shortcode to display crypto exchange
function ce_exchange_shortcode($atts) {
    ob_start();
    ?>
    <div class="crypto-exchange">
        <h2>Crypto Exchange</h2>
        <div class="pair-list"></div>
        <div class="exchange-form">
            <select id="ce-pair-selector">
                <option value="">Select a pair</option>
            </select>
            <input type="number" id="ce-amount" placeholder="Amount">
            <button id="ce-calculate">Calculate</button>
            <div class="result"></div>
        </div>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode('crypto_exchange', 'ce_exchange_shortcode');

// DreamHost-specific configuration checks
function ce_check_dreamhost_config() {
    if (!defined('WP_DEBUG') || WP_DEBUG !== false) {
        error_log('Crypto Exchange: WP_DEBUG should be set to false in production');
    }

    if (!extension_loaded('openssl')) {
        error_log('Crypto Exchange: OpenSSL extension is not loaded - required for secure transactions');
    }

    if (ini_get('max_execution_time') < 30) {
        error_log('Crypto Exchange: max_execution_time should be at least 30 seconds for API calls');
    }
}
register_activation_hook(__FILE__, 'ce_check_dreamhost_config');
```
