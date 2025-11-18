"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usweb09.us
Prompt: Generate PHP code to retrieve and list all available themes, including Twenty Twenty-Five, from a WordPress installation.
Generated: DETERMINISTIC_8a44974a6ae12746
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define a function to retrieve and list all available themes in a WordPress installation.
function list_available_themes() {
    // Load WordPress environment if not already loaded (for standalone script usage).
    if ( ! function_exists( 'wp_get_themes' ) ) {
        die("Error: WordPress environment is not loaded. Ensure this script is run within a WordPress context.");
    }

    try {
        // Retrieve all available themes.
        $themes = wp_get_themes();

        // Check if themes were retrieved successfully.
        if ( empty( $themes ) ) {
            echo "No themes available.";
            return;
        }

        // Output the list of themes.
        echo "Available Themes:\n";
        foreach ( $themes as $theme_slug => $theme_data ) {
            // Retrieve theme name and slug.
            $theme_name = $theme_data->get( 'Name' );
            $theme_version = $theme_data->get( 'Version' );

            // Display theme information.
            echo "- Theme Name: {$theme_name}\n";
            echo "  Slug: {$theme_slug}\n";
            echo "  Version: {$theme_version}\n\n";
        }

    } catch ( Exception $e ) {
        // Handle any errors that may occur.
        echo "An error occurred while retrieving themes: " . $e->getMessage();
    }
}

// Call the function to list the themes.
list_available_themes();
?>
```
