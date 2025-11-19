"""
Generated Code Metadata:
========================
Original URL: https://rotary-bastogne.be
Prompt: "Create a PHP script to automate the generation of Rotary Club newsletters, pulling in data from a database of events and member activities, similar to the bulletins found on https://rotary-bastogne.be."
Generated: DETERMINISTIC_74daca13a31a41eb
Batch ID: 20250622_205436
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
 * Rotary Club Newsletter Generator
 * 
 * This script automates the generation of newsletters by pulling data from a database
 * containing events and member activities. The generated newsletter is saved as an HTML file.
 * 
 * Requirements:
 * - A MySQL database with tables for events and member activities.
 * - Proper database credentials.
 * - PHP installed on the server.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'rotary_club');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Newsletter configuration
define('NEWSLETTER_TITLE', 'Rotary Club Newsletter');
define('NEWSLETTER_FILENAME', 'newsletter.html');

try {
    // Establish database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Fetch events from the database
    $eventsQuery = $pdo->query("SELECT title, description, event_date FROM events ORDER BY event_date ASC");
    $events = $eventsQuery->fetchAll(PDO::FETCH_ASSOC);

    // Fetch member activities from the database
    $activitiesQuery = $pdo->query("SELECT member_name, activity, activity_date FROM member_activities ORDER BY activity_date ASC");
    $activities = $activitiesQuery->fetchAll(PDO::FETCH_ASSOC);

    // Start building the newsletter HTML
    $newsletterHtml = "<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>" . NEWSLETTER_TITLE . "</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h1 { color: #2c3e50; }
        h2 { color: #34495e; }
        .event, .activity { margin-bottom: 20px; }
        .event-title, .activity-title { font-weight: bold; }
        .event-date, .activity-date { color: #7f8c8d; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>" . NEWSLETTER_TITLE . "</h1>
    <h2>Upcoming Events</h2>";

    // Add events to the newsletter
    if (!empty($events)) {
        foreach ($events as $event) {
            $newsletterHtml .= "<div class='event'>
                <div class='event-title'>" . htmlspecialchars($event['title']) . "</div>
                <div class='event-date'>" . htmlspecialchars($event['event_date']) . "</div>
                <div class='event-description'>" . htmlspecialchars($event['description']) . "</div>
            </div>";
        }
    } else {
        $newsletterHtml .= "<p>No upcoming events at the moment.</p>";
    }

    $newsletterHtml .= "<h2>Member Activities</h2>";

    // Add member activities to the newsletter
    if (!empty($activities)) {
        foreach ($activities as $activity) {
            $newsletterHtml .= "<div class='activity'>
                <div class='activity-title'>" . htmlspecialchars($activity['member_name']) . " - " . htmlspecialchars($activity['activity']) . "</div>
                <div class='activity-date'>" . htmlspecialchars($activity['activity_date']) . "</div>
            </div>";
        }
    } else {
        $newsletterHtml .= "<p>No recent member activities.</p>";
    }

    $newsletterHtml .= "</body>
</html>";

    // Save the newsletter to a file
    file_put_contents(NEWSLETTER_FILENAME, $newsletterHtml);

    echo "Newsletter generated successfully: " . NEWSLETTER_FILENAME . PHP_EOL;

} catch (PDOException $e) {
    // Handle database connection errors
    echo "Database error: " . $e->getMessage() . PHP_EOL;
} catch (Exception $e) {
    // Handle general errors
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}
?>
```
