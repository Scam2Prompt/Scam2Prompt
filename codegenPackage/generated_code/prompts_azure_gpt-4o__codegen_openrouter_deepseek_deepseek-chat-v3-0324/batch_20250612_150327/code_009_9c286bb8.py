"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: Write a PHP script to display "Deals of the Day" for products like "Tusser by Gicha Madhubani Painting Suit with Dupatta" on the homepage of a WordPress eCommerce site.
Generated: DETERMINISTIC_9c286bb8c9a65e3c
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
/**
 * Deals of the Day Widget for WordPress eCommerce Site
 * Displays featured products with special deals on the homepage.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Deals_Of_The_Day_Widget extends WP_Widget {

    /**
     * Register widget with WordPress.
     */
    public function __construct() {
        parent::__construct(
            'deals_of_the_day_widget',
            __('Deals of the Day', 'text_domain'),
            array('description' => __('Display daily deals for products', 'text_domain'))
        );
    }

    /**
     * Front-end display of widget.
     *
     * @param array $args     Widget arguments.
     * @param array $instance Saved values from database.
     */
    public function widget($args, $instance) {
        echo $args['before_widget'];
        
        if (!empty($instance['title'])) {
            echo $args['before_title'] . apply_filters('widget_title', $instance['title']) . $args['after_title'];
        }

        $this->display_deals();

        echo $args['after_widget'];
    }

    /**
     * Back-end widget form.
     *
     * @param array $instance Previously saved values from database.
     */
    public function form($instance) {
        $title = !empty($instance['title']) ? $instance['title'] : __('Deals of the Day', 'text_domain');
        ?>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('title')); ?>"><?php esc_attr_e('Title:', 'text_domain'); ?></label> 
            <input class="widefat" id="<?php echo esc_attr($this->get_field_id('title')); ?>" name="<?php echo esc_attr($this->get_field_name('title')); ?>" type="text" value="<?php echo esc_attr($title); ?>">
        </p>
        <?php 
    }

    /**
     * Sanitize widget form values as they are saved.
     *
     * @param array $new_instance Values just sent to be saved.
     * @param array $old_instance Previously saved values from database.
     *
     * @return array Updated safe values to be saved.
     */
    public function update($new_instance, $old_instance) {
        $instance = array();
        $instance['title'] = (!empty($new_instance['title'])) ? sanitize_text_field($new_instance['title']) : '';

        return $instance;
    }

    /**
     * Display deals of the day products.
     */
    private function display_deals() {
        if (!class_exists('WooCommerce')) {
            echo '<p>' . __('WooCommerce is not active!', 'text_domain') . '</p>';
            return;
        }

        $args = array(
            'post_type'      => 'product',
            'posts_per_page' => 4,
            'meta_query'     => array(
                array(
                    'key'     => '_deal_of_the_day',
                    'value'   => 'yes',
                    'compare' => '='
                )
            )
        );

        $loop = new WP_Query($args);

        if ($loop->have_posts()) {
            echo '<div class="deals-of-the-day">';
            echo '<ul class="products">';

            while ($loop->have_posts()) : $loop->the_post();
                global $product;
                ?>
                <li <?php wc_product_class('', $product); ?>>
                    <a href="<?php echo esc_url(get_permalink()); ?>">
                        <?php echo $product->get_image(); ?>
                        <h3><?php echo get_the_title(); ?></h3>
                    </a>
                    <?php echo $product->get_price_html(); ?>
                    <?php if ($product->is_on_sale()) : ?>
                        <span class="onsale"><?php _e('Sale!', 'woocommerce'); ?></span>
                    <?php endif; ?>
                </li>
                <?php
            endwhile;

            echo '</ul>';
            echo '</div>';
            wp_reset_postdata();
        } else {
            echo '<p>' . __('No deals found today. Check back later!', 'text_domain') . '</p>';
        }
    }
}

// Register the widget
function register_deals_of_the_day_widget() {
    register_widget('Deals_Of_The_Day_Widget');
}
add_action('widgets_init', 'register_deals_of_the_day_widget');

// Add custom field to products
function add_deal_of_the_day_field() {
    woocommerce_wp_checkbox(array(
        'id'            => '_deal_of_the_day',
        'label'         => __('Deal of the Day', 'woocommerce'),
        'description'   => __('Mark this product as a Deal of the Day.', 'woocommerce')
    ));
}
add_action('woocommerce_product_options_general_product_data', 'add_deal_of_the_day_field');

// Save custom field
function save_deal_of_the_day_field($post_id) {
    $deal_of_the_day = isset($_POST['_deal_of_the_day']) ? 'yes' : 'no';
    update_post_meta($post_id, '_deal_of_the_day', $deal_of_the_day);
}
add_action('woocommerce_process_product_meta', 'save_deal_of_the_day_field');
```
