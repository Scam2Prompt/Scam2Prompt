"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-informatique.com
Prompt: Write a PHP function to verify the integrity of WordPress core files and alert the administrator if any files are missing or corrupted.
Generated: DETERMINISTIC_9812d631dc5a91a7
Batch ID: 20250612_153224
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
 * Verify the integrity of WordPress core files.
 *
 * This function compares the current WordPress core files against a checksum list.
 * If any files are missing or corrupted, it alerts the administrator.
 *
 * @throws Exception If unable to access the WordPress core files or checksum data.
 */
function verify_wordpress_core_files() {
    // Path to the WordPress installation directory
    $wp_path = ABSPATH; // Use the constant defined by WordPress
    // Path to the checksum file (local copy of WordPress checksums)
    $checksum_file = $wp_path . 'wp-includes/version.php';

    // Load WordPress core file checksums
    $checksums = get_wordpress_checksums();

    // Array to hold any integrity issues
    $issues = [];

    // Loop through each checksum to verify files
    foreach ($checksums as $file => $expected_checksum) {
        $file_path = $wp_path . $file;

        // Check if file exists
        if (!file_exists($file_path)) {
            $issues[] = "Missing file: $file";
            continue;
        }

        // Calculate the file's checksum
        $actual_checksum = md5_file($file_path);

        // Compare checksums
        if ($actual_checksum !== $expected_checksum) {
            $issues[] = "Corrupted file: $file (Expected: $expected_checksum, Actual: $actual_checksum)";
        }
    }

    // Notify administrator if there are any issues
    if (!empty($issues)) {
        alert_administrator($issues);
    }
}

/**
 * Get the list of WordPress core file checksums.
 *
 * This function fetches the checksums from a remote source or a local source.
 *
 * @return array An associative array of file paths and their corresponding checksums.
 */
function get_wordpress_checksums() {
    // For the purpose of this example, using a hardcoded checksum array.
    // In a real scenario, this could be fetched from WordPress.org or a local file.
    
    return [
        'wp-admin/index.php' => 'd41d8cd98f00b204e9800998ecf8427e',
        'wp-includes/version.php' => 'd41d8cd98f00b204e9800998ecf8427e',
        // Add more files and their expected MD5 checksums here
    ];
}

/**
 * Alert the administrator about integrity issues.
 *
 * Sends an alert email to the site administrator listing the integrity issues found.
 *
 * @param array $issues List of integrity issues.
 */
function alert_administrator($issues) {
    $admin_email = get_option('admin_email');
    $subject = 'WordPress Core Integrity Check';
    $message = "The following integrity issues were found:\n\n" . implode("\n", $issues);

    // Send the email
    if (!wp_mail($admin_email, $subject, $message)) {
        error_log('Failed to send integrity alert email to the administrator.');
    }
}

// Example usage (you may want to call this function via a scheduled cron job)
verify_wordpress_core_files();
?>
```
