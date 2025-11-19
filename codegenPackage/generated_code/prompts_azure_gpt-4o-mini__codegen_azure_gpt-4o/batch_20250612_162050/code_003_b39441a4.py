"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Develop a PHP script that connects to a database and retrieves information about past events hosted by Corporación El Cristal, focusing on the "Tercera Fiesta de los Títeres."
Generated: DETERMINISTIC_b39441a4e7e2d0d2
Batch ID: 20250612_162050
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
$host = 'localhost'; // Database host
$dbname = 'events_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exceptions for errors
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// SQL query to retrieve information about the specific event
$sql = "
    SELECT 
        event_name, 
        event_date, 
        location, 
        description 
    FROM 
        events 
    WHERE 
        organizer = :organizer AND 
        event_name = :event_name
";

try {
    // Prepare the SQL statement
    $stmt = $pdo->prepare($sql);

    // Bind parameters to the query
    $stmt->bindValue(':organizer', 'Corporación El Cristal', PDO::PARAM_STR);
    $stmt->bindValue(':event_name', 'Tercera Fiesta de los Títeres', PDO::PARAM_STR);

    // Execute the query
    $stmt->execute();

    // Fetch the results
    $events = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Check if any events were found
    if (count($events) > 0) {
        // Output the event details
        foreach ($events as $event) {
            echo "Event Name: " . htmlspecialchars($event['event_name']) . PHP_EOL;
            echo "Event Date: " . htmlspecialchars($event['event_date']) . PHP_EOL;
            echo "Location: " . htmlspecialchars($event['location']) . PHP_EOL;
            echo "Description: " . htmlspecialchars($event['description']) . PHP_EOL;
            echo str_repeat("-", 40) . PHP_EOL;
        }
    } else {
        echo "No events found for 'Tercera Fiesta de los Títeres' organized by 'Corporación El Cristal'." . PHP_EOL;
    }
} catch (PDOException $e) {
    // Handle query errors
    echo "Error retrieving event data: " . $e->getMessage() . PHP_EOL;
}

// Close the database connection
$pdo = null;
?>
```
