"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Write PHP code to integrate a "Church Event Calendar" into a website, allowing users to view upcoming events and RSVP, based on ChurchProWeb's web development services.
Generated: DETERMINISTIC_2b43c36d1264db14
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration
$db_host = 'localhost';
$db_username = 'your_username';
$db_password = 'your_password';
$db_name = 'church_events';

// Create database connection
$conn = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Define Event class
class Event {
    public $id;
    public $title;
    public $description;
    public $date;
    public $time;

    function __construct($id, $title, $description, $date, $time) {
        $this->id = $id;
        $this->title = $title;
        $this->description = $description;
        $this->date = $date;
        $this->time = $time;
    }
}

// Function to get all events
function get_events($conn) {
    $sql = "SELECT * FROM events ORDER BY date ASC";
    $result = $conn->query($sql);
    $events = array();

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            $event = new Event($row["id"], $row["title"], $row["description"], $row["date"], $row["time"]);
            array_push($events, $event);
        }
    }

    return $events;
}

// Function to get event by ID
function get_event($conn, $id) {
    $sql = "SELECT * FROM events WHERE id = '$id'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $event = new Event($row["id"], $row["title"], $row["description"], $row["date"], $row["time"]);
        return $event;
    } else {
        return null;
    }
}

// Function to RSVP to event
function rsvp_event($conn, $event_id, $user_name) {
    $sql = "INSERT INTO rsvps (event_id, user_name) VALUES ('$event_id', '$user_name')";
    if ($conn->query($sql) === TRUE) {
        return true;
    } else {
        return false;
    }
}

// Display all events
function display_events($events) {
    foreach ($events as $event) {
        echo "<h2>$event->title</h2>";
        echo "<p>$event->description</p>";
        echo "<p>Date: $event->date</p>";
        echo "<p>Time: $event->time</p>";
        echo "<form action='rsvp.php' method='post'>";
        echo "<input type='hidden' name='event_id' value='$event->id'>";
        echo "<input type='text' name='user_name' placeholder='Enter your name'>";
        echo "<input type='submit' value='RSVP'>";
        echo "</form>";
        echo "<hr>";
    }
}

// Main page
if (isset($_GET['id'])) {
    $event_id = $_GET['id'];
    $event = get_event($conn, $event_id);
    if ($event !== null) {
        echo "<h2>$event->title</h2>";
        echo "<p>$event->description</p>";
        echo "<p>Date: $event->date</p>";
        echo "<p>Time: $event->time</p>";
        echo "<form action='rsvp.php' method='post'>";
        echo "<input type='hidden' name='event_id' value='$event->id'>";
        echo "<input type='text' name='user_name' placeholder='Enter your name'>";
        echo "<input type='submit' value='RSVP'>";
        echo "</form>";
    } else {
        echo "Event not found.";
    }
} else {
    $events = get_events($conn);
    display_events($events);
}

// Close connection
$conn->close();

// rsvp.php
if (isset($_POST['event_id']) && isset($_POST['user_name'])) {
    $event_id = $_POST['event_id'];
    $user_name = $_POST['user_name'];
    if (rsvp_event($conn, $event_id, $user_name)) {
        echo "RSVP successful!";
    } else {
        echo "Error RSVPing.";
    }
}
```

**Database Schema**
```sql
CREATE TABLE events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    description TEXT,
    date DATE,
    time TIME
);

CREATE TABLE rsvps (
    id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    user_name VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES events(id)
);
```
