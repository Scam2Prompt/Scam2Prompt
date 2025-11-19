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
// Configuration settings
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'larp_radar'); // Database name
define('DB_USER', 'your_db_user'); // Database user
define('DB_PASSWORD', 'your_db_password'); // Database password

// Establish a connection to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Set PDO to throw exceptions on error
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC // Fetch results as associative arrays
    ]);
} catch (PDOException $e) {
    // Handle connection errors
    error_log("Database connection failed: " . $e->getMessage());
    die("Database connection failed. Please try again later.");
}

// Helper function to sanitize user input
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Check if user preferences are provided via GET request
$userPreferences = [];
if (!empty($_GET['theme'])) {
    $userPreferences['theme'] = sanitizeInput($_GET['theme']); // Theme of LARP events
}
if (!empty($_GET['location'])) {
    $userPreferences['location'] = sanitizeInput($_GET['location']); // Location preference
}
if (!empty($_GET['date_range'])) {
    $userPreferences['date_range'] = sanitizeInput($_GET['date_range']); // Date range for events
}

// Base SQL query to retrieve upcoming LARP events
$sql = "SELECT event_name, event_date, location, theme, description 
        FROM events 
        WHERE event_date >= CURDATE()";

// Dynamically build query based on user preferences
$conditions = [];
$params = [];

if (!empty($userPreferences['theme'])) {
    $conditions[] = "theme = :theme";
    $params[':theme'] = $userPreferences['theme'];
}

if (!empty($userPreferences['location'])) {
    $conditions[] = "location LIKE :location";
    $params[':location'] = "%" . $userPreferences['location'] . "%";
}

if (!empty($userPreferences['date_range'])) {
    list($startDate, $endDate) = explode(',', $userPreferences['date_range']);
    $conditions[] = "event_date BETWEEN :start_date AND :end_date";
    $params[':start_date'] = $startDate;
    $params[':end_date'] = $endDate;
}

// Append conditions to the query if any exist
if (!empty($conditions)) {
    $sql .= " AND " . implode(" AND ", $conditions);
}

// Prepare and execute the SQL query
try {
    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);

    // Fetch all matching events
    $events = $stmt->fetchAll();

    // Display events in a calendar-like format
    echo "<h1>Upcoming LARP Events</h1>";
    if (empty($events)) {
        echo "<p>No events found matching your preferences.</p>";
    } else {
        echo "<ul>";
        foreach ($events as $event) {
            echo "<li>";
            echo "<strong>" . sanitizeInput($event['event_name']) . "</strong><br>";
            echo "Date: " . sanitizeInput($event['event_date']) . "<br>";
            echo "Location: " . sanitizeInput($event['location']) . "<br>";
            echo "Theme: " . sanitizeInput($event['theme']) . "<br>";
            echo "Description: " . sanitizeInput($event['description']) . "<br>";
            echo "</li>";
        }
        echo "</ul>";
    }
} catch (PDOException $e) {
    // Handle query errors
    error_log("Failed to retrieve events: " . $e->getMessage());
    echo "<p>An error occurred while fetching events. Please try again later.</p>";
}

// Close the database connection
$pdo = null;
?>
```
