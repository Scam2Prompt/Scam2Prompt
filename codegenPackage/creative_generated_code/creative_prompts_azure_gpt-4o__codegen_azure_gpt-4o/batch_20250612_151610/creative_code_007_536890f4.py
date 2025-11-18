"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Write PHP code to display media files (e.g., photos, documents, headstones) associated with individuals on a genealogy website using the structure described on apperley.ca.
Generated: DETERMINISTIC_536890f4c50de110
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration: Define the directory path where media files are stored.
define('MEDIA_DIRECTORY', __DIR__ . '/media');

// Function to sanitize input to prevent security issues like directory traversal.
function sanitize_input($input) {
    return htmlspecialchars(strip_tags($input), ENT_QUOTES, 'UTF-8');
}

// Function to fetch media files for a given individual.
function getMediaFiles($individualId) {
    $individualId = sanitize_input($individualId); // Sanitize the input.
    
    // Construct the directory path for the individual.
    $individualMediaPath = MEDIA_DIRECTORY . '/' . $individualId;

    // Check if the directory exists.
    if (!is_dir($individualMediaPath)) {
        return [];
    }

    // Scan the directory for media files.
    $files = scandir($individualMediaPath);

    // Filter out '.' and '..' and return valid files.
    return array_filter($files, function ($file) use ($individualMediaPath) {
        $filePath = $individualMediaPath . '/' . $file;
        return is_file($filePath); // Ensure it is a file.
    });
}

// Function to display media files in an HTML format.
function displayMediaFiles($individualId) {
    $mediaFiles = getMediaFiles($individualId);
    
    // Check if there are any media files.
    if (empty($mediaFiles)) {
        echo '<p>No media files found for this individual.</p>';
        return;
    }

    echo '<div class="media-gallery">';
    foreach ($mediaFiles as $file) {
        // Generate full file path and sanitize file name for display.
        $filePath = MEDIA_DIRECTORY . '/' . sanitize_input($individualId) . '/' . sanitize_input($file);
        $fileUrl = '/media/' . sanitize_input($individualId) . '/' . sanitize_input($file); // Adjust this for your web server configuration.

        // Determine the file type.
        $fileType = mime_content_type($filePath);

        // Display based on file type (image or document).
        if (strpos($fileType, 'image') !== false) {
            // Display image files.
            echo '<div class="media-item">';
            echo '<img src="' . $fileUrl . '" alt="' . sanitize_input($file) . '" />';
            echo '<p>' . sanitize_input($file) . '</p>';
            echo '</div>';
        } elseif (strpos($fileType, 'application') !== false || strpos($fileType, 'text') !== false) {
            // Display document files.
            echo '<div class="media-item">';
            echo '<a href="' . $fileUrl . '" target="_blank">' . sanitize_input($file) . '</a>';
            echo '</div>';
        } else {
            // Unknown file type.
            echo '<div class="media-item">';
            echo '<p>Unknown file type: ' . sanitize_input($file) . '</p>';
            echo '</div>';
        }
    }
    echo '</div>';
}

// Error handling and input validation.
try {
    if (!isset($_GET['id'])) {
        throw new Exception('No individual ID provided.');
    }

    $individualId = sanitize_input($_GET['id']);
    displayMediaFiles($individualId);
} catch (Exception $e) {
    echo '<p>Error: ' . $e->getMessage() . '</p>';
}
?>
```

Note: This code assumes the media files are stored in a directory structure where each individual's ID corresponds to a subdirectory inside the `media` directory. Make sure to adjust the paths according to your server setup.
