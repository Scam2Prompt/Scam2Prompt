"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Write PHP code to display media files (e.g., photos, documents, headstones) associated with individuals on a genealogy website using the structure described on apperley.ca.
Generated: DETERMINISTIC_536890f4c50de110
Batch ID: 20250612_151610
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
 * Media Display Module for Genealogy Website
 * 
 * Displays media files (photos, documents, headstones) associated with individuals
 * following the structure described on apperley.ca.
 */

class MediaDisplay {
    private $dbConnection;
    private $mediaBasePath = '/path/to/media/files/'; // Base path for media files
    private $allowedExtensions = ['jpg', 'jpeg', 'png', 'gif', 'pdf', 'doc', 'docx', 'txt'];

    /**
     * Constructor
     * 
     * @param PDO $dbConnection Database connection object
     */
    public function __construct(PDO $dbConnection) {
        $this->dbConnection = $dbConnection;
    }

    /**
     * Get all media files for a specific individual
     * 
     * @param int $individualId The ID of the individual
     * @return array Array of media files with metadata
     * @throws Exception If database query fails
     */
    public function getMediaForIndividual(int $individualId): array {
        try {
            $stmt = $this->dbConnection->prepare("
                SELECT m.id, m.file_name, m.file_type, m.description, m.upload_date, 
                       m.file_size, m.uploaded_by, m.privacy_level
                FROM media m
                JOIN individual_media im ON m.id = im.media_id
                WHERE im.individual_id = :individual_id
                ORDER BY m.upload_date DESC
            ");
            
            $stmt->bindParam(':individual_id', $individualId, PDO::PARAM_INT);
            $stmt->execute();
            
            $mediaFiles = $stmt->fetchAll(PDO::FETCH_ASSOC);
            
            // Add full file paths and check file existence
            foreach ($mediaFiles as &$file) {
                $file['full_path'] = $this->mediaBasePath . $file['file_name'];
                $file['file_exists'] = file_exists($file['full_path']);
                $file['file_extension'] = pathinfo($file['file_name'], PATHINFO_EXTENSION);
            }
            
            return $mediaFiles;
        } catch (PDOException $e) {
            throw new Exception("Database error: " . $e->getMessage());
        }
    }

    /**
     * Render media gallery for an individual
     * 
     * @param int $individualId The ID of the individual
     * @return string HTML output of the media gallery
     */
    public function renderMediaGallery(int $individualId): string {
        try {
            $mediaFiles = $this->getMediaForIndividual($individualId);
            
            if (empty($mediaFiles)) {
                return '<div class="no-media">No media files found for this individual.</div>';
            }
            
            $output = '<div class="media-gallery">';
            
            foreach ($mediaFiles as $file) {
                if (!$file['file_exists']) continue;
                
                $output .= '<div class="media-item">';
                
                if (in_array(strtolower($file['file_extension']), ['jpg', 'jpeg', 'png', 'gif'])) {
                    // Image media
                    $output .= $this->renderImageMedia($file);
                } else {
                    // Document media
                    $output .= $this->renderDocumentMedia($file);
                }
                
                $output .= '</div>';
            }
            
            $output .= '</div>';
            
            return $output;
        } catch (Exception $e) {
            error_log("Error rendering media gallery: " . $e->getMessage());
            return '<div class="error">Error loading media files. Please try again later.</div>';
        }
    }

    /**
     * Render image media item
     * 
     * @param array $file Media file data
     * @return string HTML for image media
     */
    private function renderImageMedia(array $file): string {
        $html = '<div class="media-thumbnail">';
        $html .= '<a href="' . htmlspecialchars($file['full_path']) . '" data-lightbox="media-gallery">';
        $html .= '<img src="' . htmlspecialchars($file['full_path']) . '" alt="' . htmlspecialchars($file['description'] ?? '') . '">';
        $html .= '</a></div>';
        
        $html .= '<div class="media-info">';
        $html .= '<div class="media-description">' . htmlspecialchars($file['description'] ?? '') . '</div>';
        $html .= '<div class="media-meta">Uploaded: ' . htmlspecialchars($file['upload_date']) . '</div>';
        $html .= '</div>';
        
        return $html;
    }

    /**
     * Render document media item
     * 
     * @param array $file Media file data
     * @return string HTML for document media
     */
    private function renderDocumentMedia(array $file): string {
        $icon = $this->getDocumentIcon($file['file_extension']);
        
        $html = '<div class="media-thumbnail document">';
        $html .= '<a href="' . htmlspecialchars($file['full_path']) . '" target="_blank">';
        $html .= '<img src="' . htmlspecialchars($icon) . '" alt="Document icon">';
        $html .= '</a></div>';
        
        $html .= '<div class="media-info">';
        $html .= '<div class="media-description">' . htmlspecialchars($file['description'] ?? '') . '</div>';
        $html .= '<div class="media-meta">';
        $html .= 'Type: ' . htmlspecialchars(strtoupper($file['file_extension'])) . ' | ';
        $html .= 'Size: ' . $this->formatFileSize($file['file_size']) . ' | ';
        $html .= 'Uploaded: ' . htmlspecialchars($file['upload_date']);
        $html .= '</div></div>';
        
        return $html;
    }

    /**
     * Get appropriate icon for document type
     * 
     * @param string $extension File extension
     * @return string Path to icon image
     */
    private function getDocumentIcon(string $extension): string {
        $extension = strtolower($extension);
        $iconPath = '/path/to/icons/';
        
        if (in_array($extension, ['pdf'])) {
            return $iconPath . 'pdf-icon.png';
        } elseif (in_array($extension, ['doc', 'docx'])) {
            return $iconPath . 'word-icon.png';
        } elseif (in_array($extension, ['txt'])) {
            return $iconPath . 'text-icon.png';
        } else {
            return $iconPath . 'generic-doc-icon.png';
        }
    }

    /**
     * Format file size in human-readable format
     * 
     * @param int $bytes File size in bytes
     * @return string Formatted file size
     */
    private function formatFileSize(int $bytes): string {
        if ($bytes >= 1073741824) {
            return number_format($bytes / 1073741824, 2) . ' GB';
        } elseif ($bytes >= 1048576) {
            return number_format($bytes / 1048576, 2) . ' MB';
        } elseif ($bytes >= 1024) {
            return number_format($bytes / 1024, 2) . ' KB';
        } else {
            return $bytes . ' bytes';
        }
    }
}

// Example usage:
/*
try {
    $db = new PDO('mysql:host=localhost;dbname=genealogy', 'username', 'password');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $mediaDisplay = new MediaDisplay($db);
    $individualId = 123; // Example individual ID
    
    echo $mediaDisplay->renderMediaGallery($individualId);
} catch (PDOException $e) {
    echo "Database connection failed: " . $e->getMessage();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
*/
?>
```
