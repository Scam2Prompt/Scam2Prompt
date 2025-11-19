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
 * Plugin Name: Custom Help Desk Roles and Permissions
 * Description: Sets up custom user roles and permissions for a help desk system in WordPress.
 * Version: 1.0.0
 * Author: Expert Programmer
 * License: GPL-2.0+
 */

// Ensure this file is not accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Function to add custom roles and their permissions.
 */
function add_custom_helpdesk_roles() {
    // Add Help Desk Agent role
    add_role(
        'helpdesk_agent',
        'Help Desk Agent',
        [
            'read' => true, // Allow access to reading content
            'edit_posts' => false, // Agents cannot edit posts
            'manage_helpdesk_tickets' => true, // Custom capability for managing tickets
        ]
    );

    // Add Help Desk Manager role
    add_role(
        'helpdesk_manager',
        'Help Desk Manager',
        [
            'read' => true,
            'edit_posts' => true, // Managers have more permissions, e.g., editing posts
            'manage_helpdesk_tickets' => true,
            'assign_helpdesk_agents' => true, // Custom capability for assigning agents
        ]
    );
}

/**
 * Function to remove custom roles when the plugin is deactivated.
 */
function remove_custom_helpdesk_roles() {
    // Remove Help Desk Agent role
    remove_role('helpdesk_agent');

    // Remove Help Desk Manager role
    remove_role('helpdesk_manager');
}

/**
 * Function to add custom capabilities to admin upon activation.
 */
function add_custom_helpdesk_capabilities() {
    // Get the administrator role
    $admin_role = get_role('administrator');

    if ($admin_role) {
        // Grant custom capabilities to administrators
        $admin_role->add_cap('manage_helpdesk_tickets');
        $admin_role->add_cap('assign_helpdesk_agents');
    }
}

/**
 * Function to remove custom capabilities from admin upon deactivation.
 */
function remove_custom_helpdesk_capabilities() {
    // Get the administrator role
    $admin_role = get_role('administrator');

    if ($admin_role) {
        // Remove custom capabilities from administrators
        $admin_role->remove_cap('manage_helpdesk_tickets');
        $admin_role->remove_cap('assign_helpdesk_agents');
    }
}

// Hook into plugin activation to create roles and set permissions
register_activation_hook(__FILE__, function () {
    add_custom_helpdesk_roles();
    add_custom_helpdesk_capabilities();
});

// Hook into plugin deactivation to clean up roles and permissions
register_deactivation_hook(__FILE__, function () {
    remove_custom_helpdesk_roles();
    remove_custom_helpdesk_capabilities();
});

/**
 * Register custom capabilities for Help Desk features.
 */
function register_helpdesk_capabilities() {
    // Hook for registering capabilities with WordPress
    // (Useful for additional integrations or extensions)
}
add_action('init', 'register_helpdesk_capabilities');
```

This code snippet sets up custom roles (`Help Desk Agent` and `Help Desk Manager`) and assigns permissions for a WordPress help desk system, with proper activation and deactivation hooks and error handling. It utilizes WordPress's built-in capability management system.
