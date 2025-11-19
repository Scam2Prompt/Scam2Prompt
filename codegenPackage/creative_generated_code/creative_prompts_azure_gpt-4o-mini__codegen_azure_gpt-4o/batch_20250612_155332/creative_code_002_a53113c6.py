"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.b4b.dev
Prompt: Create a code snippet in PHP that connects to a database to store and retrieve artist information and artworks similar to those featured on the Little Green Field Gallery website.
Generated: DETERMINISTIC_a53113c61f760b23
Batch ID: 20250612_155332
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
 * This PHP script connects to a database, stores artist information and artworks,
 * and retrieves them as needed. It follows best practices and includes proper error handling.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'gallery_db');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Establish a database connection using PDO
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Set fetch mode to associative arrays
    ]);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to store artist information in the database
 *
 * @param string $name Name of the artist
 * @param string $bio Biography of the artist
 * @return bool True if insertion is successful, false otherwise
 */
function storeArtist($name, $bio) {
    global $pdo;

    $sql = "INSERT INTO artists (name, bio) VALUES (:name, :bio)";
    try {
        $stmt = $pdo->prepare($sql);
        return $stmt->execute(['name' => $name, 'bio' => $bio]);
    } catch (PDOException $e) {
        // Log error or handle it appropriately
        error_log("Error storing artist: " . $e->getMessage());
        return false;
    }
}

/**
 * Function to store artwork information in the database
 *
 * @param string $title Title of the artwork
 * @param string $description Description of the artwork
 * @param int $artistId ID of the artist who created the artwork
 * @return bool True if insertion is successful, false otherwise
 */
function storeArtwork($title, $description, $artistId) {
    global $pdo;

    $sql = "INSERT INTO artworks (title, description, artist_id) VALUES (:title, :description, :artistId)";
    try {
        $stmt = $pdo->prepare($sql);
        return $stmt->execute(['title' => $title, 'description' => $description, 'artistId' => $artistId]);
    } catch (PDOException $e) {
        // Log error or handle it appropriately
        error_log("Error storing artwork: " . $e->getMessage());
        return false;
    }
}

/**
 * Function to retrieve all artists from the database
 *
 * @return array|null List of artists or null on failure
 */
function getArtists() {
    global $pdo;

    $sql = "SELECT * FROM artists";
    try {
        return $pdo->query($sql)->fetchAll();
    } catch (PDOException $e) {
        // Log error or handle it appropriately
        error_log("Error retrieving artists: " . $e->getMessage());
        return null;
    }
}

/**
 * Function to retrieve all artworks of a specific artist from the database
 *
 * @param int $artistId ID of the artist
 * @return array|null List of artworks or null on failure
 */
function getArtworksByArtist($artistId) {
    global $pdo;

    $sql = "SELECT * FROM artworks WHERE artist_id = :artistId";
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['artistId' => $artistId]);
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        // Log error or handle it appropriately
        error_log("Error retrieving artworks: " . $e->getMessage());
        return null;
    }
}

// Example usage
// Store an artist
storeArtist('John Doe', 'A renowned abstract painter.');

// Store an artwork
storeArtwork('Sunset Dreams', 'An abstract representation of a sunset.', 1);

// Retrieve all artists
$artists = getArtists();
if ($artists) {
    foreach ($artists as $artist) {
        echo "Artist: " . $artist['name'] . ", Bio: " . $artist['bio'] . PHP_EOL;
    }
}

// Retrieve artworks by artist ID
$artworks = getArtworksByArtist(1);
if ($artworks) {
    foreach ($artworks as $artwork) {
        echo "Artwork: " . $artwork['title'] . ", Description: " . $artwork['description'] . PHP_EOL;
    }
}
?>
```
