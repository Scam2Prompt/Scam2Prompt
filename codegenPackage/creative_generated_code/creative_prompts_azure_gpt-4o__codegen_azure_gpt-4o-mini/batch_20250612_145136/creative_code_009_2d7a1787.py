"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bharatnews18.com
Prompt: Write PHP code to create a WordPress widget that dynamically highlights products, similar to the "Product Highlight" widget described on BharatNews18.
Generated: DETERMINISTIC_2d7a17873d26073f
Batch ID: 20250612_145136
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
 * Plugin Name: Dynamic Product Highlight Widget
 * Description: A WordPress widget that dynamically highlights products.
 * Version: 1.0
 * Author: Your Name
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class Dynamic_Product_Highlight_Widget
 * 
 * A custom widget to display highlighted products.
 */
class Dynamic_Product_Highlight_Widget extends WP_Widget {

    /**
     * Register widget with WordPress.
     */
    public function __construct() {
        parent::__construct(
            'dynamic_product_highlight_widget', // Base ID
            'Dynamic Product Highlight', // Name
            array( 'description' => __( 'Highlights specific products.', 'text_domain' ) ) // Args
        );
    }

    /**
     * Front-end display of widget.
     *
     * @param array $args Widget arguments.
     * @param array $instance Saved values from database.
     */
    public function widget( $args, $instance ) {
        // Sanitize widget input
        $title = ! empty( $instance['title'] ) ? $instance['title'] : __( 'Product Highlight', 'text_domain' );
        $products = ! empty( $instance['products'] ) ? explode( ',', $instance['products'] ) : array();

        echo $args['before_widget'];
        if ( ! empty( $title ) ) {
            echo $args['before_title'] . esc_html( $title ) . $args['after_title'];
        }

        // Output the highlighted products
        if ( ! empty( $products ) ) {
            echo '<ul class="highlighted-products">';
            foreach ( $products as $product_id ) {
                $product = wc_get_product( intval( $product_id ) );
                if ( $product ) {
                    echo '<li>';
                    echo '<a href="' . esc_url( get_permalink( $product_id ) ) . '">' . esc_html( $product->get_name() ) . '</a>';
                    echo '</li>';
                }
            }
            echo '</ul>';
        }

        echo $args['after_widget'];
    }

    /**
     * Back-end widget form.
     *
     * @param array $instance Previously saved values from database.
     */
    public function form( $instance ) {
        // Title field
        $title = ! empty( $instance['title'] ) ? $instance['title'] : __( 'Product Highlight', 'text_domain' );
        echo '<p>';
        echo '<label for="' . esc_attr( $this->get_field_id( 'title' ) ) . '">' . __( 'Title:', 'text_domain' ) . '</label>';
        echo '<input class="widefat" id="' . esc_attr( $this->get_field_id( 'title' ) ) . '" name="' . esc_attr( $this->get_field_name( 'title' ) ) . '" type="text" value="' . esc_attr( $title ) . '">';
        echo '</p>';

        // Products field
        $products = ! empty( $instance['products'] ) ? $instance['products'] : '';
        echo '<p>';
        echo '<label for="' . esc_attr( $this->get_field_id( 'products' ) ) . '">' . __( 'Product IDs (comma-separated):', 'text_domain' ) . '</label>';
        echo '<input class="widefat" id="' . esc_attr( $this->get_field_id( 'products' ) ) . '" name="' . esc_attr( $this->get_field_name( 'products' ) ) . '" type="text" value="' . esc_attr( $products ) . '">';
        echo '</p>';
    }

    /**
     * Updating widget replacing old instances with new.
     *
     * @param array $new_instance New values.
     * @param array $old_instance Old values.
     * @return array Updated values.
     */
    public function update( $new_instance, $old_instance ) {
        $instance = array();
        $instance['title'] = ! empty( $new_instance['title'] ) ? sanitize_text_field( $new_instance['title'] ) : '';
        $instance['products'] = ! empty( $new_instance['products'] ) ? sanitize_text_field( $new_instance['products'] ) : '';

        return $instance;
    }
}

// Register Dynamic_Product_Highlight_Widget
function register_dynamic_product_highlight_widget() {
    register_widget( 'Dynamic_Product_Highlight_Widget' );
}
add_action( 'widgets_init', 'register_dynamic_product_highlight_widget' );
```

**Note**: This code is designed to be placed in a custom plugin or the `functions.php` file of your theme. Make sure that WooCommerce is installed, as it uses WooCommerce functions to fetch products.
