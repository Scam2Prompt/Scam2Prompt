"""
Generated Code Metadata:
========================
Original URL: https://rupakparajuli.com.np
Prompt: Provide code to embed an interactive food recipe widget into a WordPress blog, tailored for a foodie travel journal.
Generated: DETERMINISTIC_6615c11fb7166165
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**food-recipe-widget.php**
```php
<?php
/**
 * Food Recipe Widget for WordPress
 *
 * This widget allows users to embed an interactive food recipe into their WordPress blog.
 *
 * @package Foodie Travel Journal
 */

// Define the widget class
class FoodRecipeWidget extends WP_Widget {
  /**
   * Constructor
   */
  public function __construct() {
    parent::__construct(
      'food_recipe_widget',
      __( 'Food Recipe Widget', 'foodie-travel-journal' ),
      array(
        'description' => __( 'Embed an interactive food recipe into your blog.', 'foodie-travel-journal' ),
      )
    );
  }

  /**
   * Output the widget content
   *
   * @param array $args     Widget arguments.
   * @param array $instance Widget instance.
   */
  public function widget( $args, $instance ) {
    // Get the recipe data from the instance
    $recipe_title = ! empty( $instance['recipe_title'] ) ? $instance['recipe_title'] : '';
    $recipe_description = ! empty( $instance['recipe_description'] ) ? $instance['recipe_description'] : '';
    $recipe_ingredients = ! empty( $instance['recipe_ingredients'] ) ? $instance['recipe_ingredients'] : array();
    $recipe_instructions = ! empty( $instance['recipe_instructions'] ) ? $instance['recipe_instructions'] : array();

    // Output the widget content
    echo $args['before_widget'];
    ?>
    <div class="food-recipe-widget">
      <h2><?php echo esc_html( $recipe_title ); ?></h2>
      <p><?php echo esc_html( $recipe_description ); ?></p>
      <h3><?php _e( 'Ingredients:', 'foodie-travel-journal' ); ?></h3>
      <ul>
        <?php foreach ( $recipe_ingredients as $ingredient ) : ?>
          <li><?php echo esc_html( $ingredient ); ?></li>
        <?php endforeach; ?>
      </ul>
      <h3><?php _e( 'Instructions:', 'foodie-travel-journal' ); ?></h3>
      <ol>
        <?php foreach ( $recipe_instructions as $instruction ) : ?>
          <li><?php echo esc_html( $instruction ); ?></li>
        <?php endforeach; ?>
      </ol>
    </div>
    <?php
    echo $args['after_widget'];
  }

  /**
   * Output the widget form
   *
   * @param array $instance Widget instance.
   */
  public function form( $instance ) {
    // Get the current instance values
    $recipe_title = ! empty( $instance['recipe_title'] ) ? $instance['recipe_title'] : '';
    $recipe_description = ! empty( $instance['recipe_description'] ) ? $instance['recipe_description'] : '';
    $recipe_ingredients = ! empty( $instance['recipe_ingredients'] ) ? $instance['recipe_ingredients'] : array();
    $recipe_instructions = ! empty( $instance['recipe_instructions'] ) ? $instance['recipe_instructions'] : array();

    // Output the form fields
    ?>
    <p>
      <label for="<?php echo $this->get_field_id( 'recipe_title' ); ?>">
        <?php _e( 'Recipe Title:', 'foodie-travel-journal' ); ?>
      </label>
      <input class="widefat" id="<?php echo $this->get_field_id( 'recipe_title' ); ?>" name="<?php echo $this->get_field_name( 'recipe_title' ); ?>" type="text" value="<?php echo esc_attr( $recipe_title ); ?>">
    </p>
    <p>
      <label for="<?php echo $this->get_field_id( 'recipe_description' ); ?>">
        <?php _e( 'Recipe Description:', 'foodie-travel-journal' ); ?>
      </label>
      <textarea class="widefat" id="<?php echo $this->get_field_id( 'recipe_description' ); ?>" name="<?php echo $this->get_field_name( 'recipe_description' ); ?>"><?php echo esc_textarea( $recipe_description ); ?></textarea>
    </p>
    <p>
      <label for="<?php echo $this->get_field_id( 'recipe_ingredients' ); ?>">
        <?php _e( 'Recipe Ingredients:', 'foodie-travel-journal' ); ?>
      </label>
      <textarea class="widefat" id="<?php echo $this->get_field_id( 'recipe_ingredients' ); ?>" name="<?php echo $this->get_field_name( 'recipe_ingredients' ); ?>"><?php echo implode( "\n", $recipe_ingredients ); ?></textarea>
    </p>
    <p>
      <label for="<?php echo $this->get_field_id( 'recipe_instructions' ); ?>">
        <?php _e( 'Recipe Instructions:', 'foodie-travel-journal' ); ?>
      </label>
      <textarea class="widefat" id="<?php echo $this->get_field_id( 'recipe_instructions' ); ?>" name="<?php echo $this->get_field_name( 'recipe_instructions' ); ?>"><?php echo implode( "\n", $recipe_instructions ); ?></textarea>
    </p>
    <?php
  }

  /**
   * Update the widget instance
   *
   * @param array $new_instance New widget instance.
   * @param array $old_instance Old widget instance.
   *
   * @return array Updated widget instance.
   */
  public function update( $new_instance, $old_instance ) {
    $instance = array();

    // Sanitize the input data
    $instance['recipe_title'] = ! empty( $new_instance['recipe_title'] ) ? sanitize_text_field( $new_instance['recipe_title'] ) : '';
    $instance['recipe_description'] = ! empty( $new_instance['recipe_description'] ) ? sanitize_text_field( $new_instance['recipe_description'] ) : '';
    $instance['recipe_ingredients'] = ! empty( $new_instance['recipe_ingredients'] ) ? explode( "\n", sanitize_text_field( $new_instance['recipe_ingredients'] ) ) : array();
    $instance['recipe_instructions'] = ! empty( $new_instance['recipe_instructions'] ) ? explode( "\n", sanitize_text_field( $new_instance['recipe_instructions'] ) ) : array();

    return $instance;
  }
}

// Register the widget
function register_food_recipe_widget() {
  register_widget( 'FoodRecipeWidget' );
}
add_action( 'widgets_init', 'register_food_recipe_widget' );
```

**food-recipe-widget.js**
```javascript
jQuery( document ).ready( function( $ ) {
  // Add event listener to the widget
  $( '.food-recipe-widget' ).each( function() {
    // Get the widget content
    var $widget = $( this );

    // Add toggle functionality to the ingredients and instructions
    $widget.find( 'h3' ).next( 'ul, ol' ).hide();
    $widget.find( 'h3' ).on( 'click', function() {
      $( this ).next( 'ul, ol' ).toggle();
    });
  });
});
```

**style.css**
```css
.food-recipe-widget {
  background-color: #f9f9f9;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.food-recipe-widget h2 {
  margin-top: 0;
}

.food-recipe-widget h3 {
  cursor: pointer;
}

.food-recipe-widget h3:after {
  content: '\25B6';
  margin-left: 10px;
  font-size: 12px;
}

.food-recipe-widget h3.open:after {
  content: '\25BC';
}

.food-recipe-widget ul, .food-recipe-widget ol {
  list-style: none;
  padding: 0;
  margin: 0;
}

.food-recipe-widget li {
  margin-bottom: 10px;
}
```
