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
// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'gallery');     // Database name
define('DB_USER', 'root');        // Database username
define('DB_PASS', 'password');    // Database password

/**
 * Connects to the database using PDO.
 *
 * @return PDO|null Returns a PDO object on success, or null on failure.
 */
function connectToDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8";
        $pdo = new PDO($dsn, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Log the exception message
        error_log("Database connection failed: " . $e->getMessage());
        return null;
    }
}

/**
 * Inserts artist information into the database.
 *
 * @param PDO $pdo The PDO instance.
 * @param string $name The name of the artist.
 * @param string $bio The biography of the artist.
 * @return bool Returns true on success, false on failure.
 */
function insertArtist($pdo, $name, $bio) {
    $sql = "INSERT INTO artists (name, bio) VALUES (:name, :bio)";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([':name' => $name, ':bio' => $bio]);
        return true;
    } catch (PDOException $e) {
        // Log the exception message
        error_log("Failed to insert artist: " . $e->getMessage());
        return false;
    }
}

/**
 * Retrieves all artists from the database.
 *
 * @param PDO $pdo The PDO instance.
 * @return array Returns an array of artists.
 */
function getAllArtists($pdo) {
    $sql = "SELECT * FROM artists";
    
    try {
        $stmt = $pdo->query($sql);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Log the exception message
        error_log("Failed to retrieve artists: " . $e->getMessage());
        return [];
    }
}

/**
 * Inserts artwork information into the database.
 *
 * @param PDO $pdo The PDO instance.
 * @param string $title The title of the artwork.
 * @param int $artist_id The ID of the artist.
 * @param string $description The description of the artwork.
 * @return bool Returns true on success, false on failure.
 */
function insertArtwork($pdo, $title, $artist_id, $description) {
    $sql = "INSERT INTO artworks (title, artist_id, description) VALUES (:title, :artist_id, :description)";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([':title' => $title, ':artist_id' => $artist_id, ':description' => $description]);
        return true;
    } catch (PDOException $e) {
        // Log the exception message
        error_log("Failed to insert artwork: " . $e->getMessage());
        return false;
    }
}

/**
 * Retrieves all artworks from the database.
 *
 * @param PDO $pdo The PDO instance.
 * @return array Returns an array of artworks.
 */
function getAllArtworks($pdo) {
    $sql = "SELECT artworks.*, artists.name AS artist_name FROM artworks JOIN artists ON artworks.artist_id = artists.id";
    
    try {
        $stmt = $pdo->query($sql);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Log the exception message
        error_log("Failed to retrieve artworks: " . $e->getMessage());
        return [];
    }
}

// Example usage
$pdo = connectToDatabase();

if ($pdo) {
    // Insert an artist
    insertArtist($pdo, 'John Doe', 'A contemporary artist from New York.');

    // Retrieve and display all artists
    $artists = getAllArtists($pdo);
    foreach ($artists as $artist) {
        echo "Artist: " . $artist['name'] . " - Bio: " . $artist['bio'] . "\n";
    }

    // Insert an artwork
    insertArtwork($pdo, 'Sunset Dreams', 1, 'A beautiful depiction of a sunset.');

    // Retrieve and display all artworks
    $artworks = getAllArtworks($pdo);
    foreach ($artworks as $artwork) {
        echo "Artwork: " . $artwork['title'] . " by " . $artwork['artist_name'] . " - Description: " . $artwork['description'] . "\n";
    }
} else {
    echo "Unable to connect to the database.";
}
?>
```
Note: Ensure to replace `'password'` in the DB_PASS constant with your actual database password and create the necessary database and tables (`artists` and `artworks`) accordingly for this code to work.
