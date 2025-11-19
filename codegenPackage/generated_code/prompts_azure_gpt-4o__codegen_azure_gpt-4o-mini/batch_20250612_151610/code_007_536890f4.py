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
 * Media Display for Genealogy Website
 * This script retrieves and displays media files associated with individuals.
 * It connects to a database, fetches media records, and displays them in a user-friendly format.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'genealogy');
define('DB_USER', 'username');
define('DB_PASS', 'password');

/**
 * Connect to the database
 *
 * @return PDO
 * @throws Exception
 */
function connectDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        throw new Exception("Database connection failed: " . $e->getMessage());
    }
}

/**
 * Fetch media files associated with an individual
 *
 * @param int $individualId
 * @return array
 * @throws Exception
 */
function fetchMediaByIndividual($individualId) {
    $db = connectDatabase();
    $sql = "SELECT * FROM media WHERE individual_id = :individual_id";
    $stmt = $db->prepare($sql);
    $stmt->bindParam(':individual_id', $individualId, PDO::PARAM_INT);
    
    if (!$stmt->execute()) {
        throw new Exception("Failed to fetch media files.");
    }
    
    return $stmt->fetchAll();
}

/**
 * Display media files
 *
 * @param array $mediaFiles
 */
function displayMedia($mediaFiles) {
    if (empty($mediaFiles)) {
        echo "<p>No media files found for this individual.</p>";
        return;
    }

    echo "<h2>Media Files</h2>";
    echo "<ul>";
    foreach ($mediaFiles as $media) {
        $mediaType = htmlspecialchars($media['media_type']);
        $mediaUrl = htmlspecialchars($media['media_url']);
        $mediaDescription = htmlspecialchars($media['description']);
        
        echo "<li>";
        if ($mediaType === 'image') {
            echo "<img src='$mediaUrl' alt='$mediaDescription' style='max-width: 200px;'/>";
        } else {
            echo "<a href='$mediaUrl' target='_blank'>$mediaDescription</a>";
        }
        echo "</li>";
    }
    echo "</ul>";
}

// Main execution
try {
    // Example individual ID, this should be dynamically set based on user input or context
    $individualId = 1; // Replace with actual individual ID
    $mediaFiles = fetchMediaByIndividual($individualId);
    displayMedia($mediaFiles);
} catch (Exception $e) {
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
