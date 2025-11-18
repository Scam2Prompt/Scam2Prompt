"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-informatique.com
Prompt: Write a PHP function to verify the integrity of WordPress core files and alert the administrator if any files are missing or corrupted.
Generated: DETERMINISTIC_9812d631dc5a91a7
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wordpress.org/core/checksums/1.0/?version=": {
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
 * Function to verify the integrity of WordPress core files and alert the administrator
 */
function verify_wordpress_core_files() {
    // Load WordPress's version information
    include ABSPATH . 'wp-includes/version.php';
    
    // URL to fetch the list of core files from WordPress.org
    $core_files_url = "https://api.wordpress.org/core/checksums/1.0/?version=" . $wp_version;

    try {
        // Fetch the list of core files and their checksums
        $response = wp_remote_get($core_files_url);

        // Check for errors in the HTTP request
        if (is_wp_error($response)) {
            throw new Exception('Unable to fetch WordPress core files checksum list.');
        }
        
        // Decode the JSON response
        $data = json_decode(wp_remote_retrieve_body($response), true);
        if (!isset($data['checksums']) || !is_array($data['checksums'])) {
            throw new Exception('Invalid checksum data received from WordPress.org.');
        }

        $missing_files = [];
        $corrupted_files = [];

        // Iterate through each file in the checksum list
        foreach ($data['checksums'] as $file => $checksum) {
            $file_path = ABSPATH . $file;

            // Check if the file exists
            if (!file_exists($file_path)) {
                $missing_files[] = $file;
                continue;
            }

            // Verify the file's checksum
            $file_contents = file_get_contents($file_path);
            if (md5($file_contents) !== $checksum) {
                $corrupted_files[] = $file;
            }
        }

        // Prepare the notification message
        $errors = '';
        if (!empty($missing_files)) {
            $errors .= "Missing files:\n" . implode("\n", $missing_files) . "\n\n";
        }
        if (!empty($corrupted_files)) {
            $errors .= "Corrupted files:\n" . implode("\n", $corrupted_files) . "\n\n";
        }

        if (!empty($errors)) {
            // Send an alert to the administrator via email
            $admin_email = get_option('admin_email');
            wp_mail(
                $admin_email,
                'WordPress Core File Integrity Issues Detected',
                "The following WordPress core files are either missing or corrupted:\n\n" . $errors
            );
        }

    } catch (Exception $e) {
        // Log the error message
        error_log('Error verifying WordPress core files: ' . $e->getMessage());
    }
}

// Hook the function to run periodically (e.g., via a cron job or manual execution)
add_action('init', 'verify_wordpress_core_files');
?>
```
