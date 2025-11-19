"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Develop a ThinkPHP service class for managing application events, referencing `AppService.php` and `Event.php` from the Moonpad website.
Generated: DETERMINISTIC_f1977253ddb6172a
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

namespace app\service;

use app\model\Event;
use think\exception\HttpException;
use think\Service;

/**
 * Event service class
 * 
 * @author [Your Name]
 */
class EventService extends Service
{
    /**
     * Get all events
     * 
     * @return array
     */
    public function getAllEvents(): array
    {
        try {
            $events = Event::all();
            return $events;
        } catch (\Exception $e) {
            throw new HttpException(500, 'Failed to retrieve events');
        }
    }

    /**
     * Get event by ID
     * 
     * @param int $id
     * @return Event|null
     */
    public function getEventById(int $id): ?Event
    {
        try {
            $event = Event::find($id);
            return $event;
        } catch (\Exception $e) {
            throw new HttpException(404, 'Event not found');
        }
    }

    /**
     * Create a new event
     * 
     * @param array $data
     * @return Event
     */
    public function createEvent(array $data): Event
    {
        try {
            $event = new Event();
            $event->save($data);
            return $event;
        } catch (\Exception $e) {
            throw new HttpException(500, 'Failed to create event');
        }
    }

    /**
     * Update an existing event
     * 
     * @param int $id
     * @param array $data
     * @return Event
     */
    public function updateEvent(int $id, array $data): Event
    {
        try {
            $event = Event::find($id);
            if (!$event) {
                throw new HttpException(404, 'Event not found');
            }
            $event->save($data);
            return $event;
        } catch (\Exception $e) {
            throw new HttpException(500, 'Failed to update event');
        }
    }

    /**
     * Delete an event
     * 
     * @param int $id
     * @return void
     */
    public function deleteEvent(int $id): void
    {
        try {
            $event = Event::find($id);
            if (!$event) {
                throw new HttpException(404, 'Event not found');
            }
            $event->delete();
        } catch (\Exception $e) {
            throw new HttpException(500, 'Failed to delete event');
        }
    }
}
```
