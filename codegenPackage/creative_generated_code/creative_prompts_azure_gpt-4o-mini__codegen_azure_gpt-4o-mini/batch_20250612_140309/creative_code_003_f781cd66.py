"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://larpradar.com
Prompt: Develop a PHP script that connects to the Larp Radar database to retrieve and display a calendar of upcoming LARP events based on user preferences.
Generated: DETERMINISTIC_f781cd661bacdccf
Batch ID: 20250612_140309
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
 * LARP Event Calendar - A PHP script to connect to the Larp Radar database
 * and retrieve a calendar of upcoming LARP events based on user preferences.
 */

// Database configuration
$host = 'localhost'; // Database host
$db = 'larp_radar';  // Database name
$user = 'username';   // Database username
$pass = 'password';   // Database password
$charset = 'utf8mb4'; // Character set

// Data Source Name (DSN) for PDO
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// PDO options for error handling
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Fetch as associative array
    PDO::ATTR_EMULATE_PREPARES   => false,                  // Use real prepared statements
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to retrieve upcoming LARP events based on user preferences.
 *
 * @param PDO $pdo The PDO instance for database connection.
 * @param array $preferences User preferences for filtering events.
 * @return array List of upcoming LARP events.
 */
function getUpcomingEvents(PDO $pdo, array $preferences): array {
    // Prepare the SQL query
    $sql = "SELECT * FROM events WHERE event_date > NOW()";
    
    // Build the query based on user preferences
    if (!empty($preferences['location'])) {
        $sql .= " AND location = :location";
    }
    if (!empty($preferences['type'])) {
        $sql .= " AND type = :type";
    }
    
    $stmt = $pdo->prepare($sql);
    
    // Bind parameters if preferences are set
    if (!empty($preferences['location'])) {
        $stmt->bindValue(':location', $preferences['location']);
    }
    if (!empty($preferences['type'])) {
        $stmt->bindValue(':type', $preferences['type']);
    }

    // Execute the statement
    $stmt->execute();
    
    // Fetch all results
    return $stmt->fetchAll();
}

// User preferences (example, could be from a form or API request)
$userPreferences = [
    'location' => 'New York', // Example filter by location
    'type'     => 'Fantasy'    // Example filter by event type
];

// Retrieve upcoming events based on user preferences
$upcomingEvents = getUpcomingEvents($pdo, $userPreferences);

// Display the events
if ($upcomingEvents) {
    echo "<h1>Upcoming LARP Events</h1>";
    echo "<ul>";
    foreach ($upcomingEvents as $event) {
        echo "<li><strong>{$event['event_name']}</strong> - {$event['event_date']} at {$event['location']}</li>";
    }
    echo "</ul>";
} else {
    echo "<p>No upcoming events found based on your preferences.</p>";
}

// Close the PDO connection (optional, as it will close automatically on script end)
$pdo = null;
?>
```
