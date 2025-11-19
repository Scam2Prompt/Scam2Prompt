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
 * Media File Display Class for Genealogy Website
 */

// Configuration
require_once 'config.php';

/**
 * Media File Class
 */
class MediaFile
{
    private $id;
    private $type;
    private $fileName;
    private $filePath;
    private $description;
    private $individualId;

    /**
     * Constructor
     *
     * @param int    $id           Media file ID
     * @param string $type         Media file type (e.g., photo, document, headstone)
     * @param string $fileName     Media file name
     * @param string $filePath     Media file path
     * @param string $description  Media file description
     * @param int    $individualId Individual ID associated with media file
     */
    public function __construct($id, $type, $fileName, $filePath, $description, $individualId)
    {
        $this->id = $id;
        $this->type = $type;
        $this->fileName = $fileName;
        $this->filePath = $filePath;
        $this->description = $description;
        $this->individualId = $individualId;
    }

    /**
     * Get Media File ID
     *
     * @return int
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Get Media File Type
     *
     * @return string
     */
    public function getType()
    {
        return $this->type;
    }

    /**
     * Get Media File Name
     *
     * @return string
     */
    public function getFileName()
    {
        return $this->fileName;
    }

    /**
     * Get Media File Path
     *
     * @return string
     */
    public function getFilePath()
    {
        return $this->filePath;
    }

    /**
     * Get Media File Description
     *
     * @return string
     */
    public function getDescription()
    {
        return $this->description;
    }

    /**
     * Get Individual ID
     *
     * @return int
     */
    public function getIndividualId()
    {
        return $this->individualId;
    }
}

/**
 * Media File Display Class
 */
class MediaFileDisplay
{
    private $db;

    /**
     * Constructor
     *
     * @param PDO $db Database connection
     */
    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    /**
     * Get Media Files for Individual
     *
     * @param int $individualId Individual ID
     *
     * @return array
     */
    public function getMediaFilesForIndividual($individualId)
    {
        try {
            $stmt = $this->db->prepare("SELECT * FROM media_files WHERE individual_id = :individual_id");
            $stmt->bindParam(":individual_id", $individualId);
            $stmt->execute();

            $mediaFiles = [];
            while ($row = $stmt->fetch()) {
                $mediaFiles[] = new MediaFile(
                    $row["id"],
                    $row["type"],
                    $row["file_name"],
                    $row["file_path"],
                    $row["description"],
                    $row["individual_id"]
                );
            }

            return $mediaFiles;
        } catch (PDOException $e) {
            error_log("Error retrieving media files: " . $e->getMessage());
            return [];
        }
    }

    /**
     * Display Media Files
     *
     * @param int $individualId Individual ID
     */
    public function displayMediaFiles($individualId)
    {
        $mediaFiles = $this->getMediaFilesForIndividual($individualId);

        if (!empty($mediaFiles)) {
            foreach ($mediaFiles as $mediaFile) {
                echo "<div class='media-file'>";
                echo "<h2>" . $mediaFile->getFileName() . "</h2>";
                echo "<p>Type: " . $mediaFile->getType() . "</p>";
                echo "<p>Description: " . $mediaFile->getDescription() . "</p>";

                switch ($mediaFile->getType()) {
                    case "photo":
                        echo "<img src='" . $mediaFile->getFilePath() . "' alt='" . $mediaFile->getFileName() . "'>";
                        break;
                    case "document":
                        echo "<a href='" . $mediaFile->getFilePath() . "'>View Document</a>";
                        break;
                    case "headstone":
                        echo "<img src='" . $mediaFile->getFilePath() . "' alt='" . $mediaFile->getFileName() . "'>";
                        break;
                    default:
                        echo "<p>Unsupported media file type</p>";
                }

                echo "</div>";
            }
        } else {
            echo "<p>No media files found for this individual.</p>";
        }
    }
}

// Example usage
require_once 'database.php';

$db = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);

$mediaFileDisplay = new MediaFileDisplay($db);
$mediaFileDisplay->displayMediaFiles(123); // Replace with individual ID

```

```sql
CREATE TABLE media_files (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(50) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    description TEXT,
    individual_id INT NOT NULL,
    FOREIGN KEY (individual_id) REFERENCES individuals(id)
);
```
