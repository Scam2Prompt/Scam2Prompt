"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thesoftware.online
Prompt: Provide JavaScript code to enhance the search functionality on a WordPress site, enabling real-time post previews as users type, similar to the search feature described in a WooCommerce-based site.
Generated: DETERMINISTIC_7641639f861beb74
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Enhance search functionality with real-time post previews
// This script assumes jQuery is available on the WordPress site

(function($) {
    // DOM ready function
    $(document).ready(function() {
        // Attach input event listener to the search input field
        $('#search-input').on('input', function() {
            // Retrieve the current input value
            const query = $(this).val().trim();

            // Clear previous results if input is empty
            if (query.length === 0) {
                $('#search-results').empty().hide();
                return;
            }

            // Perform an AJAX request to fetch search results
            $.ajax({
                url: '/wp-admin/admin-ajax.php', // WordPress AJAX endpoint
                type: 'POST',
                data: {
                    action: 'search_posts', // Custom action for searching posts
                    query: query // The search query
                },
                dataType: 'json',
                success: function(response) {
                    // Check if the response contains results
                    if (response.success && response.data.length > 0) {
                        // Clear previous results
                        $('#search-results').empty();
                        
                        // Populate search results
                        response.data.forEach(function(post) {
                            $('#search-results').append(`
                                <div class="search-result">
                                    <h3><a href="${post.link}">${post.title}</a></h3>
                                    <p>${post.excerpt}</p>
                                </div>
                            `);
                        });

                        // Show results container
                        $('#search-results').show();
                    } else {
                        // Hide results if no matches found
                        $('#search-results').empty().hide();
                    }
                },
                error: function(xhr, status, error) {
                    // Log error message for debugging purposes
                    console.error('AJAX Error:', status, error);
                    // Optionally, show a user-friendly error message
                    $('#search-results').html('<p>Sorry, there was an error retrieving the results. Please try again.</p>').show();
                }
            });
        });
    });
})(jQuery);

// WordPress backend: functions.php
add_action('wp_ajax_search_posts', 'ajax_search_posts');
add_action('wp_ajax_nopriv_search_posts', 'ajax_search_posts');

/**
 * AJAX handler for searching posts
 */
function ajax_search_posts() {
    // Check if the query parameter is set
    if (!isset($_POST['query'])) {
        wp_send_json_error('No query parameter provided.');
    }

    $query = sanitize_text_field($_POST['query']);

    // WP_Query arguments
    $args = [
        'post_type' => 'post', // Change to your desired post type
        's' => $query, // The search query
        'posts_per_page' => 5 // Limit results
    ];

    // Execute the query
    $query = new WP_Query($args);

    // Prepare the results
    $results = [];
    if ($query->have_posts()) {
        while ($query->have_posts()) {
            $query->the_post();
            $results[] = [
                'title' => get_the_title(),
                'link' => get_permalink(),
                'excerpt' => get_the_excerpt()
            ];
        }
        wp_reset_postdata();
    }

    // Send the response
    wp_send_json_success($results);
}
```

Make sure to add an input field with `id="search-input"` and a container with `id="search-results"` in your WordPress theme where the search results will be displayed.
