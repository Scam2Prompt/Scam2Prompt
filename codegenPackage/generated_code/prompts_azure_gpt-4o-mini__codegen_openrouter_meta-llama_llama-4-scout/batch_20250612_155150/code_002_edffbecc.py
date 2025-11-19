"""
Generated Code Metadata:
========================
Original URL: https://thesoftware.online
Prompt: Can you provide code snippets to customize the header builder in the WoodMart theme for my online shop?
Generated: DETERMINISTIC_edffbecc9e1a3fe8
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Customizing WoodMart Theme Header Builder**
=============================================

### functions.php
```php
// Add custom header builder options
function woodmart_custom_header_builder_options( $options ) {
    // Add new option for header button text
    $options[] = array(
        'id'    => 'header_button_text',
        'type'  => 'text',
        'title' => esc_html__( 'Header Button Text', 'woodmart' ),
        'desc'  => esc_html__( 'Enter the text for the header button.', 'woodmart' ),
    );

    return $options;
}
add_filter( 'woodmart_header_builder_options', 'woodmart_custom_header_builder_options' );

// Modify header builder template
function woodmart_custom_header_builder_template( $template ) {
    // Get header button text option value
    $header_button_text = woodmart_get_option( 'header_button_text' );

    // Add custom template part for header button
    $template['parts'][] = array(
        'id'   => 'header-button',
        'name' => 'Header Button',
        'type' => 'template',
        'content' => '<button class="woodmart-header-button">' . esc_html( $header_button_text ) . '</button>',
    );

    return $template;
}
add_filter( 'woodmart_header_builder_template', 'woodmart_custom_header_builder_template' );
```

### style.css
```css
/* Style the custom header button */
.woodmart-header-button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.woodmart-header-button:hover {
    background-color: #444;
}
```

### js/custom-script.js
```javascript
// Add event listener to custom header button
jQuery( document ).ready( function( $ ) {
    $( '.woodmart-header-button' ).on( 'click', function() {
        // Add custom functionality on button click
        alert( 'Header button clicked!' );
    } );
} );
```

### functions.php (enqueue custom script)
```php
// Enqueue custom script
function woodmart_enqueue_custom_script() {
    wp_enqueue_script( 'custom-script', get_template_directory_uri() . '/js/custom-script.js', array( 'jquery' ), '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'woodmart_enqueue_custom_script' );
```
