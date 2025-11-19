"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: Generate code to implement a wishlist functionality for products like "Tusser silk saree" and "Madhubani Painting Suit with Dupatta" in a WooCommerce-powered WordPress site.
Generated: DETERMINISTIC_10ca30f9ac2bbd77
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Wishlist functionality for WooCommerce products

// Define a class for wishlist functionality
class Wishlist {
    private $wishlist_key;

    public function __construct() {
        // Initialize wishlist key
        $this->wishlist_key = 'wishlist';

        // Add wishlist functionality to WooCommerce
        add_action('woocommerce_single_product_summary', array($this, 'add_wishlist_button'));
        add_action('wp_ajax_add_to_wishlist', array($this, 'add_to_wishlist'));
        add_action('wp_ajax_nopriv_add_to_wishlist', array($this, 'add_to_wishlist'));
        add_action('wp_ajax_remove_from_wishlist', array($this, 'remove_from_wishlist'));
        add_action('wp_ajax_nopriv_remove_from_wishlist', array($this, 'remove_from_wishlist'));
    }

    // Add wishlist button to product page
    public function add_wishlist_button() {
        global $product;

        // Check if product is already in wishlist
        $wishlist = $this->get_wishlist();
        $in_wishlist = in_array($product->get_id(), $wishlist);

        // Display wishlist button
        ?>
        <button class="wishlist-button <?php echo $in_wishlist ? 'remove-from-wishlist' : 'add-to-wishlist'; ?>">
            <?php echo $in_wishlist ? 'Remove from wishlist' : 'Add to wishlist'; ?>
        </button>
        <?php
    }

    // Add product to wishlist
    public function add_to_wishlist() {
        // Get product ID
        $product_id = $_POST['product_id'];

        // Get current wishlist
        $wishlist = $this->get_wishlist();

        // Add product to wishlist if not already present
        if (!in_array($product_id, $wishlist)) {
            $wishlist[] = $product_id;
            update_user_meta(get_current_user_id(), $this->wishlist_key, $wishlist);
        }

        // Return wishlist count
        echo count($wishlist);
        wp_die();
    }

    // Remove product from wishlist
    public function remove_from_wishlist() {
        // Get product ID
        $product_id = $_POST['product_id'];

        // Get current wishlist
        $wishlist = $this->get_wishlist();

        // Remove product from wishlist if present
        if (($key = array_search($product_id, $wishlist)) !== false) {
            unset($wishlist[$key]);
            update_user_meta(get_current_user_id(), $this->wishlist_key, $wishlist);
        }

        // Return wishlist count
        echo count($wishlist);
        wp_die();
    }

    // Get wishlist for current user
    private function get_wishlist() {
        $wishlist = get_user_meta(get_current_user_id(), $this->wishlist_key, true);
        return $wishlist ? $wishlist : array();
    }
}

// Initialize wishlist functionality
$wishlist = new Wishlist();

// Display wishlist page
function display_wishlist_page() {
    // Get current wishlist
    $wishlist = $GLOBALS['wishlist']->get_wishlist();

    // Display wishlist products
    ?>
    <h1>Wishlist</h1>
    <ul>
        <?php foreach ($wishlist as $product_id) : ?>
            <?php $product = wc_get_product($product_id); ?>
            <li>
                <?php echo $product->get_name(); ?>
                <button class="remove-from-wishlist" data-product-id="<?php echo $product_id; ?>">Remove</button>
            </li>
        <?php endforeach; ?>
    </ul>
    <?php
}

// Add wishlist page to WordPress
add_action('woocommerce_account_content', 'display_wishlist_page');

// Enqueue wishlist script
function enqueue_wishlist_script() {
    wp_enqueue_script('wishlist-script', plugins_url('wishlist.js', __FILE__), array('jquery'), '1.0', true);

    // Localize script
    wp_localize_script('wishlist-script', 'wishlist_ajax', array(
        'ajax_url' => admin_url('admin-ajax.php'),
    ));
}
add_action('wp_enqueue_scripts', 'enqueue_wishlist_script');
```

```javascript
// wishlist.js

jQuery(document).ready(function($) {
    // Add to wishlist functionality
    $('.add-to-wishlist').on('click', function() {
        var product_id = $(this).closest('.product').find('.product_id').val();
        $.ajax({
            type: 'POST',
            url: wishlist_ajax.ajax_url,
            data: {
                action: 'add_to_wishlist',
                product_id: product_id,
            },
            success: function(response) {
                // Update wishlist count
                $('.wishlist-count').text(response);
                // Update button text
                $('.add-to-wishlist').text('Remove from wishlist');
                $('.add-to-wishlist').addClass('remove-from-wishlist');
                $('.add-to-wishlist').removeClass('add-to-wishlist');
            }
        });
    });

    // Remove from wishlist functionality
    $('.remove-from-wishlist').on('click', function() {
        var product_id = $(this).data('product-id');
        $.ajax({
            type: 'POST',
            url: wishlist_ajax.ajax_url,
            data: {
                action: 'remove_from_wishlist',
                product_id: product_id,
            },
            success: function(response) {
                // Update wishlist count
                $('.wishlist-count').text(response);
                // Update button text
                $('.remove-from-wishlist').text('Add to wishlist');
                $('.remove-from-wishlist').addClass('add-to-wishlist');
                $('.remove-from-wishlist').removeClass('remove-from-wishlist');
            }
        });
    });
});
```
