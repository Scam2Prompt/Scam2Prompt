"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Write PHP code to integrate a "Church Event Calendar" into a website, allowing users to view upcoming events and RSVP, based on ChurchProWeb's web development services.
Generated: DETERMINISTIC_2b43c36d1264db14
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
// Database connection settings (Update these with your actual credentials)
define("DB_HOST", "localhost");
define("DB_USER", "root");
define("DB_PASSWORD", "");
define("DB_NAME", "church_event_calendar");

// Establish a MySQL database connection
function getDatabaseConnection()
{
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// Fetch upcoming events from the database
function getUpcomingEvents($conn)
{
    $sql = "SELECT id, event_name, event_date, event_description 
            FROM events 
            WHERE event_date >= CURRENT_DATE 
            ORDER BY event_date ASC";
    $result = $conn->query($sql);

    if ($result === false) {
        throw new Exception("Error fetching events: " . $conn->error);
    }

    $events = [];
    while ($row = $result->fetch_assoc()) {
        $events[] = $row;
    }
    return $events;
}

// Handle RSVP submission
function handleRSVP($conn, $eventId, $userName, $userEmail)
{
    $stmt = $conn->prepare("INSERT INTO rsvps (event_id, user_name, user_email) VALUES (?, ?, ?)");
    if (!$stmt) {
        throw new Exception("Error preparing statement: " . $conn->error);
    }

    $stmt->bind_param("iss", $eventId, $userName, $userEmail);
    if (!$stmt->execute()) {
        throw new Exception("Error executing statement: " . $stmt->error);
    }

    $stmt->close();
}

// HTML for displaying the event calendar
function renderEventCalendar($events)
{
    echo "<h2>Upcoming Church Events</h2>";
    if (empty($events)) {
        echo "<p>No upcoming events found.</p>";
        return;
    }

    echo '<ul>';
    foreach ($events as $event) {
        echo '<li>';
        echo '<strong>' . htmlspecialchars($event['event_name']) . '</strong><br>';
        echo 'Date: ' . htmlspecialchars($event['event_date']) . '<br>';
        echo 'Description: ' . htmlspecialchars($event['event_description']) . '<br>';
        echo '<form method="POST">';
        echo '<input type="hidden" name="event_id" value="' . htmlspecialchars($event['id']) . '">';
        echo 'Your Name: <input type="text" name="user_name" required><br>';
        echo 'Your Email: <input type="email" name="user_email" required><br>';
        echo '<button type="submit">RSVP</button>';
        echo '</form>';
        echo '</li>';
    }
    echo '</ul>';
}

// Main script logic
try {
    $conn = getDatabaseConnection();

    // Handle RSVP form submission
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $eventId = intval($_POST['event_id']);
        $userName = $_POST['user_name'];
        $userEmail = $_POST['user_email'];

        if (empty($eventId) || empty($userName) || empty($userEmail)) {
            throw new Exception("All form fields are required.");
        }

        handleRSVP($conn, $eventId, $userName, $userEmail);
        echo "<p>Thank you for RSVPing!</p>";
    }

    // Fetch and display events
    $events = getUpcomingEvents($conn);
    renderEventCalendar($events);

    $conn->close();
} catch (Exception $e) {
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
