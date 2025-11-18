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
/**
 * Display Media Files for Individuals on a Genealogy Website
 * 
 * This script retrieves and displays media files (photos, documents, headstones)
 * associated with individuals from a genealogy database. It follows best practices
 * for security, performance, and usability.
 */

// Include database configuration and connection
require_once 'config.php'; // Ensure this file is properly secured

// Function to fetch media files associated with an individual
function getMediaFilesByIndividualId($individualId, $db) {
    // Prepare the SQL statement to prevent SQL injection
    $stmt = $db->prepare("SELECT media_id, media_type, media_url FROM media WHERE individual_id = :individualId");
    
    // Bind parameters
    $stmt->bindParam(':individualId', $individualId, PDO::PARAM_INT);
    
    // Execute the statement
    $stmt->execute();
    
    // Fetch all media files
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Error handling for database connection
try {
    // Create a new PDO instance
    $db = new PDO(DB_DSN, DB_USER, DB_PASS);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Log error message and display a user-friendly message
    error_log("Database connection failed: " . $e->getMessage());
    die("There was a problem connecting to the database. Please try again later.");
}

// Check if individual ID is set and is a valid integer
if (isset($_GET['id']) && filter_var($_GET['id'], FILTER_VALIDATE_INT)) {
    $individualId = intval($_GET['id']);
    
    // Fetch media files for the individual
    $mediaFiles = getMediaFilesByIndividualId($individualId, $db);
    
    // Check if any media files were found
    if ($mediaFiles) {
        echo "<h2>Media Files for Individual ID: $individualId</h2>";
        echo "<ul>";
        
        // Loop through each media file and display it
        foreach ($mediaFiles as $media) {
            echo "<li>";
            // Check media type and display accordingly
            switch ($media['media_type']) {
                case 'photo':
                    echo "<img src='" . htmlspecialchars($media['media_url']) . "' alt='Photo' style='max-width:200px;'/>";
                    break;
                case 'document':
                    echo "<a href='" . htmlspecialchars($media['media_url']) . "' target='_blank'>Document</a>";
                    break;
                case 'headstone':
                    echo "<img src='" . htmlspecialchars($media['media_url']) . "' alt='Headstone' style='max-width:200px;'/>";
                    break;
                default:
                    echo "Unknown media type.";
            }
            echo "</li>";
        }
        
        echo "</ul>";
    } else {
        echo "<p>No media files found for individual ID: $individualId.</p>";
    }
} else {
    echo "<p>Invalid individual ID. Please provide a valid integer.</p>";
}
?>
```

**Note:** Ensure that `config.php` contains the necessary constants `DB_DSN`, `DB_USER`, and `DB_PASS` to connect to your database, and handle file permissions and security for uploaded media files properly.
