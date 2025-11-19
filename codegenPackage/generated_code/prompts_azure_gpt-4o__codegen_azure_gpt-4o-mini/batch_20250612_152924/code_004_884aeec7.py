"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Write code in PHP to integrate video production features into an event management platform, aligning with Pozy Media's specialization in video production and troubleshooting onsite challenges.
Generated: DETERMINISTIC_884aeec7cd6f4c02
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * VideoProduction class handles video production features for the event management platform.
 */
class VideoProduction
{
    private $videoDirectory;

    /**
     * Constructor to initialize video directory.
     *
     * @param string $videoDirectory Path to the directory where videos are stored.
     */
    public function __construct($videoDirectory)
    {
        if (!is_dir($videoDirectory)) {
            throw new InvalidArgumentException("Invalid video directory provided.");
        }
        $this->videoDirectory = rtrim($videoDirectory, '/') . '/';
    }

    /**
     * Uploads a video file to the server.
     *
     * @param array $file The uploaded file information from $_FILES.
     * @return string The path to the uploaded video file.
     * @throws Exception If the upload fails.
     */
    public function uploadVideo($file)
    {
        // Check for upload errors
        if ($file['error'] !== UPLOAD_ERR_OK) {
            throw new RuntimeException("File upload error: " . $file['error']);
        }

        // Validate file type
        $allowedTypes = ['video/mp4', 'video/avi', 'video/mov'];
        if (!in_array($file['type'], $allowedTypes)) {
            throw new InvalidArgumentException("Invalid file type. Only MP4, AVI, and MOV are allowed.");
        }

        // Generate a unique filename
        $filename = uniqid('video_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
        $destination = $this->videoDirectory . $filename;

        // Move the uploaded file to the designated directory
        if (!move_uploaded_file($file['tmp_name'], $destination)) {
            throw new RuntimeException("Failed to move uploaded file.");
        }

        return $destination;
    }

    /**
     * Retrieves a list of all uploaded videos.
     *
     * @return array List of video file paths.
     */
    public function listVideos()
    {
        $videos = glob($this->videoDirectory . '*.{mp4,avi,mov}', GLOB_BRACE);
        return array_map('basename', $videos);
    }

    /**
     * Deletes a video file from the server.
     *
     * @param string $filename The name of the video file to delete.
     * @return bool True on success, false on failure.
     * @throws Exception If the file does not exist.
     */
    public function deleteVideo($filename)
    {
        $filePath = $this->videoDirectory . $filename;

        if (!file_exists($filePath)) {
            throw new InvalidArgumentException("File does not exist: " . $filename);
        }

        return unlink($filePath);
    }
}

// Example usage
try {
    $videoProduction = new VideoProduction('/path/to/video/directory');

    // Upload a video
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['video'])) {
        $uploadedFilePath = $videoProduction->uploadVideo($_FILES['video']);
        echo "Video uploaded successfully: " . $uploadedFilePath;
    }

    // List videos
    $videos = $videoProduction->listVideos();
    echo "Uploaded videos: " . implode(', ', $videos);

    // Delete a video (example)
    // $videoProduction->deleteVideo('video_example.mp4');

} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
