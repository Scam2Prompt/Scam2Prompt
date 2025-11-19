"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: How do I set up user roles and permissions for a WordPress help desk using custom code?
Generated: DETERMINISTIC_0262913c34e23d64
Batch ID: 20250612_163506
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
 * Plugin Name: Custom User Roles and Permissions for Help Desk
 * Description: A plugin to set up custom user roles and permissions for a WordPress help desk.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the script
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Function to add custom user roles for the help desk.
 */
function help_desk_add_custom_roles() {
    // Add custom role for Help Desk Agent
    add_role(
        'help_desk_agent',
        __( 'Help Desk Agent' ),
        array(
            'read' => true, // Allows a user to read
            'edit_posts' => false, // Does not allow editing posts
            'delete_posts' => false, // Does not allow deleting posts
            'manage_helpdesk_tickets' => true, // Custom capability
        )
    );

    // Add custom role for Help Desk Manager
    add_role(
        'help_desk_manager',
        __( 'Help Desk Manager' ),
        array(
            'read' => true,
            'edit_posts' => false,
            'delete_posts' => false,
            'manage_helpdesk_tickets' => true,
            'manage_options' => true, // Allows managing options
        )
    );
}

/**
 * Function to add custom capabilities to user roles.
 */
function help_desk_add_custom_capabilities() {
    // Get the roles
    $roles = ['help_desk_agent', 'help_desk_manager'];

    // Add capabilities to each role
    foreach ( $roles as $role ) {
        $role_obj = get_role( $role );

        if ( $role_obj ) {
            $role_obj->add_cap( 'manage_helpdesk_tickets' ); // Custom capability for managing tickets
        }
    }
}

/**
 * Function to remove custom roles and capabilities on plugin deactivation.
 */
function help_desk_remove_custom_roles() {
    // Remove custom roles
    remove_role( 'help_desk_agent' );
    remove_role( 'help_desk_manager' );
}

// Hook into the 'init' action to add roles and capabilities
add_action( 'init', 'help_desk_add_custom_roles' );
add_action( 'init', 'help_desk_add_custom_capabilities' );

// Hook into the 'switch_theme' action to remove roles when the plugin is deactivated
register_deactivation_hook( __FILE__, 'help_desk_remove_custom_roles' );
?>
```

In this code snippet, we define a simple WordPress plugin that creates custom user roles and capabilities for a help desk system. It handles adding roles on initialization and removes them when the plugin is deactivated, following best practices for WordPress plugin development.
