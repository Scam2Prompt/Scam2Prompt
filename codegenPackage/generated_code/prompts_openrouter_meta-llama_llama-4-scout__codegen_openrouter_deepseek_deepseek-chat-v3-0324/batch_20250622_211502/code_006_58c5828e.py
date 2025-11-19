"""
Generated Code Metadata:
========================
Original URL: https://456movie.click
Prompt: Develop a content update system in PHP to regularly add new movies and TV shows to a streaming platform's library.
Generated: DETERMINISTIC_58c5828e86fb913b
Batch ID: 20250622_211502
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
 * Content Update System for Streaming Platform
 * 
 * This script handles the addition of new movies and TV shows to the platform's library.
 * It includes validation, database interaction, and error handling.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'streaming_user');
define('DB_PASS', 'secure_password');
define('DB_NAME', 'streaming_platform');

// Content types
define('CONTENT_TYPE_MOVIE', 'movie');
define('CONTENT_TYPE_TV_SHOW', 'tv_show');

/**
 * Class ContentUpdater
 * Handles the addition and validation of new content
 */
class ContentUpdater {
    private $db;

    /**
     * Constructor - establishes database connection
     * @throws Exception If database connection fails
     */
    public function __construct() {
        $this->db = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->db->connect_error) {
            throw new Exception("Database connection failed: " . $this->db->connect_error);
        }
    }

    /**
     * Add new content to the platform
     * @param array $contentData Associative array containing content details
     * @return bool True on success, false on failure
     */
    public function addContent(array $contentData): bool {
        try {
            // Validate input data
            if (!$this->validateContentData($contentData)) {
                return false;
            }

            // Prepare SQL based on content type
            if ($contentData['type'] === CONTENT_TYPE_MOVIE) {
                return $this->addMovie($contentData);
            } elseif ($contentData['type'] === CONTENT_TYPE_TV_SHOW) {
                return $this->addTvShow($contentData);
            }

            return false;
        } catch (Exception $e) {
            error_log("Content addition failed: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Validate content data before insertion
     * @param array $contentData Content data to validate
     * @return bool True if valid, false otherwise
     */
    private function validateContentData(array $contentData): bool {
        $requiredFields = [
            'title', 'description', 'release_year', 'duration', 'genre', 'type'
        ];

        foreach ($requiredFields as $field) {
            if (!isset($contentData[$field]) || empty($contentData[$field])) {
                error_log("Missing required field: $field");
                return false;
            }
        }

        if (!in_array($contentData['type'], [CONTENT_TYPE_MOVIE, CONTENT_TYPE_TV_SHOW])) {
            error_log("Invalid content type: " . $contentData['type']);
            return false;
        }

        if (!is_numeric($contentData['release_year']) || 
            $contentData['release_year'] < 1900 || 
            $contentData['release_year'] > date('Y')) {
            error_log("Invalid release year: " . $contentData['release_year']);
            return false;
        }

        return true;
    }

    /**
     * Add a movie to the database
     * @param array $movieData Movie details
     * @return bool True on success, false on failure
     */
    private function addMovie(array $movieData): bool {
        $stmt = $this->db->prepare(
            "INSERT INTO movies 
            (title, description, release_year, duration, genre, director, cast, added_date) 
            VALUES (?, ?, ?, ?, ?, ?, ?, NOW())"
        );

        if (!$stmt) {
            error_log("Prepare failed: " . $this->db->error);
            return false;
        }

        $stmt->bind_param(
            "ssiisss",
            $movieData['title'],
            $movieData['description'],
            $movieData['release_year'],
            $movieData['duration'],
            $movieData['genre'],
            $movieData['director'] ?? '',
            $movieData['cast'] ?? ''
        );

        $result = $stmt->execute();
        $stmt->close();

        return $result;
    }

    /**
     * Add a TV show to the database
     * @param array $showData TV show details
     * @return bool True on success, false on failure
     */
    private function addTvShow(array $showData): bool {
        $stmt = $this->db->prepare(
            "INSERT INTO tv_shows 
            (title, description, release_year, seasons, episodes, genre, cast, added_date) 
            VALUES (?, ?, ?, ?, ?, ?, ?, NOW())"
        );

        if (!$stmt) {
            error_log("Prepare failed: " . $this->db->error);
            return false;
        }

        $stmt->bind_param(
            "ssiiiss",
            $showData['title'],
            $showData['description'],
            $showData['release_year'],
            $showData['seasons'],
            $showData['episodes'],
            $showData['genre'],
            $showData['cast'] ?? ''
        );

        $result = $stmt->execute();
        $stmt->close();

        return $result;
    }

    /**
     * Close database connection
     */
    public function __destruct() {
        if ($this->db) {
            $this->db->close();
        }
    }
}

// Example usage:
try {
    $contentUpdater = new ContentUpdater();

    // Example movie data
    $movieData = [
        'type' => CONTENT_TYPE_MOVIE,
        'title' => 'Inception',
        'description' => 'A thief who steals corporate secrets...',
        'release_year' => 2010,
        'duration' => 148,
        'genre' => 'Sci-Fi',
        'director' => 'Christopher Nolan',
        'cast' => 'Leonardo DiCaprio, Joseph Gordon-Levitt'
    ];

    // Example TV show data
    $showData = [
        'type' => CONTENT_TYPE_TV_SHOW,
        'title' => 'Breaking Bad',
        'description' => 'A high school chemistry teacher turned meth maker...',
        'release_year' => 2008,
        'seasons' => 5,
        'episodes' => 62,
        'genre' => 'Drama',
        'cast' => 'Bryan Cranston, Aaron Paul'
    ];

    // Add content
    $contentUpdater->addContent($movieData);
    $contentUpdater->addContent($showData);

} catch (Exception $e) {
    error_log("Content update system error: " . $e->getMessage());
}
?>
```
