"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krushinews18.com
Prompt: How can I implement a "recent posts" widget in my WordPress blog like the one mentioned on krushinews18.com?
Generated: DETERMINISTIC_770eb7903312f16a
Batch ID: 20250612_163324
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
 * Plugin Name: Recent Posts Widget
 * Description: A simple widget to display recent posts on your WordPress site.
 * Author: Your Name
 * Version: 1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class Recent_Posts_Widget
 */
class Recent_Posts_Widget extends WP_Widget {

    /**
     * Register widget with WordPress.
     */
    public function __construct() {
        parent::__construct(
            'recent_posts_widget', // Base ID
            esc_html__( 'Recent Posts', 'text_domain' ), // Name
            array( 'description' => esc_html__( 'A Widget to display recent posts', 'text_domain' ), ) // Args
        );
    }

    /**
     * Front-end display of widget.
     *
     * @param array $args Widget arguments.
     * @param array $instance Saved values from database.
     */
    public function widget( $args, $instance ) {
        // Output generated before the widget
        echo $args['before_widget'];

        // Widget title
        if ( ! empty( $instance['title'] ) ) {
            echo $args['before_title'] . esc_html( $instance['title'] ) . $args['after_title'];
        }

        // Query recent posts
        $recent_posts = new WP_Query( array(
            'posts_per_page' => $instance['number_of_posts'],
            'post_status'    => 'publish',
        ) );

        if ( $recent_posts->have_posts() ) {
            echo '<ul class="recent-posts-list">';
            while ( $recent_posts->have_posts() ) {
                $recent_posts->the_post(); ?>
                <li>
                    <a href="<?php the_permalink(); ?>" title="<?php the_title(); ?>">
                        <?php the_title(); ?>
                    </a>
                </li>
                <?php
            }
            echo '</ul>';
        } else {
            echo esc_html__( 'No recent posts available.', 'text_domain' );
        }

        // Restore original Post Data
        wp_reset_postdata();

        // Output generated after the widget
        echo $args['after_widget'];
    }

    /**
     * Backend widget form.
     *
     * @param array $instance Previously saved values from database.
     */
    public function form( $instance ) {
        $title = ! empty( $instance['title'] ) ? $instance['title'] : esc_html__( 'Recent Posts', 'text_domain' );
        $number_of_posts = ! empty( $instance['number_of_posts'] ) ? $instance['number_of_posts'] : 5; ?>
        
        <p>
            <label for="<?php echo esc_attr( $this->get_field_id( 'title' ) ); ?>"><?php esc_attr_e( 'Title:', 'text_domain' ); ?></label>
            <input class="widefat" id="<?php echo esc_attr( $this->get_field_id( 'title' ) ); ?>" name="<?php echo esc_attr( $this->get_field_name( 'title' ) ); ?>" type="text" value="<?php echo esc_attr( $title ); ?>">
        </p>
        <p>
            <label for="<?php echo esc_attr( $this->get_field_id( 'number_of_posts' ) ); ?>"><?php esc_attr_e( 'Number of Posts to Show:', 'text_domain' ); ?></label>
            <input class="tiny-text" id="<?php echo esc_attr( $this->get_field_id( 'number_of_posts' ) ); ?>" name="<?php echo esc_attr( $this->get_field_name( 'number_of_posts' ) ); ?>" type="number" step="1" min="1" value="<?php echo esc_attr( $number_of_posts ); ?>" size="3">
        </p>
        <?php
    }

    /**
     * Sanitize widget form values as they are saved.
     *
     * @param array $new_instance Values just sent to be saved.
     * @param array $old_instance Previously saved values from database.
     *
     * @return array Safe sanitized values to be saved.
     */
    public function update( $new_instance, $old_instance ) {
        $instance = array();
        $instance['title'] = ( ! empty( $new_instance['title'] ) ) ? strip_tags( $new_instance['title'] ) : '';
        $instance['number_of_posts'] = ( ! empty( $new_instance['number_of_posts'] ) ) ? intval( $new_instance['number_of_posts'] ) : 5;

        return $instance;
    }
}

/**
 * Register the widget.
 */
function register_recent_posts_widget() {
    register_widget( 'Recent_Posts_Widget' );
}

add_action( 'widgets_init', 'register_recent_posts_widget' );
?>
```
This code creates a WordPress widget that displays the recent posts. You can save this as a PHP file in the `/wp-content/plugins/` directory, activate it from the WordPress admin panel, and add it to your sidebar or any widget area.
