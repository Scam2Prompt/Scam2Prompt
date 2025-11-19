"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Develop a search functionality in a WordPress site that mimics the search feature seen on mbandjock.fr.
Generated: DETERMINISTIC_c50b5f8d1f2ba488
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for implementing a custom search functionality in a WordPress site. This code assumes that you are familiar with WordPress theme development and will be adding the code to your theme's `functions.php` file and creating a custom search form.

### Code for `functions.php`

```php
<?php
// Enqueue necessary assets
function custom_search_enqueue_scripts() {
    wp_enqueue_script('custom-search-js', get_template_directory_uri() . '/js/custom-search.js', array('jquery'), null, true);
    wp_localize_script('custom-search-js', 'search_params', array(
        'ajax_url' => admin_url('admin-ajax.php'),
    ));
}
add_action('wp_enqueue_scripts', 'custom_search_enqueue_scripts');

// Handle AJAX search request
function custom_ajax_search() {
    // Verify the AJAX request is valid
    check_ajax_referer('search_nonce', 'security');

    $search_query = sanitize_text_field($_POST['query']);

    // WP_Query to retrieve posts based on the search term
    $args = array(
        'post_type' => 'post', // Change this to your desired post type
        'posts_per_page' => 10, // Limit the number of results
        's' => $search_query, // Search term
    );

    $query = new WP_Query($args);

    if ($query->have_posts()) {
        $results = array();
        while ($query->have_posts()) {
            $query->the_post();
            $results[] = array(
                'title' => get_the_title(),
                'link' => get_permalink(),
                'excerpt' => get_the_excerpt(),
            );
        }
        wp_send_json_success($results); // Return results as JSON
    } else {
        wp_send_json_error(array('message' => 'No results found.'));
    }

    wp_die();
}
add_action('wp_ajax_nopriv_custom_ajax_search', 'custom_ajax_search');
add_action('wp_ajax_custom_ajax_search', 'custom_ajax_search');
?>

```

### Code for `searchform.php`

```php
<form id="custom-search-form" role="search" method="get" class="search-form">
    <label for="search-input">Search:</label>
    <input type="text" id="search-input" name="s" placeholder="Start typing...">
    <button type="button" id="search-button">Search</button>
    <div id="search-results"></div>
</form>
```

### Code for `js/custom-search.js`

```javascript
jQuery(document).ready(function ($) {
    $('#search-button').on('click', function () {
        var query = $('#search-input').val();

        if (query.trim() === '') {
            alert('Please enter a search term.');
            return;
        }

        // Perform AJAX request
        $.ajax({
            url: search_params.ajax_url,
            type: 'POST',
            data: {
                action: 'custom_ajax_search',
                query: query,
                security: search_params.search_nonce, // Ensure request is secure
            },
            beforeSend: function () {
                $('#search-results').html('<p>Searching...</p>');
            },
            success: function (response) {
                if (response.success) {
                    var resultsHTML = '';
                    response.data.forEach(function (result) {
                        resultsHTML += '<div class="search-result">';
                        resultsHTML += '<h4><a href="' + result.link + '">' + result.title + '</a></h4>';
                        resultsHTML += '<p>' + result.excerpt + '</p>';
                        resultsHTML += '</div>';
                    });
                    $('#search-results').html(resultsHTML);
                } else {
                    $('#search-results').html('<p>' + response.data.message + '</p>');
                }
            },
            error: function () {
                $('#search-results').html('<p>An error occurred while searching.</p>');
            },
        });
    });
});
```

### Additional Notes:
- Ensure you generate a nonce for AJAX security in your theme's header using `wp_create_nonce('search_nonce')`.
- Place the `searchform.php` file in your theme directory and load it where necessary.
- Create a file `js/custom-search.js` in your theme and include the script using `functions.php`.
