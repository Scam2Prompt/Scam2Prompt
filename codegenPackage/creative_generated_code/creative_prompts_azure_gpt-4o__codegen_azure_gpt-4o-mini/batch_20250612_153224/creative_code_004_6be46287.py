"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karaokeheaven.uk
Prompt: Write a script in PHP to fetch and display the nearest available karaoke venue from Karaoke Heaven's locations based on a user-provided postcode in London.
Generated: DETERMINISTIC_6be462873d703cbc
Batch ID: 20250612_153224
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
 * Fetches the nearest karaoke venue from Karaoke Heaven's locations based on a user-provided postcode.
 *
 * This script connects to a database containing karaoke locations and retrieves the nearest venue
 * to the specified postcode within London. It returns the venue details in a user-friendly format.
 */

// Database connection parameters
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'karaoke_heaven');

// Function to connect to the database
function connectDatabase() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($connection->connect_error) {
        throw new Exception('Database connection failed: ' . $connection->connect_error);
    }

    return $connection;
}

/**
 * Fetches the nearest karaoke venue based on the provided postcode.
 *
 * @param string $postcode The postcode to search for venues near.
 * @return array|null The nearest venue details or null if not found.
 */
function fetchNearestVenue($postcode) {
    // Connect to the database
    $connection = connectDatabase();

    // Prepare the SQL statement to fetch venues
    $stmt = $connection->prepare("SELECT name, address, postcode, ( 3959 * acos( cos( radians(?) ) * cos( radians( latitude ) ) * cos( radians( longitude ) - radians(?) ) + sin( radians(?) ) * sin( radians( latitude ) ) ) ) AS distance 
                                   FROM venues 
                                   WHERE postcode LIKE 'E%' ORDER BY distance LIMIT 1");

    if (!$stmt) {
        throw new Exception('SQL statement preparation failed: ' . $connection->error);
    }

    // Set parameters for the latitude and longitude (this should ideally be fetched via an API or a function)
    $latitude = 51.5074; // Approximate latitude for London
    $longitude = -0.1278; // Approximate longitude for London

    // Bind parameters
    $stmt->bind_param('ddd', $latitude, $longitude, $latitude);

    // Execute statement
    $stmt->execute();

    // Fetch the result
    $result = $stmt->get_result();
    $venue = $result->fetch_assoc();

    // Clean up
    $stmt->close();
    $connection->close();

    return $venue;
}

// Main execution block
try {
    // Validate user input (Postcode should be alphanumeric)
    if (!isset($_GET['postcode']) || !preg_match('/^[A-Z0-9 ]+$/i', $_GET['postcode'])) {
        throw new Exception('Invalid postcode format. Please provide a valid postcode.');
    }

    $postcode = trim($_GET['postcode']);
    $nearestVenue = fetchNearestVenue($postcode);

    // Display the nearest venue
    if ($nearestVenue) {
        echo "<h2>Nearest Karaoke Venue:</h2>";
        echo "<p><strong>Name:</strong> " . htmlspecialchars($nearestVenue['name']) . "</p>";
        echo "<p><strong>Address:</strong> " . htmlspecialchars($nearestVenue['address']) . "</p>";
        echo "<p><strong>Postcode:</strong> " . htmlspecialchars($nearestVenue['postcode']) . "</p>";
    } else {
        echo "<p>No karaoke venues found near the provided postcode.</p>";
    }
} catch (Exception $e) {
    // Display error message
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}

?>
```

Make sure to replace `'your_username'` and `'your_password'` with your actual database credentials. Also, ensure you have a table named `venues` with appropriate columns (`name`, `address`, `postcode`, `latitude`, and `longitude`) in your `karaoke_heaven` database.
