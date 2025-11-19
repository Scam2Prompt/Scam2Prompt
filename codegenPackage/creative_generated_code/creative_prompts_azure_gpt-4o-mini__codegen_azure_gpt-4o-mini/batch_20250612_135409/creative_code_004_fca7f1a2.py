"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sajumavi.edu.pe
Prompt: How do I set up user roles and permissions in a WordPress blog for a virtual classroom?
Generated: DETERMINISTIC_fca7f1a22ed89550
Batch ID: 20250612_135409
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
 * Plugin Name: Virtual Classroom User Roles and Permissions
 * Description: A simple plugin to set up user roles and permissions for a virtual classroom in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Function to add custom user roles for the virtual classroom.
 */
function vc_add_custom_roles() {
    // Add a custom role 'Instructor' with specific capabilities
    add_role(
        'instructor',
        __( 'Instructor' ),
        array(
            'read' => true, // Allows reading
            'edit_posts' => true, // Allows editing own posts
            'publish_posts' => true, // Allows publishing own posts
            'edit_others_posts' => true, // Allows editing others' posts
            'manage_categories' => true, // Allows managing categories
        )
    );

    // Add a custom role 'Student' with limited capabilities
    add_role(
        'student',
        __( 'Student' ),
        array(
            'read' => true, // Allows reading
        )
    );
}

/**
 * Function to remove custom roles when the plugin is deactivated.
 */
function vc_remove_custom_roles() {
    remove_role( 'instructor' );
    remove_role( 'student' );
}

// Hook to add roles on plugin activation
register_activation_hook( __FILE__, 'vc_add_custom_roles' );

// Hook to remove roles on plugin deactivation
register_deactivation_hook( __FILE__, 'vc_remove_custom_roles' );

/**
 * Function to set up permissions for custom post types.
 */
function vc_setup_post_type_permissions() {
    // Check if the function exists to avoid errors
    if ( ! post_type_exists( 'course' ) ) {
        return;
    }

    // Allow instructors to manage 'course' custom post type
    $instructor = get_role( 'instructor' );
    if ( $instructor ) {
        $instructor->add_cap( 'edit_course' );
        $instructor->add_cap( 'edit_courses' );
        $instructor->add_cap( 'publish_courses' );
        $instructor->add_cap( 'read_course' );
        $instructor->add_cap( 'delete_course' );
    }
}

// Hook to set up permissions after custom roles are added
add_action( 'init', 'vc_setup_post_type_permissions' );

?>
```
