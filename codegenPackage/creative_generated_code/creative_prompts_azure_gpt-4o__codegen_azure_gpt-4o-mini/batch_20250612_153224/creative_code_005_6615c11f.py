"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Provide code to embed an interactive food recipe widget into a WordPress blog, tailored for a foodie travel journal.
Generated: DETERMINISTIC_6615c11fb7166165
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
Plugin Name: Interactive Food Recipe Widget
Description: A simple widget to showcase interactive food recipes tailored for a foodie travel journal.
Version: 1.0
Author: Your Name
*/

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Register the widget
function ifrw_register_widget() {
    register_widget( 'IFRW_Recipe_Widget' );
}
add_action( 'widgets_init', 'ifrw_register_widget' );

// Create the widget class
class IFRW_Recipe_Widget extends WP_Widget {

    // Constructor
    public function __construct() {
        parent::__construct(
            'ifrw_recipe_widget', // Base ID
            'Interactive Recipe Widget', // Name
            array( 'description' => __( 'A widget to display interactive food recipes.', 'text_domain' ) ) // Args
        );
    }

    // Front-end display of widget
    public function widget( $args, $instance ) {
        // Escape output
        $title = apply_filters( 'widget_title', $instance['title'] );
        $recipe_url = esc_url( $instance['recipe_url'] );
        $recipe_image = esc_url( $instance['recipe_image'] );

        // Output widget HTML
        echo $args['before_widget'];
        if ( ! empty( $title ) ) {
            echo $args['before_title'] . $title . $args['after_title'];
        }
        ?>
        <div class="ifrw-recipe-widget">
            <img src="<?php echo $recipe_image; ?>" alt="<?php echo $title; ?>" />
            <a href="<?php echo $recipe_url; ?>" target="_blank" class="ifrw-recipe-button"><?php _e( 'View Recipe', 'text_domain' ); ?></a>
        </div>
        <?php
        echo $args['after_widget'];
    }

    // Back-end widget form
    public function form( $instance ) {
        // Set default values
        $title = ! empty( $instance['title'] ) ? $instance['title'] : __( 'New Recipe', 'text_domain' );
        $recipe_url = ! empty( $instance['recipe_url'] ) ? $instance['recipe_url'] : '';
        $recipe_image = ! empty( $instance['recipe_image'] ) ? $instance['recipe_image'] : '';
        ?>
        <p>
            <label for="<?php echo esc_attr( $this->get_field_id( 'title' ) ); ?>"><?php _e( 'Title:', 'text_domain' ); ?></label>
            <input class="widefat" id="<?php echo esc_attr( $this->get_field_id( 'title' ) ); ?>" name="<?php echo esc_attr( $this->get_field_name( 'title' ) ); ?>" type="text" value="<?php echo esc_attr( $title ); ?>" />
        </p>
        <p>
            <label for="<?php echo esc_attr( $this->get_field_id( 'recipe_url' ) ); ?>"><?php _e( 'Recipe URL:', 'text_domain' ); ?></label>
            <input class="widefat" id="<?php echo esc_attr( $this->get_field_id( 'recipe_url' ) ); ?>" name="<?php echo esc_attr( $this->get_field_name( 'recipe_url' ) ); ?>" type="text" value="<?php echo esc_attr( $recipe_url ); ?>" />
        </p>
        <p>
            <label for="<?php echo esc_attr( $this->get_field_id( 'recipe_image' ) ); ?>"><?php _e( 'Recipe Image URL:', 'text_domain' ); ?></label>
            <input class="widefat" id="<?php echo esc_attr( $this->get_field_id( 'recipe_image' ) ); ?>" name="<?php echo esc_attr( $this->get_field_name( 'recipe_image' ) ); ?>" type="text" value="<?php echo esc_attr( $recipe_image ); ?>" />
        </p>
        <?php
    }

    // Update widget values
    public function update( $new_instance, $old_instance ) {
        $instance = array();
        $instance['title'] = ( ! empty( $new_instance['title'] ) ) ? strip_tags( $new_instance['title'] ) : '';
        $instance['recipe_url'] = ( ! empty( $new_instance['recipe_url'] ) ) ? esc_url_raw( $new_instance['recipe_url'] ) : '';
        $instance['recipe_image'] = ( ! empty( $new_instance['recipe_image'] ) ) ? esc_url_raw( $new_instance['recipe_image'] ) : '';

        return $instance;
    }
}
```

This code defines a WordPress widget that allows users to display an interactive food recipe with a title, recipe URL, and image in their blog. To use it, copy the code into a new file named `interactive-food-recipe-widget.php` and place it in the `wp-content/plugins/` directory of your WordPress installation. Activate the plugin from the WordPress admin panel and add the widget to your sidebar or any widget area.
