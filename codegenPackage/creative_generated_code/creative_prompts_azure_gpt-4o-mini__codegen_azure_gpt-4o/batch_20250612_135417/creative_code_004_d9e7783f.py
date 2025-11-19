"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiffany-holz.de
Prompt: Provide an example of customizing the Ashe theme for showcasing personal projects and hobbies.
Generated: DETERMINISTIC_d9e7783f0a641816
Batch ID: 20250612_135417
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
 * Customizing the Ashe theme to showcase personal projects and hobbies.
 * This code should be added to the child theme's functions.php file or a plugin.
 */

// Ensure the code runs only within the Ashe theme.
add_action('after_setup_theme', function () {
    if (get_template() !== 'ashe') {
        return;
    }

    /**
     * Register a custom post type for Projects & Hobbies.
     */
    function register_projects_hobbies_post_type() {
        $labels = [
            'name'               => __('Projects & Hobbies', 'ashe-child'),
            'singular_name'      => __('Project & Hobby', 'ashe-child'),
            'menu_name'          => __('Projects & Hobbies', 'ashe-child'),
            'name_admin_bar'     => __('Project & Hobby', 'ashe-child'),
            'add_new'            => __('Add New', 'ashe-child'),
            'add_new_item'       => __('Add New Project or Hobby', 'ashe-child'),
            'edit_item'          => __('Edit Project or Hobby', 'ashe-child'),
            'new_item'           => __('New Project or Hobby', 'ashe-child'),
            'view_item'          => __('View Project or Hobby', 'ashe-child'),
            'all_items'          => __('All Projects & Hobbies', 'ashe-child'),
            'search_items'       => __('Search Projects & Hobbies', 'ashe-child'),
            'not_found'          => __('No Projects & Hobbies Found', 'ashe-child'),
            'not_found_in_trash' => __('No Projects & Hobbies Found in Trash', 'ashe-child'),
        ];

        $args = [
            'labels'             => $labels,
            'public'             => true,
            'has_archive'        => true,
            'rewrite'            => ['slug' => 'projects-hobbies'],
            'supports'           => ['title', 'editor', 'thumbnail', 'custom-fields', 'excerpt'],
            'menu_icon'          => 'dashicons-art',
            'show_in_rest'       => true, // Enable Gutenberg support.
        ];

        register_post_type('projects_hobbies', $args);
    }
    add_action('init', 'register_projects_hobbies_post_type');

    /**
     * Register a custom taxonomy for categorizing projects and hobbies.
     */
    function register_project_hobby_taxonomy() {
        $labels = [
            'name'              => __('Project & Hobby Categories', 'ashe-child'),
            'singular_name'     => __('Category', 'ashe-child'),
            'search_items'      => __('Search Categories', 'ashe-child'),
            'all_items'         => __('All Categories', 'ashe-child'),
            'parent_item'       => __('Parent Category', 'ashe-child'),
            'parent_item_colon' => __('Parent Category:', 'ashe-child'),
            'edit_item'         => __('Edit Category', 'ashe-child'),
            'update_item'       => __('Update Category', 'ashe-child'),
            'add_new_item'      => __('Add New Category', 'ashe-child'),
            'new_item_name'     => __('New Category Name', 'ashe-child'),
            'menu_name'         => __('Categories', 'ashe-child'),
        ];

        $args = [
            'labels'            => $labels,
            'hierarchical'      => true,
            'show_in_rest'      => true, // Enable Gutenberg support.
            'rewrite'           => ['slug' => 'project-hobby-category'],
        ];

        register_taxonomy('project_hobby_category', ['projects_hobbies'], $args);
    }
    add_action('init', 'register_project_hobby_taxonomy');

    /**
     * Display Projects & Hobbies on a custom page template.
     */
    function create_projects_hobbies_page_template($template) {
        if (is_post_type_archive('projects_hobbies')) {
            // Use a custom template located in the child theme directory.
            $custom_template = get_stylesheet_directory() . '/archive-projects_hobbies.php';
            if (file_exists($custom_template)) {
                return $custom_template;
            }
        }

        return $template;
    }
    add_filter('template_include', 'create_projects_hobbies_page_template');

    /**
     * Enqueue additional styles for customizing the display.
     */
    function enqueue_projects_hobbies_styles() {
        wp_enqueue_style('projects-hobbies-styles', get_stylesheet_directory_uri() . '/projects-hobbies.css', [], '1.0.0');
    }
    add_action('wp_enqueue_scripts', 'enqueue_projects_hobbies_styles');
});
```
