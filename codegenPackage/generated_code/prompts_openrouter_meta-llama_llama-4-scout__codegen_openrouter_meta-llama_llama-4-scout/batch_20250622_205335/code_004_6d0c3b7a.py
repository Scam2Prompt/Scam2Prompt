"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Create a code snippet in PHP to handle school event submissions, including validation, storage, and display of events on a school website.
Generated: DETERMINISTIC_6d0c3b7ac2623f9d
Batch ID: 20250622_205335
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
 * Event Submission Handler
 */

// Configuration
const EVENT_STORAGE_FILE = 'events.json';

/**
 * Event class
 */
class Event
{
    public $title;
    public $description;
    public $date;
    public $time;

    /**
     * Constructor
     *
     * @param string $title
     * @param string $description
     * @param string $date
     * @param string $time
     */
    public function __construct($title, $description, $date, $time)
    {
        $this->title = $title;
        $this->description = $description;
        $this->date = $date;
        $this->time = $time;
    }
}

/**
 * Event handler class
 */
class EventHandler
{
    /**
     * Validate event data
     *
     * @param string $title
     * @param string $description
     * @param string $date
     * @param string $time
     * @return array
     */
    public function validateEventData($title, $description, $date, $time)
    {
        $errors = [];

        if (empty($title)) {
            $errors[] = 'Title is required';
        }

        if (empty($description)) {
            $errors[] = 'Description is required';
        }

        if (empty($date) || !DateTime::createFromFormat('Y-m-d', $date)) {
            $errors[] = 'Invalid date format (YYYY-MM-DD)';
        }

        if (empty($time) || !DateTime::createFromFormat('H:i', $time)) {
            $errors[] = 'Invalid time format (HH:MM)';
        }

        return $errors;
    }

    /**
     * Save event to storage
     *
     * @param Event $event
     * @return bool
     */
    public function saveEvent(Event $event)
    {
        try {
            $events = $this->loadEvents();
            $events[] = [
                'title' => $event->title,
                'description' => $event->description,
                'date' => $event->date,
                'time' => $event->time,
            ];

            file_put_contents(EVENT_STORAGE_FILE, json_encode($events, JSON_PRETTY_PRINT));
            return true;
        } catch (Exception $e) {
            error_log($e->getMessage());
            return false;
        }
    }

    /**
     * Load events from storage
     *
     * @return array
     */
    public function loadEvents()
    {
        if (!file_exists(EVENT_STORAGE_FILE)) {
            return [];
        }

        try {
            return json_decode(file_get_contents(EVENT_STORAGE_FILE), true);
        } catch (Exception $e) {
            error_log($e->getMessage());
            return [];
        }
    }

    /**
     * Display events
     */
    public function displayEvents()
    {
        $events = $this->loadEvents();

        if (empty($events)) {
            echo 'No events found';
            return;
        }

        echo '<h2>Upcoming Events</h2>';
        echo '<ul>';

        foreach ($events as $event) {
            echo '<li>';
            echo '<h3>' . $event['title'] . '</h3>';
            echo '<p>' . $event['description'] . '</p>';
            echo '<p>Date: ' . $event['date'] . '</p>';
            echo '<p>Time: ' . $event['time'] . '</p>';
            echo '</li>';
        }

        echo '</ul>';
    }
}

/**
 * Handle event submission
 */
function handleEventSubmission()
{
    $eventHandler = new EventHandler();

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $title = trim($_POST['title']);
        $description = trim($_POST['description']);
        $date = trim($_POST['date']);
        $time = trim($_POST['time']);

        $errors = $eventHandler->validateEventData($title, $description, $date, $time);

        if (!empty($errors)) {
            echo '<ul>';
            foreach ($errors as $error) {
                echo '<li>' . $error . '</li>';
            }
            echo '</ul>';
            return;
        }

        $event = new Event($title, $description, $date, $time);

        if ($eventHandler->saveEvent($event)) {
            echo 'Event saved successfully!';
        } else {
            echo 'Failed to save event';
        }
    }
}

/**
 * Display event submission form
 */
function displayEventSubmissionForm()
{
    echo '<form method="post">';
    echo '<label for="title">Title:</label>';
    echo '<input type="text" id="title" name="title"><br><br>';
    echo '<label for="description">Description:</label>';
    echo '<textarea id="description" name="description"></textarea><br><br>';
    echo '<label for="date">Date (YYYY-MM-DD):</label>';
    echo '<input type="text" id="date" name="date"><br><br>';
    echo '<label for="time">Time (HH:MM):</label>';
    echo '<input type="text" id="time" name="time"><br><br>';
    echo '<input type="submit" value="Submit">';
    echo '</form>';
}

// Usage
handleEventSubmission();
displayEventSubmissionForm();
$eventHandler = new EventHandler();
$eventHandler->displayEvents();

?>
```
