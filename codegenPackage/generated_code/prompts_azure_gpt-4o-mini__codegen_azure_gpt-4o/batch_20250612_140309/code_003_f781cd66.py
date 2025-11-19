"""
Generated Code Metadata:
========================
Original URL: https://larpradar.com
Prompt: Develop a PHP script that connects to the Larp Radar database to retrieve and display a calendar of upcoming LARP events based on user preferences.
Generated: DETERMINISTIC_f781cd661bacdccf
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// LARP Radar Calendar Script
// This script connects to the Larp Radar database, retrieves upcoming LARP events based on user preferences, and displays them in a calendar format.

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'larp_radar'); // Database name
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password

// Establish database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable error handling
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to retrieve events based on user preferences
function getLarpEvents($pdo, $preferences) {
    // Prepare SQL query with user preferences
    $sql = "SELECT event_name, event_date, location, description 
            FROM larp_events 
            WHERE genre = :genre AND difficulty = :difficulty 
            ORDER BY event_date ASC";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            ':genre' => $preferences['genre'],
            ':difficulty' => $preferences['difficulty']
        ]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC); // Fetch results as associative array
    } catch (PDOException $e) {
        error_log("Error retrieving events: " . $e->getMessage());
        return [];
    }
}

// Example user preferences (these would typically come from user input)
$userPreferences = [
    'genre' => 'Fantasy', // Example genre preference
    'difficulty' => 'Intermediate' // Example difficulty preference
];

// Retrieve events based on user preferences
$events = getLarpEvents($pdo, $userPreferences);

// Display events in a calendar format
echo "<h1>Upcoming LARP Events</h1>";
if (!empty($events)) {
    echo "<table border='1'>";
    echo "<tr><th>Event Name</th><th>Date</th><th>Location</th><th>Description</th></tr>";
    foreach ($events as $event) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($event['event_name']) . "</td>";
        echo "<td>" . htmlspecialchars(date('F j, Y', strtotime($event['event_date']))) . "</td>";
        echo "<td>" . htmlspecialchars($event['location']) . "</td>";
        echo "<td>" . htmlspecialchars($event['description']) . "</td>";
        echo "</tr>";
    }
    echo "</table>";
} else {
    echo "<p>No events found matching your preferences.</p>";
}

// Close the database connection
$pdo = null;
?>
```
