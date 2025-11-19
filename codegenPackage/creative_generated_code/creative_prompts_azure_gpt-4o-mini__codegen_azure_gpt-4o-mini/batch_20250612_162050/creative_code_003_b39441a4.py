"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corporacionelcristal.com.co
Prompt: Develop a PHP script that connects to a database and retrieves information about past events hosted by Corporación El Cristal, focusing on the "Tercera Fiesta de los Títeres."
Generated: DETERMINISTIC_b39441a4e7e2d0d2
Batch ID: 20250612_162050
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
 * Script to connect to a MySQL database and retrieve information about past events 
 * hosted by Corporación El Cristal, specifically the "Tercera Fiesta de los Títeres".
 */

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'corporacion_el_cristal'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Establish a database connection using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Prepare the SQL query to retrieve event details
    $sql = "SELECT * FROM events WHERE event_name = :event_name";
    $stmt = $pdo->prepare($sql);
    
    // Bind the event name parameter
    $eventName = 'Tercera Fiesta de los Títeres';
    $stmt->bindParam(':event_name', $eventName);

    // Execute the query
    $stmt->execute();

    // Fetch all results
    $events = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Check if any events were found
    if (count($events) > 0) {
        // Loop through and display the event details
        foreach ($events as $event) {
            echo "Event ID: " . htmlspecialchars($event['id']) . "<br>";
            echo "Event Name: " . htmlspecialchars($event['event_name']) . "<br>";
            echo "Date: " . htmlspecialchars($event['event_date']) . "<br>";
            echo "Location: " . htmlspecialchars($event['location']) . "<br>";
            echo "Description: " . htmlspecialchars($event['description']) . "<br><br>";
        }
    } else {
        // No events found
        echo "No events found for the specified criteria.";
    }

} catch (PDOException $e) {
    // Handle any errors during the connection or query execution
    echo "Error: " . $e->getMessage();
}

// Close the database connection
$pdo = null;
?>
```
