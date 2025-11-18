"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://le13emeart.com
Prompt: Generate code in PHP to integrate a "Le 13e Art" event search feature into a website, allowing users to filter performances by date and genre.
Generated: DETERMINISTIC_5e7017e4e2bbe596
Batch ID: 20250612_151457
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
 * Le 13e Art Event Search Integration
 * This script allows users to search for performances by date and genre.
 */

// Database connection settings
$host = 'localhost';
$db = 'event_db';
$user = 'db_user';
$pass = 'db_pass';

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to fetch events based on filters
function fetchEvents($pdo, $date = null, $genre = null) {
    // Base query
    $query = "SELECT * FROM performances WHERE 1=1";
    $params = [];

    // Add date filter if provided
    if ($date) {
        $query .= " AND event_date = :event_date";
        $params[':event_date'] = $date;
    }

    // Add genre filter if provided
    if ($genre) {
        $query .= " AND genre = :genre";
        $params[':genre'] = $genre;
    }

    // Prepare and execute the query
    $stmt = $pdo->prepare($query);
    $stmt->execute($params);

    // Fetch and return events
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Check if filters are set
$date = isset($_GET['date']) ? $_GET['date'] : null;
$genre = isset($_GET['genre']) ? $_GET['genre'] : null;

try {
    // Fetch events based on user input
    $events = fetchEvents($pdo, $date, $genre);
} catch (Exception $e) {
    // Handle errors during fetching
    die("Error fetching events: " . $e->getMessage());
}

// Output the events in JSON format
header('Content-Type: application/json');
echo json_encode($events);
?>
```

### Usage:
To use this script, make sure to replace the database connection settings with your own. You can call this PHP script via an HTTP GET request with optional parameters `date` and `genre` to filter the results. For example:
```
GET /path/to/script.php?date=2023-10-01&genre=Music
```
