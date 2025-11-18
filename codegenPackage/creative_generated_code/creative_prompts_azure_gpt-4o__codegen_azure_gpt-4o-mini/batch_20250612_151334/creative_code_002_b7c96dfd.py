"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magic-eden.io
Prompt: Generate a script to integrate Magic Eden's marketplace data into a WordPress site, allowing users to browse NFT collections directly.
Generated: DETERMINISTIC_b7c96dfd0ac38d8f
Batch ID: 20250612_151334
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.magiceden.dev/v2/collections": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Magic Eden NFT Marketplace Integration
 * Description: Integrate Magic Eden's marketplace data into a WordPress site for browsing NFT collections.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue necessary scripts and styles for the plugin.
 */
function me_nft_enqueue_scripts() {
    wp_enqueue_style( 'me-nft-style', plugin_dir_url( __FILE__ ) . 'css/style.css' );
    wp_enqueue_script( 'me-nft-script', plugin_dir_url( __FILE__ ) . 'js/script.js', array('jquery'), '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'me_nft_enqueue_scripts' );

/**
 * Shortcode to display NFT collections.
 *
 * @return string HTML output for the NFT collections.
 */
function me_nft_display_collections() {
    ob_start();
    ?>
    <div id="me-nft-collections">
        <h2>NFT Collections from Magic Eden</h2>
        <div id="me-nft-list"></div>
        <div id="me-nft-loader" style="display:none;">Loading...</div>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode( 'me_nft_collections', 'me_nft_display_collections' );

/**
 * Fetch NFT collections from Magic Eden's API.
 *
 * @return void
 */
function me_nft_fetch_collections() {
    // Magic Eden API endpoint
    $url = 'https://api.magiceden.dev/v2/collections';
    
    // Make the API request
    $response = wp_remote_get( $url );

    // Check for errors in the response
    if ( is_wp_error( $response ) ) {
        wp_send_json_error( 'Failed to retrieve data: ' . $response->get_error_message() );
        return;
    }

    // Decode the JSON response
    $collections = json_decode( wp_remote_retrieve_body( $response ), true );

    // Check if the response is valid
    if ( empty( $collections ) ) {
        wp_send_json_error( 'No collections found or invalid response.' );
        return;
    }

    // Send the collections data as JSON
    wp_send_json_success( $collections );
}
add_action( 'wp_ajax_me_nft_fetch_collections', 'me_nft_fetch_collections' );
add_action( 'wp_ajax_nopriv_me_nft_fetch_collections', 'me_nft_fetch_collections' );

/**
 * JavaScript to handle fetching and displaying collections.
 */
function me_nft_js_vars() {
    ?>
    <script type="text/javascript">
        jQuery(document).ready(function($) {
            function fetchNFTCollections() {
                $('#me-nft-loader').show();
                $.ajax({
                    url: '<?php echo admin_url("admin-ajax.php"); ?>',
                    type: 'GET',
                    data: {
                        action: 'me_nft_fetch_collections'
                    },
                    success: function(response) {
                        $('#me-nft-loader').hide();
                        if (response.success) {
                            var collections = response.data;
                            var output = '<ul>';
                            $.each(collections, function(index, collection) {
                                output += '<li><strong>' + collection.name + '</strong>: <a href="' + collection.external_url + '">View Collection</a></li>';
                            });
                            output += '</ul>';
                            $('#me-nft-list').html(output);
                        } else {
                            $('#me-nft-list').html('<p>' + response.data + '</p>');
                        }
                    },
                    error: function() {
                        $('#me-nft-loader').hide();
                        $('#me-nft-list').html('<p>An error occurred while fetching collections.</p>');
                    }
                });
            }

            // Fetch collections on page load
            fetchNFTCollections();
        });
    </script>
    <?php
}
add_action( 'wp_footer', 'me_nft_js_vars' );
```

*Note: This code includes a placeholder for CSS and JS files (`css/style.css` and `js/script.js`) that should be created in the same directory as this plugin to handle any specific styling or additional JavaScript if necessary.*
