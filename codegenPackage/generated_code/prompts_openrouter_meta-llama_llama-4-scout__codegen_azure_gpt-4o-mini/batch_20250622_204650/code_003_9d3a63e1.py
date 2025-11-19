"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Develop a PHP function to display Persian, Gregorian, and Islamic calendar events, as explained in the article on omidtak.ir, and provide a code snippet.
Generated: DETERMINISTIC_9d3a63e1943ccb39
Batch ID: 20250622_204650
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
 * Class CalendarEvent
 * A class to handle and display events in Persian, Gregorian, and Islamic calendars.
 */
class CalendarEvent
{
    private $events = [];

    /**
     * Adds an event to the calendar.
     *
     * @param string $date The date of the event in 'Y-m-d' format.
     * @param string $event The description of the event.
     * @param string $calendarType The type of calendar ('persian', 'gregorian', 'islamic').
     * @throws InvalidArgumentException If the calendar type is invalid.
     */
    public function addEvent($date, $event, $calendarType)
    {
        // Validate calendar type
        if (!in_array($calendarType, ['persian', 'gregorian', 'islamic'])) {
            throw new InvalidArgumentException("Invalid calendar type: $calendarType");
        }

        // Store the event
        $this->events[] = [
            'date' => $date,
            'event' => $event,
            'calendarType' => $calendarType,
        ];
    }

    /**
     * Displays all events in a formatted manner.
     */
    public function displayEvents()
    {
        if (empty($this->events)) {
            echo "No events to display.\n";
            return;
        }

        foreach ($this->events as $event) {
            echo "Date: " . $this->formatDate($event['date'], $event['calendarType']) . "\n";
            echo "Event: " . $event['event'] . "\n";
            echo "Calendar Type: " . ucfirst($event['calendarType']) . "\n";
            echo str_repeat("-", 30) . "\n";
        }
    }

    /**
     * Formats the date based on the calendar type.
     *
     * @param string $date The date to format.
     * @param string $calendarType The type of calendar.
     * @return string The formatted date.
     */
    private function formatDate($date, $calendarType)
    {
        switch ($calendarType) {
            case 'persian':
                // Convert Gregorian date to Persian date
                return $this->convertToPersian($date);
            case 'islamic':
                // Convert Gregorian date to Islamic date
                return $this->convertToIslamic($date);
            case 'gregorian':
            default:
                return $date; // Return as is for Gregorian
        }
    }

    /**
     * Converts a Gregorian date to a Persian date.
     *
     * @param string $date The Gregorian date.
     * @return string The Persian date.
     */
    private function convertToPersian($date)
    {
        // Placeholder for actual conversion logic
        return "Persian Date: " . $date; // Replace with actual conversion
    }

    /**
     * Converts a Gregorian date to an Islamic date.
     *
     * @param string $date The Gregorian date.
     * @return string The Islamic date.
     */
    private function convertToIslamic($date)
    {
        // Placeholder for actual conversion logic
        return "Islamic Date: " . $date; // Replace with actual conversion
    }
}

// Example usage
try {
    $calendar = new CalendarEvent();
    $calendar->addEvent('2023-10-01', 'Start of the new year', 'persian');
    $calendar->addEvent('2023-10-05', 'Eid al-Fitr', 'islamic');
    $calendar->addEvent('2023-10-10', 'Independence Day', 'gregorian');
    $calendar->displayEvents();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
