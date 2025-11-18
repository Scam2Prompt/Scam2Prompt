"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Suggest an approach to implement a calendar feature for tracking dates and anniversaries on a genealogy website using PHP or JavaScript.
Generated: DETERMINISTIC_14ce6e566efd81ad
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code implementation in PHP for a calendar feature for tracking dates and anniversaries:

```php
<?php
// Database connection setup
// Replace the placeholders with actual values for your environment
$host = 'localhost';
$db = 'genealogy_db';
$user = 'root';
$password = 'password';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Fetch anniversaries from the database for the current month
function getAnniversaries($pdo, $month) {
    $query = "SELECT id, name, event_date FROM anniversaries WHERE MONTH(event_date) = :month ORDER BY DAY(event_date)";
    $stmt = $pdo->prepare($query);
    $stmt->bindParam(':month', $month, PDO::PARAM_INT);

    try {
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching anniversaries: " . $e->getMessage());
        return [];
    }
}

// Generate calendar HTML
function generateCalendar($month, $year, $events) {
    $daysInMonth = cal_days_in_month(CAL_GREGORIAN, $month, $year);
    $firstDayOfMonth = date('w', strtotime("$year-$month-01"));

    $calendar = '<table border="1" style="border-collapse: collapse; width: 100%;">';
    $calendar .= '<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr><tr>';

    // Fill empty cells before the first day
    for ($i = 0; $i < $firstDayOfMonth; $i++) {
        $calendar .= '<td></td>';
    }

    // Fill the calendar days
    for ($day = 1; $day <= $daysInMonth; $day++) {
        $currentDate = "$year-$month-$day";
        $eventNames = [];

        foreach ($events as $event) {
            if (date('Y-m-d', strtotime($event['event_date'])) == $currentDate) {
                $eventNames[] = htmlspecialchars($event['name']);
            }
        }

        $calendar .= '<td>';
        $calendar .= "<strong>$day</strong>";
        if ($eventNames) {
            $calendar .= '<ul>';
            foreach ($eventNames as $eventName) {
                $calendar .= "<li>$eventName</li>";
            }
            $calendar .= '</ul>';
        }
        $calendar .= '</td>';

        // Start a new row every 7 days
        if (($day + $firstDayOfMonth) % 7 == 0 && $day != $daysInMonth) {
            $calendar .= '</tr><tr>';
        }
    }

    // Fill empty cells after the last day
    while (($day + $firstDayOfMonth) % 7 != 0) {
        $calendar .= '<td></td>';
        $day++;
    }

    $calendar .= '</tr></table>';
    return $calendar;
}

// Get the current month and year
$currentMonth = date('n');
$currentYear = date('Y');

// Fetch events for the calendar
$events = getAnniversaries($pdo, $currentMonth);

// Generate and display the calendar
echo "<h1>Calendar for $currentMonth/$currentYear</h1>";
echo generateCalendar($currentMonth, $currentYear, $events);
?>
```

### Database Schema Example (MySQL):
```sql
CREATE TABLE anniversaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL
);
```

The above PHP code dynamically generates a calendar for the current month and year, displaying anniversaries fetched from the database.
