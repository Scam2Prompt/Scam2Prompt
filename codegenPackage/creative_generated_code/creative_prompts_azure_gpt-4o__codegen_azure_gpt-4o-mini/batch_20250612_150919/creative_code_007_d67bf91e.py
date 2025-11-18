"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.tech
Prompt: Generate a PHP script to check if the `index.html` file exists in the root directory and replace it with a custom file.
Generated: DETERMINISTIC_d67bf91eba3414e6
Batch ID: 20250612_150919
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
 * PHP script to check if 'index.html' exists in the root directory
 * and replace it with a custom file if it does.
 */

// Define the paths for the original and custom files
$originalFile = 'index.html';
$customFile = 'custom_index.html';

// Function to check if a file exists and replace it
function replaceIndexFile($originalFile, $customFile) {
    // Check if the original file exists
    if (file_exists($originalFile)) {
        // Attempt to replace the original file
        try {
            // Check if the custom file exists before proceeding
            if (!file_exists($customFile)) {
                throw new Exception("Custom file '$customFile' does not exist.");
            }

            // Replace the original file with the custom file
            if (copy($customFile, $originalFile)) {
                echo "Successfully replaced '$originalFile' with '$customFile'.";
            } else {
                throw new Exception("Failed to replace '$originalFile'.");
            }
        } catch (Exception $e) {
            // Handle exceptions and output error messages
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "'$originalFile' does not exist. No replacement needed.";
    }
}

// Call the function to perform the check and replacement
replaceIndexFile($originalFile, $customFile);
?>
```
