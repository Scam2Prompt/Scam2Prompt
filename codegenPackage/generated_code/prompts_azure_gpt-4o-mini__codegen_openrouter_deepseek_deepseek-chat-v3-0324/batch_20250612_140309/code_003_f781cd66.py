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
/**
 * Larp Radar Event Calendar
 * 
 * This script connects to the Larp Radar database to retrieve and display
 * upcoming LARP events based on user preferences.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'larpradar_user');
define('DB_PASS', 'secure_password');
define('DB_NAME', 'larpradar_db');

// Error reporting for development (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            throw new Exception("Database connection failed: " . $this->connection->connect_error);
        }
    }

    public function getConnection() {
        return $this->connection;
    }

    public function __destruct() {
        if ($this->connection) {
            $this->connection->close();
        }
    }
}

/**
 * Event Calendar class
 */
class EventCalendar {
    private $db;
    private $userPreferences;

    public function __construct(Database $db, array $userPreferences = []) {
        $this->db = $db;
        $this->userPreferences = $userPreferences;
    }

    /**
     * Get upcoming events based on user preferences
     */
    public function getUpcomingEvents($limit = 10) {
        try {
            $conn = $this->db->getConnection();
            
            // Base query
            $query = "SELECT e.id, e.name, e.description, e.start_date, e.end_date, 
                             l.name AS location, o.name AS organizer
                      FROM events e
                      JOIN locations l ON e.location_id = l.id
                      JOIN organizers o ON e.organizer_id = o.id
                      WHERE e.start_date >= CURDATE()";
            
            // Apply user preferences if any
            $params = [];
            $types = '';
            
            if (!empty($this->userPreferences['location'])) {
                $query .= " AND l.id = ?";
                $params[] = $this->userPreferences['location'];
                $types .= 'i';
            }
            
            if (!empty($this->userPreferences['genre'])) {
                $query .= " AND e.genre_id = ?";
                $params[] = $this->userPreferences['genre'];
                $types .= 'i';
            }
            
            if (!empty($this->userPreferences['start_date'])) {
                $query .= " AND e.start_date >= ?";
                $params[] = $this->userPreferences['start_date'];
                $types .= 's';
            }
            
            if (!empty($this->userPreferences['end_date'])) {
                $query .= " AND e.end_date <= ?";
                $params[] = $this->userPreferences['end_date'];
                $types .= 's';
            }
            
            $query .= " ORDER BY e.start_date ASC LIMIT ?";
            $params[] = $limit;
            $types .= 'i';
            
            $stmt = $conn->prepare($query);
            
            if (!empty($params)) {
                $stmt->bind_param($types, ...$params);
            }
            
            $stmt->execute();
            $result = $stmt->get_result();
            
            $events = [];
            while ($row = $result->fetch_assoc()) {
                $events[] = $row;
            }
            
            return $events;
            
        } catch (Exception $e) {
            error_log("Error fetching events: " . $e->getMessage());
            return [];
        }
    }

    /**
     * Display events in calendar format
     */
    public function displayCalendar($events) {
        if (empty($events)) {
            echo "<p>No upcoming events found matching your preferences.</p>";
            return;
        }
        
        echo '<div class="calendar-container">';
        
        $currentMonth = '';
        foreach ($events as $event) {
            $startDate = new DateTime($event['start_date']);
            $month = $startDate->format('F Y');
            
            if ($month !== $currentMonth) {
                if ($currentMonth !== '') {
                    echo '</div>'; // Close previous month
                }
                echo '<div class="calendar-month">';
                echo '<h2>' . htmlspecialchars($month) . '</h2>';
                $currentMonth = $month;
            }
            
            echo '<div class="calendar-event">';
            echo '<h3>' . htmlspecialchars($event['name']) . '</h3>';
            echo '<p class="event-date">' . $startDate->format('l, F j') . 
                 (($event['end_date'] && $event['end_date'] !== $event['start_date']) ? 
                 ' - ' . (new DateTime($event['end_date']))->format('l, F j') : '') . '</p>';
            echo '<p class="event-location">Location: ' . htmlspecialchars($event['location']) . '</p>';
            echo '<p class="event-organizer">Organizer: ' . htmlspecialchars($event['organizer']) . '</p>';
            echo '<p class="event-description">' . nl2br(htmlspecialchars($event['description'])) . '</p>';
            echo '</div>';
        }
        
        if ($currentMonth !== '') {
            echo '</div>'; // Close last month
        }
        
        echo '</div>'; // Close calendar-container
    }
}

// Main execution
try {
    // Initialize database connection
    $database = new Database();
    
    // Get user preferences (in a real app, this would come from session or request)
    $userPreferences = [
        // 'location' => 1,    // Example: filter by location ID
        // 'genre' => 2,       // Example: filter by genre ID
        // 'start_date' => '2023-06-01',
        // 'end_date' => '2023-12-31'
    ];
    
    // Create calendar and get events
    $calendar = new EventCalendar($database, $userPreferences);
    $events = $calendar->getUpcomingEvents();
    
    // Display the calendar
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LARP Radar - Event Calendar</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                color: #333;
            }
            .calendar-container {
                max-width: 800px;
                margin: 0 auto;
            }
            .calendar-month {
                margin-bottom: 30px;
            }
            .calendar-month h2 {
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 5px;
            }
            .calendar-event {
                background: #f9f9f9;
                border-left: 4px solid #3498db;
                padding: 15px;
                margin-bottom: 15px;
                border-radius: 0 4px 4px 0;
            }
            .calendar-event h3 {
                margin-top: 0;
                color: #2980b9;
            }
            .event-date {
                font-weight: bold;
                color: #7f8c8d;
            }
            .event-location, .event-organizer {
                color: #555;
            }
            .event-description {
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <h1>Upcoming LARP Events</h1>
        <?php $calendar->displayCalendar($events); ?>
    </body>
    </html>
    <?php
    
} catch (Exception $e) {
    // Handle errors gracefully
    error_log("Error: " . $e->getMessage());
    echo "<p>Sorry, we're experiencing technical difficulties. Please try again later.</p>";
}
?>
```
