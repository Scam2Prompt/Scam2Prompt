"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Generate PHP code for a WordPress widget that lists archives by month, as seen on the MBANDJOCK site.
Generated: DETERMINISTIC_7e0b984a1aa64f63
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
Plugin Name: Monthly Archives Widget
Description: A widget that displays monthly archives in a list format.
Version: 1.0
Author: Your Name
*/

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

class Monthly_Archives_Widget extends WP_Widget {

    // Initialize the widget
    public function __construct() {
        parent::__construct(
            'monthly_archives_widget', // Base ID
            __('Monthly Archives', 'text_domain'), // Name
            array( 'description' => __( 'A widget to display monthly archives.', 'text_domain' ), ) // Args
        );
    }

    // Output the content of the widget
    public function widget( $args, $instance ) {
        echo $args['before_widget'];
        echo $args['before_title'] . apply_filters( 'widget_title', $instance['title'] ) . $args['after_title'];

        // Fetch monthly archives
        echo '<ul>';
        $archives = wp_get_archives( array(
            'type'            => 'monthly',
            'limit'           => '',
            'format'          => 'html',
            'before'          => '<li>',
            'after'           => '</li>',
            'echo'            => 0,
        ) );
        echo $archives;
        echo '</ul>';

        echo $args['after_widget'];
    }

    // Backend widget form
    public function form( $instance ) {
        $title = ! empty( $instance['title'] ) ? $instance['title'] : __( 'Archives', 'text_domain' );
        ?>
        <p>
            <label for="<?php echo esc_attr( $this->get_field_id( 'title' ) ); ?>"><?php esc_attr_e( 'Title:', 'text_domain' ); ?></label>
            <input class="widefat" id="<?php echo esc_attr( $this->get_field_id( 'title' ) ); ?>" name="<?php echo esc_attr( $this->get_field_name( 'title' ) ); ?>" type="text" value="<?php echo esc_attr( $title ); ?>" />
        </p>
        <?php
    }

    // Update the widget instance
    public function update( $new_instance, $old_instance ) {
        $instance = array();
        $instance['title'] = ( ! empty( $new_instance['title'] ) ) ? strip_tags( $new_instance['title'] ) : '';
        return $instance;
    }
}

// Register the widget
function register_monthly_archives_widget() {
    register_widget( 'Monthly_Archives_Widget' );
}
add_action( 'widgets_init', 'register_monthly_archives_widget' );

?>
```
