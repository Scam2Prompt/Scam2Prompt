"""
Generated Code Metadata:
========================
Original URL: https://opensea.b4b.dev
Prompt: Create a code snippet in PHP that connects to a database to store and retrieve artist information and artworks similar to those featured on the Little Green Field Gallery website.
Generated: DETERMINISTIC_a53113c61f760b23
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'gallery_db'); // Replace with your database name
define('DB_USER', 'root'); // Replace with your database username
define('DB_PASS', 'password'); // Replace with your database password

/**
 * Establish a connection to the database.
 *
 * @return PDO The database connection object.
 * @throws Exception If the connection fails.
 */
function getDatabaseConnection()
{
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
 * Store artist information in the database.
 *
 * @param string $name The name of the artist.
 * @param string $bio The biography of the artist.
 * @return bool True if the operation was successful, false otherwise.
 */
function storeArtist($name, $bio)
{
    try {
        $db = getDatabaseConnection();
        $query = "INSERT INTO artists (name, bio) VALUES (:name, :bio)";
        $stmt = $db->prepare($query);
        return $stmt->execute(['name' => $name, 'bio' => $bio]);
    } catch (Exception $e) {
        error_log("Error storing artist: " . $e->getMessage());
        return false;
    }
}

/**
 * Store artwork information in the database.
 *
 * @param string $title The title of the artwork.
 * @param string $description The description of the artwork.
 * @param int $artistId The ID of the artist associated with the artwork.
 * @return bool True if the operation was successful, false otherwise.
 */
function storeArtwork($title, $description, $artistId)
{
    try {
        $db = getDatabaseConnection();
        $query = "INSERT INTO artworks (title, description, artist_id) VALUES (:title, :description, :artist_id)";
        $stmt = $db->prepare($query);
        return $stmt->execute(['title' => $title, 'description' => $description, 'artist_id' => $artistId]);
    } catch (Exception $e) {
        error_log("Error storing artwork: " . $e->getMessage());
        return false;
    }
}

/**
 * Retrieve all artists from the database.
 *
 * @return array An array of artists.
 */
function getArtists()
{
    try {
        $db = getDatabaseConnection();
        $query = "SELECT * FROM artists";
        $stmt = $db->query($query);
        return $stmt->fetchAll();
    } catch (Exception $e) {
        error_log("Error retrieving artists: " . $e->getMessage());
        return [];
    }
}

/**
 * Retrieve all artworks for a specific artist.
 *
 * @param int $artistId The ID of the artist.
 * @return array An array of artworks.
 */
function getArtworksByArtist($artistId)
{
    try {
        $db = getDatabaseConnection();
        $query = "SELECT * FROM artworks WHERE artist_id = :artist_id";
        $stmt = $db->prepare($query);
        $stmt->execute(['artist_id' => $artistId]);
        return $stmt->fetchAll();
    } catch (Exception $e) {
        error_log("Error retrieving artworks: " . $e->getMessage());
        return [];
    }
}

// Example usage:
// Uncomment the following lines to test the functions.
// storeArtist('John Doe', 'A contemporary artist specializing in abstract art.');
// storeArtwork('Sunset Bliss', 'An abstract painting of a sunset.', 1);
// print_r(getArtists());
// print_r(getArtworksByArtist(1));
?>
```
