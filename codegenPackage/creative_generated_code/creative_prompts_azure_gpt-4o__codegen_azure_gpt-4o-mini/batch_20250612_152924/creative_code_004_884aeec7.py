"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Write code in PHP to integrate video production features into an event management platform, aligning with Pozy Media's specialization in video production and troubleshooting onsite challenges.
Generated: DETERMINISTIC_884aeec7cd6f4c02
Batch ID: 20250612_152924
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
 * Video Production Integration for Event Management Platform
 * This class provides methods to manage video production features
 * aligned with Pozy Media's specialization in video production.
 */

class VideoProductionIntegration
{
    private $videoDirectory;

    /**
     * Constructor to initialize video production settings.
     *
     * @param string $videoDirectory Directory where videos will be stored.
     */
    public function __construct($videoDirectory)
    {
        // Validate the directory path
        if (!is_dir($videoDirectory) || !is_writable($videoDirectory)) {
            throw new InvalidArgumentException("Invalid video directory: $videoDirectory");
        }
        $this->videoDirectory = rtrim($videoDirectory, '/');
    }

    /**
     * Uploads a video file to the server.
     *
     * @param array $file Video file information from the form submission.
     * @return string The path of the uploaded video file.
     * @throws RuntimeException If the upload fails.
     */
    public function uploadVideo(array $file)
    {
        // Check for upload errors
        if ($file['error'] !== UPLOAD_ERR_OK) {
            throw new RuntimeException("File upload error: " . $file['error']);
        }

        // Validate file type
        $allowedTypes = ['video/mp4', 'video/x-ms-wmv', 'video/x-flv'];
        if (!in_array($file['type'], $allowedTypes)) {
            throw new InvalidArgumentException("Unsupported video type: " . $file['type']);
        }

        // Generate a unique file name
        $fileName = uniqid('video_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
        $destination = $this->videoDirectory . '/' . $fileName;

        // Move the uploaded file to the specified directory
        if (!move_uploaded_file($file['tmp_name'], $destination)) {
            throw new RuntimeException("Failed to move uploaded file to $destination");
        }

        return $destination; // Return the path of the uploaded video
    }

    /**
     * Retrieves a list of all uploaded videos.
     *
     * @return array List of uploaded video file paths.
     */
    public function getUploadedVideos()
    {
        $videos = [];
        $files = scandir($this->videoDirectory);
        foreach ($files as $file) {
            if ($file !== '.' && $file !== '..') {
                $videos[] = $this->videoDirectory . '/' . $file;
            }
        }
        return $videos; // Return the list of video files
    }

    /**
     * Deletes a video file from the server.
     *
     * @param string $videoPath The path of the video to delete.
     * @throws RuntimeException If the deletion fails.
     */
    public function deleteVideo($videoPath)
    {
        // Check if the file exists before attempting to delete
        if (!file_exists($videoPath)) {
            throw new InvalidArgumentException("Video file does not exist: $videoPath");
        }

        // Attempt to delete the video file
        if (!unlink($videoPath)) {
            throw new RuntimeException("Failed to delete video file: $videoPath");
        }
    }
}

// Example usage:
// try {
//     $videoManager = new VideoProductionIntegration('/path/to/video/directory');
//     $uploadedVideoPath = $videoManager->uploadVideo($_FILES['video_file']);
//     echo "Video uploaded successfully: " . $uploadedVideoPath;
// } catch (Exception $e) {
//     echo "Error: " . $e->getMessage();
// }
```
